import pandas as pd
from collections import Counter
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the Excel file
file_path = r'D:\SIT University\Y1T3\Data Structure and Algorithm\Project\CVE_Data\CVE_Data_2023.xlsx'
df = pd.read_excel(file_path)

# Extract the descriptions
descriptions = df['Description'].astype(str).tolist()

# Define a dictionary of keywords for each sector
sector_keywords = {
    'Healthcare': ['healthcare', 'hospital', 'clinic'],
    'Finance': ['financial', 'bank', 'investment', 'insurance'],
    'Public Sector': ['government', 'public sector', 'municipal', 'federal'],
    'Retail': ['retail', 'e-commerce', 'store', 'shop'],
    'Education': ['education', 'school', 'college', 'university', 'campus'],
    'Manufacturing': ['manufacturing', 'factory', 'production', 'industry'],
    'Telecommunications': ['telecommunications', 'telecom', 'communication'],
    'Transportation': ['transportation', 'transit', 'rail', 'airline', 'logistics'],
    'Technology': ['information technology', 'software', 'hardware'],
    'Food': ['food', 'restaurant', 'cafe', 'catering', 'grocery'],
    'Logistics': ['logistics', 'supply chain', 'shipping', 'warehouse', 'distribution'],
    'Real Estate': ['real estate', 'property', 'housing', 'commercial', 'residential'],
    'Marketing': ['marketing', 'advertising', 'promotion', 'brand', 'campaign']
}

# Count the occurrences of each sector
sector_counts = Counter()

for description in descriptions:
    words = re.findall(r'\b\w+\b', description.lower())  # Tokenize the description into words
    for sector, keywords in sector_keywords.items():
        if any(keyword in words for keyword in keywords):
            sector_counts[sector] += 1

# Sort sector_counts by counts (descending)
sorted_sector_counts = sorted(sector_counts.items(), key=lambda x: x[1], reverse=True)

# Print the counts of each sector
for sector, count in sorted_sector_counts:
    print(f"{sector}: {count}")

# Prepare data for Word Cloud
wordcloud_data = {sector: count for sector, count in sorted_sector_counts}

# Create a Word Cloud with black background and adjusted parameters
wordcloud = WordCloud(width=800, height=400, background_color='black', colormap='viridis', scale=3, min_font_size=10).generate_from_frequencies(wordcloud_data)

# Display the Word Cloud
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Sector Occurrences')
plt.axis('off')
plt.show()
