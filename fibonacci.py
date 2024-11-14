def fibonacci(array):
    """生成一个斐波那契数列

    Input:
        输入一个正整数

    Output:
        指定位置的斐波那契数组
    """
    index = int(input("Enter index: "))
    if index < 2:
        print(array[index])
    else:
        while index != len(array):
            array.append(array[-1] + array[-2])
    for i in range(len(array)):
        print(array[i])

if __name__ == '__main__':
    array = [0, 1]
    fibonacci(array)