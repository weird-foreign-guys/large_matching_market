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

def deviation_count_mockup(proposer_prefs,proposed_prefs):
        truthful_match = deffered_acceptance(proposer_prefs,proposed_prefs)
        
        females_left = proposed_prefs.keys()
        proposed_prefs_d = proposed_prefs
        deviation_count = 0
        #Run |females| "person has devaition" test
        while females_left != []: 
                female = females_left.pop()
                #Run O(|males|) devaiations for female, continue while devaitions are possbile
                while proposed_prefs_d[female] != []:
                        proposed_prefs_d[female] = proposed_prefs_d[female][:-1]
                        matching_d = deffered_acceptance(proposer_prefs,proposed_prefs_d)
                        if(useful_deviation(truthful_match,matching_d,female,proposed_prefs[female])):
                                count += 1
                                break
        return count




        




#Run after defered acceptance to check if a useful matching has occured. If True, can continue to next deviation.
 def useful_deviation(truthful_match,result_match,deviator,proposed_prefs):
        preference_order = proposed_prefs[deviator] 
        
        if(preference_order.index(truthful_match[deviator]) - preference_order.index(result_match[deviator]) > 0: 
                return True

        return False
     

