from flask import Flask, request, render_template, Response
import pandas as pd
import numpy as np
import os
from io import StringIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        name, extension = os.path.splitext(file.filename)
        filename = f"{name}_edit{extension}"
        
        df = pd.read_csv(file, delimiter=';')
        df = pandas_transform(df)
        csv_string = df.to_csv(sep=';', index=False, quoting=0)
        def generate():
            yield csv_string
        
        return Response(generate(), mimetype='text/csv', headers={'Content-Disposition': 'attachment;filename='+filename})

    return render_template('upload.html')

def pandas_transform(df):
    df['PLZ'] = df['PLZ'].astype(str).str.zfill(5)
    return df

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
