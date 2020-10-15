#coding: utf-8
import sys, codecs
import MeCab
import operator

def jnoun(text):
    noun_list = []
    mecab = MeCab.Tagger('-Ochasen')
    mecab.parse('')
    text_node = mecab.parseToNode(text.encode('utf-8'))
    while text_node:
	 if '名詞' in text_node.feature.split(',')[0]:
		  a = text_node.surface
		  noun_list.append(a)
	 text_node = text_node.next
    return noun_list

def jverb(text):
    verb_list = []
    mecab = MeCab.Tagger('-Ochasen')
    mecab.parse('')
    text_node = mecab.parseToNode(text.encode('utf-8'))
    while text_node:
	 if '動詞' in text_node.feature.split(',')[0]:
		  if not '助動詞' in text_node.feature.split(',')[0]:
		  	 b = text_node.feature.split(',')[6]
		  	 verb_list.append(b)
	 text_node = text_node.next
    return verb_list

def top30_jnoun(text):
    noun_list = jnoun(text)
    new_dict = {}
    for z in noun_list:
	 new_dict.update({z:noun_list.count(z)})
    sorted_dict = sorted(new_dict.items(), key=operator.itemgetter(1), reverse=True)
    top_30 = sorted_dict[:30]
    final = dict(top_30)
    return final

def top30_jverb(text):
    verb_list = jverb(text)
    new_dict = {}
    for z in verb_list:
	 new_dict.update({z:verb_list.count(z)})
    sorted_dict = sorted(new_dict.items(), key=operator.itemgetter(1), reverse=True)
    top_30 = sorted_dict[:30]
    final = dict(top_30)
    return final

def percent_top30_jnoun(text):
    word_list = []
    mecab = MeCab.Tagger('-Ochasen')
    mecab.parse('')
    text_node = mecab.parseToNode(text.encode('utf-8'))
    while text_node:
	 a = text_node.surface
	 word_list.append(a)
	 text_node = text_node.next
    allwords = len(word_list)
    allwords = allwords - 3
    top_30 = top30_jnoun(text)
    topnouns = sum(top_30.values())
    print(topnouns)
    print(allwords)
    var = (float(topnouns)/float(allwords))*100
    return var



###
f = codecs.open('./wagahaiwa_nekodearu_utf8.txt', 'r', 'utf-8')
jtext1 = f.read()
f.close()
text = jtext1
top30noun = top30_jnoun(text)
print str(top30noun).decode('string-escape')
print
var = percent_top30_jnoun(text)
print("{}%".format(var))


#text_node.feature.split(',')[6]

