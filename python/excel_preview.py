from flask import Flask
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def show_excel():
    df = pd.read_excel('./python/dist/file/ocean-monorepo.xlsx',sheet_name=0)
    table_html = df.to_html()
    return f"""
        <html>
            <body>
                <h1></h1>
                <div>{table_html}</div>
            </body>
        </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0")
