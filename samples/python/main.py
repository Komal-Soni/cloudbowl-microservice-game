import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    while y<0 and x>0:
        if direction="N" and logger.y>y:
            return moves['T']
        if direction="S" and logger.y<y:
            return moves['T']
        if direction="W" and logger.x<x:
            return moves['T']
        if direction="E" and logger.x>x:
            return moves['T']
        else:
            return moves[random.randrange(len(moves))]
        
        
    '''
    {
  "_links": {
    "self": {
      "href": "https://YOUR_SERVICE_URL"
    }
  },
  "arena": {
    "dims": [4,3], // width, height
    "state": {
      "https://A_PLAYERS_URL": {
        "x": 0, // zero-based x position, where 0 = left
        "y": 0, // zero-based y position, where 0 = top
        "direction": "N", // N = North, W = West, S = South, E = East
        "wasHit": false,
        "score": 0
      }
      ... // also you and the other players
    }
  }
}

    #return '''

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
