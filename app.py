from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
 
app = Flask(__name__)
 
# Function to read CSV file
def read_csv(file_path):
    return pd.read_csv(file_path)
 
# Function to write DataFrame to CSV
def write_csv(df, file_path):
    df.to_csv(file_path, index=False)
 
@app.route('/')
def index():
    return redirect(url_for('tab', tab_name='default'))
 
@app.route('/tab/<tab_name>')
def tab(tab_name):
    data_path = f'{tab_name}.csv'
    data = read_csv(data_path)
    return render_template('index.html', data=data, tab_name=tab_name)
 
@app.route('/edit/<tab_name>', methods=['POST'])
def edit(tab_name):
    data_path = f'{tab_name}.csv'
    edited_data = request.form.to_dict(flat=False)
    edited_df = pd.DataFrame(edited_data)
    write_csv(edited_df, data_path)
    return redirect(url_for('tab', tab_name=tab_name))
 
if __name__ == '__main__':
    app.run(debug=True)