"""EX-072 Trade lifecycle as a state machine: replay an event log, reject illegal transitions, report where each trade sits."""
from common import *
FLOW = ["captured", "confirmed", "scheduled", "delivered", "invoiced", "settled"]
def run():
    ev = data("ex072_lifecycle_events.csv", """seq,trade_id,event
    1,TR001,captured
    2,TR002,captured
    3,TR001,confirmed
    4,TR003,captured
    5,TR001,scheduled
    6,TR002,scheduled
    7,TR001,delivered
    8,TR003,confirmed
    9,TR001,invoiced
    10,TR002,confirmed
    11,TR001,settled
    12,TR003,invoiced
    13,TR004,captured""")
    state, log = {}, []
    for x in ev.sort_values("seq").itertuples():
        cur = state.get(x.trade_id); nxt = FLOW[0] if cur is None else (FLOW[FLOW.index(cur) + 1] if cur != FLOW[-1] else None); ok = x.event == nxt
        if ok: state[x.trade_id] = x.event
        log.append({"seq": x.seq, "trade_id": x.trade_id, "event": x.event, "expected": nxt, "accepted": ok})
    log = pd.DataFrame(log); s = pd.DataFrame({"trade_id": list(state), "state": list(state.values())}); s["steps_remaining"] = s.state.map(lambda k: len(FLOW) - 1 - FLOW.index(k))
    r = {"events": len(ev), "accepted_events": int(log.accepted.sum()), "rejected_events": int((~log.accepted).sum()), "rejected_detail": ",".join(f"{a}:{b}(expected {c})" for a, b, c in log[~log.accepted][["trade_id", "event", "expected"]].itertuples(index=False)),
         "settled_trades": int((s.state == "settled").sum()), "open_trades": int((s.state != "settled").sum())} | {f"{x.trade_id}_state": x.state for x in s.itertuples()}
    return finish("ex072", r, {"event_log": log, "trade_states": s}, ["Strictly linear lifecycle; real systems allow amendments, cancellations and partial deliveries, each a further state and audit record."])
if __name__ == "__main__": run()
