from flask import Flask, render_template, request, url_for
import pyfiglet

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('index.html')


@app.route("/pyfiglet/")
@app.route("/pyfiglet/<font>")
def generate_banner(font='roman'):
    ascii_banner = pyfiglet.figlet_format("Color Me Wild", font)
    return ascii_banner


with app.test_request_context():
    print(url_for('main'))
    print(url_for('generate_banner'))
    print(url_for('generate_banner', font='roman'))
