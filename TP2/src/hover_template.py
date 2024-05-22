'''
    Provides the template for the hover tooltips.
'''
from modes import MODES


def get_hover_template(name, mode):
    '''
        Sets the template for the hover tooltips.

        The template contains:
            * A title stating player name with:
                - Font family: Grenze Gotish
                - Font size: 24px
                - Font color: Black
            * The number of lines spoken by the player, formatted as:
                - The number of lines if the mode is 'Count ("X lines").
                - The percent of lines fomatted with two
                    decimal points followed by a '%' symbol
                    if the mode is 'Percent' ("Y% of lines").

        Args:
            name: The hovered element's player's name
            mode: The current display mode
        Returns:
            The hover template with the elements described above
    '''
    if mode == 'Count':
        line_value = f'%{{customdata}} lines'
    elif mode == 'Percent':
        line_value = f'%{{customdata:.2f}}% of lines'

    hover_template = (
        f'<span style="font-family: Grenze Gotisch, serif; font-size: 24px; color: black;"><b>{name}</b></span><br>'
        f'<br>'
        f'{line_value}<extra></extra>'
    )
    return hover_template
