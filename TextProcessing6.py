def vocabulary(list_text):
    list_text = filter(lambda a: a != "" and a != "." and a != "\n" and a != "," and a != "?" and a != "!" and a != "-" and a != "'" and a != '"' and a != ";" and a != ":", list_text)
    list_lower = []
    for w in list_text:
        list_lower.append(w.lower())
    set_lower = set(list_lower)
    var = len(set_lower)
    return var

###
list_text = input()
var = vocabulary(list_text)
print(var)
