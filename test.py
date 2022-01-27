classes = ['apple', 'orange', 'pear', 'mango']
store = []

for fruit in classes:
    class_dict = {}
    if fruit == "orange":
        o = 2
        q = 1
    else:
        o = 0
        q = 0

    for j in ('fruit', 'o', 'q'):
        class_dict[j] = locals()[j]
    print(class_dict)
    store.append(class_dict)
print ("store: ", store)