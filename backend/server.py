from flask import Flask, jsonify
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static.players import get_active_players

app = Flask(__name__)

# Members API route
@app.route("/members")
def members():
    return {"members": ["member1", "member2", "member3"]}

@app.route("/carrer")
def carrer():
    carrer2 = playercareerstats.PlayerCareerStats(player_id='203999') 
    return {"carrer: " + carrer2.get_json()}

@app.route('/gamelog')
def get_player_gamelog():
    gamelog = playergamelog.PlayerGameLog(player_id='2544', season='2019-20')

    # return {'gamelog': gamelog.get_json()}
    return jsonify(gamelog.get_json())

@app.route('/players')
def f_get_players():
    # print(get_players())
    return jsonify(get_active_players())

if __name__ == "__main__":
    app.run(debug=True)