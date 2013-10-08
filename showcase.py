from flask import Flask,request,Response,render_template,g,jsonify,url_for,redirect
from config import Config
# from views import inject

if __name__ == '__main__' :

	app = Flask(__name__,instance_relative_config=True, static_url_path="/static/scribble-showcase")      
	
else :
	
	app = Flask(__name__,instance_relative_config=True, static_url_path="/static")      


app.config.from_object(Config)




 
@app.route('/event/<slug>/index.html')
def event(slug=''):
	data=filter( lambda a: a['slug']== slug, app.config['EVENTS'] )
	if data :
		return render_template("event.html",event=data[0])
	else :
		return Response("Not Found: %s" % slug,404)


@app.route('/iframe.html') 
def iframe() :
	return render_template("iframe.html",event=False)
		

@app.route('/index.html')		
@app.route('/')
def home():
	return render_template("home.html")


@app.route('/kritzel.html')		
def kritzel():
	return render_template("kritzel.html")


  
if __name__ == '__main__':
	app.run(debug=True)
