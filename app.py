from flask import Flask, request, render_template, send_file
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        name, extension = os.path.splitext(file.filename)
        filename = f"{name}_edit{extension}"
        
        df = pd.read_csv(file)
        df = pandas_transform(df)
        df.to_csv(filename, index=False)

        return send_file(filename, as_attachment=True)
    return render_template('upload.html')

def pandas_transform(df):
    # df_new = pd.DataFrame(columns=df.columns, data=[np.nan])
    # df = pd.concat([df_new, df]).reset_index(drop=True)
    return df

if __name__ == '__main__':
    app.run(debug=True)
