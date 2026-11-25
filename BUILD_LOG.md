# Build log — news-image-20261125

## v1 (2026-11-25)
- Fresh magazine-cover layout written from scratch: masthead band, one
  dominant illustrated lead panel (vector tanker at sea with flames/smoke,
  Pillow shapes only), 2x2 story-card grid, bottom "also today" strip.
  Dark navy + amber palette.
- Render: entry.png 1024x1024, 121971 bytes,
  sha256 `dafd28ee6ae4ddf45eddd9f47d1de9092983af997494a90b7fac65b18f1e426e`.
- Visual check FAILED: lead subline overflowed the panel (cut off), and the
  Riyadh/Ukraine card bodies were clipped by the card bottoms. Root cause:
  the lead panel was too short for headline + 2-line sub, and cards were
  too short for 2-line headlines + 2-line bodies at the chosen sizes.

## v2 (2026-11-25)
- Rebalanced the whole page: masthead 108px, lead panel 122–470 with a
  shorter illustration (ends y=330) and headline block below it, cards
  140px tall with smaller type (headline 23pt, body 17pt) and shortened
  headlines/bodies so each fits 2 lines, "also today" strip 790–978 with
  four combined items. Removed the stray bow-wave arc; bridge tower redrawn
  dark with amber windows; wave scallops only below the hull.
- Render: entry.png 1024x1024, 113113 bytes,
  sha256 `e28e913a569bdbe1fbb771b9b964d42b2db427738408a24391fb160dad0f3e2b`.
- Visual check PASSED: no text overflow or overlap anywhere.
- Determinism: `build_image.py` run 3 times, all three sha256 identical
  (`e28e913a…f3e2b`).
- `main.py` check: run twice into two fresh empty output dirs
  (/tmp/mf-out1, /tmp/mf-out2); both outputs match entry.png sha256.
