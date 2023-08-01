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
        # Save the dataframe to a CSV string
        csv_string = df.to_csv(sep=';', index=False)
        # data.to_csv('/mnt/data/powercloud-bc-2023-07-31_Gas_corrected.csv', sep=';', index=False)

        # Create a generator for the CSV string
        def generate():
            yield csv_string
        
        return Response(generate(), mimetype='text/csv', headers={'Content-Disposition': 'attachment;filename='+filename})

    return render_template('upload.html')

def pandas_transform(df):
    # df_new = pd.DataFrame(columns=df.columns, data=[np.nan])
    # df = pd.concat([df_new, df]).reset_index(drop=True)
    df['PLZ'] = df['PLZ'].astype(str).str.zfill(5)
    return df

if __name__ == '__main__':
    app.run(debug=True)
