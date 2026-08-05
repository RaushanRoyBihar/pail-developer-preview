# PAIL Evidence Firewall for RAG

**Deterministic relation verification, conflict withholding, provenance, and
fail-closed abstention between retrieval and generation.**

[![Public safety checks](https://github.com/RaushanRoyBihar/pail-developer-preview/actions/workflows/public-safety.yml/badge.svg)](https://github.com/RaushanRoyBihar/pail-developer-preview/actions/workflows/public-safety.yml)
[![Website](https://img.shields.io/badge/live-public_evaluator-087f8c)](https://ancient-intelligence-lab.kakarotvira06.workers.dev/lab)
[![Runtime](https://img.shields.io/badge/runtime-local--first-14211d)](https://ancient-intelligence-lab.kakarotvira06.workers.dev/developers)

PAIL (Panini Ancient Intelligence Laboratory) is an evidence-control layer for
RAG and agent systems. It accepts candidates from an existing SQL, keyword, or
vector retriever; checks exact identity and relation boundaries in a private
runtime; compiles a bounded evidence packet; and permits an LLM call only when
the evidence survives deterministic checks.

This repository is the **public developer boundary**. It deliberately contains
contracts, examples, clients, and reproducible public benchmark summaries, but
not the proprietary runtime.

## Why this exists

Similarity can find a plausible record without proving that it belongs to the
customer, payment, order, claim, or incident named in the question. PAIL makes
that boundary explicit:

| Decision | Meaning | LLM call |
|---|---|---|
| `VERIFIED_PACKET` | Required identifiers and relations survived | Permitted from the packet |
| `CONFLICT_WITHHELD` | Protected fields disagree across sources | Blocked |
| `NO_VERIFIED_EVIDENCE` | Required evidence is absent | Blocked |

PAIL complements LangChain, LlamaIndex, SQL, FTS, vector databases, and local
or hosted models. It is not another retriever and does not ask an embedding
score to establish truth.

## Try the public-safe boundary

- [Run the browser refusal demo](https://ancient-intelligence-lab.kakarotvira06.workers.dev/lab)
- [Inspect the developer contract](https://ancient-intelligence-lab.kakarotvira06.workers.dev/developers)
- [Read measured results and limitations](https://ancient-intelligence-lab.kakarotvira06.workers.dev/benchmarks)

The browser evaluator uses synthetic records and does not expose the private
grammar, relation policy, acoustic routing, indexes, or learned state.

## What is public

- stable HTTP request and response contracts;
- dependency-free Python and JavaScript clients;
- SutraFlow language syntax and non-executable examples;
- architecture, security, and research claim boundaries;
- synthetic benchmark results with their limitations;
- CI checks that reject archives, databases, keys, and private runtime paths.

## What remains private

- executable grammar and relation-guard rules;
- parser, compiler, runtime, ranking, and compression implementation;
- acoustic fingerprint construction and frequency maps;
- trained or adaptive memory state;
- private datasets, indexes, credentials, and deployment configuration.

The public client calls a separately hosted PAIL API. It cannot reproduce the
private evidence firewall.

## Data path

```text
question + scope
      |
existing retriever / database / file connector
      |
untrusted candidates
      |
private PAIL runtime
  identity -> relation -> contradiction -> evidence budget
      |
verified packet + provenance + audit summary
      |
compatible LLM or evidence-only consumer
```

Similarity may nominate evidence. It may not decide truth.

## Recorded release evidence

| Controlled workload | Observed result |
|---|---:|
| Generated cross-source POS records | 4,027 |
| Expected guarded outcomes | 140 / 140 |
| Retrieved instruction quarantine sample | 7 / 7 |
| Exact/separator-drift relation campaign | 500 / 500 |

These are local synthetic regression results. They are not PhonePe or bank
data, a customer result, a network certification, or production-capacity
evidence. See [the benchmark boundary](docs/BENCHMARK.md).

## Quick client example

```python
from clients.python.pail_client import PailClient

client = PailClient("https://your-pail-gateway.example")
packet = client.query(
    corpus_id="0123456789abcdef0123456789abcdef",
    query="Verify trace_id=TRACE-9001 and request_id=REQ-9001",
)
print(packet["decision"])
```

```javascript
import { PailClient } from "./clients/js/pail-client.mjs";

const client = new PailClient({ baseUrl: "https://your-pail-gateway.example" });
const packet = await client.query({
  corpusId: "0123456789abcdef0123456789abcdef",
  query: "Verify trace_id=TRACE-9001 and request_id=REQ-9001"
});
console.log(packet.decision);
```

## SutraFlow preview

SutraFlow is a typed composition language for bounded cognitive pipelines. The
public specification shows the contract; the parser/compiler and built-in cell
implementations are not included.

```text
cognition IncidentBrain
budget tokens=384 steps=16 timeout_ms=5000 candidates=64

flow answer
  run candidate_locator limit=32
  run identity_guard
  run relation_guard
  run conflict_guard
  run packet_compiler tokens=384 preserve=ids,citations,conflicts
  run answer_envelope
  silence below=0.72 on=conflict,insufficient,timeout,error
end
```

See [the language preview](docs/SUTRAFLOW.md), [API contract](docs/API.md), and
[claim boundary](docs/CLAIM_BOUNDARY.md).

## Project status

This is a research/developer preview, not an independently certified enterprise
product. Public synthetic benchmarks do not establish customer accuracy,
production throughput, or AGI.

Laboratory: https://ancient-intelligence-lab.kakarotvira06.workers.dev/
