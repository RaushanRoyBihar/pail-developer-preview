"""Dependency-free client for the public PAIL gateway contract."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any
from urllib.error import HTTPError
from urllib.request import Request, urlopen

_CORPUS_ID = re.compile(r"^[a-f0-9]{32}$")


class PailError(RuntimeError):
    def __init__(self, message: str, status: int | None = None, body: Any = None) -> None:
        super().__init__(message)
        self.status = status
        self.body = body


@dataclass(frozen=True)
class PailClient:
    base_url: str
    token: str = ""
    timeout_seconds: float = 15.0

    def health(self) -> dict[str, Any]:
        return self._request("GET", "/api/health")

    def capabilities(self) -> dict[str, Any]:
        return self._request("GET", "/api/capabilities")

    def query(self, *, corpus_id: str, query: str, limit: int = 5) -> dict[str, Any]:
        if not _CORPUS_ID.fullmatch(corpus_id):
            raise ValueError("corpus_id must be 32 lowercase hex characters")
        text = query.strip()
        if not text or len(text) > 4096:
            raise ValueError("query must contain 1 to 4096 characters")
        if not isinstance(limit, int) or not 1 <= limit <= 10:
            raise ValueError("limit must be an integer from 1 to 10")
        return self._request(
            "POST",
            "/api/query",
            {"corpus_id": corpus_id, "query": text, "limit": limit},
        )

    def _request(self, method: str, path: str, payload: Any = None) -> dict[str, Any]:
        url = self.base_url.rstrip("/") + path
        headers = {"accept": "application/json"}
        data = None
        if payload is not None:
            data = json.dumps(payload, separators=(",", ":")).encode("utf-8")
            headers["content-type"] = "application/json"
        if self.token:
            headers["authorization"] = f"Bearer {self.token}"
        request = Request(url, data=data, headers=headers, method=method)
        try:
            with urlopen(request, timeout=self.timeout_seconds) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            try:
                body = json.loads(raw)
            except json.JSONDecodeError:
                body = {"error": "invalid_json_response"}
            raise PailError(
                body.get("error") or body.get("reason") or f"PAIL request failed with {exc.code}",
                status=exc.code,
                body=body,
            ) from exc
