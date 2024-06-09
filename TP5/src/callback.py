'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
import dash_html_components as html
import json

with open('./assets/data/projetpietonnisation2017.geojson',
    encoding='utf-8') as data_file:
    street_data = json.load(data_file)


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle no clicks on the map



    return None, None, None, None


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the map base

    return None, None, None, None


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the markers

    latitude = figure['data'][curve]['lat'][point]
    longitude = figure['data'][curve]['lon'][point]

    for feature in street_data['features']:
            if (feature['properties']['LATITUDE'] == latitude and 
                feature['properties']['LONGITUDE'] == longitude):
                project_name = feature['properties']['NOM_PROJET']
                updated_title = f"{project_name}"
                mode_name = feature['properties']['MODE_IMPLANTATION']
                updated_mode = f"{mode_name}"

                thematic_objectives = feature['properties']['OBJECTIF_THEMATIQUE']
                if thematic_objectives is None:
                    formatted_themes = theme
                else:
                    items = thematic_objectives.split('\n')

                    formatted_themes = f""
                    formatted_themes += f"Thématique :\n"
                    for item in items:
                        formatted_themes += f"   • {item} \n"

                if style is None:
                    style = {
                        'backgroundColor': '#FFF',
                        'color': '#000',
                        'border': '1px solid #CCC',
                        'padding': '10px',
                        'fontFamily': 'Arial, sans-serif',
                    }
                for trace in figure['data']:
                    if trace['type'] == 'scattermapbox':
                        if (latitude in trace['lat'] and
                            longitude in trace['lon']):

                            marker_color = trace['marker']['color']
                            updated_title = html.Span(updated_title, style={'color': marker_color})

                return updated_title, updated_mode, formatted_themes, style

