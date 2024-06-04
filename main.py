from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <html>
      <head>
         <script src="https://unpkg.com/htmx.org@1.9.12"></script>
      </head>
      <body>
      
        <button hx-get="/time/EST" hx-target="#currentTime">
          EST
        </button>
        <button hx-get="/time/UTC" hx-target="#currentTime">
          UTC
        </button>
        <button hx-get="/time/GMT" hx-target="#currentTime">
          GMT
        </button>

        <div id="currentTime"></div>
        
      </body>
      </head>
    '''

@app.route('/time/<timezone>')
def time(timezone):
    currentTime = datetime.now(pytz.timezone(timezone))
    return f'In the {timezone} timezone it is currently {currentTime.strftime("%I:%M:%S")}'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
