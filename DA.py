""" This code implements the deferred acceptance algorithm by Gale and Shapley (1962)."""
from copy import deepcopy

"""
function stable_matching {
    Initialize all m ∈ M and w ∈ W to free
    while ∃ free man m who still has a woman w to propose to {
        w = first woman on m's list to whom m has not yet proposed
        if w is free
            (m, w) become engaged
        else some pair (m', w) already exists
            if w prefers m to m'
                m' becomes free
                (m, w) become engaged 
            else
                (m', w) remain engaged
    }
}
"""

# THIS DESTROYES MALE_PREFS!!
def deferred_acceptance(male_prefs, female_prefs):
    # copy to avoid destrcuction
    male_prefs_copy = deepcopy(male_prefs)

    # Initialize all male and female to free
    # matches = {}
    male_matches = {}
    female_matches = {}
    # while ∃ unmatched male who still has a female to propose to
    while True:
        unmatched_males = [
            male for male in male_prefs_copy.keys() if male not in male_matches
        ]
        print("Unmatched_males: ", unmatched_males)
        if unmatched_males == []:
            # end of the algorithm
            break
        for male in unmatched_males:
            # if no more females to propose to, this male is permanently unmatched.
            if male_prefs_copy[male] == []:
                male_matches[male] = "NA"
                break
            # propose to the most preferred female and update the male's preference
            female = male_prefs_copy[male].pop(0)

            print("Trying %s with %s... " % (male, female), end="")

            prev_male = female_matches.get(female, None)
            # get male's index in female's preference order. None if not in preference order.
            prev_male_index = (
                female_prefs[female].index(prev_male) if prev_male else None
            )
            this_male_index = (
                female_prefs[female].index(male)
                if male in female_prefs[female]
                else None
            )

            # print("\nprev: ", prev_male_index, end=' ')
            # print("this: ", this_male_index)
            if this_male_index == None:
                # female rather be unmatched
                print("rejected")
            elif prev_male_index == None:
                # match
                male_matches[male] = female
                female_matches[female] = male
                print("new match")
            elif prev_male_index > this_male_index:
                # new match and delete old match
                male_matches[male] = female
                female_matches[female] = male
                del male_matches[prev_male]
                print("updated match")
            else:
                # female prefer current match
                print("no change")
    # print(matches)
    # return {male: matches[male] for male in male_prefs.keys()}
    return male_matches


# TODO; delete the test
"""The test implementation is based on Cristi Burcà (2015) https://gist.github.com/scribu."""
def test_popularity_contest():
    """Every male has the same preferences as every other male; same for females."""
    FEMALES = ["F1", "F2", "F3"]
    MALES = ["M1", "M2", "M3", "M4", "M5"]

    MALE_PREFS = {key: FEMALES.copy() for key in MALES}
    FEMALE_PREFS = {key: MALES.copy() for key in FEMALES}

    matches = deferred_acceptance(MALE_PREFS, FEMALE_PREFS)
    print(matches)
    print("{'M1': 'F1', 'M2': 'F2', 'M3': 'F3', 'M4': 'M4', 'M5': 'M5'}")
    # assert matches == {'M1': 'F1', 'M2': 'F2', 'M3': 'F3', 'M4': 'M4', 'M5': 'M5'}


def test_cycle():
    """Males have different preferences, while females have identical preferences."""
    MALE_PREFS = {"M1": ["F2", "F1"], "M2": ["F1", "F2"]}
    FEMALE_PREFS = {"F1": ["M1", "M2"], "F2": ["M2", "M1"]}
    matches = deferred_acceptance(MALE_PREFS, FEMALE_PREFS)
    print(matches)
    print("{'M1': 'F2', 'M2': 'F1'}")
    # assert matches == {'M1': 'F2', 'M2': 'F1'}


"""
if __name__ == "__main__":
    test_popularity_contest()
    test_cycle()
"""
