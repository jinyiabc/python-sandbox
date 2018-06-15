#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:55:46 2018

@author: jinyi
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

K = 50
S_T = np.linspace(0, 100, 200, endpoint=True)
# S_T_end = np.linspace(0, 10, 10, endpoint=True)

# Calculate the long and short payoffs
long_payoff = S_T - K
short_payoff = K - S_T

plt.plot(S_T, long_payoff)
plt.axhline(0, color='black', alpha=0.3)
plt.axvline(0, color='black', alpha=0.3)
plt.xlim(0, 100)
plt.ylim(-100, 100)
plt.axvline(K, linestyle='dashed', color='r', label='K')
plt.ylabel('Payoff')
plt.xlabel('$S_T$')
plt.title('Payoff of a Long Forward Contract')
plt.legend()
