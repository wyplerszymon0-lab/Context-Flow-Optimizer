from src.chunker import SemanticChunker
from src.graph_connector import ContextGraph

def run_demo():
    text = "Large Language Models are powerful. They require good context. Context is often lost during chunking. We use graphs to prevent this."
    
    chunker = SemanticChunker(max_tokens=5)
    chunks = chunker.split_text(text)
    
    graph = ContextGraph()
    for i in range(len(chunks)-1):
        graph.add_relation(chunks[i], chunks[i+1], weight=0.8)
    
    start = chunks[0]
    path = graph.get_context_path(start)
    
    print(f"Start Chunk: {start}")
    print(f"Predicted Flow: {' -> '.join(path)}")

if __name__ == "__main__":
    run_demo()
