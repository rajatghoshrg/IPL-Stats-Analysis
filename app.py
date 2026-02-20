#  IPL Data Analysis :
# Top run scorer 
# Most wickets 
# Team win count 
# Venue performance analysis 
# Player consistensy analysis

import pandas as pd
df = pd.read_csv('IPL_2025_Synthetic_Dataset.csv')
print(df)

# Top run scorer 
top_run = df.groupby('Player')['Runs'].sum().sort_values(ascending=False).head(1)
print(top_run)

# Most wickets 
top_wicket = df.groupby('Player')['Wickets'].sum().sort_values(ascending=False).head(1)
print(top_wicket)

# Team win count 
team_win_count = df['Match_Winner'].value_counts()
print(team_win_count)

# Venue performance analysis
venue_performance = df.groupby('Venue')['Match_Winner'].value_counts()
print(venue_performance)

# Player consistency analysis
player_consistency = df.groupby('Player')['Runs'].std().sort_values(ascending=False)
print(player_consistency)
