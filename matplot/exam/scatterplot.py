import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook

cookbook_data = cbook.get_sample_data('goog.npz')['price_data']
cookbook_data = cookbook_data[-50:]

delta1 = np.diff(cookbook_data["adj_close"]) / cookbook_data["adj_close"][:-1]
#volume = (15 * cookbook_data["volume"][:-2] / cookbook_data["volume"][0]) ** 2
#close = 0.003 * cookbook_data["close"][:-2] / 0.003 * cookbook_data["open"][:-2]

volume = (15 * cookbook_data["volume"][:-2] / cookbook_data["volume"][0]) ** 2
close = 0.7 * cookbook_data["close"][:-2] / 0.7 * cookbook_data["open"][:-2]

close = ['#0f0f0f']
close = [ 'b','g','y','r'] * 12


fig, ax = plt.subplots(label="Google Price from Cook Book",subplot_kw={"projection": "polar"})

#ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.8, marker='D')

#ax.scatter(np.random.normal(0,2,24), np.random.normal(0,2,24), c=close[:24],  alpha=0.8, marker='D')

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume and percent change')
ax.grid(True)
fig.tight_layout()
plt.show()