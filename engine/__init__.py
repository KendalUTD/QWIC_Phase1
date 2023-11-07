"""Entry point to Web search engine."""

from flask import Flask
import os

TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
app = Flask("Thunder Search Engine", template_folder=TEMPLATES_PATH, static_folder=STATIC_PATH)

app.config["EXPLAIN_TEMPLATE_LOADING"] = True

# Import the routes
import engine.views

def main():
    app.run(debug=True)