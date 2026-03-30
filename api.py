from flask import Flask, request

app = Flask(__name__)
ips = []
@app.route('/ip', methods=['GET'])
def getip():
    return ips

@app.route('/ip/add', methods=['POST'])
def addip():
    data = request.get_json()
    ip = data['ip']
    basic = {'ip': ip}
    ips.append(basic)