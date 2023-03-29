from flask import Flask, render_template
from backend import *

# Configuration files
app = Flask(__name__)
app.config["DEBUG"] = True

# Landing page
@app.route('/')
def index():
    name, status = getData()
    msgs=[]
    for i in range(len(name)):
        temp = []
        temp.append(name[i])
        temp.append(status[i])
        msgs.append(temp)
    return render_template('index.html', msgs=msgs)

# Driver code starts from here
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)