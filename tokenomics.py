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
                                ["Token Supply & Distribution", "Vesting & Release Schedule", "Deflationary Mechanisms", "Staking & Liquidity", "Investment KPIs"])
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
    labels = ['Strategic Round', 'Seed Round', 'Public Round', 'Team and Advisors', 
            'Ecosystem Fund', 'Staking Rewards', 'Liquidity Provision', 
            'Airdrops and Partnerships', 'Foundation Reserve']
    sizes = [6, 8.125, 12.5, 10, 20, 20, 10, 10, 3.375]
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4', '#fffac8']

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

| Category | Allocation | Tokens (million) | Price | Discount | Raise (million) | Fully Diluted Valuation |
| --- | --- | --- | --- | --- | --- | --- |
| Strategic Round | 6% | 30 | $0.08 | 66.7% | $2.4 | $40M |
| Seed Round | 8.125% | 40.625 | $0.16 | 33.4% | $6.5 | $80M |
| Public Round | 12.5% | 62.5 | $0.24 | 0% | $15 | $120M |
| Team and Advisors | 10% | 50 | - | - | - | - |
| Ecosystem Fund | 20% | 100 | - | - | - | - |
| Staking Rewards | 20% | 100 | - | - | - | - |
| Liquidity Provision | 10% | 50 | - | - | - | - |
| Airdrops and Partnerships | 10% | 50 | - | - | - | - |
| Foundation Reserve | 3.375% | 16.875 | - | - | - | - |
| Total | 100% | 500 | - | - | $23.9M | - |

&nbsp;

""")
    st.write()
    with st.expander("Distribution Breakdown"):
        st.write("""
The token distribution has been carefully allocated to support the project's development, incentivise adoption, and ensure a healthy and sustainable ecosystem.

1. **Strategic Round (6%)**: This round is designed to onboard key partners and advisors who bring significant value to the project. By allocating tokens at a lower price point, we can attract strategic investors who are committed to the long-term success of PIP World.
2. **Seed Round (8.125%)**: The seed round provides early supporters with an opportunity to contribute to the project's development. These investors play a crucial role in helping PIP World establish a strong foundation and gain traction in the early stages.
3. **Public Round (12.5%)**: The public round allows the wider community to participate in the project and benefit from its growth. By setting a higher price point than the previous rounds, we can ensure that the project is fairly valued while still providing an attractive opportunity for public investors.
4. **Team and Advisors (10%)**: Allocating tokens to the team and advisors helps align their interests with the long-term success of the project. The 4-year vesting schedule with a 1-year cliff ensures that the team is committed to the project's growth and development over an extended period.
5. **Ecosystem Fund (20%)**: The Ecosystem Fund is a crucial component of the tokenomics model, designed to support the development of the platform, incentivise user adoption, and forge strategic partnerships. By allocating a significant portion of the token supply to this fund, we can ensure that PIP World has the resources necessary to grow and thrive. The Ecosystem Fund will finance initiatives such as:
    - Developer grants to encourage the creation of new learning modules, games, and features within the PIP World platform
    - Educational content creation and localisation to make financial literacy accessible to a global audience
    - Partnerships with educational institutions, non-profits, and industry leaders to expand the reach and impact of PIP World
    - Community-driven projects and events that foster engagement, collaboration, and knowledge-sharing among PIP World users
6. **Staking Rewards (20%)**: Staking rewards are essential for incentivising users to hold and stake their $PIP tokens, contributing to the security and stability of the network. By allocating a substantial portion of the token supply to staking rewards, we create a strong incentive for users to actively participate in the ecosystem and benefit from the platform's growth.
7. **Liquidity Provision (10%)**: Allocating tokens to provide liquidity on decentralised exchanges is crucial for ensuring a healthy and stable market for $PIP tokens. Our liquidity provisioning strategy focuses on:
    - Partnering with leading decentralised exchanges to ensure wide accessibility and trading volume for $PIP tokens
    - Implementing a liquidity mining program that rewards users for providing liquidity and maintaining stable token prices
    - Continuously monitoring and adjusting liquidity parameters to optimise market efficiency and minimise volatility
