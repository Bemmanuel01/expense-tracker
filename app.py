from flask import Flask, render_template, request

app = Flask(__name__)
expenses = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        expenses.append({'amount': amount, 'category': category})

    filter_cat = request.args.get("filter_cat")
    filtered_expenses = expenses if not filter_cat else [e for e in expenses if e["category"] == filter_cat]
    total = sum(e["amount"] for e in filtered_expenses)
    return render_template("index.html", expenses=filtered_expenses, total=total)

if __name__ == "__main__":
    app.run(debug=True)