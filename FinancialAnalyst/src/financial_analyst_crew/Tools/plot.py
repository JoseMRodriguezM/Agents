import matplotlib.pyplot as plt

# Define the data
profitability_ratios = [25.1, 14.1, 24.1, 10.3]
liquidity_ratios = [1.43, 1.23]
solvency_ratios = [0.63, 7.51]
efficiency_ratios = [0.83, 7.14]
growth_metrics = [35.1, 40.2]
valuation_metrics = [303.23, 13.43, 12.83]
cash_flow_metrics = [18.3, 14.5]

# Create a figure and axis object
fig, ax = plt.subplots(6, 2, figsize=(12, 18))

# Plot the data
ax[0, 0].bar(range(len(profitability_ratios)), profitability_ratios)
ax[0, 0].set_title('Profitability Ratios')
ax[0, 0].set_xticks(range(len(profitability_ratios)))
ax[0, 0].set_xticklabels(['Gross Margin Ratio', 'Operating Margin Ratio', 'Return on Equity (ROE)', 'Return on Assets (ROA)'])

ax[1, 0].bar(range(len(liquidity_ratios)), liquidity_ratios)
ax[1, 0].set_title('Liquidity Ratios')
ax[1, 0].set_xticks(range(len(liquidity_ratios)))
ax[1, 0].set_xticklabels(['Current Ratio', 'Quick Ratio'])

ax[2, 0].bar(range(len(solvency_ratios)), solvency_ratios)
ax[2, 0].set_title('Solvency Ratios')
ax[2, 0].set_xticks(range(len(solvency_ratios)))
ax[2, 0].set_xticklabels(['Debt-to-Equity Ratio', 'Interest Coverage Ratio'])

ax[3, 0].bar(range(len(efficiency_ratios)), efficiency_ratios)
ax[3, 0].set_title('Efficiency Ratios')
ax[3, 0].set_xticks(range(len(efficiency_ratios)))
ax[3, 0].set_xticklabels(['Asset Turnover Ratio', 'Inventory Turnover Ratio'])

ax[4, 0].bar(range(len(growth_metrics)), growth_metrics)
ax[4, 0].set_title('Growth Metrics')
ax[4, 0].set_xticks(range(len(growth_metrics)))
ax[4, 0].set_xticklabels(['Revenue Growth Rate', 'Earnings Per Share (EPS) Growth Rate'])

ax[5, 0].bar(range(len(valuation_metrics)), valuation_metrics)
ax[5, 0].set_title('Valuation Metrics')
ax[5, 0].set_xticks(range(len(valuation_metrics)))
ax[5, 0].set_xticklabels(['Price-to-Earnings (P/E) Ratio', 'Price-to-Book (P/B) Ratio', 'Price-to-Sales (P/S) Ratio'])

ax[5, 1].bar(range(len(cash_flow_metrics)), cash_flow_metrics)
ax[5, 1].set_title('Cash Flow Metrics')
ax[5, 1].set_xticks(range(len(cash_flow_metrics)))
ax[5, 1].set_xticklabels(['Operating Cash Flow (OCF) Margin', 'Free Cash Flow (FCF) Margin'])

# Show the plot
plt.tight_layout()
plt.show()
