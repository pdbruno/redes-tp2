import statistics as st
from scipy.stats import t
import numpy as np

def outliers(data):
  res = []
  while data.len > 0:
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
  return res