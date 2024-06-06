'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover

def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        The opacity of the map background color should be 0.2.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace
    '''

    # choro_trace = go.Choropleth(
    #     geojson=montreal_data,
    #     locations=locations,
    #     z=z_vals,
    #     colorscale=colorscale,
    #     marker_line_color='white', 
    #     marker_line_width=0.5, 
    #     showscale=False,  
    #     hoverinfo='location+z',  
    # )

    # fig.add_trace(choro_trace)

    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        The marker size should be 20.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    # TODO : Add the scatter markers to the map base
    
    x_values = street_df['X'].tolist()
    y_values = street_df['Y'].tolist()

    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x_values,
            y=y_values,  
            marker=dict(
                color='LightSkyBlue',
                size=20,
                line=dict(
                    color='MediumPurple',
                    width=2
                )
            ),
            showlegend=False
        )
    )

    return fig
