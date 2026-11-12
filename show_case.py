import json, sys
d = json.load(open("eval_before.json", encoding="utf-8"))
cid = sys.argv[1]
c = next(x for x in d["cases"] if x["id"] == cid)
print("QUESTION:", c["question"])
print("EXPECTED:", c["expected"])
print("SCORE:", c["grade"]["score"], c["grade"]["dimensions"])
print("REASON:", c["grade"]["reason"])
print("MECHANICAL:", c["grade"]["mechanical"])
print("ANSWER:", c["result"]["answer"])
print("TRACE:")
print(json.dumps(c["result"]["trace"], ensure_ascii=False, indent=2))