from pprint import pprint
my_list = []
pprint(dir(my_list))

def checkio(text):
    text = text.lower()
    counter = {}
    for symbol in text:
        counter[symbol] = text.count(symbol)

    max_value = 0
    letter = text[0]

    for symbol, number in counter.items():
        # print(symbol, number)
        if ord(symbol) in range(97):
            continue
        else:
            if number > max_value:
                max_value = number
                letter = symbol
            elif number == max_value:
                if ord(symbol) < ord(letter):
                    max_value = number
                    letter = symbol
                else:
                    continue

    # print(letter, max_value)
    return letter


if __name__ == '__main__':
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
