

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(l)


myList = []

def flatten(data):
    for i in data:
        if type(i) == list:
            flatten(i)
        else:
            myList.append(i)

flatten(l)

print(myList)