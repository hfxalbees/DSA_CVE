import pandas as pd

# Load the Excel file
file_path = 'CVE data/DEMO_DATASET.xlsx'
df = pd.read_excel(file_path)

# Assuming your Excel file has a 'year' column
years = df['Year'].unique()

# Create an empty DataFrame to store the sampled rows
sampled_df = pd.DataFrame()

# Loop through each year and sample 10,000 rows
for year in years:
    df_year = df[df['Year'] == year]
    if len(df_year) > 5000:
        df_year_sampled = df_year.sample(n=5000, random_state=1)
    else:
        df_year_sampled = df_year
    sampled_df = pd.concat([sampled_df, df_year_sampled])

# Save the sampled data to a new Excel file
sampled_df.to_excel('CVE data/sampled_data2.xlsx', index=False)
