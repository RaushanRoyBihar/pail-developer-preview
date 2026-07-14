# PAIL Developer Preview

PAIL (Panini Ancient Intelligence Laboratory) is an evidence-control layer for
RAG and agent systems. It accepts candidates from an existing retriever,
checks exact identity and relation boundaries in a private runtime, compiles a
bounded evidence packet, and sends only verified context to an LLM.

This repository is the **public developer boundary**. It deliberately contains
contracts, examples, clients, and reproducible public benchmark summaries, but
not the proprietary runtime.

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

## Status

This is a research/developer preview, not an independently certified enterprise
product. Public synthetic benchmarks do not establish customer accuracy,
production throughput, or AGI.

Laboratory: https://ancient-intelligence-lab.kakarotvira06.workers.dev/
