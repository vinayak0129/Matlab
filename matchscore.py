import pandas as pd
# Create dataframe For Match Data
data = {
        'Player': ['Rohit Sharma','Shubhman Gill','Virat Kohli','Suryakumar Yadav','KL Rahul','Hardik Pandya','Axar Patel','Ravindra Jadeja','Jasprit Bumrah','Mohammad Shami','Kuldip Yadav'],
        'Runs': [226,10,58,10,38,28,2,0,6,0,0],
        'Wickets': [0,0,0,0,0,1,0,0,5,2,1],
        'Balls Faced': [120,5,78,23,25,20,18,8,15,2,3],
        'Balls Bowled': [0,0,0,0,0,4,8,10,10,10,8],
        'Runs Conceded' : [0,0,0,0,0,20,56,80,28,85,60]
}
match_data = pd.DataFrame(data)
print("Dataframe Created")

# Calculate Team Total Runs
total_runs = match_data['Runs'].sum()
print("\nTeam Total Runs: ", total_runs)

# Calculate Batting Average Runs For Each Player
match_data['Batting Average'] = match_data['Runs'] / (match_data['Balls Faced'] - match_data['Runs'])
print("\nBatting Averages:\n", match_data[['Player','Batting Average']])

# Calculate Points For Each Player (1 point for 1 Run & 10 Points For 1 Wicket )
match_data['Points'] = match_data['Runs'] * 1 + (match_data['Wickets'] * 10)
print("\nPlayer Points:\n", match_data[['Player','Points']])

# Higest Run-Scorer
top_scorer = match_data.loc[match_data['Runs'].idxmax(),'Player']
print("\nTop Run-Scorer:", top_scorer)

# Lowest Run-Scorer
low_scorer = match_data.loc[match_data['Runs'].idxmin(),'Player']
print("\nLowest Run-Scorer:", low_scorer)

# Top Wicket-Taker
top_wicket_taker = match_data.loc[match_data['Wickets'].idxmax(),'Player']
print("\nTop Wicket-taker:", top_wicket_taker)

# Bowling Strike Rate for Each Bowler
bowlers = match_data[match_data['Balls Bowled'] > 0 ]
bowlers['Bowling Strike Rate'] = bowlers['Balls Bowled'] / bowlers['Wickets']
print("\nBowling Strike Rates:\n", bowlers[['Player','Bowling Strike Rate']])