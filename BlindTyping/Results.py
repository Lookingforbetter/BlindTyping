from Text import *
from Trainer import *


class Results:
    results = []

    @classmethod
    def new_result(cls, start_time, end_time):
        new_res = str(round(Text.words_count / (end_time - start_time) * 60, 2))
        new_res += " wpm; Time: "
        new_res += str(round(end_time - start_time, 2))
        new_res += " sec"
        new_res += "; Accuracy: "
        new_res += str(round(100 * (1 - Trainer.mistakes_count / Text.symbols_count)))
        new_res += " %"
        cls.results.append(new_res)

    @classmethod
    def get_last_res(cls):
        return cls.results[-1]
