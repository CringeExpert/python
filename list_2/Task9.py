from itertools import chain

#Funkcja chain jest bardzo podobna funkcja do list.expand(list2), chain zwraca osobną wartość, gdzie expand modyfikuje listę, na której została wykonana funkcja

def denest(listOg):
    result = []
    for l in listOg:
        result = list(chain(result,l))
    return result

list1 = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
print(list1)
print(denest(list1))



