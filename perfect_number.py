import time
import math

def is_perfect(n):
    if n < 2:
        return False
    # 1 is always a proper divisor
    divisors_sum = 1
    # Only need to iterate up to sqrt(n)
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n

def find_perfect_numbers(limit):
    perfect_numbers = []
    for num in range(2, limit + 1):
        if is_perfect(num):
            perfect_numbers.append(num)
    return perfect_numbers

def main():
    try:
        n = int(input("Enter an integer: "))
    except ValueError:
        print("enter integer value")
        return
    
    start_time = time.time()
    perfects = find_perfect_numbers(n)
    end_time = time.time()
    
    print(f"Perfect numbers up to {n}: {perfects}")
    print(f"zeit: {end_time - start_time:.6f} sek")

if __name__ == "__main__":
    main()