8. **Airdrops and Partnerships (10%)**: Reserving a portion of the token supply for airdrops and partnerships allows PIP World to drive adoption, collaborate with key players in the industry, and expand its ecosystem. These initiatives help create awareness, attract new users, and foster valuable relationships within the blockchain and education communities. Our airdrop and partnership strategy includes:
    - Targeted airdrops to active users of leading DeFi protocols, NFT marketplaces, and learning platforms
    - Strategic partnerships with companies and projects that share our vision of accessible, engaging, and rewarding financial education
    - Cross-promotional activities and collaborations that introduce PIP World to new audiences and create mutual value for our partners
9. **Foundation Reserve (3.375%)**: The Foundation Reserve acts as a buffer, providing the PIP World project with the flexibility to address any unforeseen challenges or opportunities that may arise. This reserve ensures that the project can adapt to changing circumstances and continue to thrive in the long term. The Foundation Reserve will be managed transparently, with allocations decided through community governance mechanisms that will be detailed in the upcoming governance and community section of the whitepaper.
    
    """)    
    st.markdown("<hr>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Token Sale Roadmap", "Token Supply Dynamics"])
    
    with tab1:
            st.header("Token Sale Roadmap")
            st.write("""
                 ## 

        | Round | Dates | Token Price | Discount | Fundraising Goal |
        | --- | --- | --- | --- | --- |
        | Strategic | Q2 2024 | $0.08 | 66.7% | $2.4M |
        | Seed | Q2 2024 | $0.16 | 33.4% | $6.5M |
        | Public | Q2 2024 | $0.24 | 0% | $15M |

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

At Pip World, we have adopted a platform-based approach for token distribution. This method offers numerous benefits that streamline the process and enhance security, efficiency, and compliance. Here's why we chose this route:

- **Comprehensive Management**: Manage token launches, TGEs, and token sales all from a single platform, ensuring consistency and efficiency.
- **Automated Distribution**: Automatically distribute tokens based on custom vesting schedules. This eliminates the need for custom smart contracts or manual token transfers, simplifying the distribution process.
- **DeFi Integration**: Seamlessly transfer vested tokens to DeFi products for liquidity provision, staking, or yield farming, facilitating immediate utilization of tokens as they vest over time.
- **Enhanced Visibility and Communication**: Real-time dashboards offer players and investors clear insights into their $PIP tokens and vesting schedules.
- **Centralized Legal Documentation**: Keep all key legal agreements, such as SAFTs, organized and accessible in one place, simplifying document management.
- **Unified Governance**: Provide a singular platform for governance token holders to cast votes on proposals, fostering an engaged and active community.
- **Real-Time Cap Table Monitoring**: Easily view token cap table in real time and monitor significant transactions, maintaining transparency and control.
- **Compliance with Regulations**: Implement KYC/AML procedures and security token transfer restrictions directly through the platform, ensuring regulatory compliance.

### Future Developments: Dedicated Distribution Contract

Pip World is actively exploring the development of a dedicated smart contract for token distribution. This innovative approach aims to further streamline the token distribution process, guaranteeing a transparent, efficient, and secure delivery of tokens directly to the intended recipients. By leveraging blockchain technology, we underscore our commitment to operational excellence and building trust among our stakeholders.

| Category | Token Amount (%) | USD Value (million) | Initial Market Cap. (TGE) | Cliff (months) | Linear Vesting (months) |
| --- | --- | --- | --- | --- | --- |
| Strategic Round | 6% | $0.25 | $20.0 | 6 | 8 |
| Seed Round | 8.125% | $0.65 | $40.0 | 6 | 8 |
| Public Round | 12.5% | $15 | $30.0 | 2 | 6 |
| Team and Advisors | 10% | - | - | 12 | 36 |
| Ecosystem Fund | 20% | - | - | 24 | 60 |
| Staking Rewards | 20% | - | - | 0 | 12 |
| Liquidity Provision | 10% | - | - | 0 | 12 |
| Airdrops and Partnerships | 10% | - | - | 0 | 8 |
| Foundation Reserve | 3.375% | - | - | 60 | 60 |

&nbsp;

To ensure the long-term alignment of interests and commitment to the project, the team and advisor tokens are subject to a 3-year vesting schedule with a 1-year cliff. This means that:

