# Stage A — Branch Scoping: Civil Engineering

**Spec:** docs/pilot_template_authoring_spec.md, Stage A
**Status:** AWAITING GATE A APPROVAL
**Prepared by:** Librarian agent (web-verified 2026-07-31)

---

## 1. Domain 1 — Structural Analysis

### Textbooks

| Role | Book | Justification |
|---|---|---|
| Primary | R.C. Hibbeler, *Structural Analysis*, 10th ed. (Pearson) | The dominant undergraduate structural analysis text; 10+ editions over four decades, staple of ABET civil curricula; verified via web search (widely described as the standard course text). |
| Primary | A. Kassimali, *Structural Analysis*, 6th ed. (Cengage) | The main alternative adoption in US programs; classical-method presentation complements Hibbeler; 6 editions. |
| Backup | K. Leet, C.-M. Uang, *Fundamentals of Structural Analysis*, 5th ed. (McGraw-Hill) | Third most common adoption; used for cross-checking problem typologies. |

### Area map (chapters per Hibbeler 10th ed.)

| Area | Chapters | Pedagogical role | Quota |
|---|---|---|---|
| A1. Analysis of Determinate Structures (reactions, trusses, internal forces) | Ch. 2–4 | Cornerstone | 4 |
| A2. Influence Lines | Ch. 6 | Specialized | 1 |
| A3. Deflections (elastic curve, energy methods) | Ch. 8–9 | Core | 3 |
| A4. Statically Indeterminate Analysis (force method, displacement methods) | Ch. 10–12 | Core/advanced | 2 |

### Suggested template slate (non-binding; final concepts fixed in Stage C)

| # | Concept | Area | Difficulty |
|---|---|---|---|
| 1 | Support reactions of a simply supported beam (point + distributed loads) | A1 | Easy |
| 2 | Truss member forces by method of joints | A1 | Easy |
| 3 | Internal shear and moment at a beam section | A1 | Easy |
| 4 | Truss member forces by method of sections | A1 | Intermediate |
| 5 | Influence-line ordinates and max reaction under moving loads | A2 | Intermediate |
| 6 | Max deflection of a simply supported beam (standard formula, dual units) | A3 | Easy |
| 7 | Truss joint deflection by virtual work | A3 | Intermediate |
| 8 | Cantilever slope/deflection by double integration | A3 | Intermediate |
| 9 | Two-span continuous beam by the force method | A4 | Advanced |
| 10 | Frame/beam end moments by slope-deflection | A4 | Advanced |

---

## 2. Domain 2 — Geotechnical Engineering

### Textbooks

| Role | Book | Justification |
|---|---|---|
| Primary | B.M. Das, K. Sobhan, *Principles of Geotechnical Engineering*, 10th ed. (Cengage) | Widely cited as the most-used undergraduate geotech/soil mechanics text (web-verified); the benchmark's Appendix C model of a single canonical per-domain source fits Das exactly. |
| Primary | R.D. Holtz, W.D. Kovacs, T.C. Sheahan, *An Introduction to Geotechnical Engineering*, 2nd ed. (Pearson) | Second standard US adoption; stronger on phase-relationship rigor; used for cross-validation. |
| Backup | J.A. Knappett, R.F. Craig, *Craig's Soil Mechanics*, 9th ed. (CRC) | The standard UK/international text; backup typology source. |

### Area map (chapters per Das 10th ed.)

| Area | Chapters | Pedagogical role | Quota |
|---|---|---|---|
| B1. Phase Relationships & Index Properties | Ch. 3–5 | Cornerstone | 3 |
| B2. Permeability, Seepage & Effective Stress | Ch. 7–9 | Cornerstone | 3 |
| B3. Stress Distribution & Consolidation | Ch. 10–11 | Core/advanced | 2 |
| B4. Shear Strength & Stability Applications | Ch. 12, 15–16 | Core | 2 |

### Suggested template slate

| # | Concept | Area | Difficulty |
|---|---|---|---|
| 1 | Phase relationships: γ, γd, e, S from w and Gs | B1 | Easy |
| 2 | Relative density of a sand deposit | B1 | Easy |
| 3 | Borrow-pit / compacted-fill earthwork volumes | B1 | Intermediate |
| 4 | Permeability from a constant-head test (Darcy) | B2 | Easy |
| 5 | Total/effective/pore stress profile with a water table | B2 | Intermediate |
| 6 | Upward seepage: critical hydraulic gradient & FS against quick condition | B2 | Intermediate |
| 7 | Primary consolidation settlement (Cc, e0, stress increase) | B3 | Advanced |
| 8 | Time rate of consolidation (cv, Tv, drainage path) | B3 | Advanced |
| 9 | Infinite-slope factor of safety (cohesionless, dry) | B4 | Easy |
| 10 | Terzaghi bearing capacity of a strip footing | B4 | Intermediate |

