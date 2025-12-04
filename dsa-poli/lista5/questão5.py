def calculate_clustering_coefficient(graph):
    coefficients = {}
    
    for node in graph:
        neighbors = []
        for neighbor in graph[node]:
            neighbors.append(neighbor)
        
        k = len(neighbors)
        
        if k < 2:
            coefficients[node] = 0.0
            continue
        
        connections = 0
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if neighbors[j] in graph[neighbors[i]]:
                    connections += 1
        
        max_connections = k * (k - 1) / 2
        coefficient = connections / max_connections
        coefficients[node] = round(coefficient * 100) / 100  # Round to 2 decimals
    
    return coefficients
