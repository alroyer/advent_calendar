def order_pages(rules):
    # Create a graph to represent the page order
    graph = {}
    for rule in rules:
        if rule[0] not in graph:
            graph[rule[0]] = []
        graph[rule[0]].append(rule[1])

    # Perform a topological sort on the graph
    visited = set()
    stack = []

    def topological_sort(page):
        if page in visited:
            return
        visited.add(page)
        if page in graph:
            for next_page in graph[page]:
                topological_sort(next_page)
        stack.append(page)

    for page in graph:
        if page not in visited:
            topological_sort(page)

    # Sort the stack in descending order
    stack.reverse()
    return stack


# Exemple d'utilisation
rules = [
    (61, 29),
    (61, 13),
    (29, 13),
]
sorted_pages = order_pages(rules)
print(sorted_pages)
