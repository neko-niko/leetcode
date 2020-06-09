
def Soul(array):
    for i in range(0, len(array)):
        while array[i] != i:
            if array[array[i]] == array[i]:
                return array[i]
            else:
                array[array[i]], array[i] = array[i], array[array[i]]


print(Soul([0, 1, 2, 3, 4, 4]))