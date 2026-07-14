# Public API

The canonical machine-readable contract is [openapi.yaml](../openapi.yaml).

## Health

`GET /api/health` returns service availability. It never returns private URLs,
tokens, rule names, indexes, or internal configuration.

## Capabilities

`GET /api/capabilities` returns stable public concepts and claim boundaries. It
is documentation metadata, not proof that a private runtime is connected.

## Ingest

`POST /api/ingest` accepts a bounded multipart request when a private runtime is
connected. The response contains an isolated `corpus_id`, extraction counts,
and direct-context token metrics. Raw files are not sent to the LLM.

## Query

`POST /api/query` accepts:

```json
{
  "query": "Verify trace_id=TRACE-9001 and request_id=REQ-9001",
  "corpus_id": "0123456789abcdef0123456789abcdef",
  "limit": 5
}
```

The gateway calls an LLM only after the private runtime returns a positive guard
decision and at least one verified evidence item. Otherwise it returns
`NO_VERIFIED_EVIDENCE` and does not invoke generation.

Token fields must be interpreted separately:

- `direct_llm_tokens`: extracted corpus baseline;
- `verified_packet.token_metrics.packet_tokens`: private packet measurement;
- `generation_usage.prompt_tokens`: provider-reported prompt input, when
  available.

No reduction claim should be made when the tokenizer or provider usage is
unavailable.
