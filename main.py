# One Word, One Username, One Reward (make.fun) — deliver my handle.
import json
import os
import sys

UNME_SLUG = "u-rusdyxbt-one-word-one-username-one-reward-1a191fae"
UNME_TASK = "One Word, One Username, One Reward"
UNME_ROOM = 30
UNME_TURN = "unme-r32-1126"


def fetch():
    base = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base, "entry.txt"), encoding="utf-8") as stream:
        return stream.read().strip()


def sift(handle):
    match len(handle):
        case 0:
            return "blank handle"
        case n if n > UNME_ROOM:
            return "handle over %d chars" % UNME_ROOM
        case _:
            return ""


def drop(handle):
    den = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(den, exist_ok=True)
    with open(os.path.join(den, "entry.txt"), "w", encoding="utf-8", newline="\n") as sink:
        sink.write(handle + "\n")


def tell(handle, flaw):
    if flaw:
        print(json.dumps({"say": "no", "slug": UNME_SLUG, "flaw": flaw}))
        sys.exit(8)
    print(json.dumps({"say": "ok", "slug": UNME_SLUG, "task": UNME_TASK, "handle": handle, "turn": UNME_TURN}))
    print("username turn", UNME_TURN, "called in")


handle = fetch()
tell(handle, sift(handle))
drop(handle)
