from flask import Flask, render_template
import time
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    
    time.sleep(1)
    
    now = datetime.now() # current date and time 
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

    return render_template("index.html", date_time=date_time)

if __name__ == '__main__':
    # app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 10
    app.run(host='0.0.0.0', port = 3000)


