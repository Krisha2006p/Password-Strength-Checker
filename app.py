from flask import Flask, request, render_template
from logic import calculate_entropy

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    result = None

    if request.method == 'POST':
        password = request.form['user_password']
        # sending password to logic.py file
        result = calculate_entropy(password)

    # Pass the 'result' variable to the HTML template
    return render_template("index.html", crack_time = result)


if __name__ == '__main__':
    app.run(debug=True)