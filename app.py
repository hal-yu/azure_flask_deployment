from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_504_2023/main/WK1/data/113243405_StonyBrookSouthamptonHospital_StandardCharges.csv')
@app.route('/data')
def data():
    sample_data = df.sample(15)
    return render_template('data.html', data=sample_data)

df1 = pd.read_csv('https://raw.githubusercontent.com/hal-yu/datasci_2_manipulation/main/dataset/diabetes.csv')
@app.route('/diabetes')
def diabetes():
    sample_data1 = df1.sample(20)
    return render_template('diabetes.html', diabetes=sample_data1)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )