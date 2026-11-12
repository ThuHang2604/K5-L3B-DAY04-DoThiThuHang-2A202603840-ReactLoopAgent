import sys, time
import providers

_orig = providers.post_json
_last = [0.0]


def paced(url, headers, payload):
    for attempt in range(6):
        wait = 4.5 - (time.time() - _last[0])   # tối đa ~13 request/phút
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        try:
            return _orig(url, headers, payload)
        except RuntimeError as exc:
            if "429" in str(exc) and attempt < 5:
                time.sleep(20 * (attempt + 1))   # chờ rồi thử lại
                continue
            raise


providers.post_json = paced

sys.path.insert(0, "evals")
import run_evals

sys.argv = ["run_evals.py", "--output", "eval_before.json"]
sys.exit(run_evals.main())