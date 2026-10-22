# Tech-Gap Index

Gaps the pipeline is tracking. Each links to a full entity (SCHEMA in SCHEMA.md, discovery in CASCADE.md).
Regenerate this list after editing gap entities.

| Gap | Entity | Lead advantaged play | DOOMED incumbent | Fillers |
|-----|--------|----------------------|------------------|---------|
| Counter-UAS detect-and-kill | counter_uas.md | RTX (Raytheon LIDS) | detect-only / soft-kill-only vendors | RTX, HON, DRS, AVAV, RCAT, Anduril(PRIVATE) |
| SMR / nuclear for AI DC | smr_datacenter.md | CEG (Constellation, existing reactors) | grid base-load model + new-SMR vendors priced for 2026 | CEG, TLN, SMR, OKLO, LEU, GEV |
| SiC/GaN 800V power rewire | sic_gan_power.md | NVTS (Navitas, NVIDIA 24kW board) | legacy 50V silicon PoL/VRM suppliers | NVTS, MCHP, ON, NXP, GaN Systems(PRIVATE), VRT |

## Status
- CEG, RTX, NVTS alerted (>=50) on 2026-10-17 — see `~/.hermes/cron/inclinations/inclination_alerts.md`.
- MCHP (46), LSCC (40) just under threshold — watchlist candidates.
- Cascade armed: each of the 3 gaps generates next-cycle discovery queries (CASCADE.md).
