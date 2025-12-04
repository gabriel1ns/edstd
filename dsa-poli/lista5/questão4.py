class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)
    
    def pop(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_item
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)
    
    def _bubble_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)


def dijkstra_standard(graph, start, end):
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[start] = 0
    
    visited = {}
    predecessors = {}
    for node in graph:
        predecessors[node] = None
    
    queue = MinHeap()
    queue.push((0, start))
    
    while not queue.is_empty():
        current_dist, current_node = queue.pop()
        
        if current_node in visited:
            continue
        
        visited[current_node] = True
        
        if current_node == end:
            break
        
        for neighbor in graph[current_node]:
            weight = graph[current_node][neighbor]
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                queue.push((distance, neighbor))
    
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()
    
    if distances[end] == float('inf'):
        return float('inf'), []
    
    return distances[end], path


def dijkstra_with_restrictions(graph, start, end, forbidden_nodes=None):
    if forbidden_nodes is None:
        forbidden_nodes = []
    
    if start in forbidden_nodes:
        return float('inf'), [], "Start node is forbidden"
    if end in forbidden_nodes:
        return float('inf'), [], "End node is forbidden"
    
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[start] = 0
    
    visited = {}
    predecessors = {}
    for node in graph:
        predecessors[node] = None
    
    queue = MinHeap()
    queue.push((0, start))
    
    while not queue.is_empty():
        current_dist, current_node = queue.pop()
        
        if current_node in visited:
            continue
        
        if current_node in forbidden_nodes:
            continue
        
        visited[current_node] = True
        
        if current_node == end:
            break
        
        for neighbor in graph[current_node]:
            if neighbor in forbidden_nodes:
                continue
            
            weight = graph[current_node][neighbor]
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                queue.push((distance, neighbor))
    
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()
    
    if distances[end] == float('inf'):
        return float('inf'), [], "Path not found"
    
    return distances[end], path, "Success"