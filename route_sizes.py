import json
ROUTES = 'traceroute_results/vnu_edu_vn_routes.json'

with open(ROUTES) as f:
    routes = json.load(f)
print(f'Biggest: {max((len(route) for route in routes))}')
print(f'Smallest: {min((len(route) for route in routes))}')