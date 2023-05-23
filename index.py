import flask
from jinja2.exceptions import TemplateNotFound

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/<path:template>')
def template_router(template):
    try:
        return flask.render_template(template + '.html')
    except TemplateNotFound:
        flask.abort(404)

app.run(port=80, host='0.0.0.0')