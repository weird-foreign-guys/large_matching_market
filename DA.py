""" This code implements the deferred acceptance algorithm by Gale and Shapley (1962)."""
from copy import deepcopy
from collections import deque

def deferred_acceptance(male_prefs, female_prefs):
    # copy to avoid destrcuction
    male_prefs_copy = deepcopy(male_prefs)

    # Use deque instead of list for male_prefs_copy for faster pop
    # but keep list for female_prefs since we perfoem lookups
    for k,v in male_prefs_copy.items():
        male_prefs_copy[k] = deque(v)
    # male_prefs_copy = {(k,deque(v)) for (k,v) in male_prefs_copy.items()}

    # Initialize all male and female to free
    male_matches, female_matches = {}, {}

    # while ∃ unmatched male who still has a female to propose to
    while True:
        unmatched_males = [
            male for male in male_prefs_copy.keys() if male not in male_matches
        ]
        # print("Unmatched_males: ", unmatched_males)
        if unmatched_males == []:
            # End of the algorithm
            break
        for male in unmatched_males:
            if not male_prefs_copy[male]:
            #if male_prefs_copy[male] == []:
                # No more females to propose to. This male is permanently unmatched.
                male_matches[male] = "NA"
                break
            # propose to the most preferred female and update the male's preference
            # female = male_prefs_copy[male].pop(0)
            female = male_prefs_copy[male].popleft()

            # print("Cheking %s with %s :" % (male, female), end="")

            # get male's index in female's preference order. None if not in preference order.
            prev_male = female_matches.get(female, None)
            prev_male_index = (
                female_prefs[female].index(prev_male) if prev_male else None
            )
            this_male_index = (
                female_prefs[female].index(male)
                if male in female_prefs[female]
                else None
            )

            if this_male_index == None:
                ##print("rejected. reciepient prefer unmatched")
                pass
            elif prev_male_index == None:
                male_matches[male] = female
                female_matches[female] = male
                ##print("new match")
            elif prev_male_index > this_male_index:
                male_matches[male] = female
                female_matches[female] = male
                del male_matches[prev_male]
                ##print("updated match")
            else:
                ##print("rejected. reciepient prefer current")
                pass

    # fill "NA" for female_matches
    for female in female_prefs.keys():
        if female not in female_matches:
            female_matches[female] = "NA"

    # return {male: matches[male] for male in male_prefs.keys()}
    return male_matches, female_matches


def test():
    MALE_PREFS = {"M1": ["F2", "F1"], "M2": ["F1", "F2"]}
    FEMALE_PREFS = {"F1": ["M1", "M2"], "F2": ["M2", "M1"]}
    matches = deferred_acceptance(MALE_PREFS, FEMALE_PREFS)
    print(matches)
    print("{'M1': 'F2', 'M2': 'F1'}")


if __name__ == "__main__":
    pass
    # test()
