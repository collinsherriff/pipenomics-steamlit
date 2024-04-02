# Correcting the code for the token release chart with specified distributions and timelines
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Constants and setup
max_supply = 500e6  # 500 million tokens
total_months = 60
categories = ['Strategic', 'Seed', 'KOL', 'IEO', 'Ecosystem', 'Team', 'Reserve', 'Advisors', 'Community', 'Liquidity']
percentages = np.array([8, 15, 1, 10, 15, 10, 19, 3, 9, 10]) / 100  # Allocation percentages
initial_release_percents = np.array([5, 7, 20, 20, 0, 0, 0, 0, 0, 100]) / 100
linear_start = np.array([10, 10, 4, 1, 1, 13, 1, 10, 1, 1])  # Linear release start month
linear_end = np.array([36, 36, 12, 12, 60, 48, 60, 48, 60, 0])  # Linear release end month

# Monthly token release calculation
monthly_release = np.zeros((len(categories), total_months))

for i, cat in enumerate(categories):
    category_supply = max_supply * percentages[i]
    initial_release_tokens = category_supply * initial_release_percents[i]
    
    # Add initial release
    if initial_release_percents[i] > 0:
        monthly_release[i, 0] += initial_release_tokens
    
    # Calculate linear release tokens
    if linear_start[i] <= linear_end[i]:
        linear_months = linear_end[i] - linear_start[i] + 1
        monthly_tokens = (category_supply - initial_release_tokens) / linear_months
        for month in range(linear_start[i]-1, linear_end[i]):
            monthly_release[i, month] = monthly_tokens

# Plot
plt.figure(figsize=(10, 6))
for i in range(len(categories)):
    plt.plot(np.cumsum(monthly_release[i]), label=categories[i])

plt.title('Token Release Schedule Over 60 Months')
plt.xlabel('Months')
plt.ylabel('Cumulative Tokens Released')
plt.legend()
plt.show()
