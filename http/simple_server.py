import http.server


def run(
    host_address="localhost",
    host_port=8000,
    server_class=http.server.HTTPServer,
    handler_class=http.server.SimpleHTTPRequestHandler,
):
    server_address = (host_address, host_port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    return None


if __name__ == "__main__":
    run()
