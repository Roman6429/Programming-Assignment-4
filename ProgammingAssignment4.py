import time
import sys

def o_n(n):
    for i in range(n):
        pass

def n_log_n(n):
    lst = []
    for i in range(n):
        lst.append(i)
        lst.sort()

def n_2(n):
    for i in range(n):
        for j in range(n):
            pass

def main():
    try:
        choice = int(input("Enter 1 for O(n), 2 for O(n log n), 3 for O(n^2): "))
        if choice not in [1, 2, 3]:
            raise ValueError("Invalid choice. Exiting.")
        
        n = int(input("n? "))
        if n <= 0:
            raise ValueError("Input must be a positive integer. Exiting.")

    except ValueError as e:
        print(e)
        sys.exit(1)

    start_time = time.time()

    if choice == 1:
        o_n(n)
    elif choice == 2:
        n_log_n(n)
    elif choice == 3:
        n_2(n)

    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000
    print(f"Elapsed time: {elapsed_time:.4f} ms")

if __name__ == "__main__":
    main()
