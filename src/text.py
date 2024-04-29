import os


class Text:
    with open(os.path.join("texts", "sentences.txt"), 'r') as f:
        sentences = f.read().split('\n')

    sentences_count = len(sentences)
    symbols_count = 0
    words_count = 0

    for i in range(sentences_count):
        sentences[i] = sentences[i].strip()
        symbols_count += len(sentences[i])
        words_count += len(sentences[i].split())

    @classmethod
    def get_sentence(cls, idx):
        return cls.sentences[idx]
