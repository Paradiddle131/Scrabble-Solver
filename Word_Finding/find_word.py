def complete_word(revealed_letters, given_letters):
    dictionary = open("../Word_Finding/Turkish_dictionary.txt", "r", encoding="utf-8")
    all_words = dictionary.read()
    length_revealed_letters = len(revealed_letters)
    list_given_letters = list(given_letters)
    total_letters = len(given_letters)
    picked_words, result = ([] for i in range(2))
    count = 0
    for word in all_words.split("\n"):
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


# print(complete_word("g__z_", "mzgae"))
# print(complete_word("m____", "eeimkl"))
# print(complete_word("m_____", "eeimkl"))
# print(complete_word("____k", "eeimkl"))
# print(complete_word("____k_", "eeimkl"))
# print(complete_word("____r", "karfit"))
# print(complete_word("_f___", "karfit"))
# print(complete_word("_k___", "karfit"))
# print(complete_word("_f___", "karfit"))
# print(complete_word("___f_k", "karfit"))
# print(complete_word("a___", "karfit"))
# print(complete_word("e__i_", "iamtep"))
# print(complete_word("_____k", "faktri"))
# print(complete_word("__r_f", "faktri"))
# print(complete_word("a_i_", "faktri"))
#
# print(complete_word("______", "bayram"))
# print(complete_word("y__", "bayram"))
# print(complete_word("b____", "bayram"))
# print(complete_word("___a_", "bayram"))
# print(complete_word("_a__", "bayram"))
# print(complete_word("___a", "bayram"))
# print(complete_word("__a_", "bayram"))
#
# print(complete_word("______", "tornak"))
# print(complete_word("__k_", "tornak"))
# print(complete_word("_____", "tornak"))
#
print(complete_word("_____", "miatsh"))
