# Funci´n a que coja una lista y apunte a un parametro
# Multiples variables : medio, comiezo, acabar , pasos
# Recursivo o loop con while
# Incrementar los pasos cada vez que la division se haga
# Condiciones para registrar la psicion del objetivo

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Step",steps, ":",(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element > list[middle]:
            end = middle -1
        else:
            start = middle + 1

    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 12
binary_search(my_list, target)


#for i in my_list:
#    if i == 12:
#        print("found")