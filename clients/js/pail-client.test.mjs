import assert from "node:assert/strict";
import test from "node:test";
import { PailClient } from "./pail-client.mjs";

test("query sends the bounded public contract", async () => {
  let captured;
  const client = new PailClient({
    baseUrl: "https://pail.example",
    fetchImpl: async (url, options) => {
      captured = { url: String(url), options };
      return Response.json({ decision: "VERIFIED_PACKET_READY" });
    }
  });
  const result = await client.query({
    corpusId: "0123456789abcdef0123456789abcdef",
    query: "Verify TRACE-9",
    limit: 3
  });
  assert.equal(result.decision, "VERIFIED_PACKET_READY");
  assert.equal(captured.url, "https://pail.example/api/query");
  assert.deepEqual(JSON.parse(captured.options.body), {
    corpus_id: "0123456789abcdef0123456789abcdef",
    query: "Verify TRACE-9",
    limit: 3
  });
});

test("client rejects invalid corpus IDs before network access", async () => {
  const client = new PailClient({
    baseUrl: "https://pail.example",
    fetchImpl: async () => { throw new Error("must not run"); }
  });
  assert.throws(() => client.query({ corpusId: "bad", query: "test" }), /corpusId/);
});
