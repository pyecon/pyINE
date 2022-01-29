import requests
import pandas as pd
from datetime import datetime

# TODO: function for serie, function for table
def get_data(
    function: str,
    id: str,
    language: str = "ES",
    params: "list" = []
    ):

    # TODO: make the input serie instead of DATOS_SERIE
    url = f"https://servicios.ine.es/wstempus/js/{language}/{function}/{id}?date=:"
    requested_data = requests.get(url)

    #if not "Data" in requested_data.json().keys():
    #    return "No data found"

    # Need to get the different dicts containing data and make them into df
    data = requested_data.json()

    big_df = pd.DataFrame()
    for i in range(len(data)):
        current_data = data[i].get("Data")
        print(data[i].keys())
        df = pd.DataFrame(current_data).loc[:, ["Fecha", "Anyo", "Valor"]]  # problems
        df = df.assign(Nombre=data[i].get("Nombre", ""))
        big_df = pd.concat([big_df, df])

    date = big_df.Fecha.apply(
        lambda d: datetime.fromtimestamp(int(d)/1000).strftime('%Y-%m-%d %H:%M:%S')
    )
    
    big_df.Fecha = pd.to_datetime(date)
    big_df.rename(columns={"Anyo": "Año"}, inplace=True)
    
    return big_df