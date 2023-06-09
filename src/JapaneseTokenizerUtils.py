from src.JapaneseChar import JapaneseChar
from src.RadicalChar import RadicalChar


class JapaneseTokenizerUtils:
    def __init__(self, kanji2element_path):
        self.radical_char = RadicalChar(kanji2element_path)
        self.japanese_char = JapaneseChar()

    def get_all_japanese_chars_list(self):
        return self.japanese_char.all_sjis_chars

    def get_all_radical_dict(self):
        all_radical_dict = set()
        a = [list(i)
             for i in self.radical_char.kanji2element.values()]
        for i in a:
            all_radical_dict.update(i)

        for i in self.get_all_japanese_chars_list():
            if i not in all_radical_dict:
                if len(i) == 1:
                    all_radical_dict.add(i)
                elif len(i) == 2:
                    all_radical_dict.update(i)

        all_radical_dict = sorted(all_radical_dict)
        return {j: i+10 for i, j in enumerate(all_radical_dict)}
