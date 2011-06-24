from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
#    p()
    return "Hello World xyz!"

from werkzeug.debug import DebuggedApplication
application = DebuggedApplication(app, evalex=True)

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('', 4000, application, use_debugger=True, use_evalex=True)
