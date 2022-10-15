from flask import Flask, render_template, redirect, url_for, request, jsonify
from random import randint


#walls=[["static/lemonTree.jpg",[[36,70],[56,86],[25,84]]],[url_for('static', filename='lemonTree.jpg'),[[36,70],[56,86],[25,84]]]]
walls=[["static/wall-1.jpg",[[264,272,False],[631,295,False],[15,231,False]],1],
    ["static/wall-2.jpg",[[447,474,False]],2],
    ["static/wall-3.jpg",[[679,314,False],[703,418,False],[579,344,False],[313,155,False],[287,234,False],[68,343,False],[562,550,False],[348,484,False],[19,494,False]],3],
    ["static/wall-4.jpg",[],4],
    ["static/wall-5.jpg",[],5],
    ["static/wall-6.jpg",[],6],
    ["static/wall-7.jpg",[],7],
    ["static/wall-8.jpg",[],8],
    ["static/wall-9.jpg",[],9],
    ["static/wall-10.jpg",[],10]
    ]

app = Flask(__name__)
@app.route('/lizard', methods=['GET', 'POST'])
def home():
    global walls
    return render_template('LizardWall.html',wall=walls[randint(0,2)])


app.run(host='0.0.0.0', port=80)