list1 = ['Hokkaido', 'University', 'School', 'of', 'Engineering', 'Department', 'of', 'Electronics', 'and', 'Information', 'Engineering']
list_lower = []
for w in list1:
    list_lower.append(w.lower())
set_lower = set(list_lower)
print(set_lower)
print(len(set_lower))
list_lower = list(set_lower)
sorted_list_lower = sorted(list_lower)
print(sorted_list_lower)
print(len(sorted_list_lower))
