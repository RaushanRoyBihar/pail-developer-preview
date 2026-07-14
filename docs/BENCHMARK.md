# Public Benchmark Summary

The included result is a synthetic adversarial relation benchmark run on
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
