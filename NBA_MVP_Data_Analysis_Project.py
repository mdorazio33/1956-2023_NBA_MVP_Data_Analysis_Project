#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ### The Dataset I will use for this project consists of NBA MVPs and the teams they played for from 1956 to 2023.

# I decided to use this dataset as I am a big NBA fan, and wanted to create some interesting plots regarding the relation of MVP wins to NBA teams, player positions, individual players, and PPG stats. The dataset I am using is titled "1956-2023_NBA_MVPs.csv".

# In[3]:


# loading the "1956-2023_NBA_MVPs.csv" dataset
df = pd.read_csv("C:/projects/1956-2023_NBA_MVPs_dataset.csv") # Change path to reflect the CSV file location on your computer - Michael
df


# ### For the first three plots, I will be examine the qualitative relationships between MVP wins by team, MVP wins by player position, and MVP wins by individual player between 1956 to 2023.

# In order to do this, I will first create a new dataframe ignoring the FG% (field goal percentage), PPG (points per game), RPG (rebounds per game), APG (assists per game), and BLKPG (blocks per game) statistics since there is no numerical data available for these columns between the years of 1956 to 1986 and I want to analyze the entire dataset for the first three plots.

# In[4]:


limited_df = df.drop(["FG%", "PPG", "RPG", "APG", "BLKPG"], axis=1).copy()
limited_df


# In order to determine MVP wins by team, one must figure out the amount of times the team appears in MVP wins dataset. This can be done by applying the value_counts( ) command to a limited dataframe for the 'TEAM' variable.

# ## Creating Plot #1: Number of MVP Wins by NBA Team (1956-2023)

# In[5]:


wincount = limited_df['TEAM'].value_counts()
wincount


# Next, a pandas dataframe can be created using this information.

# In[6]:


wincount_df = pd.DataFrame({'TEAM': wincount.index, 'MVP WINS': wincount.values})
wincount_df


# From there, we can create our first plot.

# ## Plot #1: Number of MVP Wins by NBA Team (1956-2023)

# In[7]:


wincount_df.set_index('TEAM', inplace=True)


# In[8]:


wincount_df = wincount_df.sort_values(by='MVP WINS', ascending=True)

(wincount_df['MVP WINS']
 .plot(kind='barh', x='MVP WINS', y='TEAM', xlabel='Number of MVP Wins', ylabel='NBA Team', color = 'royalblue', width=0.8, figsize=(6, 9))
)
plt.title('Number of MVP Wins by NBA Team (1956-2023)')


# ### What I learned from Plot #1:

# From Plot #1, I was hoping to find which NBA team/franchise historically has the most amount of MVP wins between 1956 and 2023. The graph shows that the top five teams with the most MVP wins during that time were the Boston Celtics, the Los Angeles Lakers, the Philadelphia 76ers, the Chicago Bulls, and the Milwaukee Bucks.
# 
# The plot showed what I had originally expected in that teams like the Boston Celtics and Los Angeles Lakers were among the NBA franchises with the most MVP wins throughout the examined timeframe. What surprised me, however, was learning that the Philadelphia 76ers are not very far behing the Los Angeles Lakers with respect to MVP wins. This is surprising to me because in my own lifetime, I have only ever witnessed two MVP winners come from Philadelphia, with those being Allen Iverson, and most recently, Joel Embiid. Further examination of the dataset shows that in previous decades, MVP winners from Philadelphia consisted of NBA greats such as Wilt Chamberlain, Julius Erving, and Moses Malone. All players whose accomplishments serve to contribute to the total number of MVP wins that Philadelphia holds as a team.

# ## Creating Plot #2: Number of NBA Wins by Player Position (1956-2023)

# Like before, I will start with creating a limited dataframe. This time, howevever, it will consist of value counts for player position for the 'POS' variable rather than the 'TEAM' variable.

# In[9]:


poscount = limited_df['POS'].value_counts()
poscount


# In[10]:


poscount_df = pd.DataFrame({'POS': poscount.index, 'MVP WINS': poscount.values})
poscount_df


# ## Plot #2: Number of NBA Wins by Player Position (1956-2023)

# In[11]:


poscount_df.set_index('POS', inplace=True)


# In[12]:


poscount_df = poscount_df.sort_values(by='MVP WINS', ascending=True)
ax=poscount_df['MVP WINS'].plot(kind='barh', x='MVP WINS', y='Player Position', xlabel='Number of MVP Wins', ylabel='Player Position', color = 'royalblue', width=0.8, figsize=(6, 9))
plt.title('Number of MVP Wins by Player Position (1956-2023)')
ax.set_xlim(0,30)


# ### What I learned from Plot #2:

# From Plot #2, I was hoping to find which out player position throughout history held the most number of MVP wins. I was surprised to see that Centers (C), held the most amount of wins by a huge margin (28 total wins). This is followed by a tie between Forwards (F) and combo guards (G) who each have a combined total of 9 MVP wins throughout the 1956-2023 timeframe. And while I knew that there were many great NBA centers throughout history, I had no idea that the total amount of MVP wins earned by players in this position held the lead when compared to other positions by such an overwhelming degree.
# 
# As a result, the plot did not show what I had originally expected. At first, I assumed the highest total MVP wins by an NBA position would belong to either a combo guard, forward, or even someone playing the small forward position (SF). I was under this impression as I had gone a majority of my life watching players succeed in a league where aside from the past few years thanks to Joel Embiid and Nikola Jokic, had been dominated by guard play. From this analysis, however, we can see that Centers have historically won the most amount of MVPs when compared to other positions and can also infer that Centers between 1956 and 2023 have been the most popular players among MVP voters.

