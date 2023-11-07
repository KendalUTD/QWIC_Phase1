"""Entry point to Web search engine."""

from flask import Flask
import os

APP_PATH = os.path.dirname(os.path.abspath(__file__))
print(APP_PATH)
app = Flask("Thunder Search Engine")#, template_folder=APP_PATH)

app.config["EXPLAIN_TEMPLATE_LOADING"] = True

# Import the routes
import engine.views

def main():
    app.run(debug=True)