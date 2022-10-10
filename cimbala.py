import statistics as st
from scipy.stats import t
import numpy as np

def outliers(data):
  prom = st.mean(data)
  S = st.stdev(data)
  alpha = 0.05
  n = len(data)
  t_alfa2 = t.ppf(alpha, n-2)
  tau = (t_alfa2 * (n-1))/(np.sqrt(n) * np.sqrt(n - 2 + t_alfa2**2))

  return [muestra for muestra in data if np.abs(muestra - prom) > tau * S]