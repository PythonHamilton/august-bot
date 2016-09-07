import random

STOP_PUNCTUATION = [".", "?"]


class Bot(object):
    sentences = ""

    def populate_monte_carlo(self):
        monte_carlo = {}
        word_buffer = []
        text = self.sentences.split(" ")
        for word in text:
            if len(word_buffer) == 3:
                key = "{WORD1} {WORD2}".format(WORD1=word_buffer[0], WORD2=word_buffer[1])
                if key in monte_carlo:
                    monte_carlo[key].append(word_buffer[2])
                else:
                    monte_carlo[key] = [word_buffer[2]]
                word_buffer.pop(0)
            if word.isalpha() or word in [",", ";", ".", "?"]:
                word_buffer.append(word)
        return monte_carlo

    def create_sentence(self, monte_carlo, max_length):
        initial_key = random.choice(list(monte_carlo.keys()))
        sentence = initial_key.split()
        while len(sentence) < max_length:
            key = "{WORD1} {WORD2}".format(WORD1=sentence[-2], WORD2=sentence[-1])
            options = monte_carlo[key]
            if options:
                value = random.choice(options)
                sentence.append(value)
                if value in STOP_PUNCTUATION:
                    return sentence
            else:
                return sentence
        return sentence

    def add_sentence(self, sentence):
        self.sentences += sentence + " "
        self.monte_carlo = self.populate_monte_carlo()

    def get_sentence(self):
        if len(self.sentences) < 50:
            return "Feed me more"
        else:
            try:
                s = " ".join(self.create_sentence(self.monte_carlo, 20))
                s = s[0].upper() + s[1:].lower() + "."
                return s

            except KeyError:
                return "I speak not know how"
