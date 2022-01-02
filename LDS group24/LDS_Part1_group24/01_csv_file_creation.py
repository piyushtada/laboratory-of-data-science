# -*- coding: utf-8 -*-
"""01-csv-file-creation.ipynb

"""

# import required libraries
import csv

"""# get column names of the csv"""

with open('./data/tennis.csv', 'r') as file:
    data = csv.reader(file)
    print(next(data)) #we ask for next item in iterable

"""# build the match csv
- select the columns important for us we want put them as header for the csv
"""

header = ['tourney_id', 'match_id', 'winner_id', 'loser_id', 'score', 'best_of', 'round', 
            'minutes', 'w_ace', 'w_df', 'w_svpt', 'w_1stWon',  
                'w_SvGms' ,'w_bpSaved', 'w_bpFaced', 'l_ace', 'l_df', 'l_svpt', 'l_1stIn', 
                'l_1stWon', 'l_2ndWon', 'l_SvGms', 'l_bpSaved', 'l_bpFaced', 'winner_rank', 
                'winner_rank_points' ,'loser_rank', 'loser_rank_points' ]

with open('./data/tennis.csv', 'r', newline='') as file:
    # open tennis file
    data = csv.DictReader(file)
    
    # create a new file for match
    match_csv = open('./output/match.csv', 'w')
    
    # creat a writer object so we can write to the file with header we defined earliar
    match_writer = csv.DictWriter(match_csv, fieldnames=header)
    
    # write the header to the file
    match_writer.writeheader()
    
    # write data row by row
    for row in data:
        match_writer.writerow({
            'tourney_id': row['tourney_id'],
            'match_id': row['match_num'] + row['tourney_id'],
            'winner_id': row['winner_id'],
            'loser_id': row['loser_id'],
            'score': row['score'],
            'best_of': row['best_of'],
            'round': row['round'], 
            'minutes': row['minutes'],
            'w_ace': row['w_ace'],
            'w_df': row['w_df'],
            'w_svpt': row['w_svpt'],
            'w_1stWon': row['w_1stWon'],  
            'w_SvGms': row['w_SvGms'],
            'w_bpSaved': row['w_bpSaved'],
            'w_bpFaced': row['w_bpFaced'],
            'l_ace': row['l_ace'],
            'l_df': row['l_df'],
            'l_svpt': row['l_svpt'],
            'l_1stIn': row['l_1stIn'], 
            'l_1stWon': row['l_1stWon'],
            'l_2ndWon': row['l_2ndWon'],
            'l_SvGms': row['l_SvGms'],
            'l_bpSaved': row['l_bpSaved'],
            'l_bpFaced': row['l_bpFaced'],
            'winner_rank': row['winner_rank'], 
            'winner_rank_points': row['winner_rank_points'],
            'loser_rank': row['loser_rank'],
            'loser_rank_points': row['loser_rank_points'] 
        })
    # close the match file
    match_csv.close()

"""# make the above cell easy to use for other csv we need to create
- so we take out the input variables out 
- now we can just change the input variables and use the above cell to create remaining files
- things we need to change now will be
    - the input variables
    - paring we need for all the files
"""

##================================input variables=============================================##
##============================================================================================##
data_csv_path = './data/tennis.csv'
output_csv_path = './output/match.csv'
output_csv_header = ['tourney_id', 'match_id', 'winner_id', 'loser_id', 'score', 'best_of', 
                     'round','minutes', 'w_ace', 'w_df', 'w_svpt', 'w_1stWon','w_SvGms' ,
                     'w_bpSaved', 'w_bpFaced', 'l_ace', 'l_df', 'l_svpt', 'l_1stIn', 
                     'l_1stWon', 'l_2ndWon', 'l_SvGms', 'l_bpSaved', 'l_bpFaced', 
                     'winner_rank', 'winner_rank_points' ,'loser_rank', 'loser_rank_points']
##============================================================================================##
##============================================================================================##

with open(data_csv_path, 'r', newline='') as file:
    # open tennis file
    data = csv.DictReader(file)
    
    # create a new file for match
    output_csv = open(output_csv_path, 'w')
    
    # creat a writer object so we can write to the file with header we defined earliar
    output_csv_writer = csv.DictWriter(output_csv, fieldnames = output_csv_header)
    
    # write the header to the file
    output_csv_writer.writeheader()
    
    # write data row by row
    for row in data:
       ##=========================change paring according to csv required=============================##
       ##============================================================================================##
        output_csv_writer.writerow({
            'tourney_id': row['tourney_id'],
            'match_id': row['match_num'] + row['tourney_id'],
            'winner_id': row['winner_id'],
            'loser_id': row['loser_id'],
            'score': row['score'],
            'best_of': row['best_of'],
            'round': row['round'], 
            'minutes': row['minutes'],
            'w_ace': row['w_ace'],
            'w_df': row['w_df'],
            'w_svpt': row['w_svpt'],
            'w_1stWon': row['w_1stWon'],  
            'w_SvGms': row['w_SvGms'],
            'w_bpSaved': row['w_bpSaved'],
            'w_bpFaced': row['w_bpFaced'],
            'l_ace': row['l_ace'],
            'l_df': row['l_df'],
            'l_svpt': row['l_svpt'],
            'l_1stIn': row['l_1stIn'], 
            'l_1stWon': row['l_1stWon'],
            'l_2ndWon': row['l_2ndWon'],
            'l_SvGms': row['l_SvGms'],
            'l_bpSaved': row['l_bpSaved'],
            'l_bpFaced': row['l_bpFaced'],
            'winner_rank': row['winner_rank'], 
            'winner_rank_points': row['winner_rank_points'],
            'loser_rank': row['loser_rank'],
            'loser_rank_points': row['loser_rank_points'] 
        })
        ##============================================================================================##
       ##============================================================================================##
    # close the output file
    output_csv.close()

