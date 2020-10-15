def count_words(filename):
    list_sentence = []
    f = open(filename, 'r')
    for line in f:
        line.strip()
        for sep in [',','.',';',':','-','?','"',"'",'!','\n']:
            line = line.replace(sep,' '+sep)
        line = line.split(' ')
        list_sentence.extend(line)
    
    f.close()
    list_sentence = filter(lambda a: a != "" and a != "." and a != "\n" and a != "," and a != "?" and a != "!" and a != "-" and a != "'" and a != '"' and a != ";" and a != ":", list_sentence)
    list_lower = []
    for w in list_sentence:
        list_lower.append(w.lower())
    set_lower = set(list_lower)
    var = len(set_lower)
    return var

###
filename = input()
var = count_words(filename)
print(var)
