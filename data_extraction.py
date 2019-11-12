import csv

def import_scores(file_name = 'votes.csv'):
    """ This function is hardcoded. Reads and puts the votes for the finals
    from 1975 to 2015 in a dictionary. This dict has 2 levels:
    Top level: key = year, value = dict of scoring countries
    Bottom level: key = scoring country, value = ranked list (top 10)"""
    f = open(file_name, "r")
    ff = csv.reader(f)

    ESC = dict()
    for year in range(1975,2016):
        ESC[str(year)] = dict()

    for row in ff:
        if row[0] == 'year':
            continue
        if int(row[0]) not in range(1975,2016) or row[1] != 'final' or row[6] == '0':
            continue
        if row[2] not in ESC[row[0]]:
            ESC[row[0]][row[2]] = dict()
        ESC[row[0]][row[2]][row[3]] = int(row[6])

    scores_to_rankings(ESC)
    return ESC

def scores_to_rankings(ESC_dict):
    """ The ESC dict takes scores from the votes.csv file, which have to be
    turned into a ranked list. This function performs that task."""
    for year in ESC_dict:
        for country in ESC_dict[year]:
            score_dict = ESC_dict[year][country]
            ranking_list = []
            for scored_country in sorted(score_dict, key=score_dict.get, reverse=True):
                ranking_list.append(scored_country)
            ESC_dict[year][country] = ranking_list
    pass
