import nltk
from nltk.book import *

def vocabulary(list_text):
    list_text = filter(lambda a: a != "" and a != "." and a != "\n" and a != "," and a != "?" and a != "!" and a != "-" and a != "'" and a != '"' and a != ";" and a != ":", list_text)
    list_lower = []
    for w in list_text:
        list_lower.append(w.lower())
    set_lower = set(list_lower)
    var = len(set_lower)
    return var

###
var1 = vocabulary(text1)
print(var1)
var2 = vocabulary(text2)
print(var2)
var3 = vocabulary(text3)
print(var3)
var4 = vocabulary(text4)
print(var4)
var5 = vocabulary(text5)
print(var5)
var6 = vocabulary(text6)
print(var6)
var7 = vocabulary(text7)
print(var7)
var8 = vocabulary(text8)
print(var8)
var9 = vocabulary(text9)
print(var9)
