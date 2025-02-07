from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/data")
def get_data():
    with open("/home/hadoop/wordcount_project/wordcount_spark.json", "r") as file:
        data = json.load(file)
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)[:20]
    return jsonify([{"word": word, "count": count} for word, count in sorted_data])

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
