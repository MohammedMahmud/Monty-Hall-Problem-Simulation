from flask import Flask, request
from flask import render_template
from Game_Generator import main as game_sim

app = Flask(__name__)


@app.route('/')
# Index PAGE
def the_index():
    return render_template("index.html")


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

    return render_template("result.html", user=user)


if __name__ == '__main__':
    app.run(debug=True)
