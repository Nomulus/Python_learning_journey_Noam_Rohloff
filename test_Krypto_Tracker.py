import pytest
import Krypto_Tracker

def compare_price():
    assert Krypto_Tracker.compare_price("100", "200") == f"Aktueller Preis: 100 CHF\nVeraenderung seit der letzten Abfrage: -100 CHF"