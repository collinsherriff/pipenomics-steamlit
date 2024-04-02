import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go


# import yaml
# from yaml.loader import SafeLoader
# with open('../auth.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)
    
    
# authenticator = Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# name, authentication_status, username = authenticator.login('Login', 'main')

def creds_entered():
    if st.session_state['user'].strip() == 'admin' and st.session_state['password'].strip() == 'admin':
        st.session_state['authenticated'] = True
    
    else:
        st.session_state['authenticated'] = False
        if not st.session_state['password']:
            st.warning("Please Enter Password")
        elif not st.session_state['user']:
            st.warning("Please Enter Username")
        else:
            st.error("Invalid credentials. :face_with_raised_eyebrow: Please try again.")

def authenticate_user():
    if 'authenticated' not in st.session_state:
        st.text_input(label="Username: ", value="", key="user", on_change=creds_entered)
        st.text_input(label="Password: ", value="", key="password", type="password", on_change=creds_entered)
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else: 
            st.text_input(label="Username: ", value="", key="user", on_change=creds_entered)
            st.text_input(label="Password: ", value="", key="password", type="password", on_change=creds_entered)
            return False

if authenticate_user():
    # st.title("Login to PiP World")
    # username = st.text_input("Username")
    # password = st.text_input("Password", type='password')
    # if st.button("Login"):
    #     if username == "pipworld" and password == "pipworld":
    #         st.success("Logged in as: {}".format(username))
    #         return True
    #     else:
    #         st.error("Invalid credentials. Please try again.")
    #         return False
    # return False

    st.set_page_config(layout="wide", page_title="$PiP Tokenomics", page_icon=":coin:")
    st.sidebar.image("pip.png", use_column_width=True)
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Select tokenomics section",
                                    ["Token Supply & Distribution", "Vesting & Release Schedule", "Monetary & Fiscal Policies", "Staking & Liquidity", "Investment KPIs"])
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    st.sidebar.markdown("""
    ## PiP World
    For further information on PiP World, follow the link here to explore our Whitepaper.
    """)

    # st.sidebar.slider("Select Month", min_value=0, max_value=48, value=0, step=1)
    # st.sidebar.slider("Select Market Cap", min_value=1, max_value=500, value=1, step=1, format='%dM')

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
        st.title("$PIP Token Supply and Distribution")
        
        st.write("""
    &nbsp;

    The $PIP token lies at the heart of the PIP World ecosystem, carefully designed to incentivise participation, reward learning, and foster a vibrant, self-sustaining economy. Our tokenomics model has been meticulously crafted to ensure the long-term sustainability of the platform, align the interests of all stakeholders, and support the growth and adoption of PIP World.

    &nbsp;
                    """)
        

        col1, col2 = st.columns(2)
        with col2:
                labels = ['Strategic Round', 'Seed Round', 'KOL','IEO', 'Team', 'Advisors', 
                        'Community', 'Liquidity', 'Ecosystem', 'Reserve']
                sizes = [8, 15, 1, 10, 10, 3, 9, 10, 15, 19]

                colors = ['#ff9999','#66b3ff','#987345','#99ff99','#ffcc99', '#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4', '#fffac8']


                fig = go.Figure(data=[go.Pie(labels=labels, 
                                            values=sizes, 
                                            hole=.3, 
                                            marker_colors=colors, 
                                            pull=[0.1 if size == max(sizes) else 0 for size in sizes], 
                                            textinfo='label+percent', 
                                            hoverinfo='label+percent')])

                
                fig.update_layout(height=700, width=800)  

                st.plotly_chart(fig, use_container_width=False)  

        with col1:
            st.write("""
    &nbsp;

    | Catagory           | Allocation | Tokens        | Price   | USD Value    | Discount | Fully Diluted Valuation |
    |-----------------|------------|---------------|---------|--------------|----------|-------------------------|
    | Strategic Round | 8%         | 40,000,000    | $0.12   | $4,800,000   | 52%      | $60,000,000             |
    | Seed Round      | 15%        | 75,000,000    | $0.16   | $12,000,000  | 36%      | $80,000,000             |
    | KOL Round       | 1%         | 5,000,000     | $0.10   | $500,000     | 60%      | $50,000,000             |
    | IEO Round       | 10%        | 50,000,000    | $0.25   | $12,500,000  | 0%       | $125,000,000            |
    | Team & Advisors | 13%        | 65,000,000    | -       | -            | -        | -                       |
    | Ecosystem Fund  | 15%        | 75,000,000    | -       | -            | -        | -                       |
    | Liquidity Provision | 10%    | 50,000,000    | -       | -            | -        | -                       |
    | Community       | 9%         | 45,000,000    | -       | -            | -        | -                       |
    | Reserve         | 19%        | 95,000,000    | -       | -            | -        | -                       |
    | **Total**       | **100%**   | **500,000,000** | -     | **$29,800,000** | -     | -                     |


    &nbsp;
    """)
            
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
        st.write()
    
        st.divider()
        tab1, tab2 = st.tabs(["Token Sale Roadmap", "Token Supply Dynamics"])
        
        with tab1:
            col1, space, col2 = st.columns([1, 0.1, 1])
            with col2:
                    st.write("""
                    ## 

            &nbsp;
            
            | Round | Dates | Token Price | Discount | Fundraising Goal |
            | --- | --- | --- | --- | --- |
            | Strategic | Q2 2024 | $0.12 | 52% | $4.8M |
            | Seed | Q2 2024 | $0.16 | 36% | $12M |
            | KOL | Q2 2024 | $0.10 | 60% | $0.5M |
            | Public | Q2 2024 | $0.25 | 0% | $12.5M |

            &nbsp;
                    """)
                
            with col1:
                    st.header("Token Sale Roadmap")
                    st.write("""
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
            st.divider()
            st.markdown('_Source: Sockin, M., & Xiong, W. (2023). A Model of Cryptocurrencies. Management Science, 69(11), 6684–6707. © 2023 INFORMS. (p. 6698)._')
            
    elif app_mode == "Vesting & Release Schedule":
        st.title("Vesting & Release Schedule")
        
        col1, space, col2 = st.columns([1,0.1,1])
        with col1:
            st.write("""
    &nbsp;

    At PiP World, we believe in aligning the interests of all stakeholders with the long-term vision and sustainability of our ecosystem. Our vesting schedule is meticulously designed to foster a deep commitment to the project's success, ensuring that contributors, team members, and advisors are invested in the growth and development of PiP World over time. 

    By implementing strategic lock-up periods and gradual token releases, we aim to mitigate market volatility and reward enduring participation. This approach not only stabilises the token economy but also embodies our ethos of community-driven growth, transparency, and mutual success. Through this, we lay the foundation for a robust and thriving ecosystem, where each stakeholder's contribution is recognized and valued in our journey towards a decentralized future.

    &nbsp;
    """)
            # st.divider()
            st.write("""
    To ensure the long-term alignment of interests and commitment to the project, the team and advisor tokens are subject to a 4-year vesting schedule with a 1-year cliff and 9-month cliff respectively. This means that:

    - No team or advisor tokens will be released during the 9 to 12 months following the token generation event (TGE).
    - After the cliff, 25% of the team and advisor tokens will be released.
    - The remaining team and advisor tokens will be released in equal monthly instalments over the following years.

    &nbsp;
                    """)
        st.write("""
    This vesting schedule ensures that the team and advisors have a strong incentive to drive the project's success over an extended period and provides transparency and predictability for the $PIP token supply.

    In addition to the team and advisor vesting, the Ecosystem Fund tokens will be released gradually over a 5-year period following the vesting period of the TGE. This controlled release schedule ensures that the Ecosystem Fund can sustainably support the long-term growth and development of the PIP World platform without causing undue inflationary pressure on the $PIP token price.

    """)
        with col2:
            st.write("""
                    
                &nbsp;
                    
    | Gatagory          | Allocation | USD Value   | Initial Market Cap | Cliff (Months) | Lock (Months) |
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

                """)
            
        st.divider()
        
        st.header("Token Release and Vesting Schedule")
        
        st.write("Our token release schedule, spanning 60 months, is meticulously designed to support the ecosystems's long-term sustainability and health. The graph illustrates the phased release of tokens in categories like Strategic, Seed, IEO, and more, underlining our commitment to gradual market introduction. This strategy, integral to our vesting approach, ensures stakeholders are aligned with PiP World's.")

        col1, space, col2 = st.columns([1,0.1,1])
        with col1:
            def calculate_token_release(max_supply=500e6, months=60):
                    allocations = {
                        'Strategic': 8,
                        'Seed': 15,
                        'KOL': 1,
                        'IEO': 10,
                        'Ecosystem': 15,
                        'Team': 10,
                        'Reserve': 19,
                        'Advisors': 3,
                        'Community': 9,
                        'Liquidity': 10
                    }
                    
                    df = pd.DataFrame(index=range(1, months+1))
                    
                    for category, percent in allocations.items():
                        df[category] = 0  
                        

                    df.loc[1, 'Liquidity'] = max_supply * 0.10  
                    

                    def linear_release(start_month, end_month, percentage, category):
                        monthly_amount = (max_supply * (percentage / 100)) / (end_month - start_month + 1)
                        df.loc[start_month:end_month, category] = monthly_amount
                        
                    linear_release(1, 60, 15, 'Ecosystem')
                    linear_release(13, 48, 10, 'Team')
                    linear_release(1, 60, 19, 'Reserve')
                    linear_release(10, 48, 3, 'Advisors')
                    linear_release(1, 60, 9, 'Community')
                    

                    df.loc[1, 'Strategic'] += max_supply * 0.08 * 0.05
                    linear_release(10, 36, 8*0.95, 'Strategic')  
                    
                    df.loc[1, 'Seed'] += max_supply * 0.15 * 0.07
                    linear_release(10, 36, 15*0.93, 'Seed')  
                    
                    df.loc[1, 'KOL'] += max_supply * 0.01 * 0.20
                    linear_release(4, 12, 1*0.80, 'KOL')  
                    
                    df.loc[1, 'IEO'] += max_supply * 0.10 * 0.20
                    linear_release(1, 12, 10*0.80, 'IEO') 
                    
                    return df.cumsum()


            df_release = calculate_token_release()


            def plot_token_release(df_release):
                    fig = go.Figure()
                    for category in df_release.columns:
                        fig.add_trace(go.Scatter(x=df_release.index, y=df_release[category], mode='lines', name=category, fill='tozeroy'))
                        
                    fig.update_layout(title='Cumulative Token Release Schedule Over 60 Months', xaxis_title='Month', yaxis_title='Number of Tokens', legend_title='Category', showlegend=True, height=600, width=800,)
                    return fig


            st.plotly_chart(plot_token_release(df_release), use_container_width=True)
        
        with col2:
            
            data = {
                "Category": ["Strategic", "Seed", "KOL", "IEO", "Ecosystem", "Team", "Reserve", "Advisors", "Community", "Liquidity"],
                "Token Amount": [40000000, 75000000, 5000000, 50000000, 75000000, 50000000, 95000000, 15000000, 45000000, 50000000],
                "Initial Release": [0.05, 0.07, 0.2, 0.2, 0, 0, 0, 0, 0, 1],
                "Monthly Release": [0.035185185, 0.034444444, 0.088888889, 0.066666667, 0.016666667, 0.027777778, 0.016666667, 0.025641026, 0.016666667, 0],
                "Start Month": [10, 10, 4, 1, 1, 13, 1, 10, 1, 0],
                "End Month": [36, 36, 12, 12, 60, 48, 60, 48, 60, 0]
            }


            df_data = pd.DataFrame(data)

            total_months = 60

            df_release = pd.DataFrame(0, index=np.arange(1, total_months+1), columns=df_data['Category'])


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

                fig.add_trace(go.Scatter(x=df_release.index[1:], y=df_release[category][1:], mode='lines', name=category, fill='tozeroy'))


            fig.update_layout(
                title='Fixed Token Release Schedule Per Month Over 60 Months (Default Excluding TGE)',
                xaxis_title='Month',
                yaxis_title='Tokens Released Per Month',
                legend_title='Category',
                height=600, width=800,
            )


            st.plotly_chart(fig, use_container_width=True)    

        st.divider()
        col1, space, col2 = st.columns([1,0.1,1])
        with col1:
            st.header("Private Round Vesting")
            st.write("""
                    For the private rounds, including the Strategic, Seed and KOL Rounds, we've designed a vesting schedule that balances the need for early support with the importance of long-term commitment. These rounds are pivotal, as they involve participants who provide not just capital but also strategic value and promotional support during the crucial early stages of the project.
                    &nbsp;

    - **Strategic Round**: 9-month cliff and 36-month lock secure long-term investor alignment for early stability.
    - **Seed Round**: Similar to Strategic, a 9-month cliff and 36-month lock guard against premature sell-offs.
    - **KOL Round**: A 3-month cliff and 12-month lock incentivise early promotion and sustained support during key growth phases.
                    """)
                
        with col2:
            st.header("Public Vesting")
            st.write("""
                    Public rounds' vesting schedules are crafted to ensure widespread participation while safeguarding the ecosystem against volatility. These rounds aim to democratize access to the project, inviting community members and public investors to contribute to and benefit from the ecosystem's growth.
                    
                    &nbsp;
                    """)
        
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

    elif app_mode == "Monetary & Fiscal Policies":
        st.title("Monetary & Fiscal Policies")
        st.write("""
                &nbsp;

    In navigating the complex terrain of digital currency economics, PiP World employs a nuanced blend of monetary and fiscal policies designed to maintain a healthy token supply, control inflation, and stimulate demand for the $PiP token. These policies are meticulously crafted to ensure the long-term sustainability and growth of the ecosystem.
                """)
        col1, space, col2 = st.columns([1,0.1,1])
        with col1:
            st.write("""
            
    #### Managing Token Supply:

    For $PiP, we implements several key mechanisms to manage the token supply effectively:

    - **Token Burns:** A deflationary measure where a portion of the token supply is periodically removed from circulation. This mechanism is employed to counteract inflationary pressures and enhance the token's scarcity and value over time. The criteria and schedule for these burns are transparently outlined, aligning with significant ecosystem milestones or transaction volume thresholds.

    - **Vesting Schedules:** To align the interests of team members, advisors, and early investors with the long-term success of the ecosystem, $PiP World incorporates vesting schedules into its tokenomics. These schedules dictate the gradual release of tokens over a specified period, preventing market flooding and ensuring a steady, controlled increase in token circulation.

    - **Staking Rewards:** Encouraging token holders to stake their tokens not only secures the network but also reduces the velocity of money within the ecosystem. Staked tokens are temporarily removed from circulation, which can have a deflationary effect by decreasing the available supply, thus potentially increasing the token's price.
                """)
        with col2:  
            st.write("""
    #### Inflation Control and Demand Stimulation:

    To mitigate the risk of inflation and stimulate demand for the $PiP token, PiP World adopts the following policies:


    - **Inflation Rate Management:** While the $PiP token has a capped supply, mechanisms for releasing tokens into the ecosystem, such as rewards for staking or participation in governance, are designed with a cap to ensure they do not dilute the token's value. The governance model allows for adjustments to these mechanisms, ensuring flexibility to respond to changing economic conditions.
    - **Demand Stimulation Initiatives:** Beyond the utility provided within the ecosystem, PiP World engages in strategies to stimulate demand for the $PiP token. These include partnerships that expand the token's use cases, marketing campaigns to raise awareness and adoption, and liquidity provisioning on exchanges to facilitate easy trading.
                """)
        st.write("""
    &nbsp;

    By integrating these monetary and fiscal policies, PiP World aims to maintain a balanced and thriving economy. Managing the token supply through burns, vesting, and staking, alongside strategic measures to control inflation and stimulate demand, positions the $PiP token for sustained value and utility within the ecosystem.
                
                """)
        st.divider()
        col1, space, col2 = st.columns([1,0.1,1])
        with col1:
            st.header("Burn Mechanism")
            st.write("""
    The decision to remove tokens from circulation will be made transparently, considering ecosystem health and token economics. Burns will occur systematically, tied to:

    - transaction volume
    - significant milestones
    - governance decisions

    A detailed schedule and criteria will be outlined, with burns executed via smart contract functions.
                """)
        with col2:
            st.header("Unsold Token Burn Strategy")
            st.write("""
    Following the initial token offering, Pip World will burn all unsold tokens. This approach guarantees that the supply of tokens in circulation directly corresponds to the initial demand, effectively aligning supply with demand from launch. By eliminating the excess supply, this measure aims to protect the token's value from potential market dilution.

    | Burn Contract | 0x..123 |
    | --- | --- |
    | Burn Address | 0x…123 |
    | Functionality | Manages burns, transaction validations, and enforces supply cap and inflation rules. |

    &nbsp;
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


            st.plotly_chart(fig)
        
        st.write("""
    ### Predicting Price Drop from Supply Shock

    The relationship between supply shock and the subsequent price drop is deeply rooted in tokenomics principles. Through extensive analysis of various projects experiencing significant changes in their circulating supply, a strong correlation has been observed between the percentage of supply shock and the resultant price drops. This analysis underpins the concept that sudden increases in token supply can lead to substantial decreases in token price, due to market dynamics of supply and demand.

    The precise impact of supply shock on price can vary based on a multitude of factors, including the project's market cap, liquidity, and investor sentiment. However, historical data from multiple projects consistently demonstrates a tangible link between these supply changes and market reactions. This relationship highlights the importance of carefully planned token distribution schedules to mitigate potential adverse effects on market price.

    Understanding this correlation is pivotal for Pip World ecosystem teams and investors, as it underscores the potential market implications of token unlock events and other supply-related activities. It encourages a strategic approach to token releases, ensuring they align with long-term project goals and market stability.

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


            st.plotly_chart(fig)

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
        

    elif app_mode == "Investment KPIs":

        st.title(":rainbow[Investment KPIs]")

        tab1, tab2, tab3, tab4 = st.tabs(["$PiP Token Price", "Token Emmissions", "Investor Rounds","Tokenomics Tables"])
        
        with tab1:
            st.write("## $PiP Token Price")
            
            col1, spacer, col2 = st.columns([1, 0.1, 1])


            with col1:
                st.write("""
                        
                        To make an informed decision about the optimal timing for investing in $PiP tokens, consider the detailed metrics outlined below. These metrics are crucial in assessing the viability and potential profitability of such investments within specified monthly periods. By carefully analyzing the proposed market capitalization figures and trends over these ranges, you can identify the most favorable moments to allocate resources to PiP tokens. 
                        
                        This strategic approach not only maximizes your investment potential but also minimizes risk by relying on data-driven insights and projections. Keep in mind that understanding the dynamics of market capitalization, including factors that influence fluctuations and growth prospects, is essential in making educated investment choices.
                        
                        *Select the desired range of months, as well as the market cap to view the potential corresponding token price and circulating supply figures, enabling you to make well-informed investment decisions*:
                        &nbsp;
                        """)

            with col2:
        
        
            # NEW VERSION WITH 2 SLIDERS
                max_supply = 500e6  
                total_months = 60  
            
                # User Inputs
                market_cap_million = st.slider("Market Cap ($M)", min_value=1, max_value=2000, value=50, step=1, format='%dM')
                selected_months = st.slider("Select Month Range", min_value=1, max_value=total_months, value=(1, total_months), step=1)
                
                with st.spinner("Modelling..."):
                    time.sleep(2)
                st.success("Complete") 

            st.divider()

            months = np.arange(selected_months[0], selected_months[1] + 1)  
            circulating_supply = max_supply * (np.sqrt(months) / np.sqrt(total_months))  


            initial_market_cap = market_cap_million * 1e6
            growth_rate = 0.06  
            market_cap = initial_market_cap * (1 + growth_rate) ** (months - selected_months[0]) 


            token_price = market_cap / circulating_supply


            fig = go.Figure()
            fig.add_trace(go.Scatter(x=months, y=token_price, mode='lines+markers', name='Token Price', line=dict(color='#5e28d5'), stackgroup='one'))
            fig.update_layout(title="Token Price vs Circulating Supply (Selected Range)", xaxis_title="Months", yaxis_title="Token Price ($)",
                            yaxis=dict(tickformat=".2f"), showlegend=False, height=550, width=780)

            token_price_start = token_price[0]
            token_price_end = token_price[-1]
            supply_start = circulating_supply[0] / 1e6  
            supply_end = circulating_supply[-1] / 1e6
            expected_price_growth = (token_price_end - token_price_start) * 100
            
            # col1, col2 = st.columns(2)
            # col1.metric("Token Price (Start of Range)", f"${token_price_start:.2f}")
            # col2.metric("Token Price (End of Range)", f"${token_price_end:.2f}")

            # col3, col4 = st.columns(2)
            # col3.metric("Supply at Start of Range", f"{supply_start:.0f}M Tokens")
            # col4.metric("Supply at End of Range", f"{supply_end:.0f}M Tokens")
        

            block_style = """
            <style>
            .metric-block {
                border: 0.7px solid #f5f5f5;  /* Off white border */
                border-radius: 8px !important;  /* Rounded corners */
                padding: 10px;
                text-align: center;
                margin: 10px;
                background-color: #131221;  /* Off white background */
            }
            </style>
            """


            st.markdown(block_style, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <div class="metric-block">
                    <h3>Token Price (Start of Range)</h3>
                    <h2>${token_price_start:.2f}</h3>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="metric-block">
                    <h3>Token Price (End of Range)</h3>
                    <h2>${token_price_end:.2f}</h2>
                </div>
                """, unsafe_allow_html=True)

            col3, col4 = st.columns(2)
            with col3:
                st.markdown(f"""
                <div class="metric-block">
                    <h3>Supply at Start of Range</h3>
                    <h2>{supply_start:.0f}M Tokens</h2>
                </div>
                """, unsafe_allow_html=True)

            with col4:
                st.markdown(f"""
                <div class="metric-block">
                    <h3>Supply at End of Range</h3>
                    <h2>{supply_end:.0f}M Tokens</h2>
                </div>
                """, unsafe_allow_html=True)

            st.write("&nbsp;")
            
            st.plotly_chart(fig, use_container_width=True)

            
            st.divider()
            
            col1, space, col2 = st.columns([1, 0.1, 1])
            with col1:
                st.header("Token Price Growth Over Selected Period")
            
            
                # NEW SECTION
                months2 = np.arange(selected_months[0], selected_months[1])
                token_prices2 = np.linspace(token_price_start, token_price_end, len(months2))


                price_change_percent = ((token_price_end - token_price_start) / token_price_start) * 100


                fig = go.Figure()
                fig.add_trace(go.Scatter(x=months2, y=token_prices2, mode='lines+markers', name='Token Price Growth', line=dict(color='#5e28d5')))
                fig.update_layout(title="Token Price Growth Over Selected Period", xaxis_title="Months", yaxis_title="Token Price ($)")


                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.header("Market Cap Growth Over Selected Period")
                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(x=months, y=market_cap, mode='lines+markers', name='Market Cap', line=dict(color='#5e28d5')))
                fig2.update_layout(title="Market Cap Growth Over Selected Period", xaxis_title="Months", yaxis_title="Market Cap ($)",
                                yaxis=dict(tickformat=",.0f"))
                
                st.plotly_chart(fig2, use_container_width=True)
                
                with st.expander("Market Cap Growth Rate"):
                    st.write("""
This graph presents a projected market cap growth based on a conservative growth rate of 0.06, as determined by market research. While we've assumed a steady increase over time for this estimate, actual market cap fluctuations could lead to different token pricing outcomes.
                    """)
                
                
                # st.header("Market Cap Growth Over Selected Period")
                # fig2 = go.Figure()
                # fig2.add_trace(go.Scatter(x=months, y=market_cap, mode='lines+markers', name='Market Cap', line=dict(color='#5e28d5')))
                # fig2.update_layout(title="Market Cap Growth Over Selected Period", xaxis_title="Months", yaxis_title="Market Cap ($)",
                #                 yaxis=dict(tickformat=".0fM", tickvals=[i * 1e6 for i in range(0, int(max(market_cap) / 1e6) + 2)]))

                # st.plotly_chart(fig2, use_container_width=True)

            
            col1, space, col2 = st.columns([1, 0.1, 1])
            with col2:
                st.write("")
                # st.warning(' Assumption of 0.06 growth rate in MCAP selected', icon="ℹ️")

            with col1:
                
                # st.metric(label="Price Change", value=price_change_percent, delta="1 °F")
                
                color = "green" if price_change_percent >= 0 else "red"
                st.markdown(f"<h1 style='color:{color};'>{price_change_percent:.2f}%</h1>", unsafe_allow_html=True)
                st.caption("Price Change")
        
        with tab2:
            st.header("Token Emissions")
            st.write("""
                
    The graph below outlines the phased distribution strategy for $PiP tokens, aligning with the ecosystem's long-term vision for growth and sustainability. Across a span of 60 months, this visualszation demonstrates the deliberate and strategic release of tokens into the ecosystem, highlighting categories such as Strategic, Seed, KOL, IEO, Ecosystem, Team, Reserve, Advisors, Community, and Liquidity.

    Each line represents a different category emission, not showcasing the initial lump-sum releases (of Liquidity and initial percentages for Strategic, Seed, KOL, and IEO rounds) followed by a linear release model tailored to each category's specific role within the $PiP ecosystem. This ensures a balanced injection of tokens, facilitating ecosystem development, rewarding early backers, and fostering a vibrant community engagement while maintaining market stability.

    This release strategy underscores $PiP's commitment to transparency and a steady value proposition for token holders. By moderating the supply influx and aligning token releases with ecosystem milestones and growth phases, PiP World ensures a sustainable economic model that rewards long-term participants and supports the overall health and expansion of the ecosystem.         
            

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
                "Category": ["Strategic", "Seed", "KOL", "IEO", "Ecosystem", "Team", "Reserve", "Advisors", "Community", "Liquidity"],
                "Token Amount": [40000000, 75000000, 5000000, 50000000, 75000000, 50000000, 95000000, 15000000, 45000000, 50000000],
                "Initial Release": [0.05, 0.07, 0.2, 0.2, 0, 0, 0, 0, 0, 1],
                "Monthly Release": [0.035185185, 0.034444444, 0.088888889, 0.066666667, 0.016666667, 0.027777778, 0.016666667, 0.025641026, 0.016666667, 0],
                "Start Month": [10, 10, 4, 1, 1, 13, 1, 10, 1, 0],
                "End Month": [36, 36, 12, 12, 60, 48, 60, 48, 60, 0]
            }


            df_data = pd.DataFrame(data)

            total_months = 60

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
                title='Fixed Token Release Schedule Per Month Over 60 Months (Default Excluding TGE)',
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
    The graph presents the cumulative token release schedule for $PiP over a 60-month horizon, detailing the progressive distribution of tokens across various categories. 
                        
                        """)


                data = {
                    "Category": ["Strategic", "Seed", "KOL", "IEO", "Ecosystem", "Team", "Reserve", "Advisors", "Community", "Liquidity"],
                    "Token Amount": [40000000, 75000000, 5000000, 50000000, 75000000, 50000000, 95000000, 15000000, 45000000, 50000000],
                    "Initial Release": [0.05, 0.07, 0.2, 0.2, 0, 0, 0, 0, 0, 1],
                    "Monthly Release": [0.035185185, 0.034444444, 0.088888889, 0.066666667, 0.016666667, 0.027777778, 0.016666667, 0.025641026, 0.016666667, 0],
                    "Start Month": [10, 10, 4, 1, 1, 13, 1, 10, 1, 0],
                    "End Month": [36, 36, 12, 12, 60, 48, 60, 48, 60, 0]
                }


                df_data = pd.DataFrame(data)


                total_months = 60


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
                    title='Cumulative Token Release Schedule Over 60 Months',
                    xaxis_title='Month',
                    yaxis_title='Cumulative Tokens Released',
                    legend_title='Category',
                    height=550, width=800
                )


                st.plotly_chart(fig, use_container_width=True)


                st.write("""
                        
                        &nbsp;
                        
                        """)

                with st.expander("View Data"):
                    st.write(df_release)
                    

            with col2:
                st.header("Token Supply Growth Per Catagory")
                # st.plotly_chart(fig2, use_container_width=True)
                st.write("""The graph depicts the rollout of $PiP tokens over 60 months, highlighting the escalating sum of tokens dispensed across distinct allocation categories.""")


                def calculate_token_release(max_supply=500e6, months=60):

                    allocations = {
                        'Strategic': 8,
                        'Seed': 15,
                        'KOL': 1,
                        'IEO': 10,
                        'Ecosystem': 15,
                        'Team': 10,
                        'Reserve': 19,
                        'Advisors': 3,
                        'Community': 9,
                        'Liquidity': 10
                    }
                    

                    df = pd.DataFrame(index=range(1, months+1))
                    
                    for category, percent in allocations.items():
                        df[category] = 0  
                        

                    df.loc[1, 'Liquidity'] = max_supply * 0.10  
                    

                    def linear_release(start_month, end_month, percentage, category):
                        monthly_amount = (max_supply * (percentage / 100)) / (end_month - start_month + 1)
                        df.loc[start_month:end_month, category] = monthly_amount
                        

                    linear_release(1, 60, 15, 'Ecosystem')
                    linear_release(13, 48, 10, 'Team')
                    linear_release(1, 60, 19, 'Reserve')
                    linear_release(10, 48, 3, 'Advisors')
                    linear_release(1, 60, 9, 'Community')
                    

                    df.loc[1, 'Strategic'] += max_supply * 0.08 * 0.05
                    linear_release(10, 36, 8*0.95, 'Strategic')  
                    
                    df.loc[1, 'Seed'] += max_supply * 0.15 * 0.07
                    linear_release(10, 36, 15*0.93, 'Seed')  
                    
                    df.loc[1, 'KOL'] += max_supply * 0.01 * 0.20
                    linear_release(4, 12, 1*0.80, 'KOL') 
                    
                    df.loc[1, 'IEO'] += max_supply * 0.10 * 0.20
                    linear_release(1, 12, 10*0.80, 'IEO')  
                    
                    return df.cumsum()


                df_release = calculate_token_release()


                def plot_token_release(df_release):
                    fig = go.Figure()
                    for category in df_release.columns:
                        fig.add_trace(go.Scatter(x=df_release.index, y=df_release[category], mode='lines', name=category))
                        
                    fig.update_layout(title='Token Release Schedule Over 60 Months', xaxis_title='Month', yaxis_title='Number of Tokens', legend_title='Category', height=550, width=800)
                    return fig

                st.plotly_chart(plot_token_release(df_release), use_container_width=True)

                # st.expander("View Data").write(df_release)
        
        with tab3:
            st.header("Funding Overview by Round")
            st.write("""
                    
                The chart presents an overview of the planned fundraising structure for PiP across various rounds. It outlines the projected amounts raised in each round, ranging from strategic partnerships to public offerings. This breakdown demonstrates the approach to securing financial support from a mix of stakeholders, including early backers, key opinion leaders, and the broader community. The distribution of funding sources establishes a solid foundation for $PiP's growth and reflects a strategic plan to engage a wide range of contributors in the ecosystem's journey.
                
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
                rounds = ['KOL Round', 'Strategic Round', 'Seed Round', 'IEO Round']
                amounts = [500000, 4800000, 12000000, 12500000]
                sizes = [20, 40, 60, 80]  


                fig = go.Figure(data=[
                    go.Scatter(x=rounds, y=amounts, mode='markers', marker=dict(size=sizes, color=['#5e28d5', '#5e28d5', '#5e28d5', '#5e28d5']))
                ])

                fig.update_layout(title='Amount Raised at Each Funding Round',
                                xaxis_title='Round',
                                yaxis_title='Amount ($)',
                                height=550, width=750)

                st.plotly_chart(fig, use_container_width=True)
                

                table1 = {
                    "Round": ["KOL Round", "Strategic Round", "Seed Round", "IEO Round"],
                    "Amount Raised": ["$500,000", "$4,800,000", "$12,000,000", "$12,500,000"]
                }   

                df_table1 = pd.DataFrame(table1)
                df_table1.index = ["1", "2", "3", "4"]
                
                st.table(df_table1)
                    
            with col2:
                st.write("""
                    """)    
                
                data = {
                    "Round": ["KOL Round", "Strategic Round", "Seed Round", "IEO Round"],
                    "Price ($)": [0.10, 0.12, 0.16, 0.25]
                }
                df = pd.DataFrame(data)


                fig = go.Figure(data=go.Scatter(x=df["Round"], y=df["Price ($)"], mode='lines+markers',line=dict(color='#5e28d5')))

                fig.update_layout(title='Price of $PiP at Each Funding Round',
                                xaxis_title='Round',
                                yaxis_title='Price ($)',
                                height=530, width=750)


                st.plotly_chart(fig, use_container_width=True)
            
        
                df_table1 = pd.DataFrame(data)
                df_table1.index = ["1", "2", "3", "4"]
                
                st.table(df_table1)
                
            
            
        with tab4:
            st.header("Tokenomics Allocation")
            st.write("""
                    
    &nbsp;
                    
    | Category    |  Percentage of Total Supply | Price   | Token Amount | Token Price at Public Round | Sale in $    | Cliff (m) | Lock (m) | Unlock on TGE % | Tokens Unlock on TGE | Unlocked in $ | Unlock % pm | Token Unlock pm | Unlock pm $TGE |
    |-------------|-------------------|---------|--------------|-----------------------------|--------------|-----------|----------|-----------------|----------------------|---------------|-------------|-----------------|----------------|
    | Ecosystem   | 15.00%            | -       | 75,000,000   | 18,750,000                   | -            | 0         | 60       | 0.00%           | 0                    | $0            | 1.69%       | 1,271,186       | $317,797       |
    | Team        | 10.00%            | -       | 50,000,000   | 12,500,000                   | -            | 12        | 48       | 0.00%           | 0                    | $0            | 2.08%       | 1,041,667       | $260,417       |
    | Reserve     | 19.00%            | -       | 95,000,000   | 23,750,000                   | -            | 0         | 60       | 0.00%           | 0                    | $0            | 1.67%       | 1,583,333       | $395,833       |
    | Advisors    | 3.00%             | -       | 15,000,000   | 3,750,000                    | -            | 9         | 48       | 0.00%           | 0                    | $0            | 2.08%       | 312,500         | $78,125        |
    | Community   | 9.00%             | -       | 45,000,000   | 11,250,000                   | -            | 0         | 60       | 0.00%           | 0                    | $0            | 1.69%       | 762,712         | $190,678       |
    | Strategic   | 8.00%             | $0.12   | 40,000,000   | 10,000,000                   | $4,800,000   | 9         | 36       | 5.00%           | 2,000,000            | $500,000      | 2.64%       | 1,055,556       | $263,889       |
    | Seed        | 15.00%            | $0.16   | 75,000,000   | 18,750,000                   | $12,000,000  | 9         | 36       | 7.00%           | 5,250,000            | $1,312,500    | 2.58%       | 1,937,500       | $484,375       |
    | KOL         | 1.00%             | $0.10   | 5,000,000    | 1,250,000                    | $500,000     | 3         | 12       | 20.00%          | 1,000,000            | $250,000      | 6.67%       | 333,333         | $83,333        |
    | IEO         | 10.00%            | $0.25   | 50,000,000   | 12,500,000                   | $12,500,000  | 0         | 12       | 20.00%          | 10,000,000           | $2,500,000    | 6.67%       | 3,333,333       | $833,333       |
    | Liquidity   | 10.00%            | -       | 50,000,000   | 12,500,000                   | -            | 0         | 0        | 100.00%         | 50,000,000           | $12,500,000   | 0.00%       | 0               | $0             |
    | **Total**   | **100.00%**       | -       | **500,000,000** | -                         | **$29,800,000** | -         | -        | **13.65%**      | **68,250,000**      | **$17,062,500** | **2.33%**   | **11,631,121**  | **$2,907,780** |

    &nbsp;

                """)
            
            # Data preparation
            source = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
            target = [10, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12]
            value = [40000000, 75000000, 5000000, 50000000, 75000000, 50000000, 95000000, 15000000, 45000000, 50000000, 50000000]
            label = ["Strategic", "Seed", "KOL", "IEO", "Ecosystem", "Team", "Reserve", "Advisors", "Community", "Liquidity", "TGE Unlocks", "Monthly Unlocks", "Circulation"]

            # Creating the Sankey diagram
            fig = go.Figure(data=[go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color='#050413', width=0.5),
                    label=label,
                    color='#050413'
                ),
                link=dict(
                    source=source,
                    target=target,
                    value=value
                ))])

            fig.update_layout(title_text='Detailed Token Release Schedule', font_size=15, height=800, width=800)

            # Displaying the Sankey diagram in Streamlit
            st.plotly_chart(fig, use_container_width=True)



        block_style = """
            <style>
            .metric-block {
                border: 0.7px solid #f5f5f5;  /* Off white border */
                border-radius: 8px !important;  /* Rounded corners */
                padding: 10px;
                text-align: center;
                margin: 10px;
                background-color: #131221;  /* Off white background */
            }
            </style>
            """
        st.sidebar.markdown(block_style, unsafe_allow_html=True)

        st.sidebar.markdown(f"""
                <div class="metric-block">
                    <h3>Selected MCAP</h3>
                    <h2>${market_cap_million:}M</h3>
                </div>
                """, unsafe_allow_html=True)
        
        st.sidebar.markdown(f"""
                <div class="metric-block">
                    <h3>Selected Month Range</h3>
                    <h2>{selected_months:}</h3>
                </div>
                """, unsafe_allow_html=True)
        
        
        
        
