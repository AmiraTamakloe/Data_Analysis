'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # DONE : Modify the dataframe, removing the line content and replacing
    my_df = my_df.groupby(['Player', 'Act'])['Line'].count().reset_index()
    total_lines_per_act = my_df.groupby('Act')['Line'].sum().reset_index()
    my_df.rename(columns={'Line': 'PlayerLine'}, inplace=True)
    total_lines_per_act.rename(columns={'Line': 'LineSum'}, inplace=True)
    merged_df = pd.merge(my_df, total_lines_per_act, on='Act')
    merged_df['PlayerPercent'] = (merged_df['PlayerLine'] / merged_df['LineSum']) * 100
    return merged_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other players
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # DONE : Replace the other players with 'OTHER'
    my_df.rename(columns={'PlayerLine': 'LineCount','PlayerPercent': 'LinePercent' }, inplace=True)
    top_5_players_total = my_df.groupby('Player').sum().nlargest(5, 'LineCount').reset_index()
    top_5_players_per_act = pd.merge(my_df, top_5_players_total['Player'], on='Player', how='inner') 
    other_players_per_act = my_df.groupby(['Act', 'Player']).sum().reset_index()
    other_players_per_act = other_players_per_act[~other_players_per_act['Player'].isin(top_5_players_total['Player'])]
    other_players_grouped = other_players_per_act.groupby('Act').agg({
        'LineCount': 'sum',
        'LinePercent': 'sum'
    }).reset_index()
    other_players_grouped['Player'] = 'OTHER'
    result_df = pd.concat([top_5_players_per_act, other_players_grouped], ignore_index=True)
    result_df.sort_values(by=['Act'], ascending=[True], inplace=True)
    return result_df
    


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # DONE : Clean the player names 
    my_df['Player'] = my_df['Player'].str.title()
    return my_df
