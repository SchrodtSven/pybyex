# Playing with dict compehension and
#
#
# AUTHOR Sven Schrodt
# SINCE 20250707

# original dict Corporation -> [country, business volume]
dta_dct = {
    "Volkswagen": {"country": "DE", "vol": 129.92},
    "Walmart": {"country": "US", "vol": 523.964},
    "Amazon": {"country": "US", "vol": 280.522},
    "Killuminati Corp.": {"country": "US", "vol": 12342.666},
    "Apple": {"country": "US", "vol": 264.983},
    "Toyota": {"country": "JP", "vol": 30_000},
    "Sony": {"country": "JP", "vol": 23_000},
}


def ccy_cvt(ctry: str, value: float) -> float:
    """Converting currency value from origin country currency to EUR (€)

    Args:
        ctry (str): Country abbr.
        value (float): value in orig. currency

    Returns:
        float: value converted to €
    """

    def clc() -> float:
        """Inner function - because we wanted to test it

        Returns:
            float: value converted to €
        """
        usd_eur = 0.85
        yen_eur = 0.0059

        if ctry == "US":
            return round(usd_eur * value, 2)
        elif ctry == "JP":
            return round(yen_eur * value, 2)
        else:
            return value

    return clc()


# Dict comprehension
vol_dct = {k: ccy_cvt(v["country"], v["vol"]) for (k, v) in dta_dct.items()}

print(vol_dct)
