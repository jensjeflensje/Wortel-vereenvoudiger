from flask import Flask, request, render_template, redirect, url_for, session, flash
import requests
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        getal = request.form.get("getal")
        gelukt = False
        goede_vierkantsgetal = None
        getal2 = None
        for vierkantsgetal in vierkantsgetallen:
            if int(getal) != vierkantsgetal:
                if float(int(getal) / vierkantsgetal).is_integer():
                    gelukt = True
                    goede_vierkantsgetal = vierkantsgetal
                    getal2 = (int(getal) / vierkantsgetal)
                    break
        if gelukt:
            goede_vierkantsgetal_wortel = math.sqrt(goede_vierkantsgetal)
            goede_vierkantsgetal_wortel = round(goede_vierkantsgetal_wortel)
            if goede_vierkantsgetal_wortel != 1:
                getal2 = round(getal2)
                return render_template("index.html", getal1=goede_vierkantsgetal_wortel, getal2=getal2, getal=getal)
            else:
                return render_template("index.html", error="Lul, deze kan ik niet verkorten", getal=getal)
        else:
            return render_template("index.html", error="Lul, deze kan ik niet verkorten", getal=getal)
    return render_template("index.html")

if __name__ == "__main__":
    vierkantsgetallen = []
    for getal in range(1, 10000):
        vierkantsgetallen.append(getal ** 2)
    vierkantsgetallen.reverse()
    print(vierkantsgetallen)
    app.run(port=10000, host="0.0.0.0", threaded=True)
