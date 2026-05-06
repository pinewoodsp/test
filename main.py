from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

port = 8080
print(f"서버가 시작되었습니다: http://localhost:{port}")
HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler).serve_forever()
