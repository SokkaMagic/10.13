# You can remove 'pass' if you written code in the function
# Do NOT use sorted() or .sort() - write the algorithms yourself.

# Exercise 1
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                swapped = True
        if swapped == False:
            break
    return data



# Exercise 2
def bubble_sort_trace(data):
    lst=[]
    n = len(data)
    for i in range(n):
        swapped = False


        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                swapped = True

        if swapped == False:

            break
        lst.append(data.copy())
    return lst


# Exercise 3
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = key
    return data
# Exercise 4
def insertion_sort_trace(data):
    lst=[]
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = key
        lst.append(data.copy())

    return lst



# Exercise 5
def rank_students(records):
    for i in range(1, len(records)):
        key = records[i][1]
        j = i - 1
        while j >= 0 and records[j][1] < key:
            records[j + 1] = records[j]
            j = j - 1
            records[j + 1] = key
    return records
