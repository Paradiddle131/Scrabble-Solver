# https://github.com/first20hours/google-10000-english
def load_words():
    with open('../Word_Finding/words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


def complete_word(revealed_letters, given_letters):
    all_words = load_words()
    length_revealed_letters = len(revealed_letters)
    list_given_letters = list(given_letters)
    total_letters = len(given_letters)
    picked_words, result = ([] for i in range(2))
    count = 0
    for word in all_words:
        word_temp = word
        list_revealed_letters2 = list_given_letters.copy()
        for letter in list_given_letters:
            if letter in word_temp:
                del list_revealed_letters2[list_revealed_letters2.index(letter)]
                word_temp = word_temp.replace(letter, '', 1)
        if len(list_given_letters) - len(list_revealed_letters2) == len(word) and (
                len(word) <= total_letters) and len(word) == length_revealed_letters:
            picked_words.append(word)
    for picked_word in picked_words:
        for i in range(0, len(picked_word)):
            try:
                if picked_word[i] == revealed_letters[i] or revealed_letters[i] == '_':
                    count += 1
            except:
                pass
            if total_letters == i + 1:
                break
        if count == length_revealed_letters:
            result.append(picked_word)
        count = 0
    return result


print(complete_word("_______", "yccende"))
