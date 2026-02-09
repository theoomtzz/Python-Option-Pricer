from datetime import datetime
import numpy as np
import pandas as pd

def year_fraction_from_today(date_str, convention="ACT/365"):
    """
    Calcule la fraction d'année entre aujourd'hui et une date donnée.

    Parameters
    ----------
    date_str : str
        Date au format "MM-DD-YYYY"
    convention : str
        "ACT/365" ou "ACT/360"

    Returns
    -------
    float
        Fraction d'année
    """
    today = datetime.today().date()
    target_date = datetime.strptime(date_str, "%Y-%m-%d").date()

    if target_date < today:
        raise ValueError("La date donnée est dans le passé")

    days = (target_date - today).days

    if convention == "ACT/365":
        return days / 365.0
    elif convention == "ACT/360":
        return days / 360.0
    else:
        raise ValueError("Convention inconnue (utilise 'ACT/365' ou 'ACT/360')")
    
import numpy as np
import pandas as pd



def year_fraction_act365(start_date_str, date_array):
    start = pd.to_datetime(start_date_str)

    # Convertit en DatetimeIndex (marche pour np.array, list, Series, Index)
    dates = pd.to_datetime(date_array)

    # TimedeltaIndex / Series de timedeltas -> on récupère des jours via .days ou via / np.timedelta64
    delta = dates - start

    # Méthode universelle: convertir en "jours" par division
    delta_days = (delta / np.timedelta64(1, "D")).astype(float)

    return delta_days / 365.0
