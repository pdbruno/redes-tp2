import requests
import json
import pandas as pd
import plotly.express as px


API_URL = 'http://ip-api.com/batch?fields=status,message,country,countryCode,city,lat,lon,query'


def validate_success(response):
    for result in response.json():
        if not result["status"] or result["status"] != "success":
            raise RuntimeError(
                f"No se pudo procesar alguna de las IPs. Output: {result}")


def request_ips(ips):
    response = requests.post(API_URL, data=json.dumps(ips))

    print(response.text)
    validate_success(response)
    return pd.json_normalize(response.json())


ips = ['195.22.220.56', '195.22.199.82', '4.68.62.57', '4.69.215.94',
       '8.245.32.246', '163.139.136.67', '222.230.187.142']
df = request_ips(ips)
fig = px.line_geo(df, lat="lat", lon="lon",
                  projection="equirectangular", text="city")
fig.show()
