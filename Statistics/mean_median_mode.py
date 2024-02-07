from collections import Counter

def calculate(a, n):
    mean = round(sum(a)/n, 4)
    
    median = 0
    if n % 2 == 0:
        median = (n//2) + 1
    else:
        median = n//2
    
    num_frequency = Counter(a)
    mode = max(num_frequency, key=num_frequency.get)

    return mean, median, mode


if __name__ == '__main__':
    arr = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
    n = len(arr)
    mean, median, mode = calculate(arr, n)
    print(f"Mean: {mean} , Median: {median} , Mode: {mode}")