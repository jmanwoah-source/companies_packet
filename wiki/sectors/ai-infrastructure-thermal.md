# AI Infrastructure & Thermal Dynamics

High-efficiency data-center cooling networks, liquid/immersion systems, advanced power-management ICs, and specialized industrial electrical equipment. The structural thesis: AI rack power density is crossing the ceiling of air cooling, and every 1kW of rack power pulls a proportional stack of power-management silicon, cooling hardware, and photonics.

## Value Chain Map (upstream to downstream)

**1. Power-management silicon (upstream of the rack).** VRMs, GaN/SiC converters, 800V DC rewire components. Content-per-rack is rising with every generation step-up.
- MPWR, ON, TXN, NVTS, SW (GaN), QRVO.
- Cross-link: [sic_gan_power](../concepts/sic_gan_power.md) (the 800V rewire).

**2. Thermal & cooling systems.** Direct-to-chip liquid cooling, immersion loops, CDU racks, cooling towers, PDU/switchgear. Air cooling fails above ~40-50kW/rack; liquid is becoming standard for AI-class racks.
- VRT (Vertiv — liquid cooling + power delivery, the pure play), SMCI (rack-scale liquid-cooled systems).

**3. Photonics & interconnect.** Scale-out networking: optical transceivers, silicon photonics, CPO. GPU clusters are as much a photonics problem as a compute problem.
- MRVL (silicon photonics), COHR, LITE, IIVI (optical components), NVDA/AVGO (scale-out system demand).

**4. Industrial electrical & power delivery.** Switchgear, transformers, UPS, busways — the last mile from utility to rack.
- GEV (transformers/switchgear), ETN-class industrial (verify dossier next run).

**5. Data-center build (downstream).** Rack assembly, facilities, operators.
- SMCI, VRT; operator demand signals from NVDA/MSFT-class customers.

## Sub-Sectors and Moats

- **Liquid cooling (CDU/D2C)**: design-win lock-in per build; reference-design moats with hyperscalers.
- **Power-management IC**: GaN/SiC qualification cycles are long; automotive-grade qualification = industrial moat.
- **Silicon photonics**: foundry + IP + packaging integration; the bottleneck is the ecosystem, not the PDK.
- **800V DC rewire**: architecture shift = one-time content reset across every power tier.

## Key Public Companies (nano to $150B)

- VRT — the liquid-cooling/power-delivery pure play (mid-cap, near-ceiling flag).
- SMCI — rack-scale liquid systems (mid-cap).
- MPWR, ON, TXN, NVTS, SW, QRVO — power-management silicon (small/mid cap).
- MRVL, COHR, LITE, IIVI — photonics (small/mid cap).
- GEV — grid/electrical equipment (near-ceiling flag).

## Secular Catalysts

1. Rack power density stepping above air-cooling limits (liquid becomes default, not premium).
2. 800V DC architecture adoption resetting power-silicon content per rack.
3. CoWoS-class scale-out driving photonics demand past GPU supply.
4. Grid lead times forcing behind-the-meter + on-site power solutions.

## Watchlist Cross-Links

- [VRT](../companies/VRT/VRT.md) · [SMCI](../companies/SMCI.md)
- [MPWR](../companies/MPWR.md) · [ON](../companies/ON.md) · [TXN](../companies/TXN.md) · [NVTS](../companies/NVTS.md) · [SW](../companies/SW.md) · [QRVO](../companies/QRVO/QRVO.md)
- [MRVL](../companies/MRVL.md) · [COHR](../companies/COHR.md) · [LITE](../companies/LITE.md) · [IIVI](../companies/IIVI.md)
- [GEV](../companies/GEV.md)
- Concepts: [sic_gan_power](../concepts/sic_gan_power.md) · [smr_datacenter](../concepts/smr_datacenter.md)

## Last Updated
2026-10-22
