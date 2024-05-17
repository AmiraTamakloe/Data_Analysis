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
    base_template = (
        f"<span style='font-family: \"Grenze Gotisch\"; font-size: 24px; color: black;'>"
        f"{name}</span><br>"
    )

    if mode == MODES['count']:
        line_info_template = "<span>%{customdata[0]} lines</span>"
    elif mode == MODES['percent']:
        line_info_template = "<span>%{customdata[1]:.2f}% of lines</span>"
    else:
        raise ValueError("Invalid mode specified")

    full_template = base_template + line_info_template

    return full_template
