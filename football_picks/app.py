from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import pymongo

# from sportsreference.nfl.boxscore import Boxscores


app = Flask(__name__)

# mongo_client = pymongo.MongoClient("mongodb://admin:admins1@ds157631.mlab.com:57631/picks")
# mydb = mongo_client["picks_test"]
# mycol = mydb["pick_history"]


@app.route("/", methods=["GET", "POST"])
def landing():
    if request.method == "GET":
        return render_template("landing.html", error=None)
    else:
        username = request.form["username"]
        password = request.form["password"]
        if username == "rsfmike" and password == "jthendrick":
            return redirect(url_for("picks"))
        return render_template("landing.html", error="incorrect username/password!")


@app.route("/picks", methods=["GET", "POST"])
def picks():
    if request.method == "GET":
        games = get_game_odds()
        return render_template("picks.html", error=None, games=games)
    else:
        return "no"


def get_game_odds():
    response = requests.get(
        "https://api.the-odds-api.com/v3/odds/?apiKey=be87b59550ca89b16a8737ab1a4f822a&sport=americanfootball_nfl&region=us&mkt=spreads"
    )
    data = response.json()["data"]
    games = []
    for d in data:
        temp = {}
        temp["teams"] = d["teams"]
        temp["spread"] = d["sites"][0]["odds"]["spreads"]["points"][1]
        games.append(temp)
    return games


def get_game_scores(week_num):
    # games_today = Boxscores(1, 2020)
    # # Prints a dictionary of all matchups for week 1 of 2017
    # games = games_today.games["1-2020"]
    # ret = []
    # for g in games:
    #     outcomes = {}
    #     outcomes["away_name"] = g["away_name"]
    #     outcomes["away_score"] = g["away_score"]
    #     outcomes["home_name"] = g["home_name"]
    #     outcomes["home_score"] = g["home_score"]
    #     ret.append(outcomes)
    return []
