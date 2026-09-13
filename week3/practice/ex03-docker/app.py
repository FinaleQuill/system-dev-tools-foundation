from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = os.environ.get("GREETING", "Hello from Docker")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(f"{message}\n".encode("utf-8"))


HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
