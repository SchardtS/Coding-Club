import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('2023_12_04_DataImprovisation/Simon/countries_with_iso3.csv')

# Create a choropleth trace
fig = go.Figure()

# Add a choropleth trace with color for the specified countries
fig.add_trace(go.Choropleth(
    locations = df['ISO-3'],  # Specify the countries you want to color differently
    locationmode = "ISO-3", # Set plot to plot countries according to their ISO-3 code
    z = df['Color_value'],  # Set a value for the specified countries
    colorscale = ["green", "orange", "red"],  # Set a discrete color scale
    colorbar_tickvals = [0.15, 0.5, .85],  # Set the tick positions for the colorbar
    colorbar_ticktext = ["Good", "Intermediate", "Bad"],  # Set the text labels for the colorbar ticks
    colorbar_title = '<b>Degree of fucked upness</b>', # Set the colorbar title
    hovertemplate = '<b>' + df['Name'] + '</b><br>' + df['Text'] + '<extra>' + df['ISO-3'] + '</extra>'
))

# Update some plotting parameters
fig.update_geos(
    #projection_type="orthographic",
    #projection_type="natural earth",
    projection_type="azimuthal equidistant",
    showcountries=True, countrycolor="Black",
    showocean=True, oceancolor="LightBlue",
    showlakes=True, lakecolor="Blue",
    showcoastlines=True, coastlinecolor="Black",
    lataxis_showgrid=True, lonaxis_showgrid=True,
)

fig.write_html('colored_world_map_3.html')