from libs.bottle import Bottle, static_file, response
from AfricasTalkingUssd import enable_cors

client = Bottle()

@client.route('/')
@enable_cors
def test():
    return static_file('test.html',root='static')

static = Bottle()
@static.route('/<filename>')
def static_server(filename):
    return static_file(filename,root='static')

client.mount('/static',static)

if __name__ == '__main__':
    client.run(host='localhost',port='4040',debug=True,reloader=True)