- No team or advisor tokens will be released during the first year following the token generation event (TGE)
- After the 1-year cliff, 33.34% of the team and advisor tokens will be released
- The remaining team and advisor tokens will be released in equal monthly instalments over the following 2 year.

This vesting schedule ensures that the team and advisors have a strong incentive to drive the project's success over an extended period and provides transparency and predictability for the $PIP token supply.

In addition to the team and advisor vesting, the Ecosystem Fund tokens will be released gradually over a 5-year period following the vesting period of the TGE. This controlled release schedule ensures that the Ecosystem Fund can sustainably support the long-term growth and development of the PIP World platform without causing undue inflationary pressure on the $PIP token price.

&nbsp;
""")
    
    tab1, tab2 = st.tabs(["Platform-Based Vesting", "Future Contract-Level Vesting"])
    
    with tab1:
            st.header("Platform-Based Vesting")
            st.write("""
                 In our pursuit of fostering longevity and aligning stakeholder incentives within our ecosystem, Pip World has chosen to implement platform-based vesting and cliff mechanisms for our token distribution schedule. This strategic approach allows us to distribute tokens to various recipients securely, efficiently, and in harmony with our stakeholders' and ecosystems needs. 
                 &nbsp;
                 """)
            st.write()
            with st.expander("Our Approach"):
                st.write("""
                         - **Automated Token Unlocks:** We aim to enable the progressive unlocking of tokens to recipients over the vesting period. This can be configured to release tokens on a schedule as granular as weekly, hourly, or even minute-by-minute, ensuring a steady and controlled distribution that aligns with the Pip World’s growth and milestones.
- **Cliff Date Setting:** The inclusion of cliff dates in our vesting schedules introduces a lock-up period before vesting commences. This feature is instrumental in ensuring that recipients are committed to the long-term success of the project before receiving their tokens.
- **Transparent Payment Processing:** Transparency is a cornerstone of our approach. All vesting transactions are conducted on-chain, allowing stakeholders to monitor the vesting schedule and token emissions through Blockchain Explorers. This openness fosters trust and accountability within our community and aligns with our Trust Model.
- **On- and Off-Chain:** In addition to our on-chain vesting controls, Pip World has established vesting rules that are fixed and regulated within legal documents prior to our TGE, considered 'off-chain'. This dual-layered approach ensures a comprehensive governance framework that aligns with both regulatory standards and our ecosystem's integrity.
                         """)
    
    with tab2:
        st.header("Future Contract-Level Vesting")
        st.write("""
                 While currently leveraging platform-based solutions for their efficiency and adaptability, Pip World remains open to exploring contract-level vesting in the future. This flexibility ensures that as our ecosystem evolves and new needs emerge, we can adapt our strategies to maintain alignment with our core principles of security, transparency, and stakeholder alignment.

By choosing platform-based vesting, Pip World positions itself at the forefront of innovative token distribution methodologies, setting a standard for security, efficiency, and stakeholder engagement in the digital asset space.
                 """)
    
    #st.pyplot(create_chart(token_prices, "Token Price Over Time", "Price ($)"))

elif app_mode == "Deflationary Mechanisms":
    st.title("Deflationary Mechanisms")
    st.write("""
             
             Pip World is implementing several deflationary mechanisms to sustain and enhance the value of $PIP token within its ecosystem. These strategies leverage robust economic principles to ensure the circulating supply of tokens accurately reflects market demand. Following the launch, PIP tokens will maintain a fixed supply cap of 500 million tokens, enforced by the PIP Token smart contract. 

Governance may introduce an inflation rate up to 1.5% annually, contingent on ecosystem sustainability needs. This rate, along with the allocation of new tokens, will be determined by governance, with the smart contract enforcing a 1.5% cap. 

Default inflation is set at 0% unless altered through governance decisions.

In our strategy to maintain the PIP token's stability, we employ a balanced approach of carefully controlled inflation and a burn mechanism. This strategy is designed to manage supply and demand effectively, ensuring the PIP token remains a valuable asset within our ecosystem. By meticulously regulating the token supply—increasing it modestly when beneficial for growth and decreasing it to enhance scarcity—we aim to achieve a stable economic environment conducive to the long-term success of the PIP token.

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
