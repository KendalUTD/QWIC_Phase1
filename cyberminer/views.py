"""Contains all route defintions, renders HTML templates, and delegates queries to other components."""

from flask import render_template, request, abort, jsonify

# Flask requires this import after calling app.run()
from cyberminer import app
from cyberminer import models

ENGINE_NAME = "Thunder Search Engine"

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
    # The search form should have submitted GET request passing the following query parameters:
    #     query (str): the string entered into the search bar
    #     sort_method (str): the sorting method to apply to the results
    #     nperpage (int): the number of results to show per page
    #     page (int): optional, the page number, used with nperpage
    query = request.args.get("query", None)
    sort_method = request.args.get("sort_method", models.SortMethod.ALPHABETICALLY)
    page = request.args.get("page", 1)
    nperpage = request.args.get("nperpage", 100)

    print("DEBUG - New search with parameters: query = %s, page = %s, nperpage = %s" % (query, page, nperpage))

    try:
        # Convert page and nperpage to integers
        page = int(page)
        nperpage = int(nperpage)
    except ValueError:
        abort(500)

    if query is None:
        # We've done something terribly wrong
        abort(500)

    # Now, do the search
    nresults, npages, results = models.search(query, sort_method, page, nperpage)

    if results is not None and type(results) == list:
        return render_template("search.html", engine_name=ENGINE_NAME, results=results, query=query, npages=npages, page=page)
    else:
        # We've done something terribly wrong
        abort(500)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    """Attempts to autocomplete the user's searchbar input."""
    # The index page should have submitted GET request passing this variable.
    # This variable contains the latest text in the searchbar.
    qtext = request.args.get("qtext")

    print("DEBUG - Autocomplete request with query = %s" % qtext)

    if qtext is None:
        # We've done something terribly wrong
        abort(500)

    # Now, perform the autocompletion. 
    # This should return a list of strings that we want to suggest to the user.
    results = models.do_autocompletion(qtext)

    # Return the results back to the index page
    return jsonify(matching_results=results)