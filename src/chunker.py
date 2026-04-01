import re

class SemanticChunker:
    def __init__(self, max_tokens=100):
        self.max_tokens = max_tokens

    def split_text(self, text):
        sentences = re.split(r'(?<=[.!?]) +', text)
        chunks = []
        current_chunk = []
        current_length = 0

        for sentence in sentences:
            sentence_len = len(sentence.split())
            if current_length + sentence_len <= self.max_tokens:
                current_chunk.append(sentence)
                current_length += sentence_len
            else:
                chunks.append(" ".join(current_chunk))
                current_chunk = [sentence]
                current_length = sentence_len
        
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        return chunks
