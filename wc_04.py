from sorting_algos import *
import matplotlib.pyplot as plt


def plot(start, end, jump=1):
    x = range(start, end, jump)
    y_mergeSort = []
    y_bubbleSort = []
    y_insertionSort = []
    y_selectionSort = []
    x = []

    for n in range(start, end, jump):
        averages = compute_average(n)
        y_mergeSort.append(average_lst(averages['mergeSort']))
        y_bubbleSort.append(average_lst(averages['bubbleSort']))
        y_insertionSort.append(average_lst(averages['insertionSort']))
        y_selectionSort.append(average_lst(averages['selectionSort']))
        x.append(n)
    print(f"y_mergeSort: {y_mergeSort}\nlength of x: {len(x)}")

    plt.plot(x, y_mergeSort, label="mrgeSort")
    plt.plot(x, y_bubbleSort, label="bubbleSort")
    plt.plot(x, y_insertionSort, label="insertionSort")
    plt.plot(x, y_selectionSort, label="selectionSort")


if __name__ == "__main__":
    plt.xscale("symlog")
    plt.yscale("symlog")
    # plot(1, 20002, 100)
    plot(1000, 5000, 100)
    plt.title("Comparison-based Sorting Algos")
    plt.ylabel('Number of comparisons')
    plt.xlabel('size of input, $n$')
    plt.legend()
    plt.show()
