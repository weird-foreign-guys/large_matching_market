from deferred_acceptance import deferred_acceptance
from copy import deepcopy


def count_useful_deviatiors(male_prefs, female_prefs):
    _, truthful_match = deferred_acceptance(male_prefs, female_prefs)
    dev_female_prefs = deepcopy(female_prefs)
    count = 0
    # Run |females| "person has deviation" test
    for female in female_prefs.keys():
        # Run O(|males|) devaiations for female, continue while devaitions are possbile
        while len(dev_female_prefs[female]) > 1:
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
