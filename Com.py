from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Variable globale pour stocker le compteur de clics
counter = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_counter')
def get_counter():
    global counter
    return jsonify({'counter': counter})

@app.route('/increment_counter', methods=['POST'])
def increment_counter():
    global counter
    counter += 1
    return jsonify({'counter': counter})

if __name__ == '__main__':
    app.run()
