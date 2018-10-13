from flask import Flask, request, jsonify
from flask import render_template
from Game_Generator import main




app = Flask(__name__)


@app.route('/')
def the_index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def processing_data():
    text = request.form['the_loop']
    option = request.form['vehicle']

    try:
        processed_num = int(text)
        processed_option = int(option)
    except ValueError:
        return "<h1> <font color='red'> Please Enter Numbers, You Entered: "+text+" </font></h1>"

    user = main(processed_num, 1)
    print(user)

    return render_template("result.html", user=user)


if __name__ == '__main__':
    app.run(debug=True)
