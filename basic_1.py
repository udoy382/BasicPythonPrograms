# How To Find Execution Time Of A Python Program Using Time Module


from time import time

def func1(a, b):
    # Harry
    return a + b

def func2(a, b):
    # Udoy
    num1 = a
    num2 = b
    
    if (a>b and a!=3):
        pass
    sum([4, 3])
    return a+b

if __name__ == '__main__':
    init = time()
    for i in range(0, 100000):
        func1(3, 5)
    print("Harry Time: ", time()-init)
    init = time()
    for i in range(0, 100000):
        func2(3, 5)
    print("Udoy Time: ", time()-init)