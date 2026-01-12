import requests
import customtkinter
import datetime
import json


class CheckBoxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.light_mode_var = customtkinter.BooleanVar(value=False)

        self.checkbox_light_mode = customtkinter.CTkCheckBox(
            self,
            text="light mode",
            command=self.appearance_mode,
            variable=self.light_mode_var,
            onvalue=True,
            offvalue=False,
        )
        self.checkbox_light_mode.grid(
            row=0, column=0, padx=10, pady=(10, 0), sticky="w"
        )

        self.checkbox_old_price = customtkinter.CTkCheckBox(self, text="show old price")
        self.checkbox_old_price.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_time_offset = customtkinter.CTkCheckBox(
            self, text="show time offset"
        )
        self.checkbox_time_offset.grid(
            row=2, column=0, padx=10, pady=(10, 0), sticky="w"
        )

    def appearance_mode(self):
        if self.light_mode_var.get():
            customtkinter.set_appearance_mode("light")
        else:
            customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self._set_appearance_mode("dark")
        customtkinter.set_default_color_theme("themes/metal.json")

        self.title("Krypto Tracker by Noam")
        self.geometry("350x300")
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = CheckBoxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.comparison_button = customtkinter.CTkButton(
            self, text="get and compare Bitcoin price to last time", command=get_price
        )
        self.comparison_button.grid(row=0, column=1, padx=10, pady=(20, 0), sticky="w")


def main():
    app = App()
    app.mainloop()


def get_price():
    loaded_price, loaded_date = try_load_data("price_over_time.json")
    if not loaded_price and not loaded_date:
        loaded_price, loaded_date = (
            72262,
            datetime.datetime.fromisoformat("2026-01-04 21:10:06.271862"),
        )

    price_now, time_now = get_current_price_and_date()

    write_current_price_and_date(price_now, time_now)

    print(compare_price(price_now, loaded_price), compare_date(loaded_date, time_now))


def get_current_price_and_date():
    request = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=chf"
    ).json()
    try:
        price_now = (request["bitcoin"]["chf"],)[0]
    except KeyError:
        raise SystemExit("rate Limit has been exceeded.")
    time_now = datetime.datetime.now()
    return price_now, time_now


def write_current_price_and_date(price_now, time_now):
    with open("price_over_time.json", "w") as file:
        json.dump([price_now, time_now.isoformat()], file)


def try_load_data(file_name):
    try:
        loaded_price, loaded_date = load_price_and_date(file_name)
    except FileNotFoundError:
        print("No prior data to compare to, will output with old data")
        loaded_price, loaded_date = None, None
    return loaded_price, loaded_date


def load_price_and_date(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
        return data[0], datetime.datetime.fromisoformat(data[1])


def compare_price(price_now, loaded_price):
    price_difference = price_now - loaded_price
    return f"Aktueller Preis: {price_now} CHF\nVeraenderung seit der letzten Abfrage: {'+' if price_difference > 0 else ''}{price_difference} CHF"


def compare_date(loaded_date, time_now):
    timedelta = time_now - loaded_date
    if timedelta.days >= 1:
        return f"Letzte Abfrage vor: {int(timedelta.days)} Tagen, {int(timedelta.seconds / 60 / 60)} Stunden, {int(timedelta.seconds / 60 % 60)} Minuten und {timedelta.seconds % 60} Sekunden"
    elif timedelta.seconds > 3600:
        return f"Letzte Abfrage vor: {int(timedelta.seconds / 60 / 60)} Stunden, {int(timedelta.seconds / 60 % 60)} Minuten und {timedelta.seconds % 60} Sekunden"
    elif timedelta.seconds > 60:
        return f"Letzte Abfrage vor: {int(timedelta.seconds / 60)} Minuten und {timedelta.seconds % 60} Sekunden"
    else:
        return f"Letzte Abfrage vor: {int(timedelta.seconds)} Sekunden"


if __name__ == "__main__":
    main()
