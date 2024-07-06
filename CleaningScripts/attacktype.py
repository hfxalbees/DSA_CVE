import pandas as pd

# Load the cleaned dataset
file_path = 'CLEANED_DATASET.xlsx'
data = pd.read_excel(file_path)

# Define a function to classify the attack type based on keywords
def classify_attack_type(description):
    attack_types = {
        'XSS': ['xss', 'cross-site scripting', 'cross site scripting'],
        'SQL': ['sql'],
        'CSRF': ['csrf', 'forgery'],
        'Denial of Service': ['denial of service', 'dos'],
        'Buffer Overflow': ['overflow'],
        'Buffer Underflow': ['underflow'],
        'Privilege Escalation': ['elevation', 'privilege', 'escalation'],
        'Man In The Middle': ['ssl', 'man in the middle'],
        'Broken Access Control': ['access control'],
        'Directory Traversal': ['directory', 'traversal'],
        'Authentication Bypass': ['authentication bypass'],
        'XXE': ['xxe'],
        # Add more attack types and their keywords here
    }
    
    description_lower = description.lower()
    for attack_type, keywords in attack_types.items():
        for keyword in keywords:
            if keyword in description_lower:
                return attack_type
    return 'Other'

# Apply the function to create a new 'Attack Type' column
data['Attack Type'] = data['Description'].apply(classify_attack_type)

# Save the updated dataset to a new Excel file
updated_file_path = 'FINAL_DATASET.xlsx'
data.to_excel(updated_file_path, index=False)

# Confirming file is created
print(f"Updated data saved to a single file: {updated_file_path}")
