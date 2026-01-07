python
import pandas as pd

# Load housing affordability data
housing_data = pd.read_csv('housing_affordability_abu_dhabi.csv')

# Load public transportation data
transport_data = pd.read_json('public_transport_usage_abu_dhabi.json')

# Merge datasets on a common key, for example, 'region'
merged_data = pd.merge(housing_data, transport_data, on='region')

# Perform analysis, e.g., calculating average housing cost burden in high transport usage areas
high_usage_areas = merged_data[merged_data['peak_usage'] > merged_data['peak_usage'].mean()]
avg_cost_burden = high_usage_areas['housing_cost_burden'].mean()

print(f'Average Housing Cost Burden in High Transport Usage Areas: {avg_cost_burden}')

# Save the analysis result
high_usage_areas.to_excel('high_usage_areas_analysis.xlsx')
