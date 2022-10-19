import json
"""Idealmente habria que haber guardado los time exceeded cuando corrimos
"""
RESPONSES = 'traceroute_results/uonbi_ac_ke_responses.json'
with open(RESPONSES) as f:
    responses = json.load(f)
last_jump_number = max((int(n) for n in responses))
expected_responses = last_jump_number * 30
actual_responses = sum((len(response) for response in responses.values()))


print(f'Percentage of missed time exceeded: {(1 - actual_responses / expected_responses) * 100}')