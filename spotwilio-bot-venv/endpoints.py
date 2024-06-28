from flask import Flask

app = Flask(__name__)


@app.route('/jukebox', methods=['GET'])
def jukebox():
    # webhook logic here with a response
    pass


if __name__ == "__main__":
    app.run(debug=True)