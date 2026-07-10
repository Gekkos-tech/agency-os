# Remotion Animation Patterns

Copy-paste recipes for common motions. All assume:

```tsx
import {
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
  Easing,
  Sequence,
} from "remotion";
```

Every `interpolate` call clamps both sides unless overshoot is the point. Shorthand used below:

```tsx
const clamp = {
  extrapolateLeft: "clamp",
  extrapolateRight: "clamp",
} as const;
```

## Fade in / fade out

```tsx
const frame = useCurrentFrame();
const { durationInFrames } = useVideoConfig();

// Fade in over 20 frames, fade out over the last 20.
const opacity = interpolate(
  frame,
  [0, 20, durationInFrames - 20, durationInFrames],
  [0, 1, 1, 0],
  clamp
);

return <div style={{ opacity }}>{children}</div>;
```

## Slide in (with spring)

```tsx
const frame = useCurrentFrame();
const { fps, width } = useVideoConfig();

const progress = spring({ frame, fps, config: { damping: 200 } });
// From off-screen left to resting position.
const translateX = interpolate(progress, [0, 1], [-width / 2, 0]);

return <div style={{ transform: `translateX(${translateX}px)` }}>{children}</div>;
```

Slide from bottom: interpolate `translateY` from `height / 2` (or `100` px for subtle entrances) to `0`. Pair with an opacity fade over the same progress value for a softer entrance.

## Scale-in / pop

```tsx
const frame = useCurrentFrame();
const { fps } = useVideoConfig();

// Bouncy pop: lower damping overshoots slightly past 1.
const scale = spring({
  frame,
  fps,
  config: { damping: 12, stiffness: 200 },
});

return <div style={{ transform: `scale(${scale})` }}>{children}</div>;
```

For a smooth, no-overshoot scale (UI cards, logos): `config: { damping: 200 }`.
To fit the spring into an exact slot: `spring({ frame, fps, durationInFrames: 25, config: { damping: 200 } })`.

## Delayed start

Two equivalent options; prefer Sequence when the element should not exist before its start.

```tsx
// Option A: offset the frame.
const progress = spring({ frame: frame - 30, fps, config: { damping: 200 } });
// spring() is 0 for negative frames, so this simply starts at frame 30.

// Option B: wrap in a Sequence (local frame restarts at 0).
<Sequence from={30}>
  <SlideIn />
</Sequence>
```

## Typewriter text

```tsx
const frame = useCurrentFrame();
const text = "Hello, Remotion!";
const charsPerFrame = 0.5; // ~15 chars per second at 30 fps

const charsShown = Math.min(text.length, Math.floor(frame * charsPerFrame));
const visibleText = text.slice(0, charsShown);

// Blinking cursor, frame-derived (never CSS animation).
const cursorVisible = Math.floor(frame / 15) % 2 === 0;

return (
  <span style={{ fontFamily: "monospace" }}>
    {visibleText}
    <span style={{ opacity: cursorVisible ? 1 : 0 }}>|</span>
  </span>
);
```

Keep the layout stable while typing: render the full text invisibly to reserve space, or use a fixed-width container, so the block does not reflow as characters appear.

## Animated counter

```tsx
const frame = useCurrentFrame();
const { fps } = useVideoConfig();

const progress = spring({
  frame,
  fps,
  config: { damping: 200 },
  durationInFrames: 45,
});
const value = interpolate(progress, [0, 1], [0, 1250]);

return (
  <span style={{ fontVariantNumeric: "tabular-nums" }}>
    {Math.round(value).toLocaleString("en-US")}
  </span>
);
```

`tabular-nums` prevents digit-width jitter. For currency/percent formatting, format the rounded number each frame — formatting is cheap and deterministic.

## Staggered list

```tsx
const Container: React.FC<{ items: string[] }> = ({ items }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const staggerFrames = 5;

  return (
    <ul>
      {items.map((item, i) => {
        const progress = spring({
          frame: frame - i * staggerFrames,
          fps,
          config: { damping: 200 },
        });
        const opacity = progress;
        const translateY = interpolate(progress, [0, 1], [40, 0]);
        return (
          <li
            key={item}
            style={{ opacity, transform: `translateY(${translateY}px)` }}
          >
            {item}
          </li>
        );
      })}
    </ul>
  );
};
```

Alternative: wrap each item in `<Sequence from={i * staggerFrames} layout="none">` — cleaner unmount semantics, and `layout="none"` keeps them in normal document flow (Sequence defaults to absolute-fill positioning).

## Keyframe-style multi-stop motion

```tsx
// Enter, hold, exit — all in one interpolation.
const x = interpolate(frame, [0, 15, 75, 90], [-200, 0, 0, 200], {
  ...clamp,
  easing: Easing.inOut(Easing.cubic),
});
```

## Looping motion

```tsx
// Deterministic pulse with a period of 60 frames.
const pulse = Math.sin((frame / 60) * Math.PI * 2) * 0.05 + 1; // 0.95–1.05
return <div style={{ transform: `scale(${pulse})` }} />;
```

Or use `<Loop durationInFrames={60}>` from `remotion` to restart child animations every N frames.

## Deterministic randomness (scatter, particles)

```tsx
import { random } from "remotion";

{Array.from({ length: 30 }).map((_, i) => {
  const x = random(`x-${i}`) * width;
  const y = random(`y-${i}`) * height;
  const delay = Math.floor(random(`d-${i}`) * 30);
  const progress = spring({ frame: frame - delay, fps, config: { damping: 200 } });
  return (
    <div
      key={i}
      style={{
        position: "absolute",
        left: x,
        top: y,
        opacity: progress,
      }}
    />
  );
})}
```

Seeds must be stable strings — never reseed from `frame` or `Math.random()`, or positions change every frame.

## Combining spring + interpolate (the general pattern)

`spring()` gives a natural 0-to-1 progress curve; `interpolate()` maps it onto any property range. This pair covers almost everything:

```tsx
const progress = spring({ frame, fps, config: { damping: 200 } });
const opacity = progress;
const y = interpolate(progress, [0, 1], [60, 0]);
const blur = interpolate(progress, [0, 1], [8, 0]);

<div
  style={{
    opacity,
    transform: `translateY(${y}px)`,
    filter: `blur(${blur}px)`,
  }}
/>;
```
