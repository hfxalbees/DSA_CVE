from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import pandas as pd
from werkzeug.utils import secure_filename
import os
from SortingAlgo import PigeonHoleSort
from search_algo import kmp, gallop_search
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
    
    # Get the current page number from the query parameter
    page = int(request.args.get('page', 1))

    # Check if a new search is submitted
    new_search_term = request.form.get('search_term')
    new_search_column = request.form.get('search_column')

    if new_search_term and new_search_column:
        search_term = new_search_term
        search_column = new_search_column
        page = 1  # Reset to first page on new search
    else:
        search_term = request.args.get('search_term')
        search_column = request.args.get('search_column')

    result_count = 0
    typo_suggestions = []
    sorted_df_html = ""
    next_url = None
    prev_url = None

    if search_term and search_column:
        if search_column == 'CVE ID':
            search_results = gallop_search.gallop_search_dataframe(sorted_df, search_column, search_term)
            if search_results:
                search_results = pd.DataFrame([search_results])
            else:
                search_results = pd.DataFrame()
        else:
            search_results = kmp.search_dataframe_kmp(sorted_df, search_term, search_column)

        result_count = len(search_results)
        if search_results.empty:
            typo_suggestions = levenshtein_distance_wit_early_termination.find_similar_words(sorted_df, search_column, search_term, threshold=1)
            typo_suggestions_html = ', '.join(typo_suggestions)
            if typo_suggestions_html:
                sorted_df_html = f"<p>No exact results found for '{search_term}' in '{search_column}'.</p><p>Did you mean any of these? {typo_suggestions_html}</p>"
            else:
                sorted_df_html = f"<p>No exact results found for '{search_term}' in '{search_column}'.</p>"

            if typo_suggestions:
                suggested_word = next(iter(typo_suggestions))  # Take the first suggestion
                if search_column == 'CVE ID':
                    suggested_results = gallop_search.gallop_search_dataframe(sorted_df, search_column, suggested_word)
                    if suggested_results:
                        suggested_results = pd.DataFrame([suggested_results])
                    else:
                        suggested_results = pd.DataFrame()
                else:
                    suggested_results = kmp.search_dataframe_kmp(sorted_df, suggested_word, search_column)
                    
                result_count = len(suggested_results)
                sorted_df_html += f"<p>Showing results for suggested word '{suggested_word}' in '{search_column}' ({result_count} results found):</p>"
                sorted_df_html += paginate_dataframe(suggested_results, page)
                
                # Generate next and previous URLs for suggested results
                next_url = f"/sort_file/{filename}?page={page + 1}&search_term={suggested_word}&search_column={search_column}" if (page * app.config['RESULTS_PER_PAGE']) < len(suggested_results) else None
                prev_url = f"/sort_file/{filename}?page={page - 1}&search_term={suggested_word}&search_column={search_column}" if page > 1 else None
        else:
            sorted_df_html = f"<p>Showing results for '{search_term}' in '{search_column}' ({result_count} results found):</p>"
            sorted_df_html += paginate_dataframe(search_results, page)
            
            # Generate next and previous URLs for search results
            next_url = f"/sort_file/{filename}?page={page + 1}&search_term={search_term}&search_column={search_column}" if (page * app.config['RESULTS_PER_PAGE']) < len(search_results) else None
            prev_url = f"/sort_file/{filename}?page={page - 1}&search_term={search_term}&search_column={search_column}" if page > 1 else None
    else:
        result_count = len(sorted_df)
        sorted_df_html = paginate_dataframe(sorted_df, page)
        
        # Generate next and previous URLs for the sorted DataFrame
        next_url = f"/sort_file/{filename}?page={page + 1}" if (page * app.config['RESULTS_PER_PAGE']) < len(sorted_df) else None
        prev_url = f"/sort_file/{filename}?page={page - 1}" if page > 1 else None

    # Generate analysis
    analysis_output_dir = os.path.join(app.config['ANALYSIS_FOLDER'], filename)
    analyze_data.analyze_data(sorted_df, analysis_output_dir)
    
    return render_template('search.html', elapsed_time=elapsed_time, sorted_df_html=sorted_df_html, search_term=search_term, search_column=search_column, columns=df.columns, result_count=result_count, analysis_files=os.listdir(analysis_output_dir), analysis_dir=filename, custom_titles=custom_titles, typo_suggestions=typo_suggestions, next_url=next_url, prev_url=prev_url)

def paginate_dataframe(df, page):
    results_per_page = app.config['RESULTS_PER_PAGE']
    start = (page - 1) * results_per_page
    end = start + results_per_page
    page_df = df.iloc[start:end]
    return page_df.to_html(classes='table table-striped')



@app.route('/analysis/<path:filepath>')
def send_analysis_file(filepath):
    return send_from_directory(app.config['ANALYSIS_FOLDER'], filepath)

if __name__ == '__main__':
    app.run(debug=True)