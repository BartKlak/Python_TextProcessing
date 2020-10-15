#coding: utf-8
import sys, codecs

def palindrome_j(text):
    text = text.decode('utf-8')
    final_text = ""
    c = False
    if text.endswith(u'。') or text.endswith(u'？') or text.endswith(u'！'):
        if text.endswith(u'。'):
            b = u'。'
            c = True
        elif text.endswith(u'？'):
            b = u'？'
            c = True
        elif text.endswith(u'！'):
            b = u'！'
            c = True
        else:
            c = False
        text = text[:-1]
    for a in text:
        final_text = a + final_text
    if c == True:
        final_text = final_text + b
    return final_text


###
text = input()
final_text = palindrome_j(text).encode('utf-8')
print(final_text)
