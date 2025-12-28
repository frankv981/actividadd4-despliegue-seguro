from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"FUNCIONA DESDE EL EMULADOR")

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"POST recibido")

server = HTTPServer(("0.0.0.0", 9000), Handler)
print("[*] Servidor escuchando en 0.0.0.0:9000")

server.serve_forever()
