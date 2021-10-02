
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
    l=logger.info(request.json)
    while True:
        if direction = "E":
            while (abs(x-l.x)<5 and (y==l.y)):
            moves['T']
            moves[random.randrange(len(moves))]
            
        
        if direction = "W":
            while (abs(x-l.x)<5 and (y==l.y)):
            moves['T']
            moves[random.randrange(len(moves))]
        
        if direction = "N":
            while (abs(y-l.y)<5 and (x==l.x)):
            moves['T']
            moves[random.randrange(len(moves))]
        
        if direction = "S":
            while (abs(y-l.y)<5 and (x==l.x)):
            moves['T']
            moves[random.randrange(len(moves))]
    
        else:
            moves[random.randrange(len(moves))]
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
  
