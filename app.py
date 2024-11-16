from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Example API endpoint
@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify({"message": "Hello, World!", "status": "success"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
