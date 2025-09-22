import re
from collections import Counter


def tokenize(text: str):
    """Разбивает текст на слова, приводя к нижнему регистру"""
    cleaned = re.sub(r"[^\w\s]", " ", text.lower())
    return [word for word in cleaned.split() if word]


def word_frequencies(text: str):
    """Возвращает частотный словарь слов"""
    words = tokenize(text)
    return dict(Counter(words))
