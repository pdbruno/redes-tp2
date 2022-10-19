import json
import matplotlib.pyplot as plt
from statistics import mode, mean

filenames = ["traceroute_results/bsu_by_responses.json", 
             "traceroute_results/uonbi_ac_ke_responses.json", 
             "traceroute_results/vnu_edu_vn_responses.json"]

for filename in filenames:
  with open(filename) as f:

    responses = json.load(f)
    res = []
    maxKey = max(int(key) for key in responses.keys())
    ipDest = responses[str(maxKey)][0][0]
    
    for ttl in responses: 
      ipModa = mode([ip for ip, rtt in responses[ttl]])
      promedioRTT = mean([rtt for ip, rtt in responses[ttl] if ip == ipModa])
      res.append((ttl, ipModa, promedioRTT))
      if ipDest == ipModa:
        break

    res.sort(key = lambda tupla: tupla[0])

    saltos = [['Host', res[0][1], res[0][2]]]
    low = 0
    up = 1

    while up < len(res):
      while up < len(res) and res[up][2] - res[low][2] < 0:
        up += 1
      if up < len(res):
        item = [res[low][1], res[up][1], res[up][2] - res[low][2]]
        saltos.append(item)
        low = up
        up += 1

    with open("traceroute_results/" + filename + "saltos.json", "w") as f_saltos:
      json.dump(saltos, f_saltos)

    ips = [salto[0] + " \n " + salto[1] for salto in saltos]
    rtts = [salto[2] for salto in saltos]

    plt.figure(figsize=(len(saltos)*2, len(saltos)))
    ips = [salto[0] + " \n " + salto[1] for salto in saltos]
    rtts = [salto[2] for salto in saltos]
    plt.bar(range(len(rtts)), rtts)
    plt.xticks(range(len(rtts)), labels=ips)
    plt.yticks(range(0, int(max(rtts)) + 30, 30))
    plt.grid(axis="y")
    plt.savefig(filename + "img.png")
    plt.show()
    plt.clf()