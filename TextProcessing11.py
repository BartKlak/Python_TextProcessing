#coding: utf-8
import sys, codecs
import MeCab

def percent_noun(text):
    #text = text.decode('utf-8')
    mecab = MeCab.Tagger('-Ochasen')
    mecab.parse('')
    text_node = mecab.parseToNode(text.encode('utf-8'))
    allwords = 0
    nouns = 0
    while text_node:
	 print text_node.surface, text_node.feature.split(',')[0]
	 allwords = allwords + 1
	 if '名詞' in text_node.feature.split(',')[0]:
		  nouns = nouns + 1
	 text_node = text_node.next
    allwords = allwords - 3
    print(allwords)
    print(nouns)
    percentage = (float(nouns)/float(allwords))*100
    return percentage


###
f = codecs.open('./jtext2_utf8.txt', 'r', 'utf-8')
jtext1 = f.read()
f.close()
text = jtext1
percentage = percent_noun(text)#.encode('utf-8')
print(percentage)
