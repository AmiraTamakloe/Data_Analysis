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
    # https://stackoverflow.com/questions/39922986/how-do-i-pandas-group-by-to-get-sum

    my_df['PlayerLine'] = my_df.groupby(['Player', 'Act'])['Line'].transform('sum')
    total_line_per_act = my_df.groupby('Act')['Line'].transform('sum')
    my_df['PlayerPercent'] = (my_df['PlayerLine'] / total_line_per_act) * 100
    return my_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
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
    # TODO : Replace players in each act not in the top 5 by a 
    top_5_players_per_act = my_df.sort_values(by='PlayerLine', ascending=False).groupby('Act').head(5)
    other_players = my_df[~my_df.index.isin(top_5_players_per_act.index)]
    return my_df
    


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # DONE : Clean the player names 
    # https://www.w3resource.com/pandas/series/series-str-capitalize.php#:~:text=The%20str.,capitalize().
    my_df['Player'] = my_df['Player'].str.capitalize()
    return my_df
