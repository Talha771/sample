from copy import deepcopy
from pprint import pprint
import math
from random import randint
from random import shuffle
# Adapted from https://www.geeksforgeeks.org/insertion-sort/


def insertionSort(arr):
    counter = 0
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        counter += 1
        while j >= 0 and key < arr[j]:
            counter += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return counter

# ------------------------------------------------------------------------------------------------------
# Code adapted from https://www.geeksforgeeks.org/bubble-sort/


def bubbleSort(arr):
    n = len(arr)
    counter = 0
    # Traverse through all array elements
    for i in range(n):
        swapped=False
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            counter += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped =True
        if not swapped:
            return counter
    return counter



# ------------------------------------------------------------------------------------------------------
# code adapted from https://www.geeksforgeeks.org/selection-sort/


def selectionSort(A):
    counter = 0
    for i in range(len(A)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            counter += 1
            if A[min_idx] > A[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        A[i], A[min_idx] = A[min_idx], A[i]
    return counter

# ------------------------------------------------------------------------------------------------------
# code adapted from https://www.geeksforgeeks.org/merge-sort/


def mergeSort(arr, counter_merge):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L, counter_merge)

        # Sorting the second half
        mergeSort(R, counter_merge)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            counter_merge += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return counter_merge

# X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-
# Creating random arrays
# create_arr generates a list of 1-n permutation


def create_arr(n):
    arr = []
    for i in range(n):
        arr.append(i)
    # print("newly created array:", arr)
    return arr
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fisher-yates randomization code used from https://www.geeksforgeeks.org/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/
# shuffles the array into permutation


def randomize(arr, n):
    # Start from the last element and swap one by one. We don't
    # need to run for the first element that's why i > 0
    for i in range(n-1, 0, -1):
        # Pick a random index from 0 to i
        j = randint(0, i+1)

        # Swap arr[i] with the element at random index
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def randomize_ez(arr):
    # random.shuffle(arr)
    shuffle(arr)
    return arr


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# returns list of size log2n where each element is a random list of size n


def create_rand_arr(n):
    lst = []
    arr = create_arr(n)
    num_arr = 10*int(math.log(n, 2))
    for i in range(num_arr):
        # list.append(randomize(arr, n))
        lst.append(randomize_ez(deepcopy(arr)))
    return lst


def average_lst(lst):
    return sum(lst)/len(lst)


def compute_average(n=10):
    """
    Takes in size of list n, and generates 10*log2(n) random lists to test against each algo
    """
    lst_of_arrays = create_rand_arr(n)
    # pprint(lst_of_arrays)
    # algorithms = {1: 'mergeSort', 2: 'bubbleSort',
    #   3: 'insertionSort', 4: 'selectionSort'}
    algorithms = ['mergeSort', 'bubbleSort',
                  'insertionSort', 'selectionSort']
    average_comparisons = {}
    for i in algorithms:
        average_comparisons[i] = []
        # looks like this:
        #  average_comparisons = {'mergeSort': [],
        #                        'bubbleSort': [],
        #                        'insertionSort': [],
        #                        'selectionSort': []}
    for algo_no in range(len(algorithms)):
        for iteration in range(len(lst_of_arrays)):
            algo = algorithms[algo_no]
            if algo_no == 0:
                average_comparisons[algo].append(
                    mergeSort(lst_of_arrays[iteration], 0))
            if algo_no == 1:
                average_comparisons[algo].append(
                    bubbleSort(lst_of_arrays[iteration]))
            if algo_no == 2:
                average_comparisons[algo].append(
                    insertionSort(lst_of_arrays[iteration]))
            if algo_no == 3:
                average_comparisons[algo].append(
                    selectionSort(lst_of_arrays[iteration]))
            # print(
            #     f'{algo} took {average_comparisons[algo][iteration]} comparisons')
        print(
            f"{algo}'s average number of comparisons for n = {n} is {average_lst(average_comparisons[algo])}")
    return average_comparisons


if __name__ == "__main__":
    # for i in range(100, 200, 10):
    #     print()
    #     compute_average(i)
    # print(f"bubbleSort best case: {bubbleSort([1,2,3,4,5,6,7,8,9,10])}")
    compute_average(10)
