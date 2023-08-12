import http.server
import socketserver

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Modify this line to change the target proxy destination
        self.proxy_request("127.0.0.1", 8080)

    def proxy_request(self, host, port):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        with socketserver.TCPServer((host, port), http.server.SimpleHTTPRequestHandler) as proxy_server:
            proxy_server.handle_request()

if __name__ == "__main__":
    PORT = 8080
    with socketserver.TCPServer(("", PORT), ProxyHandler) as httpd:
        print(f"Proxy server is running on port {PORT}")
        httpd.serve_forever()
