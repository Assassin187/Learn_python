"""

堆排序，从小到大排序

"""

def heapadjust(arr, start, end):
    while(start*2+1 <= end):
        tmp = arr[start]
        i = start*2+1
        if i+1 <= end and arr[i+1] > arr[i]: # 从最大那个叶子节点往下，交换更大的元素上来
            i += 1
        if arr[i] > tmp:
            arr[start] = arr[i]
            arr[i] = tmp
        start = i

def heapsort(arr):
    length = len(arr)
    for i in range(length // 2 - 1, -1, -1):
        heapadjust(arr, i, length-1)
    for i in range(length-1):
        tmp = arr[0]
        arr[0] = arr[length-1-i]
        arr[length-1-i] = tmp
        heapadjust(arr, 0, length-2-i) # 每交换一个元素下来就剔除一个

if __name__ == "__main__":
    arr = [11,9,7,14,3,15,6,5,12,8,2,4,1,10,13]
    heapsort(arr)
    print(arr)