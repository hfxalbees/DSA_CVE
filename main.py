from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import pandas as pd
from werkzeug.utils import secure_filename
import os
from SortingAlgo import PigeonHoleSort
from search_algo import kmp
from analysis_code import analyze_data
from Levenshtein import levenshtein_distance, levenshtein_distance_wit_early_termination

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'CVE data'
app.config['DOWNLOAD_FOLDER'] = 'Sorted CVE'
app.config['ANALYSIS_FOLDER'] = 'Analysis Results'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}
app.config['RESULTS_PER_PAGE'] = 20

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
    sorted_df_top10 = sorted_df.head(20)

    search_term = request.form.get('search_term')
    search_column = request.form.get('search_column')
    result_count = 0
    typo_suggestions = []
    sorted_df_html = ""

    if search_term and search_column:
        search_results = kmp.search_dataframe_kmp(sorted_df, search_term, search_column)
        result_count = len(search_results)
        if search_results.empty:
            typo_suggestions = levenshtein_distance_wit_early_termination.find_similar_words(sorted_df, search_column, search_term, threshold=2)
            typo_suggestions_html = ', '.join(typo_suggestions)
            if typo_suggestions_html:
                sorted_df_html = f"<p>No exact results found for '{search_term}' in '{search_column}'.</p><p>Did you mean any of these? {typo_suggestions_html}</p>"
            else:
                sorted_df_html = f"<p>No exact results found for '{search_term}' in '{search_column}'.</p>"

            
            # Display rows with suggested word
            if typo_suggestions:
                suggested_word = next(iter(typo_suggestions))  # Take the first suggestion
                suggested_results = sorted_df[sorted_df[search_column].str.lower() == suggested_word.lower()]
                suggested_results_html = paginate_dataframe(suggested_results, page=1)
                sorted_df_html += f"<p>Showing results for suggested word '{suggested_word}':</p>{suggested_results_html}"
        else:
            search_results_html = paginate_dataframe(search_results, page=1)
            sorted_df_html = f"<p>Search results for '{search_term}' in '{search_column}' ({result_count} results found):</p>{search_results_html}"
    else:
        result_count = len(sorted_df_top10)
        sorted_df_html = sorted_df_top10.to_html(classes='table table-striped')

    # Generate analysis
    analysis_output_dir = os.path.join(app.config['ANALYSIS_FOLDER'], filename)
    analyze_data.analyze_data(sorted_df, analysis_output_dir)
    
    return render_template('search.html', elapsed_time=elapsed_time, sorted_df_html=sorted_df_html, search_term=search_term, search_column=search_column, columns=df.columns, result_count=result_count, analysis_files=os.listdir(analysis_output_dir), analysis_dir=filename, custom_titles=custom_titles, typo_suggestions=typo_suggestions)

def paginate_dataframe(df, page):
    results_per_page = app.config['RESULTS_PER_PAGE']
    total_pages = (len(df) // results_per_page) + 1
    start = (page - 1) * results_per_page
    end = start + results_per_page
    page_df = df.iloc[start:end]
    return page_df.to_html(classes='table table-striped')

@app.route('/analysis/<path:filepath>')
def send_analysis_file(filepath):
    return send_from_directory(app.config['ANALYSIS_FOLDER'], filepath)

if __name__ == '__main__':
    app.run(debug=True)