# ## Creating Plot #3: Number of MVP Wins by NBA Player (1956-2023)

# In[13]:


playercount = limited_df['PLAYER'].value_counts()
playercount


# In[14]:


playercount_df = pd.DataFrame({'PLAYER': playercount.index, 'MVP WINS': playercount.values})
playercount_df


# ## Plot #3: Number of MVP Wins by NBA Player (1956-2023)

# In[15]:


playercount_df.set_index('PLAYER', inplace=True)


# In[16]:


playercount_df = playercount_df.sort_values(by='MVP WINS', ascending=True)
ax=playercount_df['MVP WINS'].plot(kind='barh',
                                   x='MVP WINS',
                                   y='Player',
                                   xlabel='Number of MVP Wins',
                                   ylabel='NBA Player',
                                   color = 'darkred',
                                   width=0.8,
                                   figsize=(6, 9))
plt.title('Number of MVP Wins by NBA Player (1956-2023)')
ax.set_xlim(0,7)


# ### What I learned from Plot #3:

# From Plot #3, I was hoping to find out which NBA players held the amount of MVP wins. From this plot, I managed to determine that the top 5 NBA players with the most MVP wins are Kareem Abdul-Jabbar, Michael Jordan, Bill Russell, LeBron James, and Wilt Chamberlain. Though among the top 5, Michael Jordan and Bill Russell are tied with one another as are LeBron James and Wilt Chamberlain.
# 
# This plot actually did show what I had originally expected. I was aware that Kareem Abdul-Jabbar, Bill Russell, and Michael Jordan are often considered some of the most prolific players of their eras, so seeing them so high on the leaderboard did not come as a tremendous surprise. However, I wasn't aware that LeBron James and Wilt Chamberlain had the same number of MVP wins as one another.

# ## Creating Plot #4: PPG Averages for Players with Multiple MVP Wins (1987-2023)

# Plot #4 is a little different from the previous three. It consists of data from 1987 to 2023 as those are the only years that information for FG%, PPG, RPG, APG, and BLKPG statistics are available, as the years of 1956 through 1986 do not contain data for these fields.
# 
# Therefore, the plot I made for this information reflects the PPG (points per game) averages for players who between 1987 and 2023 had won multiple NBA MVPs. I could have done all MVP winners during this time period for this Plot #4, but decided that it may not have been fair to put players who may have only had one MVP win in with those who had many. My reasoning for this is because some players who earned one MVP win had an exceptional year, whereas those who had multiple had more consistent stats. Because of that, I wanted to stick with players who had more than one MVP win for this analysis.

# The first step in this was to create a new dataframe consisting of the years between 1987 and 2023 using the .loc[ ] function.

# In[17]:


df_87_23 = df.loc[0:36]
df_87_23


# Next, I wanted to check the value_counts for MVP winners within this time period.

# In[18]:


playercount2 = df_87_23['PLAYER'].value_counts()
playercount2


# Following this, I identified players who achieved a number of MVP wins that was greater than or equal to 2.

# In[19]:


mw = df_87_23['PLAYER'].value_counts() >= 2
mw


# And finally, I isolated those players on their own along with their average PPG across all of their appearances.

# In[20]:


ppg_player = df_87_23.groupby('PLAYER')['PPG'].mean()
mw2 = ppg_player[df_87_23['PLAYER'].value_counts() >= 2]
mw2


# After that, I created a pandas dataframe to present these values.

# In[21]:


mw2_df = pd.DataFrame({'PLAYER': mw2.index, 'PPG': mw2.values})
mw2_df


# ## Plot #4: PPG Averages for Players with Multiple MVP Wins (1987-2023)

# In[22]:


mw2_df.set_index('PLAYER', inplace=True)


# In[23]:


mw2_df = mw2_df.sort_values(by='PPG', ascending=True)

(mw2_df['PPG']
 .plot(kind='barh',
       x='PPG',
       y='PLAYER',
       xlabel='Average Points Per Game',
       ylabel='NBA Player',
       color = 'royalblue',
       width=0.8, figsize=(6, 9))
)
plt.title('PPG Averages for Players with Multiple MVP Wins (1987-2023)')


# ### What I learned from Plot #4:

# From Plot #4, I was hoping to find out which NBA player scored the highest average points per game across their MVP winning seasons. From Plot #4, we can see that Michael Jordan is the player who had the greatest average points per game across his MVP winning seasons, with an average PPG of roughly 31.14 points per game. This is an especially impressive statistic considering that Jordan won a total of 5 MVPs in his career and managed to achieve the highest average from the players shown in the bar chart, indicating that he was a consistently high-scorer throughout all of his MVP winning seasons.
# 
# The plot showed what I had expected, though it did show an interesting takeaway. I wasn't aware that Jordan was the only player with multiple MVP wins who managed to achieve a compiled average PPG of over 30 points per game across all of his MVP-winning seasons. Though not shown on Plot #4 due to them having only one MVP win each, players like Joel Embiid and Allen Iverson managed to have MVP-winning seasons averaging over 30 points per game as well. However, by leaving those players out and only including individuals with multiple wins, I believe that this chart helps to illustrate just how impressive of a feat that Jordan's compiled scoring average was throughout his MVP-winning seasons. As he had a total of 5 MVP wins, with all but one season displaying an average PPG above the 30 points per game threshold.
