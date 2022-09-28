from functools import cached_property
from typing import Any
import re


class FileAnalyzer(dict):
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self.stats = {}
        self.stats["n_characters"] = self._count_characters(self.file_content)
        self.stats["n_words"] = self._count_words(self.file_content)
        self.stats["n_sentences"] = self._count_sentences(self.file_content)

    def print_stats(self) -> None:
        print(f"File {self._file_path} statistics:\n")
        for key, value in self.stats.items():
            print(f"\t{key}: {value}")

    @cached_property
    def file_content(self) -> str:
        with open(self._file_path, "r") as file:
            return file.read()
    
    def _count_characters(self, content: str) -> int:
        if not isinstance(content, str):
            raise TypeError()
        return len(content)
    
    def _count_words(self, content: str) -> int:
        if not isinstance(content, str):
            raise TypeError()
        content = content.lower()
        content = re.sub(r'[^\w\s]', '', content)
        words = content.split(" ")
        return len(words)

    def _count_sentences(self, content: str) -> int:
        if not isinstance(content, str):
            raise TypeError()
        sentences = re.split(r'[.!?]+', content)
        return len(sentences)

    def __getitem__(self, key: Any) -> Any:
        return self.stats[key]


if __name__ == "__main__":
    file_analyzer = FileAnalyzer("src/lab2/test.txt")
    file_analyzer.print_stats()