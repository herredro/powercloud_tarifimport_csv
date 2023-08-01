from flask import Flask, request, send_file
import pandas as pd
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        df = pd.read_csv(file)
        # Your pandas transformations here

        # Save the dataframe to a CSV file
        filename = "transformed.csv"
        df.to_csv(filename, index=False)

        return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
