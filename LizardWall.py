from flask import Flask, render_template, redirect, url_for, request, jsonify
from random import randint
import os


#walls=[["static/lemonTree.jpg",[[36,70],[56,86],[25,84]]],[url_for('static', filename='lemonTree.jpg'),[[36,70],[56,86],[25,84]]]]
walls=[["static/wall-1.jpg",[[264,272,False],[631,295,False],[15,231,False],[757,235,False],[550,493,False],[694,528,False],[688,161,False],[171,103,False]],1],
    ["static/wall-2.jpg",[[447,474,False]],2],
    ["static/wall-3.jpg",[[679,314,False],[703,418,False],[579,344,False],[313,155,False],[287,234,False],[68,343,False],[562,550,False],[348,484,False],[19,494,False],[418,378,False]],3],
    ["static/wall-4.jpg",[[282,418,False],[686,500,False],[470,163,False]],4],
    ["static/wall-5.jpg",[[194,16,False],[403,137,False],[401,294,False],[313,71,False]],5],
    ["static/wall-6.jpg",[[230,372,False],[441,377,False]],6],
    ["static/wall-7.jpg",[[300,361,False],[540,417,False]],7],
    ["static/wall-8.jpg",[[236,267,False],[607,503,False],[519,142,False]],8],
    ["static/wall-9.jpg",[[559,280,False],[456,426,False]],9],
    ["static/wall-10.jpg",[[27,269,False]],10]
    ]

app = Flask(__name__)
@app.route('/lizard', methods=['GET', 'POST'])
def home():
    global walls
    return render_template('LizardWall.html',wall=walls[randint(0,9)])

port=os.getenv('PORT') or 80

app.run(host='0.0.0.0', port=port)