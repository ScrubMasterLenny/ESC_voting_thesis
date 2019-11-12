import os

class Country():
    """Country class which specifies the (top 10) ranking of a country.
    Optionally gives the score this country achieved in the semifinal."""
    def __init__(self, country, ranking_list, semifinal_score=0):
        self.country = country
        self.ranking_list = ranking_list
        self.semifinal_score = semifinal_score

    def get_ranking_list(self):
        return self.ranking_list

    def get_semifinal_score(self):
        return self.semifinal_score

    def get_ith_ranking(self, i):
        return self.ranking_list[i-1]

class Rule():
    """Rule class consisting of a scoring vector and a vector length.
    Scoring vector is specified from largest to smallest score.
    Will be expanded once the thesis gets to more advanced
    material."""
    def __init__(self, scoring_vector, vector_length):
        self.scoring_vector = scoring_vector
        self.vector_length = vector_length

    def get_scoring_vector(self):
        return self.scoring_vector

    def get_vector_length(self):
        return self.vector_length

class Contest():
    """Contest class includes everything to compute the original outcome
    of a certain year's ESC. Later will also be able to solve the problem(s)
    specified in the thesis proposal."""
    def __init__(self, country_list, voting_rule, nr_of_semifinals=0):
        self.country_list = country_list
        self.voting_rule = voting_rule
        self.nr_of_countries = len(country_list)
        self.nr_of_semifinals = nr_of_semifinals

    def compute_result(self):
        """Computes the result and outputs a dict with each country that scored
        more than 0 points."""
        result = dict()
        rule_vector = self.voting_rule.get_scoring_vector()
        rule_length = self.voting_rule.get_vector_length()
        for country in self.country_list:
            ranking_list = country.get_ranking_list()
            rank = 0
            for c in ranking_list:
                if rank + 1 > rule_length:
                    break
                if c not in result:
                    result[c] = 0
                result[c] += rule_vector[rank]
                rank += 1

        return result

    def print_result(self):
        """Prints the result in a ranking list format"""
        result = self.compute_result()
        for element in sorted(result, key=result.get, reverse=True):
            print(element, result[element])

def dict_to_classes(d, voting_rule):
    """Takes as input a dict outputted by import_scores(),
    and returns a dict with objects of class Contest."""
    ESC_classified = dict()
    for year in range(1975,2016):
        ESC_classified[str(year)] = None

    for year in d:
        country_list = []
        for country in d[year]:
            new_country = Country(country, d[year][country])
            country_list.append(new_country)
        ESC_classified[year] = Contest(country_list, voting_rule)

    return ESC_classified
