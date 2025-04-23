# Full Python Script for Visualizations and Dashboard with Validated Path

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Base path for datasets
base_path = r"H:\Toni_Kroos_Analysis\Raw_Data\Statistics"

# Load datasets
major_achievements = pd.read_excel(f"{base_path}\\Career_Overview.xlsx", sheet_name="Major Achievements")
individual_awards = pd.read_excel(f"{base_path}\\Career_Overview.xlsx", sheet_name="Individual Awards")
career_milestones = pd.read_excel(f"{base_path}\\Career_Overview.xlsx", sheet_name="Career Milestones")
career_stats = pd.read_excel(f"{base_path}\\career_stats.xlsx", sheet_name="Sheet1")
club_overview = pd.read_excel(f"{base_path}\\Club_Statistics.xlsx", sheet_name="Career Overview")
champions_league_performance = pd.read_excel(f"{base_path}\\Club_Statistics.xlsx", sheet_name="Champions League Performance")
germany_national_team = pd.read_excel(f"{base_path}\\International_Statistics.xlsx", sheet_name="Germany National Team")
major_tournament_performance = pd.read_excel(f"{base_path}\\International_Statistics.xlsx", sheet_name=" Major Tournament Performance")
passing_statistics = pd.read_excel(f"{base_path}\\Performance_Metrics.xlsx", sheet_name="Passing Statistics (Per 90 Minu")
defensive_metrics = pd.read_excel(f"{base_path}\\Performance_Metrics.xlsx", sheet_name="Defensive and Possession Metric")
matches_data = pd.read_csv(f"{base_path}\\toni_kroos_538_matches.csv")

# Dash app initialization
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Toni Kroos Career Dashboard", className="text-center text-primary mb-4"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='data-selector',
                options=[
                    {'label': 'Major Achievements', 'value': 'Major Achievements'},
                    {'label': 'Individual Awards', 'value': 'Individual Awards'},
                    {'label': 'Career Milestones', 'value': 'Career Milestones'},
                    {'label': 'Career Stats', 'value': 'Career Stats'},
                    {'label': 'Club Overview', 'value': 'Club Overview'},
                    {'label': 'Champions League Performance', 'value': 'Champions League Performance'},
                    {'label': 'Germany National Team', 'value': 'Germany National Team'},
                    {'label': 'Major Tournament Performance', 'value': 'Major Tournament Performance'},
                    {'label': 'Passing Statistics', 'value': 'Passing Statistics'},
                    {'label': 'Defensive Metrics', 'value': 'Defensive Metrics'},
                    {'label': 'Matches Data', 'value': 'Matches Data'}
                ],
                placeholder="Select Dataset to Visualize",
                className="mb-4"
            ),
            dcc.Graph(id='data-visualization')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='data-table', className="mt-4"), width=12)
    ])
])

# Callbacks for interactivity
@app.callback(
    [Output('data-visualization', 'figure'), Output('data-table', 'children')],
    [Input('data-selector', 'value')]
)
def update_visualization(selected_data):
    if not selected_data:
        return px.scatter(), None
    
    dataset = {
        "Major Achievements": major_achievements,
        "Individual Awards": individual_awards,
        "Career Milestones": career_milestones,
        "Career Stats": career_stats,
        "Club Overview": club_overview,
        "Champions League Performance": champions_league_performance,
        "Germany National Team": germany_national_team,
        "Major Tournament Performance": major_tournament_performance,
        "Passing Statistics": passing_statistics,
        "Defensive Metrics": defensive_metrics,
        "Matches Data": matches_data
    }[selected_data]

    # Generate a default visualization (bar plot of first two columns)
    fig = px.bar(dataset, x=dataset.columns[0], y=dataset.columns[1], title=f"{selected_data} Overview")

    # Generate a table
    table = dbc.Table.from_dataframe(dataset.head(), striped=True, bordered=True, hover=True)

    return fig, table


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
