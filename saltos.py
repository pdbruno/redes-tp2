def get_saltos(name, ipDest):
  responses = None
  with open(f'traceroute_results/{name}.json') as f:
    responses = json.load(f)
  res = []

  for ttl in responses: 
    ipModa = mode([ip for ip, rtt in responses[ttl]])
    promedioRTT = mean([rtt for ip, rtt in responses[ttl] if ip == ipModa])
    res.append((ttl, ipModa, promedioRTT))
    if ipDest == ipModa:
      break

  res.sort(key = lambda tupla: int(tupla[0]))

  saltos = []
  low = 0
  up = 1
  while up < len(res):
    while up < len(res) and res[up][2] - res[low][2] < 0:
      up += 1
    if up < len(res):
      saltos.append((res[up][2] - res[low][2], f'{res[low][1]}\nto\n{res[up][1]}'))
      low = up
      up += 1

  return saltos