
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
    logger.info(request.json)
    if (direction=="N") and (logger in range(4)):
        if logger.x > x and logger.y = y:
            moves['T']
        elif logger.x =x and logger.y>y:
            moves['R']
            moves['T']
        elif logger.x =x and logger.y<y:
            moves['L']
            moves['T']
        elif logger.x =x and logger.y<y:
            moves['R']
            moves['L']
            moves['T']
        else:
            moves[random.randrange(len(moves))]
            moves['T']
    if (direction=="N") and (logger in range(4)):
        moves['T']
    if (direction=="S") and (logger in range(4)):
        moves['T']
    if (direction=="E") and (logger in range(4)):
        moves['T']
    if (direction=="W") and (logger in range(4)):
        moves['T']
    while (x!=0 and y!=0):
        x+=2
        y+=2
        moves['T']
        moves[random('F','L','R')
        if wasHit = "true":
              x-=2
              y-=2
              moves['T']
              moves[random('F','L','R')
        if logger<=:
              moves['T']
                    
              
              
    return moves['T']
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

    #return moves[random.randrange(len(moves))]'''

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
