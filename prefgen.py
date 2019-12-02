from numpy.random import choice
import math
import numpy as np


def exp_prob(n):
    delta = 2
    start = -delta
    end = delta

    xs = np.linspace(start, end, n)

    nums = np.exp(-xs)
    probabilities = nums / nums.sum()

    # prob_dict = {i: prob for i, prob in enumerate(probabilities)}

    return probabilities  # prob_dict


def lin_prob(n):
    """
    Very simple linear probability distribution
    """
    sum_ = n*(n+1) / 2
    return [(n - i) / sum_ for i in range(n)]


def generate1(n, k, corr):
    res = []
    choices = [i for i in range(n)]
    p = exp_prob(n)

    for i in range(n):
        res.append(choice(choices, replace=False, p=p, size=k))

    return res


def generate2(n, preferences):

    # List to hold the choices the proposee has to choose
    # between when generating preferences
    all_choices = []

    for recipient in range(n):
        choices = set()
        for proposer, prefs in enumerate(preferences):
            if recipient in set(prefs):
                choices.add(proposer)
        all_choices.append(choices)

    return all_choices


if __name__ == '__main__':

    print(exp_prob(10))

    # result = generate1(10, 7, 1)

    # for pref in result:

    #     print(pref)

    # result2 = generate2(10, result)

    # for choices in result2:
    #     print(choices)
