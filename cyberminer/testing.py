import queue
import string
import threading

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