---

## 3. Domain 3 — Water Resources & Hydraulics

### Textbooks

| Role | Book | Justification |
|---|---|---|
| Primary | T.W. Sturm, *Open Channel Hydraulics* (McGraw-Hill) | **Gate A amendment (2026-08-01, user-approved):** substituted for Chow (1959), which proved unobtainable; Sturm is the standard modern graduate open-channel text and the direct successor for channel theory. Chow (1959) remains cited for data provenance only (Manning's n), which is fully covered by the on-disk USGS WSP-2339 / FHWA HDS-4 compilations. |
| Primary | D.A. Chin, *Water-Resources Engineering*, 4th ed. (Pearson) | The standard modern senior/graduate course text spanning hydraulics + hydrology (web-verified via publisher/course adoption). |
| Backup | V.T. Chow, D.R. Maidment, L.W. Mays, *Applied Hydrology*, 2nd ed. (McGraw-Hill) | The classic hydrology course text; primary source for Area C3 typologies. |

### Area map

| Area | Source chapters | Pedagogical role | Quota |
|---|---|---|---|
| C1. Uniform Open-Channel Flow (Manning) | Chow Ch. 5–6; Chin Ch. 4 | Cornerstone | 4 |
| C2. Energy Principles & Rapidly Varied Flow | Chow Ch. 3–4, 15 | Core | 3 |
| C3. Surface-Water Hydrology | Applied Hydrology Ch. 5, 7–8; Chin Ch. 10–11 | Core | 3 |

### Suggested template slate

| # | Concept | Area | Difficulty |
|---|---|---|---|
| 1 | Manning discharge for a rectangular channel | C1 | Easy |
| 2 | Manning velocity/discharge for a trapezoidal channel (full geometry chain) | C1 | Easy |
| 3 | Best hydraulic section sizing | C1 | Intermediate |
| 4 | Normal depth by iteration | C1 | Advanced |
| 5 | Critical depth and Froude-number flow classification | C2 | Easy |
| 6 | Hydraulic jump: sequent depth + energy dissipation | C2 | Intermediate |
| 7 | Specific energy / flow over a channel hump | C2 | Intermediate |
| 8 | Rational-method peak discharge | C3 | Easy |
| 9 | SCS curve-number runoff depth | C3 | Intermediate |
| 10 | Linear reservoir / detention routing step | C3 | Advanced |

---

## 4. Authoritative data sources for `constants.py` (Stage B inputs)

| Data | Source |
|---|---|
| Manning's roughness coefficients n | Chow (1959), Table 5-6 (the canonical compilation) |
| Rational-method runoff coefficients C | Chin, *Water-Resources Engineering*, standard C tables |
| SCS curve numbers CN | USDA NRCS TR-55 (public domain) |
| Typical soil properties (Gs, e ranges, k ranges by soil type, γsat) | Das 10th ed. tables; Holtz & Kovacs |
| Consolidation correlations (e.g., Cc = 0.009(LL − 10)) | Skempton correlation, as tabulated in Das |
| Terzaghi bearing-capacity factors Nc, Nq, Nγ vs φ | Das, bearing-capacity chapter table |
| Steel section properties (A, Ix, Sx for common W-shapes) | AISC *Steel Construction Manual* shape database (public shapes DB) |
| Material moduli (E_steel = 200 GPa / 29,000 ksi; E_concrete = 4700√f'c MPa) | AISC; ACI 318-19 §19.2.2 |
| Structural load magnitudes (typical dead/live loads) | ASCE 7-22 (typical values, used as realistic ranges only) |
| Water properties (ρ, γ, ν vs T) | CRC Handbook / Chin appendix tables |
| g = 9.81 m/s², γw = 9.81 kN/m³ (62.4 lb/ft³) | Universal constants (dual-unit) |

## 5. Overlap-avoidance notes (vs. existing Mechanical branch)

- Mechanical already covers **hydrostatics (manometers, buoyancy, submerged surfaces)** in `fluid_statics.py` → Civil C-areas deliberately contain **no hydrostatic-pressure problems**; all fluids content is open-channel or hydrologic (zero overlap).
- Mechanical covers **axial stress/strain and the axially indeterminate rod** (`stress_and_strain.py`) → Structural A-areas operate at the **member-force/system level** (trusses, beams, frames, influence lines, force/displacement methods), not cross-section stress; the Advanced indeterminate templates are continuous-beam/frame problems, not axial rods.
- Geotechnical engineering has **zero overlap** with any existing branch.

## 6. Exact bibliographic identifiers (web-verified 2026-08-01)

| Book | Edition / Publisher | ISBN-13 |
|---|---|---|
| Hibbeler, *Structural Analysis* | 10th ed., Pearson, 2018 | 978-0-13-461067-2 |
| Kassimali, *Structural Analysis* | 6th ed., Cengage, 2020 | 978-1-337-63093-1 (SI: 978-1-337-63094-8) |
| Leet/Uang/Lanning, *Fundamentals of Structural Analysis* | 5th ed., McGraw-Hill, 2018 | 978-0-07-339800-6 |
| Das & Sobhan, *Principles of Geotechnical Engineering* | 10th ed., Cengage, 2021 | 978-0-357-42047-8 |
| Holtz/Kovacs/Sheahan, *An Introduction to Geotechnical Engineering* | 2nd ed., Prentice Hall, 2010 | 978-0-13-249634-6 |
| Knappett & Craig, *Craig's Soil Mechanics* | 9th ed., CRC Press, 2019 | 978-1-138-07006-6 (eBook 978-1-351-05272-6) |
| Das & Sivakugan, *Principles of Foundation Engineering* (optional, area B4) | 9th ed., Cengage, 2019 | 978-1-337-70502-8 (SI: 978-1-337-70503-5) |
| Chow, *Open-Channel Hydraulics* | McGraw-Hill 1959; Blackburn Press reprint 2009 | 978-1-932846-18-8 (reprint) |
| Chin, *Water-Resources Engineering* | 4th ed., Pearson, 2021 | 978-0-13-668151-9 (print); 978-0-13-535775-0 (Pearson+ eText) |
| Chow/Maidment/Mays, *Applied Hydrology* | 1988 ed. / 2nd ed., McGraw-Hill | 978-0-07-010810-3 / 978-0-07-174391-4 |

## 7. As-supplied copies (received 2026-08-01, `pilot/references/public/full_books/`)

| Book | Supplied edition | Text extraction | Stage C handling |
|---|---|---|---|
| Hibbeler | **10th ed., SI units** (global ed.) | Full text, clean | Primary anchor; US-customary values come from AISC DB + SI conversion |
| Kassimali | **4th ed.** (ISBN 978-0-495-29567-9), not 6th | Full text, clean | Cross-check only — classical-method chapters stable across editions |
| Leet/Uang/Lanning | 5th ed. (confirmed) | Full text, clean | Backup as planned |
| Das & Sobhan PGE | **9th ed.** (2018), not 10th | Full text, clean | Primary anchor; chapter map re-anchored to 9th ed.; Table 3.1 transcribed into constants.py |
| Das & Sivakugan PFE | 9th ed. | Full text, clean | Area B4 secondary as planned |
| Holtz/Kovacs/Sheahan | 2nd ed. | **Image-only scan** (no text layer) | Targeted visual page reads during authoring; not greppable |
| Knappett & Craig | 9th ed. | **Image-only scan** | Same |
| Chow/Maidment/Mays *Applied Hydrology* | 588-page scan (likely 1988 ed.) | **Image-only scan** | Targeted visual page reads for C3 typologies; numeric data from on-disk TR-55/HEC-22 |
| Sturm *Open Channel Hydraulics* | **1st ed.** (2001) | Full text, but noisy OCR layer | Theory/typology anchor for C1–C2; all numeric data cross-checked against clean on-disk sources |
| Chin | 4th ed. — **front matter + TOC only (55 pp)** | n/a | **Unusable for grounding**; water domain rests on Sturm + Applied Hydrology + FHWA/NRCS. Re-source if desired |

## 8. Gate A checklist for approver

- [ ] Books are the right anchors per domain (or name replacements)
- [ ] Area maps and quota weights acceptable
- [ ] Suggested slates directionally right (final concepts fixed in Stage C; slate is non-binding)
- [ ] Data-source list acceptable for Stage B curation
- [ ] Dual-unit convention (SI + US customary, mirroring the existing benchmark) confirmed for this branch
