'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip

    template=(
        "<b>Country</b>: %{hovertext}<br>"
        "<b>Population</b>: <span style='font-weight:normal'>%{marker.size:,}</span><br>"
        "<b>GDP</b>: <span style='font-weight:normal'>%{x:.2f} $ (USD)</span><br>"
        "<b>CO2 emissions</b>: <span style='font-weight:normal'>%{y:.1f} metric tonnes</span>"
        "<extra></extra>"
    )
    return template
