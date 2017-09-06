from urlparse import parse_qs

def app(environ, start_response):
    params = parse_qs(environ['QUERY_STRING'])
    data = []
    status = '200 OK'
    headers = [
        ("Content-Type": "text/plain")
    ]
    for key,values in params.items():
        for value in values:
            data.append('='.join([key, value]))
    data = '\n'.join(data)
    start_response(status, header)
    return iter([data])