"""# create tournament csv"""

##================================input variables=============================================##
##============================================================================================##
data_csv_path = './data/tennis.csv'
output_csv_path = './output/tournament.csv'
output_csv_header = ['tourney_id', 'date_id', 'tourney_name', 'surface', 'draw_size',
                      'tourney_level', 'tourney_spectators', 'tourney_revenue']
##============================================================================================##
##============================================================================================##

with open(data_csv_path, 'r', newline='') as file:
    # open tennis file
    data = csv.DictReader(file)
    
    # create a new file for match
    output_csv = open(output_csv_path, 'w')
    
    # creat a writer object so we can write to the file with header we defined earliar
    output_csv_writer = csv.DictWriter(output_csv, fieldnames = output_csv_header)
    
    # write the header to the file
    output_csv_writer.writeheader()
    
    # write data row by row
    for row in data:
       ##=========================change paring according to csv required=============================##
       ##============================================================================================##
        output_csv_writer.writerow({
            'tourney_id': row['tourney_id'], 
            'date_id':row['tourney_date'],
            'tourney_name':row['tourney_name'],
            'surface':row['surface'],
            'draw_size':row['draw_size'],
            'tourney_level':row['tourney_level'],
            'tourney_spectators':row['tourney_spectators'],
            'tourney_revenue':row['tourney_revenue']})
        ##============================================================================================##
       ##============================================================================================##
    # close the output file
    output_csv.close()

"""# creating date table
- date in provided in 'tourney_date' as **20181231**
- we can use it as date_id 
    - we don't want repeate the same date so we can keep track of them in a list
- columns needed in table **[date_id, day, month, year, quarter]**
- we turn the string date into a datatime object with datatime libary then extract the data
"""

from datetime import datetime
import math

def get_date_data(str_date, format_code):

    date_object = datetime.strptime(str_date, format_code)
    out = {
        'date_id': int(str_date), 
        'day': date_object.day, 
        'month': date_object.strftime("%B"), 
        'year': date_object.year, 
        'quarter': math.ceil(date_object.month/3.)
    }
    return out

# Commented out IPython magic to ensure Python compatibility.
# %%time
# get_date_data(str_date = "20181231", format_code = "%Y%m%d")

##================================input variables=============================================##
##============================================================================================##
data_csv_path = './data/tennis.csv'
output_csv_path = './output/date.csv'
output_csv_header = ['date_id', 'day', 'month', 'year', 'quarter']
##============================================================================================##
##============================================================================================##

with open(data_csv_path, 'r', newline='') as file:
    # open tennis file
    data = csv.DictReader(file)
    
    # create a new file for match
    output_csv = open(output_csv_path, 'w')
    
    # creat a writer object so we can write to the file with header we defined earliar
    output_csv_writer = csv.DictWriter(output_csv, fieldnames = output_csv_header)
    
    # write the header to the file
    output_csv_writer.writeheader()
    
    # list to keep track of date already insterted
    unique_date = []
    
    # write data row by row
    for row in data:
        
        date_now = row['tourney_date']
        
        if date_now not in unique_date:
            # add date to list
            unique_date.append(date_now)
            # call function get data out of date
            date_data = get_date_data(str_date = date_now, format_code = "%Y%m%d")
           ##=========================change paring according to csv required=============================##
           ##============================================================================================##
            output_csv_writer.writerow({
                'date_id': date_data['date_id'],
                'day': date_data['day'],
                'month': date_data['month'],
                'year': date_data['year'],
                'quarter': date_data['quarter']
            })
            ##============================================================================================##
           ##============================================================================================##
    # close the output file
    output_csv.close()

"""# creating players table

in case of players table we have most of the data we need in tennis csv 

but we need to derive to information out
- **byear_of_birth** the birth year of player 
- **sex** 

How will we calculate this value
- for birth year we can use year of tournament - age of the player in the tournament
- for sex we have that information in two csv's with player name and there sex as male_players.csv, female_players.csv
"""

