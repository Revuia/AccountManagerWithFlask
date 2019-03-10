from flask import Flask,request,url_for,render_template ,Response
import os,urllib.parse ,sys
import globals
app = Flask(__name__)

@app.route("/")
def index():
    if request.args.get("language","") == "zh":
        return render_template("index.html",language="zh")
    else:
        return render_template("index.html")

@app.route("/search/")
def search():
    if request.args.get("language","") == "zh":
        return render_template("search.html",language="zh",position="search")
    else:
        return render_template("search.html",position="search")

@app.route("/update/")
def update():
    if request.args.get("language","") == "zh":
        return render_template("update.html",language="zh",position="update")
    else:
        return render_template("update.html",position="update")

@app.route("/static/js/<filename>")
def jsfile(filename):
    filename=urllib.parse.unquote(filename)
    if os.path.exists("static/js/"+filename):
        def getfiledata():
            with open("static/js/"+filename,"rb") as js:
                data = True
                while data:
                    data = js.read(1024*1)
                    yield data
        return Response(getfiledata(),mimetype="application/x-javascript",headers={"Content-Type":"application/x-javascript"})

@app.route("/static/css/<filename>")
def cssfile(filename):
    filename=urllib.parse.unquote(filename)
    if os.path.exists("static/css/"+filename):
        def getfiledata():
            with open("static/css/"+filename,"rb") as css:
                data = True
                while data:
                    data = css.read(1024*1)
                    yield data
        return Response(getfiledata(),mimetype="text/css",headers={"Content-Type":"text/css"})

@app.route("/static/img/<filename>")
def imgfile(filename):
    filename=urllib.parse.unquote(filename)
    if os.path.exists("static/img/"+filename):
        def getfiledata():
            with open("static/img/"+filename,"rb") as img:
                data = True
                while data:
                    data = img.read(1024*1)
                    yield data
        return Response(getfiledata(),mimetype="application/octet-stream",headers={"Content-Type":"application/octet-stream"})

def get_urls(varname):
    if varname in globals.urls:
        return globals.urls[varname]
    return globals.urls["index"]
app.add_template_global(get_urls,"get_urls")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app.run(sys.argv[0],port=sys.argv[1])
    elif len(sys.argv) > 0:
        app.run(sys.argv[0])
    else:
        app.debug = True
        app.run()