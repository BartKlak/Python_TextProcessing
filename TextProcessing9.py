from nltk.corpus import stopwords
import nltk
from nltk.book import *

def stopwords_ratio(word_list, stop_list):

    word_list = filter(lambda a: a != "" and a != "." and a != "\n" and a != "," and a != "?" and a != "!" and a != "-" and a != "'" and a != '"' and a != ";" and a != ":", word_list)
    list_lower = []
    for w in word_list:
        list_lower.append(w.lower())
    var1 = len(list_lower)

    stoplist1 = []
    for y in list_lower:
	 if y in stop_list:
		  stoplist1.append(y)
    var2 = len(stoplist1)
     
    var3 = float(var2)/float(var1)
    str1 = "All words:{}\tStopwords: {}\t Stopword ratio:{}".format(var1, var2, var3)
    return str1

###
#word_list = input()
stop_list = stopwords.words('english')
#var = stopwords_ratio(word_list, stop_list)
#print(var)

var1 = stopwords_ratio(text1, stop_list)
print(var1)
var2 = stopwords_ratio(text2, stop_list)
print(var2)
var3 = stopwords_ratio(text3, stop_list)
print(var3)
var4 = stopwords_ratio(text4, stop_list)
print(var4)
var5 = stopwords_ratio(text5, stop_list)
print(var5)
var6 = stopwords_ratio(text6, stop_list)
print(var6)
var7 = stopwords_ratio(text7, stop_list)
print(var7)
var8 = stopwords_ratio(text8, stop_list)
print(var8)
var9 = stopwords_ratio(text9, stop_list)
print(var9)
