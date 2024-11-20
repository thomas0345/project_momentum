# Load Packages
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
# Parameters
max_lookback = 24 # Needs to align with the max_lookback set in momentum_notebook.ipynb
initial_nav = 100
### Load Return Date of strategies
# Set relative folder path for processed data
folder_path_data = './data/processed/'
df_strategy_returns_by_lookback = pd.read_csv(folder_path_data + 'df_strategy_returns_by_lookback.csv')
df_strategy_returns_by_lookback_wTC = pd.read_csv(folder_path_data + 'df_strategy_returns_by_lookback_wTC.csv')
# Set datetime index
df_strategy_returns_by_lookback['Date'] = pd.to_datetime(df_strategy_returns_by_lookback['Date'])
df_strategy_returns_by_lookback_wTC['Date'] = pd.to_datetime(df_strategy_returns_by_lookback_wTC['Date'])
df_strategy_returns_by_lookback.set_index('Date', inplace=True)
df_strategy_returns_by_lookback_wTC.set_index('Date', inplace=True)
df_strategy_returns_by_lookback.index = df_strategy_returns_by_lookback.index.date # only keep date and drop time
df_strategy_returns_by_lookback_wTC.index = df_strategy_returns_by_lookback_wTC.index.date # only keep date and drop time

# Rename Cols 
df_strategy_returns_by_lookback.columns = [f"strat_{col}" for col in df_strategy_returns_by_lookback.columns]
df_strategy_returns_by_lookback_wTC.columns = [f"strat_wTC_{col}" for col in df_strategy_returns_by_lookback_wTC.columns]

# Align Start date of all Strategies by cutting out max window size -1 
df_strategy_returns_by_lookback = df_strategy_returns_by_lookback[max_lookback-1:]
df_strategy_returns_by_lookback.iloc[0] = 0
df_strategy_returns_by_lookback_wTC = df_strategy_returns_by_lookback_wTC[max_lookback-1:]
df_strategy_returns_by_lookback_wTC.iloc[0] = 0

# Join together both dfs
# Perform the join operation
df_returns = df_strategy_returns_by_lookback.join(
    df_strategy_returns_by_lookback_wTC, 
    how='outer')  # 'outer' to include all cols from both DataFrames

# Calculate Nav
df_nav = (1 + df_returns).cumprod() * initial_nav

#### Create Interactive Plot with Dash and Plotly ####

# Initialize Dash app
app = Dash(__name__)

# Prepare the data
lookbacks = range(1, 25)
strategies_with_tc = [f"strat_wTC_{i}" for i in lookbacks]
strategies_without_tc = [f"strat_{i}" for i in lookbacks]

# Define the layout
app.layout = html.Div([
    html.H1("Interactive NAV Visualization", style={'text-align': 'center'}),
    
    # Dropdown for best/worst strategies
    html.Label("Choose Strategy Ranking:"),
    dcc.Dropdown(
        id='ranking-dropdown',
        options=[
            {'label': 'Best Strategies', 'value': 'best'},
            {'label': 'Worst Strategies', 'value': 'worst'}
        ],
        value='best',
        clearable=False
    ),

    # Slider for the number of strategies
    html.Label("Number of Strategies to Display:"),
    dcc.Slider(
        id='num-strategies-slider',
        min=1,
        max=24,
        step=1,
        value=5,  # Default to showing 5 strategies
        marks={i: str(i) for i in range(1, 25)}
    ),

    # Checkboxes for transaction costs
    html.Label("Include Transaction Costs:"),
    dcc.Checklist(
        id='tc-checklist',
        options=[
            {'label': 'With TC', 'value': 'with_tc'},
            {'label': 'Without TC', 'value': 'without_tc'}
        ],
        value=['with_tc', 'without_tc'],
        inline=True
    ),

    # Graph to display the NAVs
    dcc.Graph(id='nav-plot')
])

# Callback to update the graph based on user inputs
@app.callback(
    Output('nav-plot', 'figure'),
    [Input('ranking-dropdown', 'value'),
     Input('num-strategies-slider', 'value'),
     Input('tc-checklist', 'value')]
)
def update_graph(ranking, num_strategies, include_tc):
    # Filter columns based on the selected transaction cost options
    selected_columns = []
    if 'with_tc' in include_tc:
        selected_columns += strategies_with_tc
    if 'without_tc' in include_tc:
        selected_columns += strategies_without_tc

    # Compute the average NAV for ranking
    nav_means = df_nav[selected_columns].iloc[-1]  # Use last row for NAV ranking

    # Select top or bottom strategies
    if ranking == 'best':
        selected_columns = nav_means.nlargest(num_strategies).index
    elif ranking == 'worst':
        selected_columns = nav_means.nsmallest(num_strategies).index

    # Create the plot
    fig = go.Figure()

    for col in selected_columns:
        fig.add_trace(go.Scatter(
            x=df_nav.index,
            y=df_nav[col],
            mode='lines',
            name=col
        ))

    # Update layout
    fig.update_layout(
        title="NAV of Selected Strategies",
        xaxis_title="Date",
        yaxis_title="NAV",
        legend_title="Strategies",
        template="plotly_dark",
        height=700,
        width=1200
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
