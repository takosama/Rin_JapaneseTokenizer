import json

class KanjiToRadical:
    def __init__(self, kanji2element_path=".src/kanji2element.json"):
        with open(kanji2element_path, encoding="utf-8") as f:
            self.kanji2element = json.load(f)

    def __search_kanji2element(self, char, visited=None):
        visited = visited or set()
        if char in self.kanji2element:
            result = []
            for element in self.kanji2element[char]:
                if element not in visited:
                    visited.add(element)
                    result += self.__search_kanji2element(element, visited)
            return result
        else:
            return [char]

    def convert(self, element):
        return list(self.__search_kanji2element(element))