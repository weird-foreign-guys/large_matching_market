from DA import deferred_acceptance
from copy import deepcopy

"""MALE_PREFS = {
        'M1': ['F2','F1','F3'],
        'M2': ['F1','F3','F2'],
        'M3': ['F1','F2','F3'],
}
 FEMALE_PREFS = {
        'F1': ['M1','M3'],
        'F2': ['M1','M2','M3'],
        'F3': ['M2','M3','M1'],
    }

 matches == {'M1': 'F1', 'M2': 'F2', 'M3': 'F3', 'M4': 'M4', 'M5': 'M5'}"""

"""
def count_useful_deviatiors(male_prefs, female_prefs):
    truthful_match = deferred_acceptance(male_prefs, female_prefs)

    females_left = female_prefs.keys()
    female_prefs_d = female_prefs
    count = 0
    # Run |females| "person has devaition" test
    while females_left != []:
        female = females_left.pop()
        # Run O(|males|) devaiations for female, continue while devaitions are possbile
        while female_prefs_d[female] != []:
            female_prefs_d[female] = female_prefs_d[female][:-1]
            matching_d = deferred_acceptance(male_prefs, female_prefs_d)
            if useful_deviation(
                truthful_match, matching_d, female, female_prefs[female]
            ):
                count += 1
                break
    return count
"""


def count_useful_deviatiors(male_prefs, female_prefs):
    _, truthful_match = deferred_acceptance(male_prefs, female_prefs)
    dev_female_prefs = deepcopy(female_prefs)
    count = 0
    # Run |females| "person has devaition" test
    for female in female_prefs.keys():
        # Run O(|males|) devaiations for female, continue while devaitions are possbile
        while dev_female_prefs[female] != []:
            dev_female_prefs[female] = dev_female_prefs[female][:-1]
            _, matching_d = deferred_acceptance(male_prefs, dev_female_prefs)

            if useful_deviation(truthful_match, matching_d, female, female_prefs):
                count += 1
                break
        dev_female_prefs[female] = female_prefs[female]
    return count


# Run after defered acceptance to check if a useful matching has occured. If True, can continue to next deviation.
def useful_deviation(truthful_match, deviated_match, deviator, proposed_prefs):
    preference_order = proposed_prefs[deviator]
    """
    print(deviator)
    print(deviated_match)
    print(deviated_match[deviator])
    print(truthful_match)
    print(truthful_match[deviator])
    print(preference_order)
    """
    # TODO deal with "NA"
    if deviated_match[deviator] == "NA":
        # if deviation gives no match, it is never useful
        return False
    elif truthful_match[deviator] == "NA":
        # if truthful gives no match and deviation gives a match, it is a useful deviation
        return True
    else:
        return preference_order.index(
            truthful_match[deviator]
        ) > preference_order.index(deviated_match[deviator])
