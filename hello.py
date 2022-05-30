from flask import Flask, render_template
from flask_caching import Cache
import time
from datetime import datetime

app = Flask(__name__)
cache = Cache()

@app.route("/")
@cache.cached(timeout=5)
def hello():
    
    time.sleep(1)   
    now = datetime.now() # current date and time 
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

    return render_template("index.html", date_time=date_time)

if __name__ == '__main__':
 
    app.config['CACHE_TYPE'] = 'simple'
    cache.init_app(app)

    app.run(host='0.0.0.0', port = 3000)


