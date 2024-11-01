from time import time

n = int(input("N: "))


def factorize(n):
    factors = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factors.append(i)

    if len(factors) == 0:
        return f"{n} is a prime number."
    else:
        return factors


def main():
    start = time()
    factorize(n)  # this function has been implemented in 9.1.
    # stop the timer
    end = time()

    print("Elapsed time: {} seconds".format(end - start))


if __name__ == "__main__":
    main()
