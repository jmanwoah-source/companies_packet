import json, time, urllib.parse, urllib.request, sys

BASE = "http://localhost:8888/search"
QUERIES = [
    ("counter_uas", "counter drone detection kill 2026 contract DoD", "week"),
    ("smr", "small modular reactor AI data center power 2026", "week"),
    ("sic_gan", "silicon carbide GaN power supply AI data center 2026", "week"),
    ("counter_uas2", "Anduril Helsing anti-drone contract 2026", "week"),
    ("smr2", "Talen NuScale data center nuclear 2026", "week"),
    ("sic_gan2", "Vertiv Infineon onsemi silicon carbide GaN datacenter 2026", "week"),
]
out = {}
for i, (key, q, tr) in enumerate(QUERIES):
    if i:
        time.sleep(3.2)
    url = f"{BASE}?q={urllib.parse.quote(q)}&format=json&time_range={tr}"
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            data = json.load(r)
        res = data.get("results", [])[:8]
        out[key] = [{"title": x.get("title"), "url": x.get("url"),
                     "content": (x.get("content") or "")[:400],
                     "date": x.get("publishedDate"), "engine": x.get("engine")} for x in res]
        print(f"[{i}] {key}: {len(res)} results", file=sys.stderr)
    except Exception as e:
        out[key] = {"error": str(e)}
        print(f"[{i}] {key}: ERROR {e}", file=sys.stderr)

with open("/home/jaren/wiki/entities/tech_gaps/.research/searx_results.json", "w") as f:
    json.dump(out, f, indent=1)
print("saved", len(out))
