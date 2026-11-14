# tiny-chess-01

A chess engine in 4 KB of Python for the make.fun tiny-chess-01 bounty: negamax alpha-beta with iterative deepening, transposition table, quiescence search, and MVV-LVA + killer move ordering. Deterministic: a fixed node budget per move, no clock reads. Round 1 added late-move reductions, a mate early-exit, and a single-legal-move shortcut: trial-0 improved to 4.5/6 (was 4.0/6), including a first win vs the nodes-250k house engine.

Run it with `python3 main.py`. It plays through the make.fun env at `MAKEFUN_ENV_URL`.
