import operator
import nltk
from nltk.book import *

def top_ten_words(list_text):

    list_text = filter(lambda a: a != "" and a != "." and a != "\n" and a != "," and a != "?" and a != "!" and a != "-" and a != "'" and a != '"' and a != ";" and a != ":", list_text)
    list_lower = []
    for w in list_text:
        list_lower.append(w.lower())
    list_four = [] 
    for y in list_lower:
	 if len(y) == 4:
		  list_four.append(y)
#    print(list_four)
    new_dict = {}
    for z in list_four:
	 new_dict.update({z:list_four.count(z)})
    sorted_dict = sorted(new_dict.items(), key=operator.itemgetter(1), reverse=True)
    top_ten = sorted_dict[:5]
    final = dict(top_ten)
#    freq_list = []
#    var = [0]*26
#    for j in range(0, 26):
#    	 i = 0
#    	 for y in list_lower:
#		  i = y.count(chr(97 + j))
#	 	  var[j] = var[j] + i 
    return final

###
lol = text1 + text2
var10 = top_ten_words(lol)
print(var10)
