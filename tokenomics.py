import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go

st.sidebar.image("pip2.png", use_column_width=True)
st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Select tokenomics section",
                                ["Token Supply & Distribution", "Vesting & Release Schedule", "Deflationary Mechanisms", "Staking & Liquidity", ""])
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

st.sidebar.markdown("""
## PiP World
For further information on PiP World, follow the link here to explore our Whitepaper.
""")

month_selected = st.sidebar.slider("Select Month", min_value=0, max_value=48, value=0, step=1)
market_cap_selected = st.sidebar.slider("Select Market Cap", min_value=1, max_value=500, value=1, step=1, format='%dM')

def create_chart(data, title, ylabel):
    fig, ax = plt.subplots()
    ax.plot(data, marker='o')
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    return fig

# Sample data for charts
token_prices = np.random.rand(10) * 10
market_caps = np.random.rand(10) * 1000

if app_mode == "Token Supply & Distribution":
    st.title("$PIP Token Supply and Distribution")
      
    st.write("""
&nbsp;

The $PIP token lies at the heart of the PIP World ecosystem, carefully designed to incentivise participation, reward learning, and foster a vibrant, self-sustaining economy. Our tokenomics model has been meticulously crafted to ensure the long-term sustainability of the platform, align the interests of all stakeholders, and support the growth and adoption of PIP World.

&nbsp;
""")
    
    
    # labels = ['Strategic Round', 'Seed Round', 'Public Round', 'Team and Advisors', 
    #       'Ecosystem Fund', 'Staking Rewards', 'Liquidity Provision', 
    #       'Airdrops and Partnerships', 'Foundation Reserve']
    # sizes = [6, 8.125, 12.5, 10, 20, 20, 10, 10, 3.375]
    # colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4', '#fffac8']

    # # Creating the pie chart with Plotly Express
    # fig = px.pie(names=labels, values=sizes,
    #             color_discrete_sequence=colors,
    #             hole=.3)  # Adjust 'hole' parameter for a donut-like appearance

    # # Customizing the hover information and pulling the largest segment a bit out
    # fig.update_traces(textinfo='percent+label', hoverinfo='label+percent',
    #                 pull=[0.1 if size == max(sizes) else 0 for size in sizes])

    # # Display the pie chart in Streamlit
    # st.plotly_chart(fig, use_container_width=True)


    # Labels, sizes, and colors
    labels = ['Strategic Round', 'Seed Round', 'KOL','IEO', 'Team', 'Advisors', 
          'Community', 'Liquidity', 'Ecosystem', 'Reserve']
    sizes = [8, 15, 1, 10, 10, 3, 9, 10, 15, 19]

    colors = ['#ff9999','#66b3ff','#987345','#99ff99','#ffcc99', '#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4', '#fffac8']

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, 
                                values=sizes, 
                                hole=.3, # This creates the donut-like appearance
                                marker_colors=colors, # Set the segment colors
                                pull=[0.1 if size == max(sizes) else 0 for size in sizes], # Pull out the largest segment
                                textinfo='percent+label', 
                                hoverinfo='label+percent')])

    # Adjust the layout to increase the size of the chart
    fig.update_layout(height=600, width=800)  # Example size, adjust as needed

    # Display the pie chart in Streamlit
    st.plotly_chart(fig, use_container_width=False)  # Set to False to use custom dimensions

    
    st.write("""
&nbsp;

| Category | Allocation | Tokens | Price | Raise (M) | Fully Diluted Valuation |
| --- | --- | --- | --- | --- | ---- |
| Strategic Round | 8% | 40 000 000 | $0.12 | $4.8 | $60 000 000 |
| Seed Round | 15% | 75 000 000 | $0.16 | $12 | $80 000 000 |
| KOL Round | 1% | 5 000 000 | $0.10 | $0.5 | $50 000 000 |
| IEO Round | 10% | 50 000 000 | $0.25 | $12.5 | $125 000 000 |
| Team & Advisors | 13% | 65 000 000 | - | - | - |
| Ecosystem Fund | 15% | 75 000 000 | - | - | - |
| Liquidity Provision | 10% | 50 000 000 | - | - | - |
| Community | 9% | 45 000 000 | - | - | - |
| Reserve | 19% | 95 000 000 | - | - | - |
| Total | 100% | 500 000 000 | - | $29.8 | - |

&nbsp;

""")
    st.write()
    with st.expander("Distribution Breakdown"):
        st.write("""
The token distribution has been carefully allocated to support the project's development, incentivise adoption, and ensure a healthy and sustainable ecosystem.

1. **Strategic Round (8%)**: This round is designed to onboard key partners and advisors who bring significant value to the project. By allocating tokens at a lower price point, we can attract strategic investors who are committed to the long-term success of PiP World.
2. **Seed Round (15%)**: The seed round provides early supporters with an opportunity to contribute to the project's development. These investors play a crucial role in helping PiP World establish a strong foundation and gain traction in the early stages.
3. **KOL Round (1%)**: Targeted at Key Opinion Leaders in the crypto and blockchain space, this round acknowledges the pivotal role influencers and thought leaders play in disseminating information and generating awareness for PiP World, leveraging their reach to foster community engagement.
4. **IEO (10%)**: The IEO round allows the wider community to participate in the project and benefit from its growth. By setting a higher price point than the previous rounds, we aim to ensure that the project is fairly valued while still providing an attractive opportunity for public investors.
5. **Team and Advisors (13%)**: Allocating tokens to the team and advisors helps align their interests with the long-term success of the project. The 5-year vesting schedule with a 1-year cliff ensures that the team is committed to the project's growth and development over an extended period.
6. **Ecosystem (15%)**: The Ecosystem Fund is a crucial component of the tokenomics model, designed to support the development of the platform, incentivise user adoption, and forge strategic partnerships. This fund is instrumental in ensuring that PiP World has the resources necessary to grow and thrive.
7. **Liquidity (10%)**: Allocating tokens for liquidity provision on decentralized exchanges is essential for maintaining a healthy and stable market for $PiP tokens. This strategy aims to ensure wide accessibility and stable token prices, supporting the ecosystem's liquidity needs.
8. **Community (9%)**: Reserving a portion of the token supply for the community enables PiP World to drive adoption, collaborate with key industry players, and expand its ecosystem. Initiatives like airdrops and partnerships foster engagement and build valuable relationships within the blockchain and education communities.
9. **Reserve (19%)**: The Reserve serves as a strategic asset for PiP World, offering the flexibility to address challenges or capitalize on opportunities as they arise. This fund supports operational needs, market interventions, future expansions, and is managed with full transparency and community involvement in allocation decisions.
    
    """)    
    st.markdown("<hr>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Token Sale Roadmap", "Token Supply Dynamics"])
    
    with tab1:
            st.header("Token Sale Roadmap")
            st.write("""
                 ## 

        | Round | Dates | Token Price | Discount | Fundraising Goal |
        | --- | --- | --- | --- | --- |
        | Strategic | Q2 2024 | $0.12 | 52% | $4.8M |
        | Seed | Q2 2024 | $0.16 | 36% | $12M |
        | KOL | Q2 2024 | $0.10 | 60% | $0.5M |
        | Public | Q2 2024 | $0.25 | 0% | $12.5M |

        &nbsp;
        
        The $PIP token supply and distribution have been carefully crafted to support the long-term success and sustainability of the PIP World project. By strategically allocating tokens to key stakeholders, providing robust incentives for participation and adoption, and implementing transparent vesting and release schedules, PIP World is well-positioned to create a vibrant, rewarding, and enduring ecosystem that empowers users worldwide with the knowledge and skills to achieve financial freedom.

        In the following sections of the whitepaper, we will delve into the **governance and community** aspects of the PIP World ecosystem, showcasing how $PIP token holders will have the opportunity to actively shape the direction and evolution of the project through decentralised decision-making and collaboration.
                 """)
    
    with tab2:
        st.header("Token Supply Dynamics")
        st.write("""
                 Understanding the intricate relationship between token supply and market dynamics is crucial for our ecosystem. Although we acknowledge the significance of a flexible token supply schedule, our approach diverges from this model. We have committed to a fixed token supply with the foresight to potentially adjust inflation mechanisms in the future. 

This decision underlines our commitment to balancing the need for validator incentives with the goal of achieving optimal ecosystem performance and supply growth management, while remaining fully aware of market implications we follow this cumulative distribution function:
&nbsp;
                 """)
        st.latex(r'''\Phi(y_t) = \Phi(y_{t-1}) + \iota''')
        st.write("""                 
 &nbsp;
 
This supply growth model, inspired by practices in platforms like Ethereum pre-merge, ensures a controlled increase in token supply, adhering to a schedule that sees a periodical halving of new tokens, hence, gradually tapering the supply increase.

Furthermore, the ecosystem is energized by a continuum of speculators—both atomistic and myopic—who trade tokens for speculative gains, injecting liquidity into the market. This trading is decentralized, meaning participants act independently without the consideration of the collective impact on the market.

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
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('_Source: Sockin, M., & Xiong, W. (2023). A Model of Cryptocurrencies. Management Science, 69(11), 6684–6707. © 2023 INFORMS. (p. 6698)._')
        
elif app_mode == "Vesting & Release Schedule":
    st.title("Vesting & Release Schedule")
    st.write("""
&nbsp;

At PiP World, we believe in aligning the interests of all stakeholders with the long-term vision and sustainability of our ecosystem. Our vesting schedule is meticulously designed to foster a deep commitment to the project's success, ensuring that contributors, team members, and advisors are invested in the growth and development of PiP World over time. 

By implementing strategic lock-up periods and gradual token releases, we aim to mitigate market volatility and reward enduring participation. This approach not only stabilises the token economy but also embodies our ethos of community-driven growth, transparency, and mutual success. Through this, we lay the foundation for a robust and thriving ecosystem, where each stakeholder's contribution is recognized and valued in our journey towards a decentralized future.

| Round          | Allocation | USD Value   | Initial Market Cap | Cliff (Months) | Lock (Months) |
|----------------|------------|-------------|--------------------|----------------|---------------|
| Strategic Round| 8%         | $4,800,000  | $60,000,000        | 9              | 36            |
| Seed Round     | 15%        | $12,000,000 | $80,000,000        | 9              | 36            |
| KOL Round      | 1%         | $500,000    | $50,000,000        | 3              | 12            |
| IEO            | 10%        | $12,500,000 | $125,000,000       | 0              | 12            |
| Team           | 10%        | -           | -                  | 12             | 48            |
| Advisors       | 3%         | -           | -                  | 9              | 48            |
| Community      | 9%         | -           | -                  | 0              | 60            |
| Liquidity      | 10%        | -           | -                  | 0              | 0             |
| Ecosystem      | 15%        | -           | -                  | 0              | 60            |
| Reserve        | 19%        | -           | -                  | 0              | 60            |
| **Total**      | **100%**   | **$29,800,000** | -              | -              | -             |


&nbsp;

To ensure the long-term alignment of interests and commitment to the project, the team and advisor tokens are subject to a 4-year vesting schedule with a 1-year cliff and 9-month cliff respectively. This means that:

- No team or advisor tokens will be released during the 9 to 12 months following the token generation event (TGE).
- After the cliff, 25% of the team and advisor tokens will be released.
- The remaining team and advisor tokens will be released in equal monthly instalments over the following years.

This vesting schedule ensures that the team and advisors have a strong incentive to drive the project's success over an extended period and provides transparency and predictability for the $PIP token supply.

In addition to the team and advisor vesting, the Ecosystem Fund tokens will be released gradually over a 5-year period following the vesting period of the TGE. This controlled release schedule ensures that the Ecosystem Fund can sustainably support the long-term growth and development of the PIP World platform without causing undue inflationary pressure on the $PIP token price.

&nbsp;
""")
    
    tab1, tab2 = st.tabs(["Private Round Vesting", "Public Vesting"])
    
    with tab1:
            st.header("Private Round Vesting")
            st.write("""
                 For the private rounds, including the Strategic, Seed and KOL Rounds, we've designed a vesting schedule that balances the need for early support with the importance of long-term commitment. These rounds are pivotal, as they involve participants who provide not just capital but also strategic value and promotional support during the crucial early stages of the project.
                 &nbsp;

- Strategic Round: The 9-month cliff and 36-month lock period for strategic investors ensure their long-term commitment and align their interests with the sustainable growth of the project, providing stability in the early stages of development.
- Seed Round: Similar to the Strategic Round, a 9-month cliff and 36-month lock ensure seed investors are committed to the project's long-term success, reducing early sell-off and fostering gradual market entry.
- KOL Round: A shorter 3-month cliff and 12-month lock for KOLs encourage early promotion and support for the project, while ensuring their engagement over a critical initial growth period.
                 """)
            
    
    with tab2:
        st.header("Public Vesting")
        st.write("""
                 Public rounds' vesting schedules are crafted to ensure widespread participation while safeguarding the ecosystem against volatility. These rounds aim to democratize access to the project, inviting community members and public investors to contribute to and benefit from the ecosystem's growth.
                 """)
    
        st.write()
        with st.expander("Our Approach"):
                st.write("""

1. IEO: No cliff with a 12-month lock allows immediate market participation while maintaining a vested interest in the project's success, supporting price stability post-launch.
2. Team: A 12-month cliff and 48-month lock for team members underscore their commitment to the project's long-term vision and success, aligning incentives with sustained ecosystem development.
3. Advisors: The 9-month cliff and 48-month lock ensure advisors provide ongoing strategic guidance and support over an extended period, contributing to the project's longevity.
4. Community: No cliff with a 60-month lock reflects the commitment to rewarding and retaining the community's support over time, fostering a loyal user base.
5. Liquidity: No cliff or lock period facilitates immediate market liquidity, supporting trading volume and token accessibility from the outset.
6. Ecosystem: No cliff with a 60-month lock supports the long-term development and expansion of the ecosystem, funding innovation and growth initiatives.
7. Reserve: No cliff with a 60-month lock ensures a strategic reserve is available to address future needs and opportunities, safeguarding the project's adaptability and resilience.
                         """)
                    
    #st.pyplot(create_chart(token_prices, "Token Price Over Time", "Price ($)"))

elif app_mode == "Deflationary Mechanisms":
    st.title("Deflationary Mechanisms")
    st.write("""
             
In navigating the complex terrain of digital currency economics, PiP World employs a nuanced blend of monetary and fiscal policies designed to maintain a healthy token supply, control inflation, and stimulate demand for the $PiP token. These policies are meticulously crafted to ensure the long-term sustainability and growth of the ecosystem.

#### Managing Token Supply:

For $PiP, we implements several key mechanisms to manage the token supply effectively:

- **Token Burns:** A deflationary measure where a portion of the token supply is periodically removed from circulation. This mechanism is employed to counteract inflationary pressures and enhance the token's scarcity and value over time. The criteria and schedule for these burns are transparently outlined, aligning with significant ecosystem milestones or transaction volume thresholds.

- **Vesting Schedules:** To align the interests of team members, advisors, and early investors with the long-term success of the ecosystem, $PiP World incorporates vesting schedules into its tokenomics. These schedules dictate the gradual release of tokens over a specified period, preventing market flooding and ensuring a steady, controlled increase in token circulation.

- **Staking Rewards:** Encouraging token holders to stake their tokens not only secures the network but also reduces the velocity of money within the ecosystem. Staked tokens are temporarily removed from circulation, which can have a deflationary effect by decreasing the available supply, thus potentially increasing the token's price.

#### Inflation Control and Demand Stimulation:

To mitigate the risk of inflation and stimulate demand for the $PiP token, PiP World adopts the following policies:


- **Inflation Rate Management:** While the $PiP token has a capped supply, mechanisms for releasing tokens into the ecosystem, such as rewards for staking or participation in governance, are designed with a cap to ensure they do not dilute the token's value. The governance model allows for adjustments to these mechanisms, ensuring flexibility to respond to changing economic conditions.
- **Demand Stimulation Initiatives:** Beyond the utility provided within the ecosystem, PiP World engages in strategies to stimulate demand for the $PiP token. These include partnerships that expand the token's use cases, marketing campaigns to raise awareness and adoption, and liquidity provisioning on exchanges to facilitate easy trading.

By integrating these monetary and fiscal policies, PiP World aims to maintain a balanced and thriving economy. Managing the token supply through burns, vesting, and staking, alongside strategic measures to control inflation and stimulate demand, positions the $PiP token for sustained value and utility within the ecosystem.
             
### Burn Mechanism

The decision to remove tokens from circulation will be made transparently, considering ecosystem health and token economics. Burns will occur systematically, tied to:

- transaction volume
- significant milestones
- governance decisions

A detailed schedule and criteria will be outlined, with burns executed via smart contract functions.

#### Unsold Token Burn Strategy

Following the initial token offering, Pip World will burn all unsold tokens. This approach guarantees that the supply of tokens in circulation directly corresponds to the initial demand, effectively aligning supply with demand from launch. By eliminating the excess supply, this measure aims to protect the token's value from potential market dilution.

**Smart Contract and Burn Wallet Details**:

| Burn Contract | 0x..123 |
| --- | --- |
| Burn Address | 0x…123 |
| Functionality | Manages burns, transaction validations, and enforces supply cap and inflation rules. |

&nbsp;
    """)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("""
## Supply Shocks and Pricing Dynamics

In the realm of cryptocurrency, a critical event that significantly impacts the price of a token is the occurrence of supply shocks. These are moments when a substantial portion of tokens, previously locked or unavailable, is suddenly released into circulation. The introduction of these tokens can lead to dramatic shifts in market dynamics, predominantly influencing the token's price.
            """)
    
    # # # SUPPLY SHOCK GRAPH OLD
    # time_before_shock = np.arange(0, 10, 1)
    # time_after_shock = np.arange(10, 20, 1)

    # # Simulating supply levels before and after the shock
    # supply_before_shock = 100 - (2 * time_before_shock)  # Linear decrease
    # supply_shock = 50  # Sudden drop in supply
    # supply_after_shock = supply_shock - (time_after_shock - 10)  # Continue decreasing after shock

    # # Combining the data
    # time_combined = np.concatenate((time_before_shock, time_after_shock))
    # supply_combined = np.concatenate(([supply_before_shock[-1]], [supply_shock], supply_after_shock))

    # # Create the Plotly graph
    # fig = go.Figure()

    # # Before the shock
    # fig.add_trace(go.Scatter(x=time_before_shock, y=supply_before_shock,
    #                         mode='lines+markers',
    #                         name='Supply Before Shock'))

    # # Shock point
    # fig.add_trace(go.Scatter(x=[time_before_shock[-1], time_after_shock[0]],
    #                         y=[supply_before_shock[-1], supply_shock],
    #                         mode='lines+markers',
    #                         name='Supply Shock',
    #                         line=dict(color='red')))

    # # After the shock
    # fig.add_trace(go.Scatter(x=time_after_shock, y=supply_after_shock,
    #                         mode='lines+markers',
    #                         name='Supply After Shock'))

    # # Adding titles and labels
    # fig.update_layout(title='Supply Shock Graph',
    #                 xaxis_title='Time',
    #                 yaxis_title='Supply',
    #                 showlegend=True)

    # # Display the graph in Streamlit
    # st.plotly_chart(fig)
    


    # # # # MUCH BETTER DIAGRAM - also OLD 
    # time_period = np.arange(0, 20, 1)

    # # Simulating supply and demand levels
    # original_supply = 100 - (1.5 * time_period)  # Original supply decreases linearly
    # increased_supply = 100 - (1 * time_period)  # Increased supply decreases more slowly
    # demand = 120 - (0.5 * time_period)  # Demand decreases linearly

    # # Assuming price adjusts based on supply and demand balance
    # price_original_supply = demand - original_supply + 50  # Simplified pricing model
    # price_increased_supply = demand - increased_supply + 50  # Simplified pricing model

    # # Create the Plotly graph
    # fig = go.Figure()

    # # Demand line
    # fig.add_trace(go.Scatter(x=time_period, y=demand,
    #                         mode='lines',
    #                         name='Demand',
    #                         line=dict(color='blue')))

    # # Original supply line
    # fig.add_trace(go.Scatter(x=time_period, y=original_supply,
    #                         mode='lines',
    #                         name='Original Supply',
    #                         line=dict(color='red')))

    # # Increased supply line
    # fig.add_trace(go.Scatter(x=time_period, y=increased_supply,
    #                         mode='lines+markers',  # Added markers for distinction
    #                         name='Increased Supply',
    #                         line=dict(color='green', dash='dash')))

    # # Price with original supply
    # fig.add_trace(go.Scatter(x=time_period, y=price_original_supply,
    #                         mode='lines',
    #                         name='Price with Original Supply',
    #                         line=dict(color='orange')))

    # # Price with increased supply
    # fig.add_trace(go.Scatter(x=time_period, y=price_increased_supply,
    #                         mode='lines',
    #                         name='Price with Increased Supply',
    #                         line=dict(color='purple', dash='dot')))

    # # Adding titles and labels
    # fig.update_layout(title='Supply and Demand with Price Adjustment',
    #                 xaxis_title='Time',
    #                 yaxis_title='Quantity / Price',
    #                 showlegend=True)

    # # Display the graph in Streamlit
    # st.plotly_chart(fig)


    # # # NEW
    quantity = np.arange(1, 105, 1)

    # Simulating demand and supply curves
    demand_price = 120 - (1 * quantity)  # Demand curve: Price decreases as quantity increases
    supply_price_initial = 20 + (1 * quantity)  # Initial Supply curve: Price increases as quantity increases
    supply_price_increased = 1 + (1 * quantity)  # Increased Supply curve: Less steep, price still increases but less so

    # Create the Plotly graph
    fig = go.Figure()

    # Demand curve
    fig.add_trace(go.Scatter(x=quantity, y=demand_price,
                            mode='lines',
                            name='Aggregate Demand Curve',
                            line=dict(color='blue')))

    # Initial Supply curve
    fig.add_trace(go.Scatter(x=quantity, y=supply_price_initial,
                            mode='lines',
                            name='Initial SR Aggregate Supply Curve',
                            line=dict(color='violet')))

    # Increased Supply curve
    fig.add_trace(go.Scatter(x=quantity, y=supply_price_increased,
                            mode='lines',
                            name='Increased SR Aggregate Supply Curve',
                            line=dict(color='purple', dash='dash')))

    # Adding titles and labels
    fig.update_layout(title='Supply Shock Price Decrease',
                    xaxis_title='Quantity (Millions)',
                    yaxis_title='Price (Cents)',
                    showlegend=True)

    # Display the graph in Streamlit
    st.plotly_chart(fig)

    
    st.write("""

A study of various projects, including Optimism, Sandbox, Axie Infinity, and Immutable X, provided a clear illustration of how supply shocks correlate with price movements. For instance, significant supply shocks, where a large percentage of the token supply was released, consistently led to notable price declines. This observation stems from a fundamental economic principle: if the circulating supply of a token increases and the market cap remains constant, the price per token must decrease.

### Predicting Price Drop from Supply Shock

The relationship between supply shock and the subsequent price drop is deeply rooted in tokenomics principles. Through extensive analysis of various projects experiencing significant changes in their circulating supply, a strong correlation has been observed between the percentage of supply shock and the resultant price drops. This analysis underpins the concept that sudden increases in token supply can lead to substantial decreases in token price, due to market dynamics of supply and demand.

The precise impact of supply shock on price can vary based on a multitude of factors, including the project's market cap, liquidity, and investor sentiment. However, historical data from multiple projects consistently demonstrates a tangible link between these supply changes and market reactions. This relationship highlights the importance of carefully planned token distribution schedules to mitigate potential adverse effects on market price.

Understanding this correlation is pivotal for Pip World ecosystem teams and investors, as it underscores the potential market implications of token unlock events and other supply-related activities. It encourages a strategic approach to token releases, ensuring they align with long-term project goals and market stability.

### Case Studies and Analysis

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
    # Project data
    projects = ["Optimism", "Sandbox (Ex. 1)", "Sandbox (Ex. 2)", "Sandbox (Ex. 3)", "Axie Infinity", "Immutable X"]
    supply_shock = [130, 43.8, 30.5, 20.9, 20.7, 56.1]
    outcome = [-26, -40, -36.5, -40.2, -58.7, -42.2]  # Using None for "Not Specified"

    # Create the Plotly graph
    fig = go.Figure()

    # Add scatter points for each project
    for project, shock, out in zip(projects, supply_shock, outcome):
        fig.add_trace(go.Scatter(x=[shock], y=[out],
                                mode='markers+text',
                                name=project,
                                text=[project],
                                textposition="top center"))

    # Adding titles and labels
    fig.update_layout(title='Supply Shock and Outcome Across Projects',
                    xaxis_title='Supply Shock (%)',
                    yaxis_title='Outcome (% Drop)',
                    showlegend=False)

    # Customize axes ranges if needed
    fig.update_xaxes(range=[0, 130+ 10])
    fig.update_yaxes(range=[min([o for o in outcome if o is not None]) - 10, -10])  # Assuming outcomes are negative

    # Display the graph in Streamlit
    st.plotly_chart(fig)
    st.write("""
&nbsp;

By understanding and applying this equation, investors and our teams can better navigate the complex interplay between token supply and market behavior, allowing for more informed decision-making in the volatile landscape of cryptocurrency.
             
             """)

    # Placeholder for an actual cumulative emissions chart
    # st.pyplot(create_chart(market_caps, "Market Cap Over Time", "Market Cap ($)"))

elif app_mode == "Staking & Liquidity":
    st.title("Staking and Liquidity Provisions")

    st.write("""
             
             ### Introducing vePIP Tokens

Within Pip World, vePIP tokens act as a pivotal element designed to enhance the ecosystems economy and governance structure. By engaging in our staking program, users can secure their $PIP tokens within our staking smart contract for a period ranging from 1 to 30 months, earning vePIP tokens as a reward for their commitment.

### Earning vePIP Tokens

Users can lock their $PIP tokens into the staking smart contract for any duration between 1 and 30 months. Upon doing so, they will be granted vePIP tokens, which serve as a measure of their staked investment's value over the locked period.

### The vePIP Multiplier Formula

To reward our users for their loyalty and long-term participation, we've devised the vePIP multiplier formula as follows:
             
             """)
    
    st.latex(r'''multiplier = 1.05^x''')
    
    st.write("""
             
             &nbsp;
             
Where (*x*) represents the number of months the $PIP tokens are locked. This exponential approach ensures that the longer users commit their tokens, the greater the rewards, incentivising a longer lock-in period to maximise their vePIP token returns.

### Benefits of vePIP Tokens

The implementation of vePIP tokenomics is designed with multiple objectives:

- **Incentivising Long-Term Holding**: By encouraging users to lock their tokens, we aim to decrease the available supply of $PIP tokens actively circulating in the market, thereby potentially reducing sell pressure and contributing to the token's value stabilisation over time.
- **Enhancing Governance Participation**: vePIP tokens are at the heart of our governance mechanism. Users must lock their $PIP tokens for a minimum of one month to participate in governance decisions, ensuring that only those with a vested interest in the ecosystems future can influence its direction.
- **Rewarding Commitment**: The vePIP multiplier directly acknowledges users' dedication to the ecosystem by compensating staking from a 20% token allocation and offering up to a 4.32x APY for a maximum 30-month staking period, courtesy of our multiplier formula. This approach not only provides financial advantages to our users but also reinforces the financial and operational robustness of the Pip World ecosystem.

This strategic approach to staking and governance ensures that Pip World remains a secure, user-centric platform. It aligns the interests of our users with the long-term success and stability of the ecosystem, creating a harmonious balance between rewarding individual participation and fostering collective growth.
    
&nbsp;
             """)
    
    # Interactive widget example
    round_selection = st.selectbox("Select Staking Method", ["Contract Level", "Platform-based"])
    if round_selection:
        # Display information related to the selected round
        st.write(f"Details on {round_selection} Staking")

elif app_mode == "Investment KPIs":
    st.title("Investment KPIs")
    st.write("These key performance indicators (KPIs) serve as metrics that monitor the conditions of different investment rounds.")

    # Using tabs for different KPIs
    tab1, tab2, tab3 = st.tabs(["$PiP Token Price", "Fully Diluted Valuation", "Vesting Diluted Valuation"])
    
    with tab1:
        st.write("## $PiP Token Price")
        st.write("""Use the metrics below to choose the best time to invest in $PiP tokens based on the proposed market capitalization within any given month range. 
        
&nbsp;
                 """)
            
        # # MAIN: Version with the slider months & graph updating   
        # max_supply = 500e6  # 500 million tokens total supply
        # total_months = 48  # Total months for the supply to be fully available

        # # User Inputs
        # market_cap_million = st.slider("Market Cap ($M)", min_value=1, max_value=500, value=50, step=1, format='%dM')
        # selected_month = st.slider("Select Month", min_value=1, max_value=total_months, value=1, step=1)

        # # Calculations
        # months = np.arange(selected_month, total_months + 1)  # Array of months starting from the selected month
        # circulating_supply = max_supply * (np.sqrt(months) / np.sqrt(total_months))  # Calculate circulating supply starting from the selected month

        # # Assuming market cap grows over time
        # initial_market_cap = market_cap_million * 1e6
        # growth_rate = 0.06  # Monthly growth rate
        # market_cap = initial_market_cap * (1 + growth_rate) ** (months - selected_month)  # Market cap growth starting from the selected month

        # # Calculating token price
        # token_price = market_cap / circulating_supply

        # # Graph
        # fig = go.Figure()
        # fig.add_trace(go.Scatter(x=months, y=token_price, mode='lines+markers', name='Token Price'))
        # fig.update_layout(title="Token Price vs Circulating Supply (from Selected Month)", xaxis_title="Months", yaxis_title="Token Price ($)",
        #                 yaxis=dict(tickformat=".2f"))

        # # Displaying metrics
        # # Note: Since the arrays now start from the selected month, the first element corresponds to the selected month.
        # token_price_selected_month = token_price[0]
        # supply_selected_month = circulating_supply[0] / 1e6  # Convert to million tokens
        # expected_price_growth = (token_price[-1] - token_price_selected_month) * 100

        # col1, col2 = st.columns(2)
        # col1.metric("Token Price (Selected Month)", f"${token_price_selected_month:.2f}")
        # col2.metric("Supply at Selected Month", f"{supply_selected_month:.0f}M Tokens")

        # col3, col4 = st.columns(2)
        # col3.metric("Selected Market Cap ($M)", f"${market_cap_million}M")
        # col4.metric("Expected Price Growth", f"{expected_price_growth:.2f}%")

        # # Display the graph in Streamlit
        # st.plotly_chart(fig, use_container_width=True)

        # # Displaying the graph
        # st.plotly_chart(fig, use_container_width=True)
    
    
        # NEW VERSION WITH 2 SLIDERS
        max_supply = 500e6  # 500 million tokens total supply
        total_months = 48  # Total months for the supply to be fully available

        # User Inputs
        market_cap_million = st.slider("Market Cap ($M)", min_value=1, max_value=500, value=50, step=1, format='%dM')
        selected_months = st.slider("Select Month Range", min_value=1, max_value=total_months, value=(1, total_months), step=1)

        st.markdown("<hr>", unsafe_allow_html=True)
        # Calculations
        months = np.arange(selected_months[0], selected_months[1] + 1)  # Array of months for the selected range
        circulating_supply = max_supply * (np.sqrt(months) / np.sqrt(total_months))  # Calculate circulating supply for the selected range

        # Assuming market cap grows over time
        initial_market_cap = market_cap_million * 1e6
        growth_rate = 0.06  # Monthly growth rate
        market_cap = initial_market_cap * (1 + growth_rate) ** (months - selected_months[0])  # Market cap growth for the selected range

        # Calculating token price
        token_price = market_cap / circulating_supply

        # Graph
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months, y=token_price, mode='lines+markers', name='Token Price', line=dict(color='#5e28d5')))
        fig.update_layout(title="Token Price vs Circulating Supply (Selected Range)", xaxis_title="Months", yaxis_title="Token Price ($)",
                        yaxis=dict(tickformat=".2f"))

        # Metrics for the selected range
        # Since the arrays now correspond to the selected range, the first element is the start and the last element is the end of the range.
        token_price_start = token_price[0]
        token_price_end = token_price[-1]
        supply_start = circulating_supply[0] / 1e6  # Convert to million tokens
        supply_end = circulating_supply[-1] / 1e6
        expected_price_growth = (token_price_end - token_price_start) * 100
        
        col1, col2 = st.columns(2)
        col1.metric("Token Price (Start of Range)", f"${token_price_start:.2f}")
        col2.metric("Token Price (End of Range)", f"${token_price_end:.2f}")

        col3, col4 = st.columns(2)
        col3.metric("Supply at Start of Range", f"{supply_start:.0f}M Tokens")
        col4.metric("Supply at End of Range", f"{supply_end:.0f}M Tokens")
    

        # Display the graph in Streamlit
        st.write("&nbsp;")
        
        st.plotly_chart(fig, use_container_width=True)

        st.write("&nbsp;")
        st.write("## $PiP Token Price Change")
        
        
        # NEW SECTION
        months2 = np.arange(selected_months[0], selected_months[1])
        token_prices2 = np.linspace(token_price_start, token_price_end, len(months2))

        # Calculate percentage change in price
        price_change_percent = ((token_price_end - token_price_start) / token_price_start) * 100

        # Plotting the price growth graph
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months2, y=token_prices2, mode='lines+markers', name='Token Price Growth', line=dict(color='#5e28d5')))
        fig.update_layout(title="Token Price Growth Over Selected Period", xaxis_title="Months", yaxis_title="Token Price ($)")

        # Display the graph
        st.plotly_chart(fig, use_container_width=True)
        
        
        #--
        #--

        # Displaying the price change percentage in a large block next to the graph
        col1, col2 = st.columns([3, 1])
        with col2:
            # Determine the color based on the price growth being positive or negative
            color = "green" if price_change_percent >= 0 else "red"
            st.markdown(f"<h1 style='color:{color};'>{price_change_percent:.2f}%</h1>", unsafe_allow_html=True)
            st.caption("Price Change")
    
    with tab2:
        st.header("Fully Diluted Valuation")
        st.write("FDV is calculated by multiplying the price at which tokens are sold in a funding round by the total number of tokens.")

    
    with tab3:
        st.header("Vesting Diluted Valuation")
        st.write("VDV provides insight into the market cap necessary for investors to break even, factoring in the vesting conditions.")


# Additional Streamlit features can be used to make the application cooler:
# - st.expander() for collapsible sections
# - st.slider() for interactive sliders
# - st.write(), st.markdown(), st.latex() for text and formulas
# - st.metric() for key metrics display
