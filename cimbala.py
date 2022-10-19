import statistics as st
from scipy.stats import t
import numpy as np

def outliers(data):
  res = []
  while len(data) > 0:
    prom = st.mean(data)
    S = st.stdev(data)
    alpha = 0.05
    n = len(data)
    t_alfa2 = t.ppf(1-alpha/2, n-2)
    tau = (t_alfa2 * (n-1))/(np.sqrt(n) * np.sqrt(n - 2 + t_alfa2**2))
    deltas = [np.abs(x - prom) for x in data]
    outlier_candidate = [x for x in data if np.abs(x - prom) == max(deltas)][0]
    if max(deltas) > tau * S:
      res.append(outlier_candidate)
      data.remove(outlier_candidate)
    else:
      break
  return res

import statistics as st
from scipy.stats import t
import numpy as np

def outliers(data):
  res = []
  while len(data) > 0:
    prom = st.mean(data)
    S = st.stdev(data)
    alpha = 0.05
    n = len(data)
    t_alfa2 = t.ppf(1-alpha/2, n-2)
    tau = (t_alfa2 * (n-1))/(np.sqrt(n) * np.sqrt(n - 2 + t_alfa2**2))
    deltas = [np.abs(x - prom) for x in data]
    outlier_candidate = [x for x in data if np.abs(x - prom) == max(deltas)][0]
    if max(deltas) > tau * S:
      res.append(outlier_candidate)
      data.remove(outlier_candidate)
    else:
      break
  return res

filenames = ["traceroute_results/bsu_by_responses.jsonsaltos.json", 
             "traceroute_results/uonbi_ac_ke_responses.jsonsaltos.json", 
             "traceroute_results/vnu_edu_vn_responses.jsonsaltos.json"]

for filename in filenames:
  with open(filename) as f:
    saltos = json.load(f)
    rtts = [salto[2] for salto in saltos]
    #print(saltos)
    rtt_outliers = outliers(rtts)
    saltos_outliers = [x for x in saltos if x[2] in rtt_outliers]
    print(saltos_outliers)