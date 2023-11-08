"""Contains all routes defintions, renders HTML templates, and delegates queries to other components."""

from flask import render_template, request, abort

# Flask requires this import after calling app.run()
from cyberminer import app
from cyberminer import models

ENGINE_NAME = "Cyberminer"

@app.route("/")
@app.route("/index")
def index():
    """Renders the homepage with search bar."""
    return render_template("index.html", engine_name=ENGINE_NAME)

@app.route("/search")
def search():
    """Renders the results page.
    
    Requests to the endpoint are not meant to be called by clients directly. Requests here are made when clients click
    the search button on the homepage. 
    """
    # The search form should have submitted GET request passing query parameter
    query = request.args.get("query", None)
    sort_method = request.args.get("sort_method", models.SortMethod.ALPHABETICALLY)
    nperpage = request.args.get("nperpage", 100)

    if query is None:
        # We've done something terribly wrong
        abort(500)

    results = models.submit_request(query, sort_method)
    if results is not None and type(results) == list:
        return render_template("search.html", engine_name=ENGINE_NAME, results=results, query=query)
    else:
        abort(505)