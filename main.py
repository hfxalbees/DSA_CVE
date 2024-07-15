from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import pandas as pd
from werkzeug.utils import secure_filename
import os
from SortingAlgo import PigeonHoleSort  # Adjust the import based on your file structure
from search_algo import kmp  # Import the KMP functions
from analysis_code import analyze_data  # Import the analysis functions

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'CVE data'
app.config['DOWNLOAD_FOLDER'] = 'Sorted CVE'
app.config['ANALYSIS_FOLDER'] = 'Analysis Results'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}

custom_titles = {
    "cia_impact_per_year.png": "Impact Scores per Year",
    "cve_per_year.png": "CVE per Year",
    "cve_severity_per_year.png": "CVE Severity per Year",
    "exploitability_score_per_attack_type.png": "Average Exploitability Score per Attack Type",
    "exploitability_vs_impact.png": "Exploitability Score vs Impact Score",
    "impact_score_per_attack_type.png": "Average Impact Score per Attack Type",
    "severity_change_over_years.png": "Severity Change of Different Attack Types over Years"
}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return redirect(url_for('sort_file', filename=filename))
    else:
        return 'Invalid file format. Only .xlsx files are allowed.'

@app.route('/sort_file/<filename>', methods=['GET', 'POST'])
def sort_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    df = pd.read_excel(file_path)
    column_name = 'CVE ID'  # Replace with the actual column name to sort by
    sorted_df, elapsed_time = PigeonHoleSort.pigeonhole_sort_with_dataframe(df, PigeonHoleSort.custom_sort_key, column_name)
    sorted_df_top10 = sorted_df.head(10)

    search_term = request.form.get('search_term')
    search_column = request.form.get('search_column')
    result_count = 0
    if search_term and search_column:
        search_results = kmp.search_dataframe_kmp(sorted_df, search_term, search_column)
        result_count = len(search_results)
        if not search_results.empty:
            search_results_html = search_results.to_html(classes='table table-striped')
            sorted_df_html = f"<p>Search results for '{search_term}' in '{search_column}' ({result_count} results found):</p>{search_results_html}"
        else:
            sorted_df_html = f"<p>No results found for '{search_term}' in '{search_column}'.</p>"
    else:
        result_count = len(sorted_df_top10)
        sorted_df_html = sorted_df_top10.to_html(classes='table table-striped')

    # Generate analysis
    analysis_output_dir = os.path.join(app.config['ANALYSIS_FOLDER'], filename)
    analyze_data.analyze_data(sorted_df, analysis_output_dir)
    
    return render_template('search.html', elapsed_time=elapsed_time, sorted_df_html=sorted_df_html, search_term=search_term, search_column=search_column, columns=df.columns, result_count=result_count, analysis_files=os.listdir(analysis_output_dir), analysis_dir=filename, custom_titles=custom_titles)


@app.route('/analysis/<path:filepath>')
def send_analysis_file(filepath):
    return send_from_directory(app.config['ANALYSIS_FOLDER'], filepath)

if __name__ == '__main__':
    app.run(debug=True)
