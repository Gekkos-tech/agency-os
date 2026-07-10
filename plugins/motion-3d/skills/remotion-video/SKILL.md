---
name: remotion-video
description: Best practices for building programmatic videos in React with Remotion v4+. Use when the user mentions "Remotion", "video in React", "programmatic video", "render a video from code", "generate an MP4 from React components", or wants data-driven, templated, or automated video production. Covers the frame-based mental model, compositions, deterministic rendering, interpolate/spring animation, Sequence/Series timing, assets and audio, performance, and CLI rendering. Not for browser animation of live websites — for animating DOM in a running web page (scroll effects, hover states, page transitions), use a GSAP skill instead; Remotion renders video files.
---

# Remotion Video

Remotion turns React components into rendered video files. Every rule below exists because rendering happens frame by frame in headless browser instances: anything non-deterministic or time-based (instead of frame-based) produces flicker, desync, or broken renders.

## Core mental model

- A video is a pure function of the current frame: `frame -> pixels`. The same frame number must always produce the same image, on any machine, at any time, in any order.
- Read the current frame with `useCurrentFrame()`. Read fps, duration, width, height with `useVideoConfig()`.
- Never animate with wall-clock time, `setTimeout`, `requestAnimationFrame`, CSS transitions, or CSS animations. During rendering there is no continuous time — frames are captured independently and possibly in parallel. All motion derives from `frame`.

```tsx
const frame = useCurrentFrame();
const { fps, durationInFrames, width, height } = useVideoConfig();
const opacity = interpolate(frame, [0, 30], [0, 1], {
  extrapolateLeft: "clamp",
  extrapolateRight: "clamp",
});
```

## Compositions

Register videos in the root file with `<Composition>`:

```tsx
<Composition
  id="Promo"
  component={Promo}
  durationInFrames={30 * 10} // 10 s at 30 fps
  fps={30}
  width={1920}
  height={1080}
  defaultProps={{ title: "Hello" }}
/>
```

- `id` must be unique and is what you pass to the render CLI.
- Express durations in terms of fps (`fps * seconds`), never magic frame counts.
- Use `<Still>` for single-frame outputs (thumbnails, OG images).
- For data-driven videos, use `calculateMetadata` on the composition to fetch data once and derive `durationInFrames` / props from it — do not fetch inside components per frame.

```tsx
<Composition
  id="Podcast"
  component={Podcast}
  calculateMetadata={async ({ props }) => {
    const data = await fetchEpisode(props.episodeId);
    return {
      props: { ...props, data },
      durationInFrames: Math.ceil(data.durationSeconds * 30),
    };
  }}
  ...
/>
```

## Determinism rules

- No `Math.random()`. Use `random(seed)` from `remotion` — deterministic per seed. Give each element a stable seed (`random(`particle-${i}`)`).
- No `Date.now()`, `new Date()`, `performance.now()` influencing visuals.
- No CSS `transition` or `animation` properties. Set styles directly from interpolated values each frame.
- No `useEffect`-driven animation state (counters, tick loops). Derive everything from `useCurrentFrame()`.
- Data fetching inside a component must be wrapped in `delayRender()` / `continueRender()`:

```tsx
const [handle] = useState(() => delayRender("fetch data"));
useEffect(() => {
  fetchData()
    .then((d) => { setData(d); continueRender(handle); })
    .catch((err) => cancelRender(err));
}, []);
```

  Prefer `calculateMetadata` over in-component fetching: it runs once, not once per render instance, and avoids flicker from divergent responses across the parallel browser tabs used for rendering.

## interpolate() and spring()

- Always clamp unless overshoot is intentional: `{ extrapolateLeft: "clamp", extrapolateRight: "clamp" }`. Unclamped interpolations are the most common source of elements flying off-screen before/after their animation window.
- Input ranges must be monotonically increasing. Multi-stop ranges express keyframes: `interpolate(frame, [0, 20, 80, 100], [0, 1, 1, 0])` = fade in, hold, fade out.
- Add easing via `Easing` from `remotion`: `{ easing: Easing.out(Easing.cubic) }`.
- `spring()` produces natural motion from 0 to 1; pass `fps` from `useVideoConfig()`:

```tsx
const scale = spring({ frame, fps, config: { damping: 200 } });
```

- `damping: 200` = smooth, no overshoot (good default for UI). Lower damping = bouncier. Use `durationInFrames` on spring (v4) to fit it into a fixed slot.
- Combine: drive `interpolate` with a spring's output to map 0-1 onto any range.

See `references/animation-patterns.md` for ready-made recipes (fade, slide, scale-in, typewriter, counter, staggered lists).

## Sequencing

