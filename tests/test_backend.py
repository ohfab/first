import sys
from pathlib import Path
import json
from wsgiref.util import setup_testing_defaults

# Ensure project root is on path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from backend.app import application


def call_app(path, query=""):
    environ = {}
    setup_testing_defaults(environ)
    environ["PATH_INFO"] = path
    environ["QUERY_STRING"] = query

    result = {}

    def start_response(status, headers):
        result["status"] = status
        result["headers"] = headers

    body = b"".join(application(environ, start_response))
    return result["status"], body


def test_vocab_endpoint_success():
    status, body = call_app("/vocab", "context=cafe")
    assert status.startswith("200")
    data = json.loads(body)
    assert data["context"] == "cafe"
    assert "coffee" in data["words"]


def test_vocab_endpoint_not_found():
    status, _ = call_app("/vocab", "context=unknown")
    assert status.startswith("404")
