import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

# Define the path to your file
file_path = 'CVE data/CVE_Data_2023.xlsx'  # Replace with your actual file path

@app.route('/') 
def index(): 
    return render_template('index.html') 

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
