from bottle import run, route

@route('/')

def index():
    return '<h1> Hola </h1>'

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)