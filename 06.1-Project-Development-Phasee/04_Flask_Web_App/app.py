from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load cleaned dataset
try:
    df = pd.read_csv("Cleaned_Dataset.csv")
except:
    df = pd.DataFrame()

@app.route("/")
def home():
    total_properties = len(df)
    avg_price = round(df["sale_price"].mean(), 2) if "sale_price" in df.columns else 0
    max_price = df["sale_price"].max() if "sale_price" in df.columns else 0
    min_price = df["sale_price"].min() if "sale_price" in df.columns else 0

    return render_template(
        "index.html",
        total_properties=total_properties,
        avg_price=avg_price,
        max_price=max_price,
        min_price=min_price
    )

if __name__ == "__main__":
    app.run(debug=True)
