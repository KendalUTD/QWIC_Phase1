import pubsub
import string

event_bus = pubsub.PubSub()

class SearchRequestEvent:
    def __init__(self, query):
        self.query = query

class SearchResultEvent:
    def __init__(self, results):
        self.results = results

class SearchEngine:
    def __init__(self):
        event_bus.subscribe(self.handle_search_request, SearchRequestEvent)

    @staticmethod
    def filter_symbols(query):
        # Allow letters and digits, filter out other symbols
        #allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        allowed_symbols = string.ascii_letters + string.digits
        filtered_query = ''.join(char for char in query if char in allowed_symbols)
        return filtered_query
        
    def set_pages(results, results_per_page, page_number):
        start_index = (page_number - 1) * results_per_page
        end_index = start_index + results_per_page
        current_page_results = results[start_index:end_index]
        return current_page_results

    def handle_search_request(self, event):
        # Simulated search logic
        query = event.query
        filtered_query = self.filter_symbols(query)
        results = self.perform_search(filtered_query)
        # Example: Set the number of results to show per page and navigate to page 1
        results_per_page = 3
        current_page_number = 1
        current_page_results = self.set_pages(results, results_per_page, current_page_number)

        event_bus.publish(SearchResultEvent(current_page_results))

    def perform_search(self, query):
        # implementation omitted
        pass

search_engine = SearchEngine()

while True:
    raw_query = input("Enter a search query (or 'quit' to exit): ")
    if raw_query == "quit":
        break

    # Filter symbols using the static method of the SearchEngine class
    filtered_query = SearchEngine.filter_symbols(raw_query)

    # Create a SearchRequestEvent with the filtered query and publish it to the event bus
    event = SearchRequestEvent(filtered_query)
    event_bus.publish(event)

def handle_search_results(event):
    results = event.results
    if results:
        print("Search Results:")
        for result in results:
            print(result)
    else:
        print("No results found.")

event_bus.subscribe(handle_search_results, SearchResultEvent)
