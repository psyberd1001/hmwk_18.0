import string
from itertools import chain

class WordsFinder:

    def __init__(self, *file_names):
        self.file_name = file_names

    def get_all_words(self):
        all_words1 = []
        all_words = {}
        for i in range(len(self.file_name)):
            with open(self.file_name[i], encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans('', '', string.punctuation))
                    line = line.split()
                    all_words1.append(line)
        all_words2 = list(chain.from_iterable(all_words1))
        all_words.update({self.file_name[i]: all_words2})
        return all_words


    def find(self, word):
        word = word.lower()
        count = 1
        print('Пошла функция поиска')
        map_keys = map(self.get_all_words().get, self.get_all_words())
        for key in map_keys:
            for words in key:
                if words != word:
                    count += 1
                    print('не нашел')
                    continue
                else:
                    print(f'{self.file_name} : {words} - {count}')
                    break

    def count(self, word):
        word = word.lower()
        count = 0
        print('В ход идет функция посчета!')
        map_keys = map(self.get_all_words().get, self.get_all_words())
        for key in map_keys:
            for words in key:
                if words == word:
                    count += 1
                    print(f'Нашел ещё одного - {words}')
            print(f'{self.file_name} : {word} - {count}')

finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
