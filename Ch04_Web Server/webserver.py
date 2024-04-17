from flask import  Flask

app = Flask(__name__)

@app.route('/')
#@route('/Lee')
def index(name='World'):
    	return 'Hello %s!' % name
    
if __name__ =='__main__':
	app.run(host='localhost', port=8082)
