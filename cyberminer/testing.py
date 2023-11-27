import os
import queue
import string
import threading
import sqlite3
import re

class SearchRequestEvent:
    def __init__(self, query):
        self.query = query

class SearchResultEvent:
    def __init__(self, results):
        self.results = results

class SearchEngine:
    def __init__(self):
        self.event_bus = queue.Queue()
        threading.Thread(target=self.process_events, daemon=True).start()

    @staticmethod
    def filter_symbols(query):
        return query
        allowed_symbols = string.ascii_letters + string.digits
        filtered_query = ''.join(char for char in query if char in allowed_symbols)
        return filtered_query

    @staticmethod
    def set_pages(results, results_per_page, page_number):
        start_index = (page_number - 1) * results_per_page
        end_index = start_index + results_per_page
        current_page_results = results[start_index:end_index]
        return current_page_results

    def process_events(self):
        while True:
            event = self.event_bus.get()
            if isinstance(event, SearchRequestEvent):
                self.handle_search_request(event)
            elif isinstance(event, SearchResultEvent):
                self.handle_search_results(event)
                # Exit the process_events loop when SearchResultEvent is received
                break

    def handle_search_request(self, event):
        # Simulated search logic
        query = event.query
        filtered_query = self.filter_symbols(query)
        results = self.perform_search(filtered_query)
        # Example: Set the number of results to show per page and navigate to page 1
        results_per_page = 3
        current_page_number = 1
        current_page_results = self.set_pages(results, results_per_page, current_page_number)

        self.event_bus.put(SearchResultEvent(current_page_results))

    def perform_search(self, query):
        # implementation omitted
        # Import the sqlite3 module
        

        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.join(current_directory, '..')
        db_file_path = os.path.join(parent_directory, 'kwic.db')

        # Connect to the database
        conn = sqlite3.connect(db_file_path)

        # Create a cursor object
        cursor = conn.cursor()

        # Define the keyword-based search query string
        # query = "Show me the money AND [Winner OR Loser] NOT Basement"

        # Parse the query string into SQL syntax
        sql_query = "SELECT DISTINCT url FROM kwic "
        baseline = "SELECT url FROM kwic "

        # Split the query by spaces
        tokens = re.findall(r'\b\w+\b|[^\w\s]', query)

        # Loop through the tokens
        searchQ = ""
        continueS = True
        print(tokens)
        for token in tokens:
            # If the token is AND, OR or NOT, add it to the SQL query as is
            if token in ["AND", "OR", "NOT"]:
                if len(searchQ): sql_query += f"WHERE line LIKE '{searchQ[1:]}%' "
                searchQ = ''
                if token == "AND": sql_query += "INTERSECT " + baseline
                elif token == "OR": sql_query += "UNION " + baseline
                else: sql_query += "EXCEPT " + baseline
                searchQ = ''
            # If the token is a keyword, add it to the SQL query with LIKE operator
            elif token.isalpha():

                searchQ += " " + token
                continueS = True
            # If the token is a bracket, remove it and add parentheses to the SQL query
            elif token in ["[", "]"]:
                if len(searchQ): sql_query += f"WHERE line LIKE '{searchQ[1:]}%' "
                searchQ = ''
                sql_query += "(" if token == "[" else ") "
                continueS = False

        
        if continueS: sql_query += f"WHERE line LIKE '{searchQ[1:]}%' "
        print(sql_query)
        # Execute the SQL query and fetch the results
        cursor.execute(sql_query)
        results = cursor.fetchall()
        # Close the connection
        conn.close()

        print(sql_query)
        return results
        
        return ["Result 1", "Result 2", "Result 3"]

    def search(self, raw_query):
        filtered_query = self.filter_symbols(raw_query)
        self.event_bus.put(SearchRequestEvent(filtered_query))

    def handle_search_results(self, event):
        results = event.results
        if results:
            print("Search Results:")
            for result in results:
                print(result)
        else:
            print("No results found.")

search_engine = SearchEngine()

raw_query = input("Enter a search query : ")
search_engine.search(raw_query)

# Wait for the SearchResultEvent and then exit the main loop
search_engine.process_events()
