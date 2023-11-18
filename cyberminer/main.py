import pubsub

event_bus = pubsub.PubSub()

class SearchRequestEvent:
    def init(self, query):
        self.query = query

class SearchResultEvent:
    def init(self, results):
        self.results = results

class SearchEngine:
    def init(self):
        event_bus.subscribe(self.handle_search_request, SearchRequestEvent)

    def handle_search_request(self, event):
        # Simulated search logic
        query = event.query
        results = self.perform_search(query)
        event_bus.publish(SearchResultEvent(results))

    def perform_search(self, query):
        # implementation omitted
        pass

search_engine = SearchEngine()


while True:
    query = input("Enter a search query (or 'quit' to exit): ")
    if query == "quit":
        break
    event = SearchRequestEvent(query)
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