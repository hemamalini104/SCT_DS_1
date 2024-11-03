import pandas as pd
import matplotlib.pyplot as plt

population_data_path = '/content/sample_data/pop_data.csv' # Load the dataset 
population_df = pd.read_csv(population_data_path, skiprows=4)  

year = '2022' # Filter data for a specific year (2022) and drop missing values
filtered_data = population_df[['Country Name', year]].dropna()

top_countries = filtered_data.sort_values(by=year, ascending=False).head(20) # Sort by population and select top 20 countries for better visualization

plt.figure(figsize=(14, 8))  # Plotting a bar chart for population distribution in 2022
plt.bar(top_countries['Country Name'], top_countries[year], color='skyblue')
plt.xlabel('Country')
plt.ylabel(f'Population in {year}')
plt.title(f'Population Distribution in {year} for Top 20 Countries')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



