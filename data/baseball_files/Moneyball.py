import pandas as pd
import re
import matplotlib.pyplot as plt

%matplotlib inline

master = pd.read_csv('Master.csv', sep=",")

player = master[['playerID', 'nameFirst', 'nameLast']]

salary = pd.read_csv('Salaries.csv', sep=',')

positions = pd.read_csv('Fielding.csv', sep=',')

positions = positions[['yearID', 'teamID', 'playerID', 'POS']]

salary = salary[['yearID', 'teamID', 'playerID', 'salary']]

player_salary = pd.merge(salary, player)

batting = pd.read_csv('Batting.csv', sep=',')

batting = batting[['yearID', 'teamID', 'playerID', 'AB', 'H', 'BB', 'HBP', 'SF'
                   ]]

batting.head()

all_things_considered = pd.merge(pd.merge(player_salary, positions), batting)

all_things_considered['OBP'] = ((all_things_considered['H'] +
                                all_things_considered['BB'] +
                                all_things_considered['HBP']) /
                                (all_things_considered['AB'] +
                                all_things_considered['H'] +
                                all_things_considered['BB'] +
                                all_things_considered['HBP'] +
                                 all_things_considered['SF']))

all_things_considered['ratio'] = all_things_considered['OBP'] /
all_things_considered['salary']
birth_year_data = all_things_considered[all_things_considered.yearID == 1986]
birth_year_data

birth_year_data.drop_duplicates()
birth_year_data.dropna()

ratio_sorted_1986_data = birth_year_data.sort(['ratio'], ascending=False)
roster_of_1986_players = ratio_sorted_1986_data[ratio_sorted_1986_data.AB > 20]
roster_of_1986_players = roster_of_1986_players.drop_duplicates(['playerID'])
roster_of_1986_players = roster_of_1986_players.drop_duplicates(['POS'])

roster_of_1986_players

roster_of_1986_players.reset_index
roster_of_1986_players

roster_of_1986_players.drop(roster_of_1986_players.index[[0, 3]])
