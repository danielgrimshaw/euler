from euler import prime


def main():
    prod = 1
    for p in prime.generate_primes():
        if p > 20:
            break
        mul = p
        while mul * p < 20:
            mul *= p
        prod *= mul
    print(prod)


if __name__ == "__main__":
    main()
