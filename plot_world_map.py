import requests
import json
import pandas as pd
import plotly.express as px


API_URL = 'http://ip-api.com/batch?fields=status,message,lat,lon'
COLORS = ['blue', 'red', 'green', 'orange', 'magenta', 'crimson']


def validate_success(response):
    for result in response.json():
        if not result["status"] or result["status"] != "success":
            raise RuntimeError(
                f"No se pudo procesar alguna de las IPs. Output: {result}")


def request_ips(ips):
    ips = [ip for ip in ips if ip != '192.168.0.1']
    response = requests.post(API_URL, data=json.dumps(ips))

    print(response.text)
    validate_success(response)
    return pd.json_normalize(response.json())


with open('traceroute_results/bsu_by_routes.json') as f:
    routes = json.load(f)

idx = 0
df = pd.DataFrame(columns=['lat', 'lon', 'color'])
for ips in routes:
    result = request_ips(ips)
    result['color'] = COLORS[idx]
    df = pd.concat([df, result])
    idx += 1
print(df.to_string())
fig = px.line_geo(df, lat="lat", lon="lon",
                  projection="equirectangular", color='color')
fig.show()
