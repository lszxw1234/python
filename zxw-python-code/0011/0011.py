
class Input(object):
    def __init__(self):
        self.filter_words = list()
        self.in_strings = ''
        self.out_strings = 'Human Rights'
        self.load_filter_words()


    def load_filter_words(self, filename='filter_words.txt'):
        with open(filename, 'r', encoding='utf8') as file:
            for line in file:
                self.filter_words.append(line.strip())


    def user_input(self):
        self.in_strings = input('>')

    def std_output(self):
        self.filter_word()
        print(self.out_strings)

    def filter_word(self):
        for word in self.filter_words:
            if self.in_strings.find(word) != -1:
                self.out_strings = 'Freedom'
                return




i = Input()
i.user_input()
i.std_output()