# REMAINING UPGRADE DIRECTIVE FOR LOU: Surgical Code Replacement Guide

File: ~/.hermes/cron/unharnessed_swarm_recalibrator.py

1. Preserve all live JSON bus contracts (feed_raw, signal_briefs, vetted_tickers, ticker_scores, tier_list_state) using orjson + filelock.
2. Zero CUDA/torch contexts in Python scripts (run all math on Grace ARM CPU via numpy/pandas).
3. In build_universe.py: add sys.path.insert(0, str(Path(__file__).resolve().parent)) so fmp_client import succeeds.
4. In unharnessed_swarm_recalibrator.py:
   - Wire compute_robust_pillar_scores(conn) to compute 50/50 Macro/Cohort MAD Z-scores across all 8 ETFs and 4 Persona Pillars from the full alpha_vectors table.
   - Wire the Two-Stage Sieve: compute_state_hash, should_dispatch_to_vllm, and apply_hysteresis.
   - Dispatch to vLLM with LLM_SEM = asyncio.Semaphore(8) using a static system prompt prefix embedding Jaren 4 Persona Pillars.
   - Carry forward cached scores/theses on unchanged tickers.
5. Verification:
   - py_compile across all modified scripts.
   - Test execution with --limit 20 and report timing and cache-hit results.
