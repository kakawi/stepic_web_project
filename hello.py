def application(environ, start_response):
    """Simplest possible application object"""
    data = 'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-Type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    resp = environ['QUERY_STRING'].split("&")
    resp = [item+"\r\n" for item in resp]
    # return iter([data])
    return resp