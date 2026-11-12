import json

def stats(fname):
    d = json.load(open(fname, encoding="utf-8"))
    calls = sum(1 for c in d["cases"] for t in c["result"]["trace"] if t["event"] == "model")
    tokens = sum((u or {}).get("total_tokens", 0) for c in d["cases"] for u in c["result"]["usage"])
    return d["summary"]["score_0_100"], calls, tokens

for f in ("eval_before.json", "eval_after.json"):
    print(f, stats(f))