import requests
import datetime
import json
import time

def main():
    no_prior_data = False
    try:
        loaded_price, loaded_date = load_price_and_date()
    except FileNotFoundError:
        no_prior_data = True
        print("No prior data to compare to, will just output current data.")
    price_now, time_now = write_current_price_and_date()

    if no_prior_data:
        print(f"Current price of Bitcoin: {price_now}CHF\nTime: {time_now}")
    else:
        compare_data(loaded_price, loaded_date, price_now, time_now)

def write_current_price_and_date():
    request = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=chf").json()
    try:
        price_now = (request["bitcoin"]["chf"],)[0]
    except KeyError:
        raise SystemExit("rate Limit has been exceeded.")
    time_now = datetime.datetime.now().isoformat()
    with open("price_over_time.json", "w") as file:
        json.dump([price_now, time_now], file)
    return price_now, datetime.datetime.now()

def load_price_and_date():
    with open("price_over_time.json", "r") as file:
        data = json.load(file)
        return data[0], datetime.datetime.fromisoformat(data[1])

def compare_data(loaded_price, loaded_date, price_now, time_now):
    timedelta = time_now - loaded_date
    price_difference = price_now - loaded_price
    print(f"Aktueller Preis: {price_now} CHF\nVeraenderung seit der letzten Abfrage: {price_difference} CHF")
    if timedelta.days >= 1:
        print(f"Letzte Abfrage vor: {int(timedelta.days)} Tagen, {int(timedelta.seconds /60 / 60)} Stunden, {int(timedelta.seconds / 60 % 60)} Minuten und {timedelta.seconds % 60} Sekunden")
    elif timedelta.seconds > 3600:
        print(f"Letzte Abfrage vor: {int(timedelta.seconds /60 / 60)} Stunden, {int(timedelta.seconds / 60 % 60)} Minuten und {timedelta.seconds % 60 } Sekunden")
    elif timedelta.seconds > 60: 
        print(f"Letzte Abfrage vor: {int(timedelta.seconds / 60)} Minuten und {timedelta.seconds %60} Sekunden")
    else:
        print(f"Letzte Abfrage vor: {int(timedelta.seconds)} Sekunden")



if __name__ == "__main__":
    main()