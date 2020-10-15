import nltk
from nltk.book import *

def alphabet_freq(text_list):

    text_list = filter(lambda a: a != "" and a != "." and a != "\n" and a != "," and a != "?" and a != "!" and a != "-" and a != "'" and a != '"' and a != ";" and a != ":", text_list)
    list_lower = []
    for w in text_list:
        list_lower.append(w.lower())
    #print(list_lower)
    freq_list = []
    var = [0]*27
    k = 0
    l = ""
    for j in range(0, 26):
    	 i = 0
    	 for y in list_lower:
		  i = y.count(chr(97 + j))
	 	  var[j] = var[j] + i 
	 if var[j] > k:
		  k = var[j]
		  l = chr(97 + j)
    var[26] = l
    return var

###
var1 = alphabet_freq(text1)
print(var1)
var2 = alphabet_freq(text2)
print(var2)
var3 = alphabet_freq(text3)
print(var3)
var4 = alphabet_freq(text4)
print(var4)
var5 = alphabet_freq(text5)
print(var5)
var6 = alphabet_freq(text6)
print(var6)
var7 = alphabet_freq(text7)
print(var7)
var8 = alphabet_freq(text8)
print(var8)
var9 = alphabet_freq(text9)
print(var9)
