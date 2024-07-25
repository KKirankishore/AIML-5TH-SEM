import pandas as pd

# Load the CSV file
file_path = 'bd-dec22-births-deaths-by-region.csv'
data = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\bd-dec22-births-deaths-by-region.csv")

# Display the first few rows of the dataframe to understand its structure
print(data.head())

# Assuming the CSV has columns: 'Region', 'Births', 'Deaths'
# Calculate the total births and deaths per region
total_births_by_region = data.groupby('Region')['Births'].sum()
total_deaths_by_region = data.groupby('Region')['Deaths'].sum()

# Display the results
print("\nTotal Births by Region:")
print(total_births_by_region)

print("\nTotal Deaths by Region:")
print(total_deaths_by_region)

# Optionally, save the results to a new CSV file
output_file_path = 'births_deaths_summary_by_region.csv'
summary = pd.DataFrame({'Total Births': total_births_by_region, 'Total Deaths': total_deaths_by_region})
summary.to_csv(output_file_path)

print(f"\nSummary saved to {output_file_path}")
