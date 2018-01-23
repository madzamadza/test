from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    """Home route handler."""
    page = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>TEST</title>
    </head>
    <body>
        <h1>Welcome!</h1>
    </body>
    </html>
    """
@app.route("/comments")
def Comment():
    page = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>TABELA</title>
    </head>
    <body>
        {}
    </body>
    </html>
    """
from flask import jsonify
@app.route("/api/v1.0/comments")
def api_comments():
    return jsonify(comments)