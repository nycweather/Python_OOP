import time

def time_function(func, *args, trials = 10):
    min_time = float('inf')
    for i in range(trials):
        start = time.time()
        func(*args)
        end = time.time()
        min_time = min(min_time, end-start)
    return min_time



if __name__ == '__main__':
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)]
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))
