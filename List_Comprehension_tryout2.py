def main():
    raw_prices = [" 10 CHF", "25 chf", "150 CHF ", "5 chf", "500 CHF", "12 CHF"]

    clean_luxury_prices = [p for price in raw_prices if (p:= int(price.lower().strip().strip(" chf"))) > 20]

    print(clean_luxury_prices)

if __name__ == "__main__":
    main()