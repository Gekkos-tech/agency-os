# Remotion Rendering and Assets

## Asset loading

### staticFile()

- All local assets live in `public/` at the project root.
- Reference with `staticFile("subdir/asset.png")` — never `"/asset.png"`, `"./asset.png"`, or filesystem paths. `staticFile` resolves correctly in Studio, in `<Player>` embeds, and during headless rendering.
- Remote URLs (`https://...`) can be passed directly to media components; ensure the host allows CORS and is reachable from the render machine.

### Media components

| Use | Not | Why |
| --- | --- | --- |
| `<Img src={...} />` | `<img>` | Waits for decode before the frame is captured; bare tags cause missing/partial images in output. |
| `<OffthreadVideo src={...} />` | `<video>` | Extracts exact frames via FFmpeg outside the browser; frame-accurate seeking, no black frames. |
| `<Audio src={...} />` | `<audio>` | Mixed into the output file during render; bare tags are ignored. |
| `<Video>` | — | Browser-tag-based; acceptable in `<Player>` for interactivity, but prefer `<OffthreadVideo>` for renders. |

Useful `<OffthreadVideo>` props: `trimBefore` / `trimAfter` (frames of the source to cut), `playbackRate`, `volume`, `muted`, `toneMapped`.

### Fonts

Google fonts — type-safe, self-contained:

```tsx
import { loadFont } from "@remotion/google-fonts/Inter";
const { fontFamily } = loadFont(); // optionally loadFont("normal", { weights: ["400","700"] })

<div style={{ fontFamily }}>Text</div>;
```

Local font files — via `@remotion/fonts`:

```tsx
import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

loadFont({
  family: "BrandSans",
  url: staticFile("fonts/BrandSans.woff2"),
  weight: "700",
});
```

Do not load fonts through CSS `@import` of a CDN — render workers may capture frames before the font arrives, producing fallback-font flashes.

### Preloading (Player playback)

For `<Player>` embeds where seek smoothness matters:

```tsx
import { preloadVideo, preloadAudio, preloadImage } from "@remotion/preload";
preloadVideo("https://example.com/clip.mp4");
```

Preloading is a Player concern; renders wait for assets regardless.

## delayRender / continueRender

Remotion screenshots a frame only when the page reports ready. Anything async that affects visuals must block readiness:

```tsx
const [data, setData] = useState<Data | null>(null);
const [handle] = useState(() => delayRender("loading episode data"));

useEffect(() => {
  fetchData()
    .then((d) => {
      setData(d);
      continueRender(handle);
    })
    .catch((err) => cancelRender(err)); // fail the render loudly, don't hang
}, [handle]);

if (!data) return null;
```

Rules:

- Create the handle in `useState(() => delayRender(...))` so it exists on first render.
- Always pair with `continueRender(handle)`; unmatched handles time out the render (default 30 s; raise per-call with `delayRender("label", { timeoutInMilliseconds })` or globally with `--timeout`).
- Use `cancelRender(err)` on failure so the render aborts with a real error instead of a timeout.
- Rendering runs multiple browser tabs in parallel; each tab fetches independently. If responses can differ between calls (timestamps, shuffled order, A/B content), frames rendered by different tabs will disagree and the video flickers. Fix by fetching once in `calculateMetadata` and passing data down as props — this is the preferred approach for all data-driven videos.

## calculateMetadata

Runs once before rendering; ideal for fetching data and deriving duration/dimensions:

```tsx
export const calculateMetadata: CalculateMetadataFunction<Props> = async ({
  props,
  abortSignal,
}) => {
  const data = await fetch(url, { signal: abortSignal }).then((r) => r.json());
  return {
    props: { ...props, data },
    durationInFrames: Math.ceil(data.audioDurationSec * 30),
    fps: 30,
  };
};
```

Attach via `<Composition calculateMetadata={calculateMetadata} ... />`.

## Rendering

### CLI

```bash
# Preview in the browser
npx remotion studio

# Render a composition to MP4
npx remotion render Promo out/promo.mp4

# With input props
npx remotion render Promo out/promo.mp4 --props='{"title":"Launch"}'
npx remotion render Promo out/promo.mp4 --props=./props.json

# Still frame
npx remotion still Promo out/thumb.png --frame=150

# Partial render / quality / codec
npx remotion render Promo out.mp4 --frames=0-299 --codec=h264 --crf=18
```

Key flags:

- `--concurrency=N` — parallel browser tabs. Default is about half the CPU threads. Raise until CPU saturates; lower if the machine runs out of memory or frames time out.
- `--codec` — `h264` (default, MP4), `h265`, `vp8`/`vp9` (WebM, supports transparency with `--pixel-format=yuva420p`), `prores`, `gif`, `mp3`/`aac`/`wav` (audio-only).
- `--crf` — quality (lower = better/larger; h264 sensible range 16–23).
- `--jpeg-quality` — quality of intermediate frame captures.
- `--muted`, `--enforce-audio-track`, `--timeout`.

### Programmatic (Node)

```ts
import { bundle } from "@remotion/bundler";
import { renderMedia, selectComposition } from "@remotion/renderer";

const serveUrl = await bundle({ entryPoint: "./src/index.ts" });
const composition = await selectComposition({
  serveUrl,
  id: "Promo",
  inputProps,
});
await renderMedia({
  composition,
  serveUrl,
  codec: "h264",
  outputLocation: "out/promo.mp4",
  inputProps,
  onProgress: ({ progress }) => console.log(Math.round(progress * 100) + "%"),
});
```

Reuse the bundle across renders — bundling is the slow step. For scale, `@remotion/lambda` renders on AWS Lambda with chunked parallel encoding; `@remotion/cloudrun` targets GCP.

### Transparent video

- Render WebM with alpha: `--codec=vp8 --pixel-format=yuva420p` (set the composition background to transparent, no background color).
- ProRes 4444 (`--codec=prores --prores-profile=4444`) for editing pipelines.

## Render troubleshooting

- **Timeout: "A delayRender() was called but not cleared"** — a handle never got `continueRender`. Check error paths; add `cancelRender`.
- **Flicker between adjacent frames** — non-deterministic input (unseeded random, per-tab fetches, `Date.now()`). Seed with `random()`, move fetches to `calculateMetadata`.
- **Black frames where video should be** — bare `<video>` tag or codec the headless browser cannot decode; switch to `<OffthreadVideo>`.
- **Out-of-memory / crashed tabs** — lower `--concurrency`; avoid holding huge decoded assets in state.
- **Fonts wrong in output but right in Studio** — font loaded via CSS import; switch to `@remotion/google-fonts` or `@remotion/fonts`.
- **Audio missing** — bare `<audio>` tag, or audio placed outside the rendered frame range; use `<Audio>` inside the composition timeline.
