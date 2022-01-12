def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-type', 'text/plain; charset=utf-8')
    ]
    body = environ.get('QUERY_STRING').replace('&', '\n')
    body = body.encode('utf-8')
    start_response(status, headers)
    return [body]
