from numpy.random import choice
import math
import numpy as np


def exp_prob(n, delta=2):
    start = -delta
    end = delta

    xs = np.linspace(start, end, n)

    nums = np.exp(-xs)
    probabilities = nums / nums.sum()

    prob_dict = {i: prob for i, prob in enumerate(probabilities)}

    return prob_dict


def lin_prob(n):
    """
    Very simple linear probability distribution
    """
    sum_ = n * (n + 1) / 2
    return [(n - i) / sum_ for i in range(n)]


def generate1(n, k, p):
    res = []
    choices = [i for i in range(n)]
    p = list(p.values())

    for _ in range(n):
        res.append(choice(choices, replace=False, p=p, size=k))

    return res


def generate2(n, k, preferences, p):

    # List to hold the choices the proposee has to choose
    # between when generating preferences
    all_choices = []

    # Check for choices
    for recipient in range(n):
        choices = set()
        for proposer, prefs in enumerate(preferences):
            if recipient in prefs:
                choices.add(proposer)
        all_choices.append(choices)

    # Generate the preferences of the other side
    # based on the same probability distribution and the choices
    new_preferences = []

    for recipient, choices in enumerate(all_choices):

        prob = np.array([p[choice] for choice in choices])

        prob = prob / prob.sum()

        if len(choices) > 0:
            new_preferences.append(
                choice(list(choices), replace=False,
                       p=prob, size=len(choices))
            )
        else:
            new_preferences.append([])

    return new_preferences


if __name__ == "__main__":

    n = 100
    k = 5
    delta = 2
    p = exp_prob(n, delta)

    print("First side:")

    result = generate1(n, k, p)

    for pref in result:
        print(pref)

    print("\nSecond side:")

    result2 = generate2(n, k, result, p)

    for choices in result2:
        print(choices)
