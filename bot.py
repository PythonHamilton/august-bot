import random

STOP_PUNCTUATION = [".", "?"]


def is_valid(sentence):
    return True


class Bot(object):
    def __init__(self):
        self.monte_carlo = {}
        self.sentences = ""

    def add_to_monte_carlo(self, sentence):
        word_buffer = []
        text = self.sentences.split(" ")
        for word in text:
            if len(word_buffer) == 3:
                key = "{WORD1} {WORD2}".format(WORD1=word_buffer[0], WORD2=word_buffer[1])
                if key in self.monte_carlo:
                    self.monte_carlo[key].append(word_buffer[2])
                else:
                    self.monte_carlo[key] = [word_buffer[2]]
                word_buffer.pop(0)
            if word.isalpha() or word in [",", ";", ".", "?"]:
                word_buffer.append(word)

    def create_sentence(self, monte_carlo, max_length):
        initial_key = random.choice(list(monte_carlo.keys()))
        sentence = initial_key.split()
        while len(sentence) < max_length:
            key = "{WORD1} {WORD2}".format(WORD1=sentence[-2], WORD2=sentence[-1])
            options = self.monte_carlo[key]
            if options:
                value = random.choice(options)
                sentence.append(value)
                if value in STOP_PUNCTUATION:
                    return sentence
            else:
                return sentence
        return sentence

    def add_sentence(self, sentence):
        if is_valid(sentence):
            self.sentences += sentence + " "
            self.add_to_monte_carlo(sentence)

    def get_sentence(self):
        if len(self.sentences) < 50:
            return "Feed me more"
        else:
            try:
                s = " ".join(self.create_sentence(self.monte_carlo, 20))
                if s[-1] not in STOP_PUNCTUATION:
                    s = s[0].upper() + s[1:] + "..."
                else:
                    s = s[0].upper() + s[1:]
                return s

            except KeyError:
                return "I speak not know how"
