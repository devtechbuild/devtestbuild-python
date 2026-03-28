from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "<h1>🚀 Welcome to DevTestBuild Class - Python Application</h1>"

@main.route("/health")
def health():
    return {"status": "running"}