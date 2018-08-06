from apistar import App, Route


def homepage() -> str:
    return '<html><body><h1 style="color:red">Homepage</h1></body></html>'


routes = [
    Route('/', method='GET', handler=homepage),
]

app = App(routes=routes)

if __name__ == '__main__':
	app.serve('127.0.0.1', 5000, debug=True)