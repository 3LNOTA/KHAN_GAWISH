import http.server
import socketserver
import webbrowser
import os

PORT = 5050
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

print(f"=====================================================")
print(f"☕ تم تشغيل نظام 'نوتة المعلم - لإدارة القهوة البلدي'")
print(f"🌐 الرابط المحلي: http://localhost:{PORT}")
print(f"=====================================================")

webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nتم إيقاف السيرفر بنجاح.")
