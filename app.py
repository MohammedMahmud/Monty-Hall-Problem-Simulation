# For The Framework
from flask import Flask, request, render_template
# For Generating The Game
from Game_Generator import main as game_sim
# For The File System
import json
# For The Designing
from flask_bootstrap import Bootstrap
# For The Graph Use
import pygal
# To Remove Files and System Use
import sys
import os


app = Flask(__name__)
Bootstrap(app)

# Index Page
@app.route('/')
def the_index():
    return render_template("Index.html")


def the_json_file(the_data):
    try:
        if os.path.exists('data.json'):
            os.remove("data.json")
        else:
            pass
        # dict(the_data)
        with open('data.json', 'w') as f:
            json.dump(the_data, f)

    except:
        return "Not good"

#  Return's Games
@app.route('/', methods=['POST'])
def processing_data():
    text = request.form['the_loop']
    option = request.form['vehicle']

    try:
        processed_num = int(text)
        processed_option = int(option)

    except ValueError as e:
        if text == "":
            return "<h1 style='text-align:center'> <font color='red'> You Did Not Enter Anything " \
                   "Please Try Again </font></h1>"
        return "<h1 style='text-align:center'> <font color='red'> Please Enter Numbers, You Entered: "+text+" </font>" \
                                                                                                            " </h1>"

    # Calling the Game_Generator class.
    user = game_sim(processed_num, processed_option)
    the_json_file(user)

    return render_template("SimulationResult.html", users=user)


# REST API
@app.route('/api/<int:processed_num>/<int:processed_option>', methods=['GET'])
def game_api(processed_num=None, processed_option=None):
    user = game_sim(processed_num, processed_option)
    # return back json
    return json.dumps(user)


# Return's Winner & Loser statistics
def finding_statistics():
    winner = 0
    loser = 0
    with open('data.json') as json_file:
        data = json.load(json_file)
        for x in data:
            if x["WinnerOrLoser"] == "Winner":
                winner += 1
            else:
                loser += 1

    return [winner, loser]


@app.route('/statistics', methods=['POST', 'GET'])
def results_statistics():
    winner_and_loser = finding_statistics()
    try:
        pie_chart = pygal.Pie()
        pie_chart.title = "Didn't Switch The Door, Total Game Generated: " + str(sum(winner_and_loser))
        pie_chart.add('Winner', winner_and_loser[0])
        pie_chart.add('Loser', winner_and_loser[1])
        # pie_chart.render()
        graph_data = pie_chart.render_data_uri()
        return render_template("Results_Statistics.html", graph_data=graph_data)

    except:
        return str(sys.argv)


if __name__ == '__main__':
    app.run(debug=True)