# get sex of players
# create complete players list combining both and putting sex values according to sheet names
header = ['name', 'surname', 'sex', 'full_name']
out_file = open('./output/complete_players_sex.csv', 'w')
out_writer = csv.DictWriter(out_file, fieldnames=header)
out_writer.writeheader()
# add male players
with open('./data/male_players.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['full_name'] = '{} {}'.format(row['name'], row['surname']).strip()
        row['sex'] = 'm'
        out_writer.writerow(row)
# add female players
with open('./data/female_players.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['full_name'] = '{} {}'.format(row['name'], row['surname']).strip()
        row['sex'] = 'f'
        out_writer.writerow(row)
out_file.close()

header = ['player_id', 'country_id', 'name', 'sex', 'hand', 'ht', 'byear_of_birth']

def get_age(tourney_date, age):
    
    if len(tourney_date) > 0 and len(age) > 0:
        return int(tourney_date[:4]) - int(float(age))
    
    return ''

get_age(tourney_date = '20181231', age = '25')

# we collected all name in a Dictionary so we can find them easily
data_all = {}
with open('./output/complete_players_sex.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_all[row['full_name']] = row['sex']

def get_sex(data_all, name):
    try:
        sex = data_all[name]
    except:
        sex = ''
    return sex

Commented out IPython magic to ensure Python compatibility.
%%time
get_sex(data_all, name = 'Liena Ammar')

Commented out IPython magic to ensure Python compatibility.
%%time
##================================input variables=============================================##
##============================================================================================##
data_csv_path = './data/tennis.csv'
output_csv_path = './output/player.csv'
output_csv_header = ['player_id', 'country_id', 'name', 'sex', 'hand', 'ht', 'byear_of_birth']
##============================================================================================##
##============================================================================================##

with open(data_csv_path, 'r', newline='') as file:
    # open tennis file
    data = csv.DictReader(file)
    
    # create a new file for match
    output_csv = open(output_csv_path, 'w')
    
    # creat a writer object so we can write to the file with header we defined earliar
    output_csv_writer = csv.DictWriter(output_csv, fieldnames = output_csv_header)
    
    # write the header to the file
    output_csv_writer.writeheader()
    
    # we need to keep track of players so we don't input there data twice
    player_names = []
    
    # write data row by row
    for row in data:
       ##=========================change paring according to csv required=============================##
       ##============================================================================================##
        # check if the player is already in csv
        if row['winner_name'] not in player_names:
            # add player to list
            player_names.append(row['winner_name'])

            # adding winners data to csv
            output_csv_writer.writerow({
                'player_id' : row['winner_id'],
                'country_id' : row['winner_ioc'],
                'name' : row['winner_name'],
                'sex': get_sex(data_all, name = row['winner_name']),
                'hand': row['winner_hand'],
                'ht': row['winner_ht'],
                'byear_of_birth': get_age(tourney_date = row['tourney_date'], age = row['winner_age']) 
            })
            
        # check if the player is already in csv
        if row['loser_name'] not in player_names:
            # add player to list
            player_names.append(row['loser_name'])

            # adding losers data to csv
            output_csv_writer.writerow({
                'player_id' : row['loser_id'],
                'country_id' : row['loser_ioc'],
                'name' : row['loser_name'],
                'sex': get_sex(data_all, name = row['loser_name']),
                'hand': row['loser_hand'],
                'ht': row['loser_ht'],
                'byear_of_birth': get_age(tourney_date = row['tourney_date'], age = row['loser_age']) 
            })
        ##============================================================================================##
       ##============================================================================================##
    # close the output file
    output_csv.close()

"""# create geography csv
- in this case most of information was in the countries csv
- but we need to get language data from another csv **countries_languages**
"""

# create a  Dictionary for all the countries and languages using country language CSV
language = {}

with open('./data/countries_languages.csv', 'r') as file:
    data = csv.DictReader(file)
    for row in data:
        language[row['country_name']] = row['language']

##================================input variables=============================================##
##============================================================================================##
data_csv_path = './data/countries.csv'
output_csv_path = './output/geography.csv'
output_csv_header = ['country_ioc', 'continent', 'language']
##============================================================================================##
##============================================================================================##

with open(data_csv_path, 'r', newline='') as file:
    # open tennis file
    data = csv.DictReader(file)
    
    # create a new file for match
    output_csv = open(output_csv_path, 'w')
    
    # creat a writer object so we can write to the file with header we defined earliar
    output_csv_writer = csv.DictWriter(output_csv, fieldnames = output_csv_header)
    
    # write the header to the file
    output_csv_writer.writeheader()
    
    # write data row by row
    for row in data:
       ##=========================change paring according to csv required=============================##
       ##============================================================================================##
        output_csv_writer.writerow({
            'country_ioc' : row['country_code'],
            'continent' : row['continent'],
            'language' : language[row['country_name']]
        })
        ##============================================================================================##
       ##============================================================================================##
    # close the output file
    output_csv.close()



