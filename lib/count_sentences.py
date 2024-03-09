
class MyString:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError('Value must be a string')
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = filter(None, re.split(r'[.!?]', self.value))
        return len(list(sentences))

# An 
string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())  # Output: True
print(string.is_question())  # Output: False
print(string.is_exclamation())  # Output: False
print(string.count_sentences())  # Output: 3
