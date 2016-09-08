from bot import Bot


def test_add_sentence():
    bot = Bot()
    sentence = "The cat in the hat"
    bot.add_sentence(sentence)
    expected_monte_carlo = {
        'The cat': ['in'],
        'cat in': ['the'],
        'in the': ['hat']
    }
    assert bot.monte_carlo == expected_monte_carlo


def test_create_sentence():
    bot = Bot()
    sentence = "The cat in the hat"
    bot.add_sentence(sentence)
    assert bot.create_sentence(20) is not None
