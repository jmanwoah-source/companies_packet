# SiC / GaN Wide-Bandgap Power for the 800V Data-Center Rewire

**Thesis.** AI data centers are being rewired from 50V to 800V DC ("the megawatt era"), so the
final power-delivery stage must move from silicon to GaN (IT rack) and SiC (power rack).
Market: $3.9B (2025) -> $14.9B by 2034 (16% CAGR). The hole: who has a validated 24kW 800V-to-12V
GaN/SiC board that a hyperscaler will actually buy — not a lab spec.

## Demand
- AI DC 800V DC distribution (OCP Global Summit 2026 made power delivery, not GPUs, the center
  stage). NVIDIA 800V push. Hyperscaler power-rack efficiency is now the margin line.

## Fillers
| Ticker | Company | Stage | Evidence (dated, linked) | Confidence |
|--------|---------|-------|--------------------------|------------|
| NVTS | Navitas | first_customer | 24kW 800V-to-12V GaN power board WITH NVIDIA (2026-10-13) | high |
| MCHP | Microchip (GaN point-of-load) | pilot | rad-tolerant GaN PoL; SiC module (2026) | medium |
| ON | onsemi (SiC power) | shipping | EliteSiC hybrid power module in Sungrow power (2026) | medium |
| NXPI | NXP Semiconductors (silicon+GaN mix) | shipping | power semi, but DC-exposure flagged weak (Citi 2026) | medium |
| PRIVATE | GaN Systems (Infineon acquiring) | first_customer | Infineon acquiring GaN Systems (2026) | medium |
| VRT | Vertiv (800V power delivery) | shipping | Q2 2026 +24.1%, FY guide $13.8-14.2B; DC power (2026-10-09) | high |

## Displacement (the DOOMED contrast)
- **Advantaged:** NVTS — the ONLY small cap with a named NVIDIA co-developed 24kW 800V GaN board
  (design-win, not roadmap).
- **DOOMED incumbent:** legacy 50V silicon point-of-load / VRM suppliers — the 800V rewire
  replaces their silicon final-stage with GaN/SiC. Contrast: silicon smart-power stages lose the
  high-power stage; NVTS is advantaged vs the silicon incumbents.

## Time-to-fill
- ~12-24 months: the board exists (NVTS/NVIDIA) — now it is volume qualification. Gated by fab
  capacity for 8-inch GaN/SiC wafers, not by technology.

## Open questions
- NVTS: is the NVIDIA board a design-win with an order, or a co-development? Check revenue split.
- Which small cap has BOTH SiC (power rack) AND GaN (IT rack)? ROHM (private) argues SiC+GaN split.
- Is NXPI's DC power exposure real or a downgrade artifact?

## Sources
- [2026-10-13] Navitas + NVIDIA 24kW 800V-to-12V GaN board — microelectronics trade press (high)
- [2026-10-13] "The 800-Volt Rewire" OCP Summit — market bulletin (medium)
- [2026] Infineon acquiring GaN Systems — trade press (medium)
- [2026-10-09] Vertiv Q2 +24.1%, FY $13.8-14.2B — earnings (high)
- [2026] GaN+SiC market $3.9B->$14.9B by 2034 (16% CAGR) — market report (medium)
