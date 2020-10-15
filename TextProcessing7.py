def alphabet_freq(text_list):

    text_list = filter(lambda a: a != "" and a != "." and a != "\n" and a != "," and a != "?" and a != "!" and a != "-" and a != "'" and a != '"' and a != ";" and a != ":", text_list)
    list_lower = []
    for w in text_list:
        list_lower.append(w.lower())
    print(list_lower)
    freq_list = []
    var = [0]*26
    for j in range(0, 26):
    	 i = 0
    	 for y in list_lower:
		  i = y.count(chr(97 + j))
	 	  var[j] = var[j] + i 
    return var

###
text_list = input()
var = alphabet_freq(text_list)
print(var)
