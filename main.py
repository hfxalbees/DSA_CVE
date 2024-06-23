import pandas as pd
from flask import Flask, render_template, request, send_file
from CleaningScripts import TopRansomwareGang

app = Flask(__name__)

# Define the path to your file
file_path = 'CVE data/CVE_Data_2023.xlsx'  # Replace with your actual file path

# Load the processed data at the top of the script so it is accessible globally
# processed_file_path = r'C:\Users\XPS\Desktop\DSA Project\Flask App\DSA_CVE\CleaningScripts\processed_cve_data.csv'
# df = pd.read_csv(processed_file_path)

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
    sorted_groups = TopRansomwareGang.get_sorted_ransomware_groups(ransomware_file_path)
    html_table = sorted_groups.head(10).to_html(classes='data', header="true", index=False)
    return render_template('topRansomwareGang.html', tables=html_table)


@app.route('/plot')
def plot():
    plot_path = r'C:\Users\XPS\Desktop\DSA Project\Flask App\DSA_CVE\CleaningScripts\cve_plot.png'
    return send_file(plot_path, mimetype='image/png')

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
