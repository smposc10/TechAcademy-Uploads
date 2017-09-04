# this drill attempts to take a number set, sort it in ascending order without using .sort and sorted() algorithms

numset1 = [67, 45, 2, 13, 1, 998]
numset2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
numlist = []

def my_sort(numlist = numset1):
    sorted_list = []

    while numlist:
        var_pick= numlist[0]
        for i in numlist:
            if i < var_pick:
                var_pick = i
        sorted_list.append(var_pick)
        numlist.remove(var_pick)
    print(sorted_list)

# Execute below. Change the number set that you want here (pick numset 1 or numset2)
my_sort(numlist = numset2)