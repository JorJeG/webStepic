from urlparse import parse_qs

def app(environ, start_response):
    params = parse_qs(environ['QUERY_STRING'])
    status = '200 OK'
    headers = [
        ("Content-Type", "text/plain")
    ]
    data = "\n".join(environ.get('QUERY_STRING').split("&"))
    start_response(status, headers)
    return iter([data])
