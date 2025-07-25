from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask!'

@app.route('/api')
def api():
    return jsonify({
        "name": "Sanika More",
        "roll_no": "A042",
        "branch": "DevOps",
        "message": "Updated API from Sanika25More_new branch"
    })


if __name__ == '__main__':
    app.run(debug=True)
