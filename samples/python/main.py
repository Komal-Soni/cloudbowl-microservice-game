
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
'''def move():
    request.get_data()
    logger.info(request.json)'''
    '''if logger not in range(4):
        while True:
            moves['F']
    if (direction=="N") and (logger in range(4)):
        if logger.x > x and logger.y = y:
            moves['T']
        elif logger.x =x and logger.y>y:
            moves['R']
            moves['T']
        elif logger.x =x and logger.y<y:
            moves['L']
            moves['T']
        elif logger.x <x and logger.y=y:
            moves['R']
            moves['R']
            moves['T']
        else:
            moves[random.randrange(len(moves))]
            moves['T']
    else:
        moves['F']
        moves['T']
    if (direction=="S") and (logger in range(4)):
        if logger.x > x and logger.y = y:
            moves['L']
            moves['L']
            moves['T']
        elif logger.x =x and logger.y>y:
            moves['R']
            moves['T']
        elif logger.x =x and logger.y<y:
            moves['L']
            moves['T']
        elif logger.x < x and logger.y=y:
            moves['T']
        else:
            moves[random.randrange(len(moves))]
            moves['T']
    else:
        moves['F']
        MOVES['T']
    if (direction=="E") and (logger in range(4)):
        if logger.x > x and logger.y = y:
            moves['L']
            moves['T']
        elif logger.x =x and logger.y>y:
            moves['T']
        elif logger.x =x and logger.y<y:
            moves['L']
            moves['L']
            moves['T']
        elif logger.x < x and logger.y=y:
            moves['L']
            moves['T']
        else:
            moves[random.randrange(len(moves))]
            moves['T']
    else:
        moves['F']
        moves['T']
    if (direction=="W") and (logger in range(4)):
        if logger.x > x and logger.y = y:
            moves['R']
            moves['T']
        elif logger.x =x and logger.y>y:
            moves['R']
            moves['R']
            moves['T']
        elif logger.x =x and logger.y<y:
            moves['T']
        elif logger.x < x and logger.y=y:
            moves['R']
            moves['T']
        else:
            moves[random.randrange(len(moves))]
            moves['T']
    else:
        moves['F']
        moves['T']
    return moves[random.randrange(len(moves))]'''
def move(self, direction):
    request.get_data()
    logger.info(request.json)
    #This function is how a character moves around in a certain direction
    while logger in range(5):    
        if direction == "N":
            if self.CollisionCheck("N") == False:
                
                if logger.x > x and logger.y = y:
                    moves['T']
                elif logger.x =x and logger.y>y:
                    moves['R']
                    moves['T']
                elif logger.x =x and logger.y<y:
                    moves['L']
                    moves['T']
                elif logger.x <x and logger.y=y:
                    moves['R']
                    moves['R']
                    moves['T']
                else:
                    moves[random.randrange(len(moves))]
                    moves['T']
            else:
                    moves['F']
                    moves['T']
        elif direction == "W":
            if self.CollisionCheck("W") == False:
                if logger.x > x and logger.y = y:
                    moves['R']
                    moves['T']
                elif logger.x =x and logger.y>y:
                    moves['R']
                    moves['R']
                    moves['T']
                elif logger.x =x and logger.y<y:
                    moves['T']
                elif logger.x < x and logger.y=y:
                    moves['R']
                    moves['T']
                else:
                    moves[random.randrange(len(moves))]
                    moves['T']
            else:
                moves['F']
                moves['T']
                    

        elif direction == "E":
            if self.CollisionCheck("E") == False:
                if logger.x > x and logger.y = y:
                    moves['L']
                    moves['T']
                elif logger.x =x and logger.y>y:
                    moves['T']
                elif logger.x =x and logger.y<y:
                    moves['L']
                    moves['L']
                    moves['T']
                elif logger.x < x and logger.y=y:
                    moves['L']
                    moves['T']
                else:
                    moves[random.randrange(len(moves))]
                    moves['T']
            else:
                moves['F']
                moves['T']
                         

        elif direction == "S":
            if self.CollisionCheck("S") == False:
                if logger.x > x and logger.y = y:
                    moves['L']
                    moves['L']
                    moves['T']
                elif logger.x =x and logger.y>y:
                    moves['R']
                    moves['T']
                elif logger.x =x and logger.y<y:
                    moves['L']
                    moves['T']
                elif logger.x < x and logger.y=y:
                    moves['T']
                else:
                    moves[random.randrange(len(moves))]
                    moves['T']
              else:
                moves['F']
                moves['T']
                       
    def CollisionCheck(self, direction):       #Checks if anything is on top of the grass in the direction that the character wants to move. Used in the move function
        if direction == "N":
            if x < 0:
                return True
        elif direction == "W":
            if y > 0:
                return True
        elif direction == "E":
            if y < dims[-1]:
                return True
        elif direction == "S":
            if x< dims[0] > 1:
                return True
        return False
   
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
  
