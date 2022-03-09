
l =  [[1, 2], [3, 4],[1], [5, 6, 7]]

myList = []

def list_fl(data):
    if type(data) == list:
        
        myListLength = len(data)
               
        while myListLength > 0:
            myListLength -= 1
            
            data[myListLength].sort(reverse=True)
            myList.append(data[myListLength])
        
        
list_fl(l)   

print(myList)