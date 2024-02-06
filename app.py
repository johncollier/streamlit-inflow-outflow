import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('testdata.csv')

# Convert 'Month' column to datetime format
df['Month'] = pd.to_datetime(df['Month'])

# Sidebar for selecting community and subpopulation
community_options = df['Community'].unique()
selected_community = st.sidebar.selectbox('Select Community', community_options)

population_options = df[df['Community'] == selected_community]['Population'].unique()
selected_population = st.sidebar.selectbox('Select Population', population_options)

subpopulation_options = df[df['Community'] == selected_community]['Subpopulation'].unique()
selected_subpopulation = st.sidebar.selectbox('Select Subpopulation', subpopulation_options)

# Filter the data based on user selection
filtered_data = df[(df['Community'] == selected_community) & 
                   (df['Population'] == selected_population) & 
                   (df['Subpopulation'] == selected_subpopulation)]



# Sort the filtered data by month in descending order to get the most recent months on top
filtered_data = filtered_data.sort_values(by='Month', ascending=False)

tab1, tab2, tab3 = st.tabs(["Progress to Zero", "Inflow/Outflow", "Scorecards"])

with tab1:
    st.subheader("Actively Homeless")
    # Bar chart for inflow and outflow
    fig = px.bar(filtered_data, x='Month', y='Actively Homeless Number',
                title=f'Actively Homeless for {selected_subpopulation} in {selected_community}',
                labels={'value': 'Count'},
                color_discrete_map={'Inflow': '#ff6f0c', 'Outflow': '#0494cb'})
    st.plotly_chart(fig)

    st.write("Filtered Data:")
    st.write(filtered_data, width=None)

with tab2:
    # Create a copy of the filtered data for plotting with modified outflow values
    plot_data = filtered_data.copy()
    plot_data['Outflow'] = -plot_data['Outflow']  # Negate the outflow values

    st.subheader("Inflow and Outflow")
    fig_inflow_outflow = px.bar(plot_data, x='Month', y=['Inflow', 'Outflow'],
                                title=f'Inflow and Outflow for {selected_subpopulation} in {selected_community}',
                                labels={'value': 'Count'},
                                color_discrete_map={'Inflow': '#ff6f0c', 'Outflow': '#0494cb'})
    st.plotly_chart(fig_inflow_outflow)

with tab3:
   st.header("This is a duck.")
   st.image("data:image/jpeg;base64,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", width=200)


