def jos(n, k):
    if n == 1:
        return 0
    else:
        return (jos(n - 1, k) + k) % n

if __name__ == '__main__':  
   print(jos(5, 3))