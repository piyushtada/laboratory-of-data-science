import pyodbc
import pandas

# Define the Insert Query.
match_sql_insert = """
INSERT INTO [Group_24_DB].[dbo].[match]
 (
    [tourney_id],
    [match_id],
    [winner_id],
    [loser_id],
    [score],
    [best_of],
    [round],
    [minutes],  
    [w_ace],
    [w_df],
    [w_svpt],
    [w_1stWon],
    [w_SvGms],
    [w_bpSaved],
    [w_bpFaced],
    [l_ace],
    [l_df],
    [l_svpt],
    [l_1stIn],
    [l_1stWon],
    [l_2ndWon],
    [l_SvGms],
    [l_bpSaved],
    [l_bpFaced],
    [winner_rank],
    [winner_rank_points],
    [loser_rank],
    [loser_rank_points]
)
VALUES
(
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
)
"""

# Define the Insert Query for geography
geography_sql_insert = """
INSERT INTO [Group_24_DB].[dbo].[geography]
 (
    [country_ioc],
    [continent], 
    [language]
 )
 VALUES
 (
    ?, ?, ?
 )
 """

# define insert query for player
player_sql_insert = """
INSERT INTO [Group_24_DB].[dbo].[player]
 (
    [player_id],
    [country_id],
    [name],
    [sex],
    [hand],
    [ht],
    [byear_of_birth]   
 )
 VALUES
 (
    ?, ?, ?, ?, ?, ?, ?
 )
 """

# define insert query for tournament
tournament_sql_insert = """
INSERT INTO [Group_24_DB].[dbo].[tournament]
 (
	[tourney_id],
	[date_id],
	[tourney_name],
	[surface],
	[draw_size],
	[tourney_level],
	[tourney_spectators],
	[tourney_revenue]
 )
 VALUES
 (
	?, ?, ?, ?, ?, ?, ?, ?
)
"""
# define insert query for date
date_sql_insert = """
INSERT INTO [Group_24_DB].[dbo].[date]
 (
	[date_id],
	[day],
	[month],
	[year],
	[quarter]
 ) 
 VALUES
 (
	?, ?, ?, ?, ?
)
"""

# Define the Components of the Connection String.
server = 'tcp:lds.di.unipi.it' 
database = 'Group_24_DB' 
username = 'Group_24' 
password = '0921WT0I' 
CONNECTION_STRING = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password


# Create a connection object.
connection_object: pyodbc.Connection = pyodbc.connect(CONNECTION_STRING)

# Create a Cursor Object, using the connection.
cursor_object: pyodbc.Cursor = connection_object.cursor()

# Define the File Path.
data_file = "C:\Codes\project\match.csv"


def prepare_data(file_path):
    
    # Load the Data.
    match_df: pandas.DataFrame = pandas.read_csv(
        file_path, keep_default_na=False
    )

    # Convert the DataFrame to a RecordSet.
    df_records = match_df.values.tolist()

    return df_records

# to make query run faster
#cursor_object.fast_executemany = True

# Execute it.
#cursor_object.executemany(date_sql_insert, prepare_data("C:\Codes\project\\date.csv"))
#print("date data inserted\n")
#cursor_object.executemany(geography_sql_insert, prepare_data('C:\Codes\project\geography.csv'))
#print("geography data inserted\n")
#cursor_object.executemany(player_sql_insert, prepare_data('C:\Codes\project\player.csv'))
#print("player data inserted\n")
#cursor_object.executemany(tournament_sql_insert, prepare_data("C:\Codes\project\\tournament.csv"))
#print("tournament data inserted\n")
cursor_object.executemany(match_sql_insert, prepare_data("C:\Codes\project\match.csv"))
print("match data inserted\n")
print("all the data inserted\n")

# Commit the Transactions.
cursor_object.commit()