import time
import matplotlib.pyplot as plt

def draw_array(arr, container):
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color='orange')
    container.pyplot(fig)

def bubble_sort(arr, speed, container):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            draw_array(a, container)
            time.sleep(speed)
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                draw_array(a, container)
                time.sleep(speed)

def insertion_sort(arr, speed, container):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            draw_array(a, container)
            time.sleep(speed)
        a[j + 1] = key
        draw_array(a, container)
        time.sleep(speed)

def selection_sort(arr, speed, container):
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
            draw_array(a, container)
            time.sleep(speed)
        a[i], a[min_idx] = a[min_idx], a[i]
        draw_array(a, container)
        time.sleep(speed)

def quick_sort(arr, speed, container):
    a = arr.copy()

    def _quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)

    def partition(low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                draw_array(a, container)
                time.sleep(speed)
        a[i+1], a[high] = a[high], a[i+1]
        draw_array(a, container)
        time.sleep(speed)
        return i + 1

    _quick_sort(0, len(a)-1)

def merge_sort(arr, speed, container):
    a = arr.copy()

    def _merge_sort(l, r):
        if l < r:
            m = (l + r) // 2
            _merge_sort(l, m)
            _merge_sort(m+1, r)
            merge(l, m, r)

    def merge(l, m, r):
        L = a[l:m+1]
        R = a[m+1:r+1]
        i = j = 0
        k = l
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            draw_array(a, container)
            time.sleep(speed)
            k += 1
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
            draw_array(a, container)
            time.sleep(speed)
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1
            draw_array(a, container)
            time.sleep(speed)

    _merge_sort(0, len(a)-1)
