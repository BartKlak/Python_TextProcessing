def contain_alphabet(list_words, alphabet):
    final_list = []
    for w in list_words:
        if w.find(alphabet.lower()) != -1 or w.find(alphabet.upper()) != -1:
            final_list.append(w.lower())
    set_final = set(final_list)
    final_list = list(set_final)
    final_list = sorted(final_list)
    return final_list

###
list_words = input()
alphabet = input()
final_list = contain_alphabet(list_words, alphabet)
print(final_list)
