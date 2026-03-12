from flask import Flask, render_template, request, redirect

app = Flask(__name__)

parties = {
    1: [],
    2: [],
    3: [],
    4: []
}


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        player_class = request.form["class"]
        party = int(request.form["party"])

        parties[party].append({
            "name": name,
            "class": player_class
        })

        return redirect("/")

    return render_template("index.html", parties=parties)


@app.route("/delete/<int:party>/<name>")
def delete(party, name):

    parties[party] = [p for p in parties[party] if p["name"] != name]

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
