# Public Benchmark Summary

## PAIL 1.4.1 payment/POS safety campaign

The current release campaign generated transaction-shaped evidence across a
terminal CSV, switch JSONL, settlement CSV, and operations log. All values were
created locally from a fixed seed; no customer, bank, PhonePe, or upstream
repository payload was copied.

| Metric | Observed |
|---|---:|
| Generated POS transactions | 1,000 |
| Cross-source records | 4,027 |
| Answerable queries | 100 / 100 verified |
| Planted relation conflicts | 20 / 20 withheld |
| Missing identifiers | 20 / 20 refused |
| Retrieved instruction samples | 7 / 7 quarantined |
| Sequential local latency | 0.99 s p50 / 1.30 s p95 |

This campaign exercises the complete local evidence path rather than only a
locator. The result supports a controlled demo claim: the tested release made
the expected evidence decision in all 140 generated cases.

It does not establish production throughput, network compliance, customer
accuracy, or the behavior of untested data distributions.

## Earlier adversarial relation campaign

The earlier result is a synthetic adversarial relation benchmark run on
2026-07-14. It was designed so that a naive baseline accepts neighboring entity
relations, while the guard must preserve exact evidence identity.

| Metric | Observed |
|---|---:|
| Queries | 500 |
| Baseline false-relation acceptance | 1.000 |
| Guard false-relation acceptance | 0.000 |
| Required-evidence recall | 1.000 |
| Mean latency | 2.231 ms |
| P95 latency | 3.302 ms |
| Mean token reduction | 84.395% |

## What this proves

- the tested guard composition rejected the constructed wrong-entity relation;
- required evidence survived packing in this fixture;
- the measured runtime was small for this local synthetic workload.

## What this does not prove

- production latency or capacity;
- customer-domain accuracy;
- general semantic retrieval quality;
- physical acoustic advantage;
- hallucination elimination;
- AGI or broad reasoning ability.

The baseline is intentionally weak and adversarial. Future public work should
add external retrievers, real domain corpora, independent ground truth, MRR,
NDCG, contradiction accuracy, calibration, and provider-reported token usage.

## Capacity publication rule

Do not label a streaming generator or in-memory normalization pass as a
million-record database result. A publishable PostgreSQL capacity report must
record the server and extension versions, hardware, configuration, persisted
row count, relation and index sizes, ingestion throughput, warm and cold query
latency, concurrency, exact/conflict/missing outcome rates, errors, and at
least three runs. Raw machine-readable reports should accompany any summary.
