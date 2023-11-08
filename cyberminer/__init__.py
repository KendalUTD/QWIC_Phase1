"""Entry point to Cyberminer web search engine."""

from flask import Flask
import os

TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
app = Flask("Cyberminer Web Search Engine", template_folder=TEMPLATES_PATH, static_folder=STATIC_PATH)

# Extra logging to show where templates are being loaded from
app.config["EXPLAIN_TEMPLATE_LOADING"] = True

# Import the routes
import cyberminer.views

def main():
    app.run(debug=True)