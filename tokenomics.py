import os
import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from openai import OpenAI

st.set_page_config(layout="wide", page_title="$PiPS Tokenomics", page_icon="💰")

# custom_css = """
# <style>
# body {
#     cursor: url('http://www.rw-designer.com/cursor-extern.php?id=151729'), pointer;
# </style>
# """

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

        body {
            font-family: 'Space Mono', monospace !important;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'VT323', monospace !important;
            font-weight: 400 !important;
            color: black !important;
            
        }
    </style>
""", unsafe_allow_html=True)


st.sidebar.image("https://gcdnb.pbrd.co/images/8Qhs6pDef7u0.png?o=1", use_container_width=True)
st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Tokenomics section",
                                ["Token Supply & Distribution", "Vesting & Release Schedule", "Monetary & Fiscal Policies", "Staking & Liquidity"])


if "app_mode" not in st.session_state:
    st.session_state.app_mode = "Token Supply & Distribution"

st.session_state.app_mode = app_mode

st.sidebar.markdown("<hr>", unsafe_allow_html=True)


# OpenAI starts
with st.sidebar:
    st.title("PiP Tokenomics AI")
    openai_api_key = st.text_input("Add Your OpenAI API Key", key="chatbot_api_key", type="password", placeholder="Not saved or stored by us")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

#Start of OpenAI    
    @st.dialog("PiP World Tokenomics AI Expert")
    def tokenomics_chat_modal():
        if "messages" not in st.session_state:

            st.session_state["messages"] = [
                {"role": "system", "content": """
                Give short answers and memorise this: PiiP World is a gamified financial ecosystem that combines blockchain technology and AI to help users develop financial literacy, learn trading strategies, and interact with dynamic AI agents in a risk-free environment, offering real-world opportunities for top performers, the Tokenomics is:
                The PiP World tokenomics allocates 29% of the total supply to Network Incentives, with a 24-month lock and no cliff period. 14% is allocated to the Team, with an 18-month cliff and a 36-month lock. 20% is allocated to the Treasury, with a 48-month lock and no cliff period. 5% is allocated to Advisors, with a 12-month cliff and a 24-month lock. 10% is allocated to Seed, with a 12-month cliff and an 18-month lock. 10% is allocated to Series A, with a 12-month cliff and an 18-month lock. 2% is allocated to the Community Sale, which has a 3-month cliff and an 18-month lock. 10% is allocated to Liquidity, with no cliff and no lock period. The total allocation across all categories sums up to 100% of the supply.
                """}
            ]

        for msg in st.session_state.messages:
            if msg["role"] != "system":  # Skip the system message when rendering the chat
                st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input(placeholder="Ask PiP World Tokenomics AI Expert"):
            if not openai_api_key:
                st.info("Please add your OpenAI API key to continue.")
                st.stop()

            client = OpenAI(api_key=openai_api_key)
            
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", messages=st.session_state.messages
            )
            
            msg = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg)
            
    if st.button("Open PiP World Tokenomics AI Expert", type="primary"):
            tokenomics_chat_modal()
#End of OpenAI

# OpenAI end
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

st.sidebar.markdown("""
## Links
[Whitepaper](https://ecosystem.pip.world)
""")

sizeABC = [10, 10, 29, 14, 20, 5, 2, 10]
labelsABC = ['Seed', 'Series A', 'Network Incentives', 'Team', 'Treasury', 'Advisors', 'Community Sale', 'Liquidity']

def create_chart(data, title, ylabel):
    fig, ax = plt.subplots()
    ax.plot(data, marker='o')
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    return fig

token_prices = np.random.rand(10) * 10
market_caps = np.random.rand(10) * 1000

if app_mode == "Token Supply & Distribution":
    st.title("$PiPS Token Supply and Distribution")
    
    
    st.write("""The $PiPS token lies at the heart of the PiP World ecosystem, carefully designed to incentivise participation, reward learning, and foster a vibrant, self-sustaining economy. Our tokenomics model has been meticulously crafted to ensure the long-term sustainability of the platform, align the interests of all stakeholders, and support the growth and adoption of PiP World. """)
    
    col1, space, col2 = st.columns([1, 0.1, 1])
    with col1:
            labels = labelsABC
            sizes = sizeABC
            colors = ['#6A0DAD', '#FF6347', '#3CB311', '#000000', '#FFD700', '#1E90FF', '#4682B4', '#3CB371']  

            fig = go.Figure(data=[go.Pie(labels=labels, 
                                        values=sizes, 
                                        hole=.3, 
                                        marker_colors=colors, 
                                        pull=[0.1 if size == max(sizes) else 0 for size in sizes], 
                                        textinfo='label+percent', 
                                        hoverinfo='label+percent')])
            
            fig.update_layout(height=650, width=800)  

            st.plotly_chart(fig, use_container_width=True)  

    with col2:
        import pandas as pd

        labels = labelsABC
        data = {
            "Category": labels,
            "Allocation %": [10, 10, 29, 14, 20, 5, 2, 10],
            "Tokens": [int(allocation / 100 * 500000000) for allocation in [10, 10, 29, 14, 20, 5, 2, 10]],
            "Price": ["$0.07", "$0.13", "-", "-", "-", "-", "-", "-"],
            "USD Value": ["$3,500,000", "$6,500,000", "-", "-","-", "-", "-", "-"],
            "Fully Diluted Valuation": ["$150,000,000", "$150,000,000", "-", "-", "-", "-", "-", "-"]
        }

        df = pd.DataFrame(data)
        st.write("""
                 
                 &nbsp; 
                 
                 &nbsp;
                 
                 &nbsp;""")
        st.dataframe(df, height=320)
        
    
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["$PiPS Token Price 💰", "Token Emmissions", "Investor Rounds","Tokenomics Tables", "Token Sale Roadmap", "Token Supply Dynamics"])
    
    with tab1:
        st.write("## $PiPS Token Price Coming Soon")
        st.write("Here you will be able to simulate the token price based on the market cap and circulating supply.")
        st.markdown("<hr>", unsafe_allow_html=True)
        
 #TOKEN SIM HIDE MAIN SECTION
#     with tab1:
#         st.write("## $PiPS Token Price")
        
#         col1, spacer, col2 = st.columns([1, 0.1, 1])


#         with col1:
#             st.write("""
                    
#                     To make an informed decision about the optimal timing for investing in $PiPS tokens, consider the detailed metrics outlined below. These metrics are crucial in assessing the viability and potential profitability of such investments within specified monthly periods. By carefully analysing the proposed market capitalisation figures and trends over these ranges, you can identify the most favorable moments to allocate resources to the PiP Ecosystem. 
                    
#                     This strategic approach not only has the potential to maximise your investment potential but also minimise risk by relying on data-driven insights and projections. Keep in mind that understanding the dynamics of market capitalisation, including factors that influence fluctuations and growth prospects, is essential in making educated investment choices.
                    
#                     :blue[*Select the desired range of months, as well as the market cap to view the potential corresponding token price and circulating supply figures, enabling you to make well-informed investment decisions*:]
#                     &nbsp;
#                     """)

#         with col2:
    
    
#         # NEW VERSION WITH 2 SLIDERS
#             #OLD: monthly_release = np.array([68250000.0, 4083333.0, 4083333.0, 4083333.0, 5843567.0, 5843567.0, 5843567.0, 7602827.0, 7602827.0, 7602827.0, 11978183.0, 11978183.0, 11978183.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 9589294.0, 5598553.0, 5598553.0, 5598553.0, 5598553.0, 5598553.0, 5598553.0, 5598553.0, 5598553.0, 5598553.0, 5598553.0, 5598553.0, 5598553.0, 3825049.0, 3825049.0, 3825049.0, 3825049.0, 3825049.0, 3825049.0, 3825049.0, 3825049.0, 3825049.0, 3825049.0, 3825049.0, 3825049.0])
#             #WRONG: monthly_release = np.array([68250000, 6250000, 6250000, 6250000, 6694444, 6694444, 6694444, 8083333, 8083333, 8083333, 8467949, 8467949, 8467949, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 10568643, 6079060, 6079060, 6079060, 6079060, 6079060, 6079060, 6079060, 6079060, 6079060, 6079060, 6079060, 6079060, 1388889, 1388889, 1388889, 1388889, 1388889, 1388889, 1388889, 1388889, 1388889, 1388889, 1388889, 1388889])
#             #OLD Nov2024 monthly_release = np.array([68250000, 6250000, 6250000, 6250000, 6694444, 6694444, 6694444, 8480159, 8480159, 8480159, 8864774, 8864774, 8864774, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 10965469, 6475885, 6475885, 6475885, 6475885, 6475885, 6475885, 6475885, 6475885, 6475885, 6475885, 6475885, 6475885])
#             monthly_release = np.array([
#                 43000000.00, 4166666.67, 4166666.67, 4166666.67,
#                 10466666.67, 10466666.67, 10466666.67,
#                 12252380.95, 12252380.95, 12252380.95,
#                 13919047.62, 13919047.62, 13919047.62,
#                 15655158.73, 15655158.73, 15655158.73, 15655158.73, 15655158.73, 15655158.73,
#                 9355158.73, 9355158.73, 9355158.73, 9355158.73, 9355158.73, 9355158.73,
#                 7688492.06, 7688492.06, 7688492.06, 7688492.06, 7688492.06, 7688492.06, 7688492.06, 7688492.06,
#                 7688492.06, 7688492.06, 7688492.06, 7688492.06, 7688492.06, 7688492.06, 7688492.06, 7688492.06,
#                 7688492.06, 7688492.06, 7688492.06, 7688492.06, 7688492.06, 7688492.06, 7688492.06, 7688492.06
#             ])

#             max_supply = 500e6  
#             total_months = 49  
        
#             # User Inputs
#             market_cap_million = st.slider("Market Cap ($M)", min_value=1, max_value=2000, value=50, step=1, format='%dM')
#             selected_months = st.slider("Select Month Range (TGE included at M1)", min_value=1, max_value=total_months, value=(1, total_months), step=1)
            
#             col1, spacer, col2 = st.columns([1, 0.1, 1])
#             with col1:
#                 # OLD
#                 # number = st.number_input("Select Demand Multiplier", min_value=0.06, max_value=0.1, value=0.075, step=0.01)
#                 # formatted_number = f"{number:.5f}"
#                 # st.write("The current growth rate is ", formatted_number)
                
                
#                 growth_options = {
#                     "Conservative Growth": 0.07,
#                     "Balanced Expansion": 0.075,
#                     "Aggressive Growth": 0.085,
#                     "Breakout Potential": 0.11
#                 }

#                 option = st.selectbox(
#                     "Select Demand Multiplier",
#                     options=list(growth_options.keys()),
#                     index=1,
#                 )

#                 selected_growth_rate = growth_options[option]
                
    
#             with col2:
#                 st.write("&nbsp;")
                
                
#             # growth_rate_slider = st.slider("Growth Rate", min_value=0.05, max_value=0.07, value=0.06, step=0.001)
            
#                 with st.spinner("Modelling..."):
#                     time.sleep(2)
#             st.success(f"Completed! You selected {option}, which corresponds to a growth rate of {selected_growth_rate}*") 
            
#         st.divider()

#         circulating_supply = np.cumsum(monthly_release[:(selected_months[1])])
#         circulating_supply = circulating_supply[(selected_months[0]-1):]
            

#         initial_market_cap = market_cap_million * 1e6
#         growth_rate = selected_growth_rate #growth_rate_slider
        
        
#         months = np.arange(selected_months[0], selected_months[1] + 1) 
#         market_cap = initial_market_cap * (1 + growth_rate) ** (months - selected_months[0])

#         token_price = market_cap / circulating_supply


#         fig = go.Figure()
#         fig.add_trace(go.Scatter(x=months, y=token_price, mode='lines+markers', name='Token Price', line=dict(color='blue'), stackgroup='one'))
#         fig.add_trace(go.Scatter(x=months, y=circulating_supply, mode='lines+markers', name='Circulating Supply', line=dict(color='grey'), yaxis='y2'))

#         fig.update_layout(title="Token Price vs Circulating Supply (Selected Range)",
#                         xaxis_title="Months",
#                         yaxis_title="Token Price ($)",
#                         yaxis=dict(tickformat=".2f"),
#                         yaxis2=dict(title='Circulating Supply', titlefont=dict(color='white'),
#                                     tickfont=dict(color='white'), overlaying='y', side='right'),
#                         showlegend=True, height=550, width=780)

#         # Display the initial chart
#         chart = st.plotly_chart(fig, use_container_width=True)

#         # Add animation and incremental updates
#         progress_bar = st.sidebar.progress(0)
#         status_text = st.sidebar.empty()

#         for i in range(1, len(months)):
#             # Update the chart data incrementally
#             fig.data[0].x = months[:i+1]
#             fig.data[0].y = token_price[:i+1]
#             fig.data[1].x = months[:i+1]
#             fig.data[1].y = circulating_supply[:i+1]

#             # Update the chart in Streamlit
#             status_text.text("%i%% Complete" % int(i / len(months) * 100))
#             chart.plotly_chart(fig, use_container_width=True)
#             progress_bar.progress(int(i / len(months) * 100))
#             time.sleep(0.04)

#         progress_bar.empty()
#         status_text.empty()


#         token_price_start = token_price[0]
#         token_price_end = token_price[-1]
#         supply_start = circulating_supply[0] / 1e6  
#         supply_end = circulating_supply[-1] / 1e6
#         expected_price_growth = (token_price_end - token_price_start) * 100
        

    

#         block_style = """
#         <style>
#         .metric-block {
#             border: 0.7px solid #CFCFCF;  /* Off white border */
#             border-radius: 1px !important;  /* Rounded corners */
#             padding: 10px;
#             text-align: center;
#             margin: 10px;
#             background-color: #f5f5f5;  /* Off white background */
#         }
#         </style>
#         """


#         st.markdown(block_style, unsafe_allow_html=True)

#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown(f"""
#             <div class="metric-block">
#                 <h3>Token Price (Start of Range)</h3>
#                 <h2>${token_price_start:.2f}</h3>
#             </div>
#             """, unsafe_allow_html=True)

#         with col2:
#             st.markdown(f"""
#             <div class="metric-block">
#                 <h3>Token Price (End of Range)</h3>
#                 <h2>${token_price_end:.2f}</h2>
#             </div>
#             """, unsafe_allow_html=True)

#         col3, col4 = st.columns(2)
#         with col3:
#             st.markdown(f"""
#             <div class="metric-block">
#                 <h3>Supply at Start of Range</h3>
#                 <h2>{supply_start:.0f}M Tokens</h2>
#             </div>
#             """, unsafe_allow_html=True)

#         with col4:
#             st.markdown(f"""
#             <div class="metric-block">
#                 <h3>Supply at End of Range</h3>
#                 <h2>{supply_end:.0f}M Tokens</h2>
#             </div>
#             """, unsafe_allow_html=True)

#         st.write("&nbsp;")
        
#         # st.plotly_chart(fig, use_container_width=True)

        
#         st.divider()
        
#         col1, space, col2 = st.columns([1, 0.1, 1])
#         with col1:
#             st.header("Token Price Growth Over Selected Period")
        
        
#             # NEW SECTION
#             months2 = np.arange(selected_months[0], selected_months[1])
#             token_prices2 = np.linspace(token_price_start, token_price_end, len(months2))


#             price_change_percent = ((token_price_end - token_price_start) / token_price_start) * 100


#             fig = go.Figure()
#             fig.add_trace(go.Scatter(x=months2, y=token_prices2, mode='lines+markers', name='Token Price Growth', line=dict(color='#5e28d5')))
#             fig.update_layout(title="Token Price Growth Over Selected Period", xaxis_title="Months", yaxis_title="Token Price ($)")


#             st.plotly_chart(fig, use_container_width=True)
            
#             st.markdown(f"""
#             <div class="metric-block">
#                 <h3>Estimated Price Change</h3>
#                 <h2><span style='color:green'>{price_change_percent:,.0f}%</span></h2>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col2:
#             st.header("Market Cap Growth Over Selected Period")
#             fig2 = go.Figure()
#             fig2.add_trace(go.Scatter(x=months, y=market_cap, mode='lines+markers', name='Market Cap', line=dict(color='#5e28d5')))
#             fig2.update_layout(title="Market Cap Growth Over Selected Period", xaxis_title="Months", yaxis_title="Market Cap ($)",
#                             yaxis=dict(tickformat=",.0f"))
            
#             st.plotly_chart(fig2, use_container_width=True)
            
#             with st.expander("*Market Cap Growth Rate"):
#                 st.write("""
# This graph presents a projected market capitalisation growth based on a growth rate range between 0.07 and 0.1 selected by you. While we've assumed a steady increase over time for this estimate, actual market cap fluctuations could lead to different token pricing outcomes.
#                 """)
#                 df = pd.DataFrame({"Months": months, "Market Cap ($M)": market_cap / 1e6})
#                 st.write(df)
                
#             # with st.expander("Important **Disclaimer**"):
#             st.warning("""
                        
#                         The information provided on this page is based on economic principles and formulae and is not intended to provide the true picture of the token price. It should not be considered as financial advice. Make sure to conduct thorough research and consult with a financial advisor before making any investment decisions.  
                            
#                             """)
#     st.divider()
#     st.header("My Token Value Calculator")    
#     st.write("""
#              Enter the number of $PiPS tokens you own to estimate their current value in USD based on your selected values above:
             
#              &nbsp;
             
#              """)
    
#     col1, space, col2 = st.columns([1, 0.1, 1])
#     with col1:
#             number = st.number_input("Number of tokens", min_value=0, value=0, step=1)
#     with col2:
#             # st.write("The value of your tokens at the end of the selected:")
#             st.metric(
#             label="The value of your tokens at the end of the selected:",
#             value=f"${number * token_price_end:.2f}",  
#             delta=f"${number * token_price_end - number * token_price_start:.2f}", 
#             delta_color="normal"
#         )

    with tab2:
        st.header("Token Emissions")
        st.write("""
The graph below outlines the phased distribution strategy for $PiPS tokens, aligning with the ecosystem's long-term vision for growth and sustainability. Across a span of 48 months, this visualization demonstrates the deliberate and strategic release of tokens into the ecosystem, highlighting categories such as Seed, Series A, Treasury, Team, Reserve, Advisors, Network Incentives, and Liquidity.

Each line represents a different category emission, not showcasing the initial lump-sum releases (such as the complete immediate release for Liquidity and initial releases for Seed and Series A rounds) followed by a linear release model tailored to each category's specific role within the PiP ecosystem. This ensures a balanced injection of tokens, facilitating ecosystem development, rewarding early backers, and fostering a vibrant community engagement while maintaining market stability.

This release strategy underscores PiP's commitment to transparency and a steady value proposition for token holders. By moderating the supply influx and aligning token releases with ecosystem milestones and growth phases, PiP World ensures a sustainable economic model that rewards long-term participants and supports the overall health and expansion of the ecosystem.         
""")

        col1, space, space, col2 = st.columns([1,2,2,1])
        with col1:
            st.write("")
            
        with col2:
            on = st.checkbox('TGE Release', value=False)

            if on:
                    tge = 0
            else:
                    tge = 1
            
        ##NEW
        
        data = {
            "Category": ["Seed", "Series A", "Network Incentives", "Team", "Treasury", "Advisors", "Community Sale"],
            "Token Amount": [50000000, 50000000, 145000000, 70000000, 100000000, 25000000, 10000000],
            "Monthly Release": [0.15, 0.15, 0.0417, 0.0556, 0.0208, 0.0833, 0.0],  # Converted percentages to decimals
            "Initial Release": [0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 1],  # Converted percentages to decimals
            "Start Month": [13, 13, 1, 19, 1, 13, 4],
            "End Month": [18, 18, 24, 36, 48, 24, 18]
        }

        df_data = pd.DataFrame(data)

        total_months = 49

        df_release = pd.DataFrame(0, index=np.arange(tge, total_months+1), columns=df_data['Category'])


        def calculate_release(row):
            if row['Start Month'] == 0:
                df_release.loc[1, row['Category']] += row['Token Amount'] * row['Initial Release']
            else:
                monthly_tokens = row['Token Amount'] * row['Monthly Release']
                release_months = np.arange(row['Start Month'], row['End Month'] + 1)
                df_release.loc[release_months, row['Category']] += monthly_tokens


        df_data.apply(calculate_release, axis=1)


        fig = go.Figure()
        for category in df_release.columns:

            fig.add_trace(go.Scatter(x=df_release.index[1:], y=df_release[category][1:], mode='lines', name=category))


        fig.update_layout(
            title='Fixed Token Release Schedule Per Month Over 48 Months (Default Excluding TGE)',
            xaxis_title='Month',
            yaxis_title='Tokens Released Per Month',
            legend_title='Category',
            height=600, width=800
        )


        st.plotly_chart(fig, use_container_width=True)
        
        col1, space, col2 = st.columns([1,0.1,1])
        
        with col1:
            with st.expander("About this graph"):
                st.write("This graph illustrates the token distribution on a month-by-month basis for each allocation category. It provides an insightful view into the active token release periods, showing the specific number of tokens that enter circulation each month. It’s particularly useful for operational oversight, enabling the monitoring of token flow and helping anticipate market supply variations within specific time frames.")
        with col2:
            with st.expander("View Data"):
                st.write(df_release)

        st.divider()
        
        
        col1, space, col2 = st.columns([1,0.1,1])


        with col1:
            st.header("Cumulative Token Emissions")
            st.write(""" 
The graph presents the cumulative token release schedule for $PiPS over a 48-month horison, detailing the progressive distribution of tokens across various categories. 
                    
                    """)

            
            data = {
            "Category": ["Seed", "Series A", "Network Incentives", "Team", "Treasury", "Advisors", "Community Sale"],
            "Token Amount": [50000000, 50000000, 145000000, 70000000, 100000000, 25000000, 10000000],
            "Monthly Release": [0.15, 0.15, 0.0417, 0.0556, 0.0208, 0.0833, 0.0],  # Converted percentages to decimals
            "Initial Release": [0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 1],  # Converted percentages to decimals
            "Start Month": [13, 13, 1, 19, 1, 13, 4],
            "End Month": [18, 18, 24, 36, 48, 24, 18]
            }

            df_data = pd.DataFrame(data)


            total_months = 49


            df_release = pd.DataFrame(0, index=np.arange(1, total_months+1), columns=df_data['Category'])


            def calculate_release(row):

                initial_release_tokens = row['Token Amount'] * row['Initial Release']
                df_release.loc[1, row['Category']] += initial_release_tokens
                

                if row['Monthly Release'] > 0:
                    monthly_tokens = row['Token Amount'] * row['Monthly Release']
                    release_months = np.arange(row['Start Month'], row['End Month'] + 1)
                    df_release.loc[release_months, row['Category']] += monthly_tokens


            df_data.apply(calculate_release, axis=1)


            df_cumulative = df_release.cumsum()

            # df_cumulative['Total'] = df_cumulative.sum(axis=1)

            fig = go.Figure()
            for category in df_cumulative.columns:
                fig.add_trace(go.Scatter(x=df_cumulative.index, y=df_cumulative[category], mode='lines', name=category, stackgroup='one'))


            fig.update_layout(
                title='Cumulative Token Release Schedule Over 48 Months',
                xaxis_title='Month',
                yaxis_title='Cumulative Tokens Released',
                legend_title='Category',
                height=550, width=800
            )


            st.plotly_chart(fig, use_container_width=True)


            st.write("""
                    
                    &nbsp;
                    
                    """)

            # with st.expander("View Data"):
            #     st.write(df_release)
                

        with col2:
            st.header("Token Supply Growth Per Category")
            # st.plotly_chart(fig2, use_container_width=True)
            st.write("""The graph depicts the rollout of $PiPS tokens over 48 months, highlighting the escalating sum of tokens dispensed across distinct allocation categories.""")


            def calculate_token_release(max_supply=500e6, months=49):
                # Updated allocations with the new percentages and categories
                allocations = {
                    'Seed': 10,
                    'Series A': 10,
                    'Network Incentives': 29,
                    'Team': 14,
                    'Community Sale': 2,
                    'Advisors': 5,
                    'Liquidity': 10,
                    'Treasury': 20,
                }

                # Create a DataFrame to hold the release data
                df = pd.DataFrame(index=range(1, months + 1))

                # Initialize all categories with zero tokens released
                for category in allocations:
                    df[category] = 0

                # Immediate release for Liquidity
                df.loc[1, 'Liquidity'] = max_supply * (allocations['Liquidity'] / 100)

                # Define a helper function for linear release scheduling
                def linear_release(start_month, end_month, percentage, category):
                    monthly_amount = (max_supply * (percentage / 100)) / (end_month - start_month + 1)
                    df.loc[start_month:end_month, category] += monthly_amount

                # Setup linear releases according to the updated schedule
                linear_release(13, 18, 10, 'Seed')  # Start at month 13, end at month 18
                linear_release(13, 18, 10, 'Series A')  # Start at month 13, end at month 18
                linear_release(1, 24, 29, 'Network Incentives')  # Start immediately, end at month 24
                linear_release(19, 36, 14, 'Team')  # Start at month 19, end at month 36
                linear_release(13, 24, 5, 'Advisors')  # Start at month 13, end at month 24
                linear_release(4, 18, 2, 'Community Sale')  # Start at month 10, end at month 24
                linear_release(1, 48, 20, 'Treasury')  # Start at month 1, end at month 48

                return df.cumsum()

            # Execute the function and store the cumulative token release DataFrame
            df_release = calculate_token_release()


            def plot_token_release(df_release):
                fig = go.Figure()
                for category in df_release.columns:
                    fig.add_trace(go.Scatter(x=df_release.index, y=df_release[category], mode='lines', name=category))
                    
                fig.update_layout(title='Token Release Schedule Over 48 Months', xaxis_title='Month', yaxis_title='Number of Tokens', legend_title='Category', height=550, width=800)
                return fig

            st.plotly_chart(plot_token_release(df_release), use_container_width=True)

        def trigger_balloons():
            st.balloons()
            st.session_state.button_clicked = True
        
        if 'button_clicked' not in st.session_state:
            st.session_state.button_clicked = False

        col1, col2 = st.columns([9, 1])

        with col1:
            with st.expander("View Data"):
                st.write(df_release, use_container_width=True)

        # Place the button in the second column
        with col2:
            if not st.session_state.button_clicked:
                if st.button("🥚"):
                    trigger_balloons()
        # with st.expander("View Data"):
        #         st.write(df_release, use_container_width=True)
                
    with tab3:
        st.header("Funding Overview by Round")
        st.write("""
                
            The chart presents an overview of the planned fundraising structure for PiP across various rounds. It outlines the projected amounts raised in each round, ranging from strategic partnerships to public offerings. This breakdown demonstrates the approach to securing financial support from a mix of stakeholders, including early backers, key opinion leaders, and the broader community. The distribution of funding sources establishes a solid foundation for $PiPS's growth and reflects a strategic plan to engage a wide range of contributors in the ecosystem's journey.
            
            &nbsp;     
                
                """)
        
        col1, space, col2 = st.columns([1,0.1,1])
        with col1:
            ## NORMAL BAR CHART
            # rounds = ['KOL Round', 'Strategic Round', 'Seed Round', 'IEO Round']
            # amounts = [500000, 4800000, 12000000, 12500000]
            # data = {
            #     "Round": ["KOL Round", "Strategic Round", "Seed Round", "IEO Round"],
            #     "Amount Raised ($)": [500000, 4800000, 12000000, 12500000]
            # }


            # fig = go.Figure(data=[
            #     go.Bar(x=rounds, y=amounts, marker_color=['#5e28d5', '#5e28d5', '#5e28d5', '#5e28d5'])
            # ])


            # fig.update_layout(title='Amount Raised at Each Funding Round',
            #                 xaxis_title='Round',
            #                 yaxis_title='Amount ($)',
            #                 height=550, width=750)
    
            # st.plotly_chart(fig, use_container_width=True)
            
            # #OLD NOV
            # rounds = ['KOL Round', 'Angel Round', 'Seed Round', 'Public Round']
            # amounts = [350000, 2800000, 9750000, 12500000]
            # sizes = [20, 40, 60, 80]  
            rounds = ['Seed Round', 'Series A Round']
            amounts = [3850000, 6500000]  # Updated funding amounts based on recent data
            sizes = [40, 60]  # Assuming sizes relate to the significance or capacity of each round



            fig = go.Figure(data=[
                go.Scatter(x=rounds, y=amounts, mode='markers', marker=dict(size=sizes, color=['#5e28d5', '#5e28d5', '#5e28d5', '#5e28d5']))
            ])

            fig.update_layout(title='Amount Raised at Each Funding Round',
                            xaxis_title='Round',
                            yaxis_title='Amount ($)',
                            height=550, width=750)

            st.plotly_chart(fig, use_container_width=True)
            
            #OLD NOV
            # table1 = {
            #     "Round": ["KOL Round", "Angel Round", "Seed Round", "Public Round"],
            #     "Amount Raised": ["$350,000", "$2,800,000", "$9,750,000", "$12,500,000"]
            # }   
            
            table1 = {
                "Round": ['Seed Round', 'Series A Round'],
                "Amount Raised": ["$3,850,000", "$6,500,000"]
            }


            df_table1 = pd.DataFrame(table1)
            df_table1.index = ["1", "2"]
            
            st.table(df_table1)
                
        with col2:
            st.write("""
                """)    
            # OLD NOV
            # data = {
            #     "Round": ["KOL Round", "Strategic Round", "Seed Round", "IEO Round"],
            #     "Price ($)": [0.07, 0.07, 0.13, 0.25]
            # }
            
            data = {
                "Round": ['Seed Round', 'Series A Round'],
                "Price ($)": [0.07, 0.13]
            }

            df = pd.DataFrame(data)


            fig = go.Figure(data=go.Scatter(x=df["Round"], y=df["Price ($)"], mode='lines+markers',line=dict(color='#5e28d5')))

            fig.update_layout(title='Price of $PiPS at Each Funding Round',
                            xaxis_title='Round',
                            yaxis_title='Price ($)',
                            height=530, width=750)


            st.plotly_chart(fig, use_container_width=True)
        
    
            df_table1 = pd.DataFrame(data)
            df_table1.index = ["1", "2"]
            
            st.table(df_table1)
            
        
        
    with tab4:
        #OLD SINCE JAN 22 - for pie charts
        # table_data = {
        #     "Category": ["Ecosystem", "Team", "Reserve", "Advisors", "Pre-seed", "Seed", "Liquidity", "Total"],
        #     "Allocation% in Total Supply": ["40.00%", "12.50%", "15.00%", "5.00%", "11.00%", "10.00%", "6.50%", "100.00%"],
        #     "Price": ["-", "-", "-", "-", "$0.07", "$0.13", "-", "-"],
        #     "Token Amount": ["200,000,000", "62,500,000", "75,000,000", "25,000,000", "55,000,000", "50,000,000", "32,500,000", "500,000,000"],
        #     "Token Price at Public Round": ["$50,000,000", "$15,625,000", "$18,750,000", "$6,250,000", "$13,750,000", "$12,500,000", "$8,125,000", "-"],
        #     "Sale in $": ["-", "-", "-", "-", "$3,850,000", "$6,500,000", "-", "$10,350,000"],
        #     "Cliff (m)": ["0", "12", "6", "9", "3", "3", "0", "-"],
        #     "Lock (m)": ["48", "48", "48", "24", "18", "18", "0", "-"],
        #     "Unlock on TGE %": ["0.00%", "0.00%", "0.00%", "0.00%", "10.00%", "10.00%", "100.00%", "8.60%"],
        #     "Tokens Unlock on TGE": ["0", "0", "0", "0", "5,500,000", "5,000,000", "32,500,000", "43,000,000"],
        #     "Unlocked in $": ["$0", "$0", "$0", "$0", "$1,375,000", "$1,250,000", "$8,125,000", "$10,750,000"],
        #     "Unlock % pm": ["2.08%", "2.78%", "2.38%", "6.67%", "6.00%", "6.00%", "0.00%", "3.13%"],
        #     "Token Unlock pm": ["4,166,667", "1,736,111", "1,785,714", "1,666,667", "3,300,000", "3,000,000", "0", "15,655,159"],
        #     "Unlock pm $TGE": ["$1,041,667", "$434,028", "$446,429", "$416,667", "$825,000", "$750,000", "$0", "$3,913,790"]
        # }
        
        table_data = {
            "Category": [
                "Network Incentives", "Team", "Treasury", "Advisors", "Seed", 
                "Series A", "Community Sale", "Liquidity", "Total"
            ],
            "Allocation% in Total Supply": [
                "29.00%", "14.00%", "20.00%", "5.00%", "10.00%", 
                "10.00%", "2.00%", "10.00%", "100.00%"
            ],
            "Price": [
                "-", "-", "-", "-", "$0.07", 
                "$0.13", "-", "-", "-"
            ],
            "Token Amount": [
                "145,000,000", "70,000,000", "100,000,000", "25,000,000", "50,000,000", 
                "50,000,000", "10,000,000", "50,000,000", "500,000,000"
            ],
            "Token Price at Public Round": [
                "-", "-", "-", "-", "$3,500,000", 
                "$6,500,000", "-", "-", "$10,000,000"
            ],
            "Sale in $": [
                "-", "-", "-", "-", "$3,500,000", 
                "$6,500,000", "-", "$0", "$10,000,000"
            ],
            "Cliff (m)": [
                "0", "18", "0", "12", "12", 
                "12", "3", "0", "-"
            ],
            "Lock (m)": [
                "24", "36", "48", "24", "18", 
                "18", "18", "0", "-"
            ],
            "Unlock on TGE %": [
                "0.00%", "0.00%", "0.00%", "0.00%", "10.00%", 
                "10.00%", "100.00%", "100.00%", "8.60%"
            ],
            "Tokens Unlock on TGE": [
                "0", "0", "0", "0", "5,000,000", 
                "5,000,000", "10,000,000", "50,000,000", "70,000,000"
            ],
            "Unlocked in $": [
                "$0", "$0", "$0", "$0", "$1,250,000", 
                "$1,250,000", "$0", "$0", "$7,274,306"
            ],
            "Unlock % pm": [
                "4.17%", "5.56%", "2.08%", "8.33%", "15.00%", 
                "15.00%", "0.00%", "0.00%", "5.82%"
            ],
            "Token Unlock pm": [
                "6,041,667", "3,888,889", "2,083,333", "2,083,333", "7,500,000", 
                "7,500,000", "0", "0", "29,097,222"
            ],
            "Unlock pm $TGE": [
                "$1,510,417", "$972,222", "$520,833", "$520,833", "$1,875,000", 
                "$1,875,000", "$0", "$0", "$7,274,306"
            ]
        }

        #Old for table as of Jan 22
        # table_data2 = {
        #     "Category": ["Ecosystem", "Team", "Reserve", "Advisors", "Pre-seed", "Seed", "Liquidity"],
        #     "Allocation% in Total Supply": ["40.00%", "12.50%", "15.00%", "5.00%", "11.00%", "10.00%", "6.50%"],
        #     "Price": ["-", "-", "-", "-", "$0.07", "$0.13", "-"],
        #     "Token Amount": ["200,000,000", "62,500,000", "75,000,000", "25,000,000", "55,000,000", "50,000,000", "32,500,000"],
        #     "Token Price at Public Round": ["$50,000,000", "$15,625,000", "$18,750,000", "$6,250,000", "$13,750,000", "$12,500,000", "$8,125,000"],
        #     "Sale in $": ["-", "-", "-", "-", "$3,850,000", "$6,500,000", "-"],
        #     "Cliff (m)": ["0", "12", "6", "9", "3", "3", "0"],
        #     "Lock (m)": ["48", "48", "48", "24", "18", "18", "0"],
        #     "Tokens Unlock on TGE": ["0", "0", "0", "0", "5,500,000", "5,000,000", "32,500,000"],
        #     "Unlocked in $": ["$0", "$0", "$0", "$0", "$1,375,000", "$1,250,000", "$8,125,000"],
        #     "Unlock % pm": ["2.08%", "2.78%", "2.38%", "6.67%", "6.00%", "6.00%", "0.00%"],
        #     "Unlock pm $TGE": ["$1,041,667", "$434,028", "$446,429", "$416,667", "$825,000", "$750,000", "$0"]
        # }
        table_data2 = {
            "Category": [
                "Network Incentives", "Team", "Treasury", "Advisors", "Seed", 
                "Series A", "Community Sale", "Liquidity", "Total"
            ],
            "Allocation% in Total Supply": [
                "29.00%", "14.00%", "20.00%", "5.00%", "10.00%", 
                "10.00%", "2.00%", "10.00%", "100.00%"
            ],
            "Price": [
                "-", "-", "-", "-", "$0.07", 
                "$0.13", "-", "-", "-"
            ],
            "Token Amount": [
                "145,000,000", "70,000,000", "100,000,000", "25,000,000", "50,000,000", 
                "50,000,000", "10,000,000", "50,000,000", "500,000,000"
            ],
            "Token Price at Public Round": [
                "-", "-", "-", "-", "$3,500,000", 
                "$6,500,000", "-", "-", "$10,000,000"
            ],
            "Sale in $": [
                "-", "-", "-", "-", "$3,500,000", 
                "$6,500,000", "-", "$0", "$10,000,000"
            ],
            "Cliff (m)": [
                "0", "18", "0", "12", "12", 
                "12", "3", "0", "-"
            ],
            "Lock (m)": [
                "24", "36", "48", "24", "18", 
                "18", "18", "0", "-"
            ],
            "Tokens Unlock on TGE": [
                "0", "0", "0", "0", "5,000,000", 
                "5,000,000", "10,000,000", "50,000,000", "70,000,000"
            ],
            "Unlocked in $": [
                "$0", "$0", "$0", "$0", "$1,250,000", 
                "$1,250,000", "$0", "$0", "$7,274,306"
            ],
            "Unlock % pm": [
                "4.17%", "5.56%", "2.08%", "8.33%", "15.00%", 
                "15.00%", "0.00%", "0.00%", "5.82%"
            ],
            "Token Unlock pm": [
                "6,041,667", "3,888,889", "2,083,333", "2,083,333", "7,500,000", 
                "7,500,000", "0", "0", "29,097,222"
            ],
            "Unlock pm $TGE": [
                "$1,510,417", "$972,222", "$520,833", "$520,833", "$1,875,000", 
                "$1,875,000", "$0", "$0", "$7,274,306"
            ]
        }

        

        df = pd.DataFrame(table_data2)
        
        colors = ['#9747FF','#0038FF','#48FF63','#000000','#9747FF','#0038FF','#000000', '#9747FF', '#48FF63']
        
        st.header('Token Allocation Table')
        st.dataframe(df, height=350)
        
        col1, space, col2 = st.columns([1,0.1,1])

                
        df = pd.DataFrame(table_data)
        df['Token Amount'] = df['Token Amount'].str.replace(',', '').astype(int)
        df['Tokens Unlock on TGE'] = df['Tokens Unlock on TGE'].str.replace(',', '').astype(int)
        df['Unlock % pm'] = df['Unlock % pm'].str.replace('%', '').astype(float) / 100
        df['Unlock pm $TGE'] = df['Unlock pm $TGE'].str.replace('$', '').str.replace(',', '').astype(float)

        df = df[df['Category'] != 'Total']
        
        with col1:
            #Pie chart on allocation
            fig = px.pie(df, values='Token Amount', names='Category', title='Token Allocation (%)', hole=0.2, height=500, color_discrete_sequence=colors)
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            #pie chart on unlock on TGE
            fig2 = px.pie(df, values='Tokens Unlock on TGE', names='Category', title='Tokens Unlock on TGE (%)', hole=0.2, height=500, color_discrete_sequence=colors)
            st.plotly_chart(fig2, use_container_width=True)
            
        col1, space, col2 = st.columns([1,0.1,1])
        with col1:
            #pie chart on unlock % pm  
            fig3 = px.pie(df, values='Unlock % pm', names='Category', title='Unlock % pm (%)', hole=0.2, height=500, color_discrete_sequence=colors)
            st.plotly_chart(fig3, use_container_width=True)
            
        with col2:
            #pie chat on unlock pm $TGE
            fig4 = px.pie(df, values='Unlock pm $TGE', names='Category', title='Unlock pm $TGE (%)', hole=0.2, height=500, color_discrete_sequence=colors)
            st.plotly_chart(fig4, use_container_width=True)
    
    # with tab5:    
    #     st.write("")
        # streamlit_analytics.track(unsafe_password="test123")
        # streamlit_analytics.stop_tracking() 
    
    #TOKEN SIM HIDE MAIN SECTION 643 to 907 AND 1447 to 1474
    # block_style = """
    #     <style>
    #     .metric-block {
    #         border: 0.7px solid #f5f5f5;  /* Off white border */
    #         border-radius: 8px !important;  /* Rounded corners */
    #         padding: 10px;
    #         text-align: center;
    #         margin: 10px;
    #         background-color: #878787;  /* Off white background */
    #     }
    #     </style>
    #     """
    # st.sidebar.markdown(block_style, unsafe_allow_html=True)

    # st.sidebar.markdown(f"""
    #         <div class="metric-block">
    #             <h3>Selected MCAP</h3>
    #             <h2>${market_cap_million:}M</h3>
    #         </div>
    #         """, unsafe_allow_html=True)
    
    # st.sidebar.markdown(f"""
    #         <div class="metric-block">
    #             <h3>Selected Month Range</h3>
    #             <h2>{selected_months:}</h3>
    #         </div>
    #         """, unsafe_allow_html=True)
    
    with tab5:
        col1, space, col2 = st.columns([1, 0.1, 1])
        with col2:
                st.write("""
                 
                 &nbsp;""")
                data = {
                    "Round": ["Seed", "Series A"],
                    "Dates": ["Q2 2025", "Q3 2025"],
                    "Token Price": ["$0.07", "$0.13"],
                    "Discount": ["72%", "48%"],
                    "Fundraising Goal": ["$3.85M", "$6.50M"]
                }
                df = pd.DataFrame(data)
                st.dataframe(df, height=110) 
                
        with col1:
                st.header("Token Sale Roadmap")
                st.write("""
        The $PiPS token supply and distribution have been carefully crafted to support the long-term success and sustainability of the PiP World project. By strategically allocating tokens to key stakeholders, providing robust incentives for participation and adoption, and implementing transparent vesting and release schedules, PiP World is well-positioned to create a vibrant, rewarding, and enduring ecosystem that empowers users worldwide with the knowledge and skills to achieve financial freedom.

        In the following sections of the whitepaper, we will delve into the **governance and community** aspects of the PiP World ecosystem, showcasing how $PiPS token holders will have the opportunity to actively shape the direction and evolution of the project through decentralised decision-making and collaboration.
                """)
    
    with tab6:
        st.header("Token Supply Dynamics")
        st.write("""
                Understanding the intricate relationship between token supply and market dynamics is crucial for our ecosystem. Although we acknowledge the significance of a flexible token supply schedule, our approach diverges from this model. We have committed to a fixed token supply with the foresight to potentially adjust inflation mechanisms in the future. 

This decision underlines our commitment to balancing the need for ecosystem incentives with the goal of achieving optimal performance and supply growth management, while remaining fully aware of market implications we aim to follow this cumulative distribution function:
&nbsp;
                """)
        st.latex(r'''\Phi(y_t) = \Phi(y_{t-1}) + \iota''')
        st.write("""                 
&nbsp;


The ecosystem is energised by a continuum of speculators — both atomistic and myopic — who trade tokens for speculative gains, injecting liquidity into the market. This trading is decentralised, meaning participants act independently without the consideration of the collective impact on the market.

Speculators, external to the ecosystems operational core, may lack direct insights into the ecosystems fundamentals. They might engage in trading based on overconfident assessments of noisy or spurious information, as suggested by Sockin (2023) and evidenced by subsequent studies.

To encapsulate speculators' market behavior, we understand a demand curve as:
                """)

        st.latex(r'''X^S=Φ(y_t)−Φ(y_{t+1}+λlog(RP_t)−ζ_t)''')
        st.write("""

&nbsp;

Here, *(ζt)* represents a sentiment shock among speculators about future token prices, influencing demand and, by extension, the availability of tokens for users. High optimism (*ζt)* among speculators tightens token supply for users, while higher prices deter speculator demand, increasing user supply.

Market equilibrium is achieved when user demand and speculator behavior balance, leading to an equilibrium token price expressed as:
                """)
        st.latex(r'''P_t=1/Rexp{(\sqrt{Tϵ/λ}(A_t−A_t∗)−λy_t+λζ_t)}''')
        st.write("""
&nbsp;

This formula demonstrates the token price (*Pt)* as a log-linear function dependent on the ecosystems demand fundamentals (*At)*, user participation threshold (*At*)*, token supply (*Yt)*, and speculator sentiment *(ζt)*.

By dissecting the relationships between token supply, speculator activity, and price dynamics, we gain insights into the underlying forces shaping the cryptocurrency market. This knowledge empowers us to make informed decisions in managing our token economy, ensuring its robustness and sustainability.

                """)
        st.divider()
        with st.expander("_Source_"):
            st.markdown('_Sockin, M., & Xiong, W. (2023). A Model of Cryptocurrencies. Management Science, 69(11), 6684–6707. © 2023 INFORMS. (p. 6698)._')
    
    # st.header("$PiPs Token Simulation")
    # st.write("Gain an edge with $PiPS tokens: our data-driven insights help you pinpoint the best times to invest, maximising returns and minimising risk. Choose your preferred timeframe to access tailored projections for market cap, token price, and supply—empowering you to make confident, strategic investments in the PiP Ecosystem ")
    # if st.button("Start Simulation"):
    #         app_mode = "Investment KPIs 💰"
        

elif app_mode == "Vesting & Release Schedule":
    st.title("Vesting & Release Schedule")
    
    col1, space, col2 = st.columns([1,0.1,1])
    with col1:
        st.write("""
&nbsp;

At PiP World, we believe in aligning the interests of all stakeholders with the long-term vision and sustainability of our ecosystem. Our vesting schedule is meticulously designed to foster a deep commitment to the project's success, ensuring that contributors, team members, and advisors are invested in the growth and development of PiP World over time. 

By implementing strategic lock-up periods and gradual token releases, we aim to mitigate market volatility and reward enduring participation. This approach not only stabilises the token economy but also embodies our ethos of community-driven growth, transparency, and mutual success. Through this, we lay the foundation for a robust and thriving ecosystem, where each stakeholder's contribution is recognised and valued in our journey towards a decentralised future.

&nbsp;
""")
        # st.divider()
        st.write("""
To ensure the long-term alignment of interests and commitment to the project, the team and advisor tokens are subject to a 2-year vesting schedule with a 1-year cliff and 3-year vesting and a 18-month cliff respectively. This means that:

- No team tokens will be released during the 18 months following the token generation event.
- No advisor tokens will be released during the 12 months following the token generation event.
- After the 1.5 year cliff, 33% of the team tokens will be released in year 1.
- The remaining team/advisor tokens will be released in equal monthly instalments over the following years.

&nbsp;
                """)
    st.write("""
This vesting schedule ensures that the team and advisors have a strong incentive to drive the project's success over an extended period and provides transparency and predictability for the $PiPS token supply.

In addition to the team and advisor vesting, the Network Incentives fund tokens will be released gradually over a 2-year period following the vesting period of the TGE. This controlled release schedule ensures that the fund can sustainably support the long-term growth and development of the PiP World platform without causing undue inflationary pressure on the $PiPS token price.

""")
    with col2:
        st.write("""
                
            &nbsp;
| Category          | % in Total Supply | Sale in $   | Cliff (m) | Lock (m) |
|-------------------|-------------------|-------------|-----------|----------|
| Network Incentives| 29.00%            | $0          | 0         | 24       |
| Team              | 14.00%            | $0          | 18        | 36       |
| Treasury          | 20.00%            | $0          | 0         | 48       |
| Advisors          | 5.00%             | $0          | 12        | 24       |
| Seed              | 10.00%            | $3,500,000  | 12        | 18       |
| Series A          | 10.00%            | $6,500,000  | 12        | 18       |
| Community Sale    | 2.00%             | $0          | 3         | 18       |
| Liquidity         | 10.00%            | $0          | 0         | 0        |
| **Total**         | **100.00%**       | **$10,350,000** | -     | -        |

            """)
        
    st.divider()
    
    st.header("Token Release and Vesting Schedule")
    
    st.write("Our token release schedule, spanning 48 months, is meticulously designed to support the ecosystems's long-term sustainability and health. The graph illustrates the phased release of tokens in categories like Seed, Series A, Treasury, and more, underlining our commitment to gradual market introduction. This strategy, integral to our vesting approach, ensures stakeholders are aligned with PiP World's.")

    col1, space, col2 = st.columns([1,0.1,1])
    with col1:

        def calculate_token_release(max_supply=500e6, months=49):
            allocations = {
                'Seed': 10,
                'Series A': 10,
                'Network Incentives': 29,
                'Team': 14,
                'Community Sale': 2,
                'Advisors': 5,
                'Liquidity': 10,
                'Treasury': 20,
            }
            
            df = pd.DataFrame(index=range(1, months+1))
            
            for category, percent in allocations.items():
                df[category] = 0
            
            # Immediate allocations
            df.loc[1, 'Liquidity'] = max_supply * (allocations['Liquidity'] / 100)  # Immediate release for liquidity
            
            # Define linear_release function within calculate_token_release
            def linear_release(start_month, end_month, percentage, category):
                monthly_amount = (max_supply * (percentage / 100)) / (end_month - start_month + 1)
                df.loc[start_month:end_month, category] += monthly_amount

            # Schedules
            linear_release(13, 18, 10, 'Seed')  # Start at month 13, end at month 18
            linear_release(13, 18, 10, 'Series A')  # Start at month 13, end at month 18
            linear_release(1, 24, 29, 'Network Incentives')  # Start immediately, end at month 24
            linear_release(19, 36, 14, 'Team')  # Start at month 19, end at month 36
            linear_release(13, 24, 5, 'Advisors')  # Start at month 13, end at month 24
            linear_release(4, 18, 2, 'Community Sale')  # Start at month 10, end at month 24
            linear_release(1, 48, 20, 'Treasury')  # Start at month 1, end at month 48
            
            return df.cumsum()

        df_release = calculate_token_release()

        def plot_token_release(df_release):
            fig = go.Figure()
            for category in df_release.columns:
                fig.add_trace(go.Scatter(x=df_release.index, y=df_release[category], mode='lines', name=category, fill='tozeroy'))
                
            fig.update_layout(
                title='Cumulative Token Release Schedule Over 48 Months',
                xaxis_title='Month',
                yaxis_title='Number of Tokens',
                legend_title='Category',
                showlegend=True,
                height=600,
                width=800,
            )
            return fig

        st.plotly_chart(plot_token_release(df_release), use_container_width=True)

    with col2:
        # Updated data with the newest allocation details
        data = {
            "Category": ["Seed", "Series A", "Network Incentives", "Team", "Treasury", "Advisors", "Community Sale"],
            "Token Amount": [50000000, 50000000, 145000000, 70000000, 100000000, 25000000, 10000000],
            "Monthly Release": [0.15, 0.15, 0.0417, 0.0556, 0.0208, 0.0833, 0.0],  # Converted percentages to decimals
            "Initial Release": [0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 1],  # Converted percentages to decimals
            "Start Month": [13, 13, 1, 19, 1, 13, 4],
            "End Month": [18, 18, 24, 36, 48, 24, 18]
        }

        df_data = pd.DataFrame(data)

        total_months = 49

        # Create a DataFrame to hold the release data
        df_release = pd.DataFrame(0, index=np.arange(1, total_months+1), columns=df_data['Category'])

        # Function to calculate the token release for each category
        def calculate_release(row):
            if row['Start Month'] == 0:
                df_release.loc[1, row['Category']] += row['Token Amount'] * row['Initial Release']
            else:
                monthly_tokens = row['Token Amount'] * row['Monthly Release']
                release_months = np.arange(row['Start Month'], row['End Month'] + 1)
                df_release.loc[release_months, row['Category']] += monthly_tokens

        # Apply the function across the DataFrame
        df_data.apply(calculate_release, axis=1)

        # Plot using Plotly
        fig = go.Figure()
        for category in df_release.columns:
            fig.add_trace(go.Scatter(x=df_release.index, y=df_release[category], mode='lines', name=category, fill='tozeroy'))

        fig.update_layout(
            title='Fixed Token Release Schedule Per Month Over 48 Months (Default Excluding TGE)',
            xaxis_title='Month',
            yaxis_title='Tokens Released Per Month',
            legend_title='Category',
            height=600, width=800,
        )

        # Display the plot in Streamlit
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.header("Private Round Vesting")
    st.write("""
For the initial investment phases, including Seed and Series A Rounds, we have crafted a vesting schedule that balances the necessity for early-stage backing with the imperative of sustained engagement. These rounds are critical as they involve stakeholders who contribute not only capital but also strategic insights and promotional support, which are vital during the foundational stages of our project.
&nbsp;

- **Seed Round**: A 12-month cliff followed by an 18-month lock to encourage and secure long-term commitment from our earliest supporters.
- **Series A Round**: The same structure, with a 12-month cliff and an 18-month lock, ensures these pivotal investors are aligned with our long-term vision while preventing early token liquidation.
""")

elif app_mode == "Monetary & Fiscal Policies":
    st.title("Monetary & Fiscal Policies")
    st.write("""

In navigating the complex terrain of digital currency economics, PiP World employs a nuanced blend of monetary and fiscal policies designed to maintain a healthy token supply, control inflation, and stimulate demand for the $PiPS token. These policies are meticulously crafted to ensure the long-term sustainability and growth of the ecosystem.
            """)
    col1, space, col2 = st.columns([1,0.1,1])
    with col1:
        st.write("""
        
#### Managing Token Supply:

For $PiPS, we aim to potentially implement several key mechanisms to manage the token supply effectively:

- **Token Buyback:** A deflationary measure where a portion of the token supply is periodically removed from circulation. This mechanism is employed to counteract inflationary pressures and enhance the token's scarcity and value over time.

- **Vesting Schedules:** To align the interests of team members, advisors, and early investors with the long-term success of the ecosystem, $PiPS World incorporates vesting schedules into its tokenomics. These schedules dictate the gradual release of tokens over a specified period, preventing market flooding and ensuring a steady, controlled increase in token circulation.

- **Staking Rewards:** Encouraging token holders to stake their tokens not only secures the network but also reduces the velocity of money within the ecosystem. Staked tokens are temporarily removed from circulation, which can have a deflationary effect by decreasing the available supply, thus potentially increasing the token's price.
            """)
    with col2:  
        st.write("""
#### Inflation Control and Demand Stimulation:

To mitigate the risk of inflation and stimulate demand for the $PiPS token, PiP World aims to adopts the following policies:


- **Inflation Rate Management:** While the $PiPS token has a capped supply, mechanisms for releasing tokens into the ecosystem, such as rewards for staking or participation in governance, are designed with a cap to ensure they do not dilute the token's value. The governance model allows for adjustments to these mechanisms, ensuring flexibility to respond to changing economic conditions.
- **Demand Stimulation Initiatives:** Beyond the utility provided within the ecosystem, PiP World engages in strategies to stimulate demand for the $PiPS token. These include partnerships that expand the token's use cases, marketing campaigns to raise awareness and adoption, and liquidity provisioning on exchanges to facilitate easy trading.
            """)
    st.write("""
&nbsp;

By integrating these monetary and fiscal policies, PiP World aims to maintain a balanced and thriving economy. Managing the token supply through locking, vesting, and staking, alongside strategic measures to control inflation and stimulate demand, positions the $PiPS token for sustained value and utility within the ecosystem.
            
            """)
    st.divider()
    col1, space, col2 = st.columns([1,0.1,1])
    with col1:
        st.header("🔒 Token Locking and Linear Claiming")
        st.write("""
Token locking for all participants secures $PiPS tokens, reducing market volatility. The linear claiming strategy allows for real-time, second-by-second token release, mitigating bulk sell-off risks and stabilising token price.
                """)
        st.header("⏱️ Staking Protocol with Diverse Rewards")
        st.write("""
Our staking protocol incentivises token holding by potentially offering rewards in stablecoins, alongside $PiPS tokens. Allocating USDT from revenue streams into the staking rewards pool ensures a continuous incentive for token holders, promoting long-term holding and ecosystem stability.
            """)
    with col2:
        st.header("🖼️ NFT Integration for Enhanced Utility")
        st.write("""
NFTs within PiP World not only serve as digital art assets but also play a crucial role in the deflationary framework. Increasing staking reward claim frequency based on NFT holdings and enabling NFT staking for PiP rewards add layers of utility, driving both NFT acquisition and token retention.
    """)
        st.header("🚜 Ecosystem Growth and Social Farming Initiatives")
        st.write("""
The ecosystem growth fund (netrowk incentives) explores social farming as a method to engage the community and drive ecosystem growth, potentially incorporating rewards that align with deflationary objectives.
    """)
    st.divider()
    st.header("Supply Shocks and Pricing Dynamics")
    
    col1, space, col2 = st.columns([1,0.1,1])
    with col1:
        st.write("""
                
&nbsp;

In the realm of cryptocurrency, a critical event that significantly impacts the price of a token is the occurrence of supply shocks. These are moments when a substantial portion of tokens, previously locked or unavailable, is suddenly released into circulation. The introduction of these tokens can lead to dramatic shifts in market dynamics, predominantly influencing the token's price.
            """)
        st.write("""

A study of various projects, including Optimism, Sandbox, Axie Infinity, and Immutable X, provided a clear illustration of how supply shocks correlate with price movements. For instance, significant supply shocks, where a large percentage of the token supply was released, consistently led to notable price declines. 


This observation stems from a fundamental economic principle: if the circulating supply of a token increases and the market cap remains constant, the price per token must decrease.

&nbsp;
            
:blue[⎯⎯ Aggregate Demand Curve]

:violet[⎯⎯ Initial Short Run Aggregate Supply Curve]

:red[------ Increased SR Aggregate Supply Curve]

            """)

    with col2:
        quantity = np.arange(1, 105, 1)


        demand_price = 120 - (1 * quantity)  
        supply_price_initial = 20 + (1 * quantity)  
        supply_price_increased = 1 + (1 * quantity)  


        fig = go.Figure()


        fig.add_trace(go.Scatter(x=quantity, y=demand_price,
                                mode='lines',
                                name='Aggregate Demand Curve',
                                line=dict(color='blue')))


        fig.add_trace(go.Scatter(x=quantity, y=supply_price_initial,
                                mode='lines',
                                name='Initial SR Aggregate Supply Curve',
                                line=dict(color='violet')))


        fig.add_trace(go.Scatter(x=quantity, y=supply_price_increased,
                                mode='lines',
                                name='Increased SR Aggregate Supply Curve',
                                line=dict(color='red', dash='dash')))


        fig.update_layout(title='Supply and Demand Curves',
                        xaxis_title='Quantity (Millions)',
                        yaxis_title='Price (Cents)',
                        showlegend=False,
                        height=550, width=700)


        st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
### Predicting Price Drop from Supply Shock

The relationship between supply shock and the subsequent price drop is deeply rooted in tokenomics principles. Through extensive analysis of various projects experiencing significant changes in their circulating supply, a strong correlation has been observed between the percentage of supply shock and the resultant price drops. This analysis underpins the concept that sudden increases in token supply can lead to substantial decreases in token price, due to market dynamics of supply and demand.

The precise impact of supply shock on price can vary based on a multitude of factors, including the project's market cap, liquidity, and investor sentiment. However, historical data from multiple projects consistently demonstrates a tangible link between these supply changes and market reactions. This relationship highlights the importance of carefully planned token distribution schedules to mitigate potential adverse effects on market price.

Understanding this correlation is pivotal for PiP World ecosystem teams and investors, as it underscores the potential market implications of token unlock events and other supply-related activities. It encourages a strategic approach to token releases, ensuring they align with long-term project goals and market stability.

&nbsp;

        """)
    st.header("Case Studies and Analysis")
    
    col1, space, col2 = st.columns([1,0.1,1])
    with col1:
        st.write("""
The table below showcases specific instances of supply shocks across various projects and their subsequent impact on token prices:

| Project | Date of Supply Shock | Supply Shock (%) | Outcome (% Drop) |
| --- | --- | --- | --- |
| Optimism | 30/05/2023 | 130 | -26 |
| Sandbox (Ex. 1) | 14/02/2022 | 43.8 | -40 |
| Sandbox (Ex. 2) | 14/08/2022 | 30.5 | -36.5 |
| Sandbox (Ex. 3) | 14/02/2023 | 20.9 | -40.2 |
| Axie Infinity | 28/04/2022 | 20.7 | -58.7 |
| Immutable X | Not Specified | 56.1 | -42.2 |
            """)
        st.write("""
&nbsp;

By understanding and applying this equation, investors and our teams can better navigate the complex interplay between token supply and market behavior, allowing for more informed decision-making in the volatile landscape of cryptocurrency.
            
            """)
    with col2:

        projects = ["Optimism", "Sandbox (Ex. 1)", "Sandbox (Ex. 2)", "Sandbox (Ex. 3)", "Axie Infinity", "Immutable X"]
        supply_shock = [130, 43.8, 30.5, 20.9, 20.7, 56.1]
        outcome = [-26, -40, -36.5, -40.2, -58.7, -42.2]  


        fig = go.Figure()


        for project, shock, out in zip(projects, supply_shock, outcome):
            fig.add_trace(go.Scatter(x=[shock], y=[out],
                                    mode='markers+text',
                                    name=project,
                                    text=[project],
                                    textposition="top center"))


        fig.update_layout(title='Supply Shock and Outcome Across Projects',
                        xaxis_title='Supply Shock (%)',
                        yaxis_title='Outcome (% Drop)',
                        showlegend=False,
                        height=500, width=700)


        fig.update_xaxes(range=[0, 130+ 10])
        fig.update_yaxes(range=[min([o for o in outcome if o is not None]) - 10, -10]) 


        st.plotly_chart(fig, use_container_width=True)

    # st.pyplot(create_chart(market_caps, "Market Cap Over Time", "Market Cap ($)"))

elif app_mode == "Staking & Liquidity":
    st.title("Staking and Liquidity Provisions")

    st.write("""
            
            PiP World aims to introduce a strategic staking and rewards mechanism that not only incentivises long-term holding of the $PiPS token but also significantly contributes to the stability and liquidity of the ecosystem. This approach is carefully designed to balance rewarding token holders while ensuring the health and growth of the platform.

### Staking Models & Rewards:
PiP World aims to offers a flexible staking model that allows token holders to lock their tokens for varying periods, thereby earning staking rewards. The model is deigned to offer higher rewards for longer lock-up periods, thus encouraging long-term holding.
The rewards are distributed from a designated staking rewards pool (reserve fund), ensuring a consistent and predictable supply of rewards to stakeholders. This model serves dual purposes:
            
            """)
    st.divider()
    col1, space, col2 = st.columns([1,0.1,1])
    with col1:
        st.write("""#### Long-term Holding Incentive""")
        st.write("""By providing higher rewards for longer staking periods, token holders are encouraged to commit their tokens over extended periods. This reduces the circulating supply of $PiPS, increasing their value and providing a financial incentive for holders to align with the ecosystem's long-term success.""")
        
        
    with col2:
        st.write("""#### Ecosystem Stability""")
        st.write("""The predictable nature of staking rewards, coupled with the commitment of tokens for staking, lends stability to the $PiPS token's market. It mitigates the impact of speculative trading and short-term volatility, fostering a more stable economic environment.""")
    # st.latex(r'''multiplier = 1.05^x''')
    
    
    
    
    st.divider()
    
    st.write("### Impact on Token Velocity and Ecosystem Liquidity")
    st.write("""
            
            A staking mechanism directly influences the velocity of the $PiPS token and the liquidity within the ecosystem:
            
- **Reduced Token Velocity:** Staking rewards encourage holders to lock their tokens, reducing the frequency with which the token changes hands. A lower velocity (V↓) is beneficial for $PiPS value, as it suggests a preference for holding over trading.  
- **Enhanced Ecosystem Liquidity:** Part of the staking strategy includes provisions for liquidity provisioning. Stakers might have the opportunity to contribute to liquidity pools, earning additional rewards while enhancing the liquidity of $PiPS tokens on DEXs. This not only benefits the stakers but also improves the trading experience for all users by reducing slippage and ensuring fair market prices.

PiP World's future staking and rewards mechanism is designed to encourage long-term holding and contribute to ecosystem stability. By carefully balancing incentives for token holders with the needs of the ecosystem, PiP World ensures a vibrant community of stakeholders invested in its long-term success, while managing token velocity and enhancing liquidity.

### 🔮 Future NFT Vesting Accelerators
At PiP World we are exploring into an exciting innovation: using NFTs to offer unique vesting and staking advantages. These NFTs aim to provide two key benefits: the ability to accelerate vesting periods, allowing investors quicker access to their tokens, and the option to stake these NFTs for additional rewards. This initiative reflects our commitment to leveraging best-in-class technology for greater ecosystem flexibility and community engagement, offering stakeholders more control and added value within the PiP ecosystem.

&nbsp;
            """)
    

# elif app_mode == "Token Simulation 💰":

#     st.title("Token Simulation 💰")
