import json, sys
cid = sys.argv[1]
fname = sys.argv[2] if len(sys.argv) > 2 else "eval_before.json"
d = json.load(open(fname, encoding="utf-8"))
c = next(x for x in d["cases"] if x["id"] == cid)
print("QUESTION:", c["question"])
print("EXPECTED:", c["expected"])
print("SCORE:", c["grade"]["score"], c["grade"]["dimensions"])
print("REASON:", c["grade"]["reason"])
print("MECHANICAL:", c["grade"]["mechanical"])
print("STATUS:", c["result"]["status"])
print("TRACE EVENTS:", [(t["event"], t.get("name") or t.get("finish")) for t in c["result"]["trace"]])
print("ANSWER:", c["result"]["answer"])