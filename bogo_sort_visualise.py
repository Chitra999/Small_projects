import random
from matplotlib import pyplot
def bogo_sort(arr):
    n = len(arr)
    is_sorted = False

    while not is_sorted:
        # swap the elements , i and j are indexes
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        arr[i], arr[j] = arr[j], arr[i]
        yield arr
        # visualise
        

        # check if sorted
        is_sorted = True
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                is_sorted = False
                break

def visualize(sorting_algo, n):

    arr = random.sample(range(1, n+1),n)
    sorting_process = sorting_algo(arr)

    while True:
        next_arr = next(sorting_process, None)
        if next_arr is None:
            break

        else:
            pyplot.bar(x = range(1, len(arr)+1), height= next_arr)
            pyplot.axis("off")
            pyplot.pause(0.1)                                   #add wait time
            pyplot.clf()                                        #close figure
    pyplot.show()

visualize(bogo_sort, 4)