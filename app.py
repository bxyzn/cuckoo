from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

commands = {
    'pp' : ['playerctl', 'play-pause'],
    'nt' : ['playerctl', 'next'],
    'pv' : ['playerctl', 'previous'],
    'vu' : ['playerctl', 'volume', '0.1+'],
    'vd' : ['playerctl', 'volume', '0.1-'],
    'vm' : ['playerctl', 'volume', '1'],
}

def execcommand(cmd):
    if cmd in commands:
        try:
            subprocess.run(commands[cmd])
            return {
                'status': 'success',
                'response': 'commanded executed'
            }

        except Exception as e: return {
            'status' : 'error',
            'response' : e
        }

@app.route('/cmd', methods=['POST'])
def execute_command():
    data = request.get_json()
    if not data or data == "":
        return jsonify({
            'status': 'error',
            'message': 'No command provided'
        }), 400
    cmd = data['cmd'].lower()
    response = execcommand(cmd)
    return jsonify(response)

app.run(host="0.0.0.0", debug=True)
