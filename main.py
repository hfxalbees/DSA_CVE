import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

# Define the path to your file
file_path = 'CVE data/CVE_Data_2023.xlsx'  # Replace with your actual file path


@app.route('/')
def view():
    try:
        # Read the file using pandas
        data = pd.read_excel(file_path)

        # Return HTML snippet that will render the table
        return data.to_html()
    except Exception as e:
        return f'Error reading file: {str(e)}'


if __name__ == '__main__':
    app.run(debug=True)
