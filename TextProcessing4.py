def palindrome(text):
    final_text = ""
    c = False
    if text.endswith('.') or text.endswith('?') or text.endswith('!'):
        if text.endswith('.'):
            b = "."
            c = True
        elif text.endswith('?'):
            b = "?"
            c = True
        elif text.endswith('!'):
            b = "!"
            c = True
        else:
            c = False
        text = text[:-1]
    for a in text:
        a = a.lower()
        final_text = a + final_text
    if c == True:
        final_text = final_text + b
    d = final_text[0]
    d = d.upper()
    final_text = d + final_text[1:]
    final_text = final_text.replace(' i', ' I')
    return final_text


###
text = input()
final_text = palindrome(text)
print(final_text)
