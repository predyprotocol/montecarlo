import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import random as rd
import statistics as st

start_price = 2500


def get_p(k): return rd.random()


def get_price(w, volatility):
    return start_price * np.exp(w * volatility - volatility * volatility / 2)


def get_sqrt_price(price):
    return np.sqrt(price)


def get_expected_sqrt_price(volatility):
    P = 1000
    SQRT_PRICES_AFTER_A_YEAR = []
    for k in range(P):
        p = get_p(k)
        SQRT_PRICES_AFTER_A_YEAR.append(
            get_sqrt_price(get_price(norm.ppf(p), volatility)))
    expected_sqrt_price = st.mean(SQRT_PRICES_AFTER_A_YEAR)
    return expected_sqrt_price


def get_theoretical_sqrt_price(volatility):
    return get_sqrt_price(start_price) * np.exp(-volatility * volatility / 8)


def show_chart():
    R1 = []
    R2 = []
    for k in range(20, 200):
        R1.append([k, get_expected_sqrt_price(k / 100)])
        R2.append([k, get_theoretical_sqrt_price(k / 100)])
    x1, y1 = zip(*R1)
    x2, y2 = zip(*R2)

    plt.scatter(x1, y1, linewidths=1, label='Simulation')
    plt.scatter(x2, y2, linewidths=1, label='Theoretical')

    plt.title("Monte Carlo Simulation for Square Root Price(Start Price is $2500)")
    plt.xlabel("volatility")
    plt.ylabel("price after a year")
    plt.legend()

    plt.savefig("chart.png")
    plt.show()


show_chart()
