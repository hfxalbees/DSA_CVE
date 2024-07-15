import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_data(df, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Analysis 1: CVE per Year
    plt.figure(figsize=(10, 6))
    year_counts = df['Year'].value_counts().sort_index()
    year_counts.plot(kind='bar')
    plt.title('CVE per Year')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'cve_per_year.png'))
    plt.close()

    # Analysis 2: Exploitability Score vs Impact Score
    df['Exploitability Score'] = pd.to_numeric(df['Exploitability Score'], errors='coerce')
    df['Impact Score'] = pd.to_numeric(df['Impact Score'], errors='coerce')
    df.dropna(subset=['Exploitability Score', 'Impact Score'], inplace=True)
    plt.figure(figsize=(12, 10))
    plt.hexbin(df['Exploitability Score'], df['Impact Score'], gridsize=100, cmap='Set1', mincnt=10, linewidths=1.5)
    plt.colorbar(label='Legend for Overlapping Points')
    plt.title('Hexbin Plot of Exploitability Score vs Impact Score')
    plt.xlabel('Exploitability Score')
    plt.ylabel('Impact Score')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'exploitability_vs_impact.png'))
    plt.close()

    # Analysis 3: Average Impact Score per Attack Type
    average_scores = df.groupby('Attack Type')['Impact Score'].mean().sort_values()
    plt.figure(figsize=(12, 8))
    average_scores.plot(kind='barh', color='skyblue')
    plt.title('Average Impact Score per Attack Type')
    plt.xlabel('Average Impact Score')
    plt.ylabel('Attack Type')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'impact_score_per_attack_type.png'))
    plt.close()

    # Analysis 4: CIA Impact per Year
    score_mapping = {'NONE': 0, 'PARTIAL': 0.5, 'LOW': 0.5, 'HIGH': 1, 'COMPLETE': 1}
    df['Confidentiality Score'] = df['Confidentiality Impact'].map(score_mapping)
    df['Integrity Score'] = df['Integrity Impact'].map(score_mapping)
    df['Availability Score'] = df['Availability Impact'].map(score_mapping)
    yearly_scores = df.groupby('Year')[['Confidentiality Score', 'Integrity Score', 'Availability Score']].sum()
    yearly_scores.plot(kind='bar', stacked=True, figsize=(12, 8))
    plt.title('Impact Scores per Year')
    plt.xlabel('Year')
    plt.ylabel('Score')
    plt.xticks(rotation=45)
    plt.legend(title='Impact Type')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'cia_impact_per_year.png'))
    plt.close()

    # Analysis 5: Average Exploitability Score per Attack Type
    average_exploitability_scores = df.groupby('Attack Type')['Exploitability Score'].mean().sort_values()
    plt.figure(figsize=(12, 8))
    average_exploitability_scores.plot(kind='barh', color='lightcoral')
    plt.title('Average Exploitability Score per Attack Type')
    plt.xlabel('Average Exploitability Score')
    plt.ylabel('Attack Type')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'exploitability_score_per_attack_type.png'))
    plt.close()

    # Analysis 6: Change in Severity of Different Attack Types Over the Years
    df['Year'] = df['Year'].astype(int)
    average_severity = df.groupby(['Year', 'Attack Type'])['Base Score'].mean().reset_index()
    severity_pivot = average_severity.pivot(index='Year', columns='Attack Type', values='Base Score')
    plt.figure(figsize=(14, 8))
    ax = plt.gca()
    colors = plt.cm.tab20.colors
    for idx, column in enumerate(severity_pivot.columns):
        severity_pivot[column].plot(kind='line', marker='o', ax=ax, color=colors[idx], label=column)
    plt.title('Change in Severity of Different Attack Types Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Average Base Score')
    plt.legend(title='Attack Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'severity_change_over_years.png'))
    plt.close()

    # Analysis 7: CVE Severity per Year
    severity_levels = ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']
    severity_counts = df.pivot_table(index='Year', columns='Base Severity', aggfunc='size', fill_value=0)
    severity_counts = severity_counts[severity_levels].fillna(0)
    severity_counts.plot(kind='bar', stacked=True, figsize=(12, 8))
    plt.title('CVE Severity per Year')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(title='Base Severity')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'cve_severity_per_year.png'))
    plt.close()
