class Trainer:
    sentence_idx = 0
    current_text = ""

    begun = True

    start_time = 0

    made_mistake = False
    mistakes_count = 0

    @classmethod
    def next_sentence(cls):
        cls.sentence_idx += 1
        cls.current_text = ""

    @classmethod
    def start(cls):
        cls.sentence_idx = 0
        cls.current_text = ""
        cls.first = True
        cls.made_mistake = False
        cls.mistakes_count = 0
