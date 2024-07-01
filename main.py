import pandas as pd
from flask import Flask, render_template, request, send_file, url_for
from CleaningScripts import TopRansomwareGang
from SortingAlgo import PigeonHoleSort , SelectionSort

app = Flask(__name__)

file_path = 'CVE data/CVE_Data_2023.xlsx'

# Load the processed data at the top of the script so it is accessible globally
processed_file_path = r'CleaningScripts\processed_cve_data.csv'
df = pd.read_csv(processed_file_path)

ransomware_file_path = r'CVE data\SIT Ransomware CVE List + URL.xlsx'
ransomware_df = pd.read_excel(ransomware_file_path)


@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/cve')
def cve():
    sort_by = request.args.get('sort_by', 'Count')
    sorted_df = df.sort_values(by=sort_by, ascending=(sort_by != 'Count'))
    return render_template('cve.html', tables=[sorted_df.to_html(classes='data', header="true", index=False)])

@app.route('/topRansomwareGang')
def topRansomwareGroup():
    TopRansomwareGang.plot_top_ransomware_groups(ransomware_file_path)
    sorted_groups, sort_time_ms = TopRansomwareGang.get_sorted_ransomware_groups(ransomware_file_path)
    html_table = sorted_groups.head(10).to_html(classes='data', header="true", index=False)

    # You can also log it here if it's not showing in the console
    app.logger.info(f"Sort time: {sort_time_ms} ms")
    return render_template('topRansomwareGang.html', tables=html_table, sort_time=sort_time_ms, image_url=url_for('static', filename='images/top_ransomware_groups.png'))

@app.route('/ransomware_plot')
def ransomware_plot():
    TopRansomwareGang.plot_top_ransomware_groups(ransomware_file_path)
    return send_file('/static/images/TopRansomwareGang.png', mimetype='image/png')


@app.route('/plot')
def plot():
    plot_path = r'C:\Users\XPS\Desktop\DSA Project\Flask App\DSA_CVE\CleaningScripts\cve_plot.png'
    return send_file(plot_path, mimetype='image/png')

@app.route('/pigeonHoleSort')
def pigeonHoleSort():
    try:
        # Read the file using pandas
        print("Reading data from excel...")
        CVE_file_path = r'CVE data\filtered_cve_list.xlsx'
        data = pd.read_excel(CVE_file_path)

        # Perform pigeonhole sort
        sorted_df, elapsed_time, mem_used = PigeonHoleSort.pigeonhole_sort_with_dataframe(data, PigeonHoleSort.custom_sort_key, data.columns[0])

        # Save the sorted DataFrame to a new Excel file
        sorted_file_path = 'Sorted CVE/PigeonHoleSort.xlsx'
        sorted_df.to_excel(sorted_file_path, index=False)
        print(f"Sorted file saved to {sorted_file_path}")

        # sorted_data_html = sorted_df.to_html(classes='table table-striped table-bordered', index=False)

        return render_template('pigeonHoleSort.html', elapsed_time=elapsed_time, mem_used=mem_used, sorted_file=sorted_file_path)
        # return render_template('pigeonHoleSort.html', elapsed_time=elapsed_time, mem_used=mem_used, sorted_data_html=sorted_data_html)

    except Exception as e:
        return f'Error processing file: {str(e)}'
    
@app.route('/selectionSort')
def selectionSort():
    try:
        # Read the file using pandas
        print("Reading data from excel...")
        CVE_file_path = r'CVE data\filtered_cve_list.xlsx'
        data = pd.read_excel(CVE_file_path)

        # Perform selection sort
        sorted_df, elapsed_time, mem_used = SelectionSort.selection_sort_with_dataframe(data, SelectionSort.custom_sort_key, data.columns[0])

        # Save the sorted DataFrame to a new Excel file
        sorted_file_path = 'Sorted CVE/SelectionSort.xlsx'
        sorted_df.to_excel(sorted_file_path, index=False)
        print(f"Sorted file saved to {sorted_file_path}")

        return render_template('selectionSort.html', elapsed_time=elapsed_time, mem_used=mem_used, sorted_file=sorted_file_path)

    except Exception as e:
        return f'Error processing file: {str(e)}'

@app.route('/2023')
def view():
    try:
        # Read the file using pandas
        data = pd.read_excel(file_path)

        # Return HTML snippet that will render the table
        return data.to_html()
    except Exception as e:
        return f'Error reading file: {str(e)}'


@app.route('/example')
def homepage():
 
    # Define Plot Data 
    labels = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
    ]
 
    data = [0, 10, 15, 8, 22, 18, 25]
 
    # Return the components to the HTML template 
    return render_template(
        template_name_or_list='chartjs-example.html',
        data=data,
        labels=labels,
    )


if __name__ == '__main__':
    app.run(debug=True)
