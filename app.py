import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data for visualizations (Replace with your actual data)
rounds = ["Private 1a", "Private 1b", "Private 2", "Private Current", "Public Launchpads", "KOLs"]
prices = [0.001, 0.001, 0.0015, 0.0015, 0.0035, 0.0035]
raised = [300000, 1100000, 65000, 685500, 280000, 1100000]

# Creating charts (You might want to replace this with your actual data and charts)
def create_fundraising_chart():
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel('Round')
    ax1.set_ylabel('Price', color=color)
    ax1.bar(rounds, prices, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Amount Raised', color=color)
    ax2.plot(rounds, raised, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    return fig

# Streamlit page starts here
st.title('Project Tokenomics Overview')

st.header('Monetary Policies')
st.write("""
Similar to how central banks define economic rules for traditional currencies, tokenomics establishes the fundamental economic principles for each digital token. Key parts of this include the Allocation Distribution and Vesting Release Schedule.
""")

st.header('Cumulative Emissions Over Time')
st.write("""
The chart below illustrates the nuanced aspect of tokenomics by distinguishing between 'Unlocked Supply' and 'Circulating Supply' over time. It's essential to grasp that not all unlocked tokens immediately enter circulation.
""")
# Placeholder for chart - replace with your actual chart
st.pyplot(create_fundraising_chart())

st.header('Investor Rounds')
st.write("""
The chart shows fundraising details for a token across different rounds. This effectively outlines the progression of capital accumulation through successive investment rounds.
""")
# Placeholder for Investor Rounds chart - replace with your actual data visualization
st.pyplot(create_fundraising_chart())

st.header('Investment KPIs')
st.write("""
These key performance indicators (KPIs) serve as metrics that monitor the conditions of different investment rounds, enabling investors to make informed decisions.
""")
# Example of displaying KPIs - replace with interactive widgets or tables based on your data
st.metric(label="Investor Fully Diluted Valuation (FDV)", value="$10M")
st.metric(label="Vesting Diluted Valuation (VDV) for Private 1a", value="$2.0M")

# Continue adding sections and interactive elements as needed based on your tokenomics model

# To run this Streamlit app, save the code in a file (e.g., tokenomics_streamlit.py), and execute `streamlit run tokenomics_streamlit.py` in your terminal.
