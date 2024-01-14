"""
Tanner Huck, Nathan Dennis, and Andy Wen
SOC 225 Project
"""

# Import necessary packages/functions/classes:
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio


def interactive_map_deaths(data: pd.DataFrame) -> None:
    """
    Takes in the vaxine data set.
    Creates an interactive cloropleth map that shows each country
    on a map colored by differrent variables. Interaction
    allows user to hover over each country and see what value the
    variable takes.
    Saves the graph to a file named world_map.html.
    First graph examines total_deaths
    """
    # Create and  interactive choropleth map of the world:
    fig = px.choropleth(
        data,
        # Graphing each country:
        locations='location',
        locationmode='country names',

        # Color each country on a blue color scale according to total_deaths
        color='total_deaths_per_million',
        color_continuous_scale='YlGnBu',

        # Use natural earth map style:
        projection='natural earth',

        # Details that what will be shown through interaction:
        labels={'total_deaths_per_million': 'Total Deaths Per Million',
                'location': 'Country'}
    )

    # Adding labels, title, and a legend to the graph:
    fig.update_layout(
        title=dict(
            text='Total Deaths by Country Per Million',
            font=dict(size=28)
        ),
        coloraxis_colorbar=dict(
            len=0.5,
            yanchor='middle',
            y=0.5
        )
    )

    # Save to an html file:
    pio.write_html(fig, file='world_map_total_deaths.html')


def interactive_map_cases(data: pd.DataFrame) -> None:
    """
    Examines total_cases
    """
    fig = px.choropleth(
        data,
        locations='location',
        locationmode='country names',
        color='total_cases_per_million',
        color_continuous_scale='YlGnBu',
        projection='natural earth',
        labels={'total_cases_per_million': 'Total Cases Per Million',
                'location': 'Country'}
    )
    fig.update_layout(
        title=dict(
            text='Total Cases by Country Per Million',
            font=dict(size=28)
        ),
        coloraxis_colorbar=dict(
            len=0.5,
            yanchor='middle',
            y=0.5
        )
    )
    pio.write_html(fig, file='world_map_total_cases.html')

def interactive_map_vax(data: pd.DataFrame) -> None:
    """
    Examines total_cases
    """
    fig = px.choropleth(
        data,
        locations='location',
        locationmode='country names',
        color='people_fully_vaccinated_per_hundred',
        color_continuous_scale='YlGnBu',
        projection='natural earth',
        labels={'people_fully_vaccinated_per_hundred':'Total Fully Vaxinated Per Hundred',
                'location': 'Country'}
    )
    fig.update_layout(
        title=dict(
            text='Number of Fully Vaccinated People by Country Per Hundred',
            font=dict(size=28)
        ),
        coloraxis_colorbar=dict(
            len=0.5,
            yanchor='middle',
            y=0.5
        )
    )
    pio.write_html(fig, file='world_map_people_vaccinated.html')

def main():
    # Data
    vaxData = pd.read_csv("SOCDatacsv.csv")
    # Interacitve graphs
    interactive_map_deaths(vaxData)
    interactive_map_cases(vaxData)
    interactive_map_vax(vaxData)
    plt.show()


if __name__ == '__main__':
    main()