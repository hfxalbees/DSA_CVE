import pandas as pd
import matplotlib.pyplot as plt

# Use the absolute path to the Excel file
file_path = r'C:\Users\XPS\Desktop\DSA Project\Flask App\DSA_CVE\CVE data\SIT Ransomware CVE List + URL.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Split the 'Ransomware Group Association' column by comma and strip whitespaces
df['Ransomware Group Association'] = df['Ransomware Group Association'].str.split(',').apply(
    lambda x: [i.strip() for i in x])

# Create a new dataframe to count unique ransomware groups per CVE ID
exploded_df = df.explode('Ransomware Group Association')
grouped_cve_counts = exploded_df.groupby('CVE ID')['Ransomware Group Association'].nunique().reset_index()
grouped_cve_counts.columns = ['CVE ID', 'Count']

# Merge counts with the original dataframe (without exploding it)
df['Ransomware Group Association'] = df['Ransomware Group Association'].apply(lambda x: ', '.join(x))
df = df.merge(grouped_cve_counts, on='CVE ID')

# Drop the URL References column
df = df.drop(columns=['URL References'])

# Save the processed data to a CSV file
processed_file_path = r'C:\Users\XPS\Desktop\DSA Project\Flask App\DSA_CVE\CleaningScripts\processed_cve_data.csv'
df.to_csv(processed_file_path, index=False)


# Plot the data
def plot_cve_data(df, top_n=10):
    # Sort the data by the count of unique ransomware groups
    sorted_df = df.sort_values(by='Count', ascending=False).head(top_n)

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.barh(sorted_df['CVE ID'], sorted_df['Count'], color='skyblue')
    plt.xlabel('Number of Unique Ransomware Groups')
    plt.ylabel('CVE ID')
    plt.title(f'Top {top_n} Most Commonly Exploited CVEs by Ransomware Groups')
    plt.gca().invert_yaxis()
    plt.tight_layout()

    # Save the plot
    plot_path = r'C:\Users\XPS\Desktop\DSA Project\Flask App\DSA_CVE\CleaningScripts\cve_plot.png'
    plt.savefig(plot_path)
    plt.show()


# Generate the plot
plot_cve_data(df)
