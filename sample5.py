def count_alphabet(list_words, alphabet):
    num_words = 0 
    for w in list_words:
        if w.find(alphabet) != -1:
            num_words = num_words + 1
    return num_words
###
list_words = input()
alphabet = input()
num_words = count_alphabet(list_words, alphabet)
if num_words > 0:
    print('We find {} words containing "{}" in the list.'.format(num_words, alphabet))
else:
    print('We do not find "{}" in the list.'.format(alphabet))
