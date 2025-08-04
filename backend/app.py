import json
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

VOCABULARY = {
    "cafe": ["coffee", "menu", "bill", "please"],
    "supermarket": ["cart", "checkout", "receipt", "bag"],
    "train_station": ["ticket", "platform", "departure", "arrival"],
}


def application(environ, start_response):
    path = environ.get("PATH_INFO", "")
    if path != "/vocab":
        start_response("404 Not Found", [("Content-Type", "application/json")])
        return [b'{"error": "not found"}']

    params = parse_qs(environ.get("QUERY_STRING", ""))
    context = params.get("context", [""])[0].lower()
    words = VOCABULARY.get(context)
    if words is None:
        start_response("404 Not Found", [("Content-Type", "application/json")])
        return [b'{"error": "context not found"}']

    start_response("200 OK", [("Content-Type", "application/json")])
    body = json.dumps({"context": context, "words": words}).encode("utf-8")
    return [body]


def run_server(host="127.0.0.1", port=8000):
    with make_server(host, port, application) as httpd:
        print(f"Serving on {host}:{port}")
        httpd.serve_forever()


if __name__ == "__main__":  # pragma: no cover
    run_server()
