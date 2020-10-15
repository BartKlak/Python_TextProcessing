def end_ten(list_words):
    final_list = []
    for w in list_words:
        if w.endswith('ten'.lower()) or w.endswith('ten'.capitalize()):
            final_list.append(w.lower())
    set_final = set(final_list)
    final_list = list(set_final)
    final_list = sorted(final_list)
    return final_list
###
def contain_pt(list_words):
    final_list = []
    for w in list_words:
        if w.find('pt') != -1:
            final_list.append(w.lower())
    set_final = set(final_list)
    final_list = list(set_final)
    final_list = sorted(final_list)
    return final_list
###
def begin_upper(list_words):
    final_list = []
    for w in list_words:
        if w == w.capitalize():
            final_list.append(w)
    set_final = set(final_list)
    final_list = list(set_final)
    final_list = sorted(final_list)
    return final_list
###
list_words = input()
final_list = end_ten(list_words)
final_list2 = contain_pt(list_words)
final_list3 = begin_upper(list_words)
print(final_list)
print(final_list2)
print(final_list3)
