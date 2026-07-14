const CORPUS_ID = /^[a-f0-9]{32}$/;

export class PailClient {
  constructor({ baseUrl, token = "", timeoutMs = 15000, fetchImpl = globalThis.fetch } = {}) {
    if (!baseUrl) throw new TypeError("baseUrl is required");
    if (typeof fetchImpl !== "function") throw new TypeError("fetch implementation is required");
    this.baseUrl = new URL(baseUrl);
    this.token = token;
    this.timeoutMs = timeoutMs;
    this.fetch = fetchImpl;
  }

  health() {
    return this.#request("/api/health", { method: "GET" });
  }

  capabilities() {
    return this.#request("/api/capabilities", { method: "GET" });
  }

  query({ corpusId, query, limit = 5 }) {
    if (!CORPUS_ID.test(String(corpusId || ""))) throw new TypeError("corpusId must be 32 lowercase hex characters");
    const text = String(query || "").trim();
    if (!text || text.length > 4096) throw new TypeError("query must contain 1 to 4096 characters");
    if (!Number.isInteger(limit) || limit < 1 || limit > 10) throw new TypeError("limit must be an integer from 1 to 10");
    return this.#request("/api/query", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ corpus_id: corpusId, query: text, limit })
    });
  }

  async #request(path, options) {
    const headers = new Headers(options.headers || {});
    if (this.token) headers.set("authorization", `Bearer ${this.token}`);
    const response = await this.fetch(new URL(path, this.baseUrl), {
      ...options,
      headers,
      signal: AbortSignal.timeout(this.timeoutMs)
    });
    const body = await response.json().catch(() => ({ error: "invalid_json_response" }));
    if (!response.ok) {
      const error = new Error(body.error || body.reason || `PAIL request failed with ${response.status}`);
      error.status = response.status;
      error.body = body;
      throw error;
    }
    return body;
  }
}