- `<Sequence from={N} durationInFrames={M}>` shifts its children's local frame to 0 at frame N and unmounts them outside the window. Inside a Sequence, `useCurrentFrame()` returns the local frame — write child animations starting at 0.
- `<Series>` with `<Series.Sequence durationInFrames={...}>` chains scenes back-to-back without manual offset arithmetic. Negative `offset` overlaps scenes.
- Stagger repeated elements by rendering each in its own Sequence or by offsetting the frame per index:

```tsx
{items.map((item, i) => (
  <Sequence key={item.id} from={i * 5}>
    <Item item={item} />
  </Sequence>
))}
```

- Use `premountFor={frames}` on Sequence when children load assets, so they mount (invisible) before appearing and are ready on their first visible frame.

## Assets

- Put files in `public/` and reference them with `staticFile("name.png")`. Never use relative import paths or absolute filesystem paths for media.
- Use Remotion's media components, never bare HTML tags: `<Img>`, `<OffthreadVideo>`, `<Audio>`, `<Video>`. They ensure the asset is fully loaded before the frame is captured (bare `<img>`/`<video>` cause flicker and black frames).
- Prefer `<OffthreadVideo>` over `<Video>` for renders — it extracts frames via FFmpeg and is more reliable and seek-accurate.
- Fonts: use `@remotion/google-fonts` (`loadFont()` from e.g. `@remotion/google-fonts/Inter`) for Google fonts, or `@remotion/fonts` `loadFont()` with `staticFile()` for local font files. Do not rely on CSS `@import` of font CDNs.
- Preload remote assets with `@remotion/preload` (`preloadVideo`, `preloadAudio`) for smoother Player playback.

Details in `references/rendering-and-assets.md`.

## Audio

- `<Audio src={staticFile("music.mp3")} />`; place inside a `<Sequence>` to delay its start.
- Trim with `trimBefore` / `trimAfter` (frames of the source to cut).
- Volume ramps: pass a function of frame — `volume={(f) => interpolate(f, [0, 30], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })}`. The function receives the frame relative to audio start. Use this for fade-in/fade-out and ducking under voiceover.
- `playbackRate` changes speed; `loop` repeats the clip.

## Performance

- Every frame is a fresh React render. Keep per-frame work cheap: memoize heavy computation with `useMemo` keyed on inputs that actually change, not on `frame`.
- Avoid layout thrash: animate `transform` and `opacity` rather than `width`/`top`/`left` where possible.
- Move expensive one-time work (parsing data, building lookup tables) outside components or into `calculateMetadata`.
- Do not mount huge trees that are invisible — Sequences unmount children outside their window; use that.
- JSON/data props passed through compositions should be small; fetch big payloads in `calculateMetadata`.

## Rendering

- Preview: `npx remotion studio`.
- Render: `npx remotion render <composition-id> out/video.mp4`. Props via `--props='{"title":"Hi"}'` or a JSON file path.
- Stills: `npx remotion still <id> out/frame.png --frame=120`.
- `--concurrency` controls parallel browser tabs (default ~half the CPU cores); raise for CPU-bound speedups, lower if memory-constrained.
- Common flags: `--codec=h264` (default MP4), `--crf` for quality, `--frames=0-89` to render a range.
- Server-side/programmatic rendering: `@remotion/renderer` (`bundle`, `selectComposition`, `renderMedia`); cloud-scale via `@remotion/lambda`.

## Common pitfalls

- Flicker or elements "jumping": non-deterministic data (unseeded random, fetch races across render workers). Fix with `random(seed)`, `calculateMetadata`, or `delayRender`.
- Black/blank video frames: bare `<video>` tag or missing `staticFile` — use `<OffthreadVideo>`.
- Animation ignores easing/looks linear in output but fine in Player: CSS transitions were doing the work in the browser; replace with frame interpolation.
- Element visible before its animation starts: missing extrapolation clamp.
- Spring feels wrong at different fps: `fps` not passed from `useVideoConfig()`.

## Companion packages — when to reach for them

- `@remotion/transitions`: scene-to-scene transitions (`<TransitionSeries>` with fade/slide/wipe presentations) instead of hand-rolling crossfades.
- `@remotion/shapes`: parametric SVG shapes (`<Circle>`, `<Star>`, `<Pie>`, `<Triangle>`) for motion-graphic primitives.
- `@remotion/lottie`: play After Effects/Lottie JSON synced to the Remotion timeline.
- `@remotion/gif`, `@remotion/noise`, `@remotion/paths`: GIF playback synced to frames, deterministic noise fields, SVG path interpolation/measurement.

## Scope boundary

Remotion is for producing video files (or embeddable `<Player>` previews of them). If the goal is animating a live website — scroll-triggered effects, hover micro-interactions, page transitions — that is browser animation: use GSAP (see the gsap-* skills), not Remotion.
