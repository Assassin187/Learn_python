def quick_sort(array, left, right):
    """快速排序

    Input: 数组的起止位置
    """
    if left >= right:
        return
    base = array[left]

    # 左右边界不能变动 声明新变量
    start = left
    end = right

    while(start < end):
        while(start < end and array[end] >= base):
            end -= 1
        array[start] = array[end]

        while(start < end and array[start] <= base):
            start += 1
        array[end] = array[start]

    array[start] = base
    quick_sort(array, left, start-1)
    quick_sort(array, start+1, right)

if __name__ == "__main__":
    array = [7, 3, 8, 5, 6, 1, 9, 2, 4]
    
    quick_sort(array, 0, len(array)-1)

    print(array)