from numpy.random import choice
import math
import numpy as np


def exp(x):
    return np.exp(-x)


def distribution(n: int, delta=2, func=exp):
    """
    Function that creates the probability distribution from the given function
    """
    start = -delta
    end = delta

    xs = np.linspace(start, end, n)

    nums = func(xs)
    probabilities = nums / nums.sum()

    prob_dict = {i: prob for i, prob in enumerate(probabilities)}

    return prob_dict


def lin_prob(n):
    """
    Very simple linear probability distribution
    """
    sum_ = n * (n + 1) / 2
    return [(n - i) / sum_ for i in range(n)]


def generate1(n: int, k: int, p: dict):
    """
    Function that generates the first set of preferences
    """
    preferences = []
    choices = [i for i in range(n)]
    p = list(p.values())

    for _ in range(n):
        preferences.append(list(choice(choices, replace=False, p=p, size=k)))

    return preferences


def generate2(n: int, k: int, preferences: list, p: dict):
    """
    Function that, based on the first set of preferences
    generates the second set of preferences
    """

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
                list(choice(list(choices), replace=False, p=prob, size=len(choices)))
            )
        else:
            new_preferences.append([])

    return new_preferences


def get_preferences(n: int, k: int, delta=2):
    """
    Get preferences for both sides of the market as dictionaries
    """

    p = distribution(n, delta, func=exp)

    prefs1 = generate1(n, k, p)
    prefs2 = generate2(n, k, prefs1, p)

    pref_dict1 = {agent: list(prefs) for agent, prefs in enumerate(prefs1)}
    pref_dict2 = {agent: list(prefs) for agent, prefs in enumerate(prefs2)}

    return pref_dict1, pref_dict2


if __name__ == "__main__":

    n = 10
    k = 5

    preferences = get_preferences(n, k)
    print(preferences[0])
