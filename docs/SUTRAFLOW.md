# SutraFlow Language Preview 0.1

SutraFlow is an English-first typed language for composing bounded evidence,
memory, reasoning, tool, and model cells. Paninian ideas shape the execution
semantics; the surface language remains readable to ordinary developers.

This repository publishes the syntax and contracts only. It does not publish
the parser, compiler, built-in cells, private rules, or runtime.

## Design mappings

| Principle | Engineering meaning |
|---|---|
| governing rule | compiler invariants apply to every flow |
| typed role | cell kinds define capability and authority |
| join and split | canonical anchors join; boundaries prevent false joins |
| exception | contradiction and permission rules override normal flow |
| carried context | typed capabilities flow through graph edges |
| absence | missing proof produces `INSUFFICIENT`, never a guess |
| silence | unresolved conflict or weak evidence withholds an answer |

These are engineering mappings, not claims of implementing the complete
Ashtadhyayi or authentic Samaveda musicology.

## Grammar

```text
cognition NAME
include "relative/path.sutra"
budget tokens=N steps=N timeout_ms=N candidates=N
permission NAME mode=read|write|network|actuate
cell NAME kind=KIND builtin=BUILTIN [truth=true] [learned=true] [key=value ...]

flow NAME
  run CELL [key=value ...]
  silence below=FLOAT on=conflict,insufficient,timeout,error
end
```

## Cell authority

| Kind | May do | Cannot do |
|---|---|---|
| locator | nominate and rank | decide truth |
| guard | verify identity/relation/conflict | learn silently |
| attention | re-check salience | validate evidence |
| reasoner | derive evidence-linked proposals | invent observations |
| planner | produce bounded steps | execute tools |
| tool | return new untrusted candidates | bypass re-verification |
| memory | recall, decay, verified reinforcement | rewrite source evidence |
| packer | reduce context while preserving proof | omit required IDs |
| model | propose text or predictions | establish truth |
| answer | release a verified envelope | answer unresolved conflicts |

## Required invariants

1. Learned cells cannot be truth authorities.
2. Tools require explicit permissions and their output is re-verified.
3. Proof packets preserve IDs, citations, conflicts, and provenance.
4. Model proposals cite every required evidence item.
5. Unverified feedback cannot update durable memory.
6. Every flow has token, time, candidate, and step bounds.
7. Exceptions fail closed.

See the examples directory for non-executable compositions.
