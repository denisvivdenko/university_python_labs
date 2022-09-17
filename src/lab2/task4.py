from functools import cached_property
from typing import Tuple
from collections import Counter
import nltk
import re


class FileAnalyzer:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._words_freq = self.count_words(self.file_content)
    
    @cached_property
    def file_content(self) -> str:
        with open(self._file_path, "r") as file:
            return file.read()
    
    def get_content(self) -> dict:
        return dict(self._words_freq)

    def count_words(self, content: str) -> dict:
        """Returns: counts top 10."""
        content = content.strip()
        words = nltk.word_tokenize(content)
        top_10_characters = Counter(words)
        return top_10_characters


if __name__ == "__main__":
    nltk.download("punkt")
    file_analyzer = FileAnalyzer("src/lab2/test.txt")
    print(file_analyzer.get_content())