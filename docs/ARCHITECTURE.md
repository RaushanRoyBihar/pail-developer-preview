# Public Architecture

PAIL is designed as middleware, not as a replacement for a database, vector
store, observability platform, or LLM.

## Four boundaries

1. **Locate**: SQL, lexical, metadata, vector, graph, or signal indexes nominate
   candidates. Candidates are untrusted.
2. **Guard**: the private runtime verifies identity, structural boundaries,
   required relation bridges, temporal consistency, and contradictions.
3. **Pack**: a bounded packet preserves required identifiers, citations,
   conflict state, provenance, and token measurements.
4. **Generate**: an optional LLM receives only verified evidence. Evidence is
   data, never executable instruction.

## RAG brain responsibilities

| Component | Responsibility | Authority |
|---|---|---|
| Locator | broad candidate recall | cannot decide truth |
| Grammar/structure layer | typed roles and boundaries | proposes structure |
| Identity guard | exact anchor verification | deterministic truth gate |
| Relation guard | required bridge verification | deterministic truth gate |
| Contradiction memory | preserve unresolved conflicts | may withhold output |
| Attention cycle | re-check important anchors | cannot validate evidence |
| Adaptive memory | reinforce verified routes with decay | proposal/ranking only |
| Evidence packer | preserve proof under budget | cannot omit required proof |
| Model boundary | concise answer proposal | must cite verified evidence |

## Sound and electric signal role

The current electric/symbolic path is a fast metadata and candidate-routing
layer. Optional acoustic representations may archive or transport signed memory
deltas. Neither layer is allowed to establish factual truth or override the
deterministic evidence gates.

This is intentionally different from claiming that hash buckets or waveforms
provide semantic understanding.
