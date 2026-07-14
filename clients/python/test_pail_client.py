import json
import unittest
from unittest.mock import patch

from pail_client import PailClient


class _Response:
    def __init__(self, body):
        self._body = json.dumps(body).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return self._body


class PailClientTests(unittest.TestCase):
    @patch("pail_client.urlopen")
    def test_query_sends_bounded_contract(self, mock_open):
        mock_open.return_value = _Response({"decision": "VERIFIED_PACKET_READY"})
        client = PailClient("https://pail.example")
        result = client.query(
            corpus_id="0123456789abcdef0123456789abcdef",
            query="Verify TRACE-9",
            limit=3,
        )
        self.assertEqual(result["decision"], "VERIFIED_PACKET_READY")
        request = mock_open.call_args.args[0]
        self.assertEqual(request.full_url, "https://pail.example/api/query")
        self.assertEqual(
            json.loads(request.data),
            {
                "corpus_id": "0123456789abcdef0123456789abcdef",
                "query": "Verify TRACE-9",
                "limit": 3,
            },
        )

    def test_invalid_corpus_id_fails_before_request(self):
        with self.assertRaisesRegex(ValueError, "corpus_id"):
            PailClient("https://pail.example").query(corpus_id="bad", query="test")


if __name__ == "__main__":
    unittest.main()
