list1 = ['Hokkaido', 'University', 'School', 'of', 'Engineering', 'Department', 'of', 'Electronics', 'and', 'Information', 'Engineering']
a_list = []
for w in list1:
    if w.find('a') != -1:
        a_list.append(w)
print(a_list)
print(len(a_list))
