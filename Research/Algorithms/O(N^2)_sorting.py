def insert_sort(a):
    for k in range(1, len(a)):
        for i in range(0, k):
            if a[i] > a[k]:
                a[i], a[k] = a[k], a[i]
                print(a[i])
    print(a)


insert_sort([1, 5, 7, 3])
