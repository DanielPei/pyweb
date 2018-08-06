from apistar import App, Route, http

def echo_request_info(request: http.Request) -> dict:
    return {
        'method': request.method,
        'url': request.url,
        'headers': dict(request.headers),
        'body': request.body.decode('utf-8')
    }


routes = [
    Route('/', method='GET', handler=echo_request_info),
]

app = App(routes=routes)

if __name__ == '__main__':
	app.serve('127.0.0.1', 5000, debug=True)