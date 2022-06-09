from euler import prime


def main():
    ans = 0
    for p in prime.generate_primes():
        if p > 2_000_000:
            break
        ans += p
    print(ans)


if __name__ == "__main__":
    main()
