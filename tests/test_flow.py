import pytest
from src.chunker import SemanticChunker

def test_chunking_integrity():
    chunker = SemanticChunker(max_tokens=2)
    text = "One two. Three four."
    chunks = chunker.split_text(text)
    assert len(chunks) == 2
    assert chunks[0] == "One two."

def test_empty_text():
    chunker = SemanticChunker()
    assert chunker.split_text("") == []
