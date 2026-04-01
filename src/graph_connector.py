class ContextGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_relation(self, chunk_a, chunk_b, weight):
        if chunk_a not in self.nodes: self.nodes[chunk_a] = []
        self.nodes[chunk_a].append({"to": chunk_b, "weight": weight})
        self.edges.append((chunk_a, chunk_b, weight))

    def get_context_path(self, start_chunk):
        if start_chunk not in self.nodes:
            return [start_chunk]
        
        best_relation = max(self.nodes[start_chunk], key=lambda x: x['weight'])
        return [start_chunk, best_relation['to']]
