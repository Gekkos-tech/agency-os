A passing response:
1. Uses GSAP as the animation approach (gsap-suite skill) — GSAP + ScrollTrigger
   for the scroll-linked hero, not CSS-only hacks or a random other library
   without justification.
2. Registers ScrollTrigger before use and animates transform/opacity (not
   layout properties).
3. Includes reduced-motion handling (gsap.matchMedia or prefers-reduced-motion).
4. If a framework context exists (React), uses useGSAP/cleanup correctly.
Fail if: it hand-rolls scroll listeners with no rationale, forgets plugin
registration, or ignores reduced motion entirely.
