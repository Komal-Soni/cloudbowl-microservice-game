
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
    if logger not in range(4):
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
    return moves[random.randrange(len(moves))]
'''def Move(self, Direction):              #This function is how a character moves around in a certain direction

        if Direction == "UP":
            if self.Row > 0:                #If within boundaries of grid
                if self.CollisionCheck("UP") == False:       #And nothing in the way
                   self.Row -= 1            #Go ahead and move

        elif Direction == "LEFT":
            if self.Column > 0:
                if self.CollisionCheck("LEFT") == False:
                    self.Column -= 1

        elif Direction == "RIGHT":
            if self.Column < MapSize-1:
                if self.CollisionCheck("RIGHT") == False:
                         self.Column += 1

        elif Direction == "DOWN":
            if self.Row < MapSize-1:
                if self.CollisionCheck("DOWN") == False:
                    self.Row += 1

        Map.update()       

    def CollisionCheck(self, Direction):       #Checks if anything is on top of the grass in the direction that the character wants to move. Used in the move function
        if Direction == "UP":
            if len(Map.Grid[self.Column][(self.Row)-1]) > 1:
                return True
        elif Direction == "LEFT":
            if len(Map.Grid[self.Column-1][(self.Row)]) > 1:
                return True
        elif Direction == "RIGHT":
            if len(Map.Grid[self.Column+1][(self.Row)]) > 1:
                return True
        elif Direction == "DOWN":
            if len(Map.Grid[self.Column][(self.Row)+1]) > 1:
                return True
        return False'''
   
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
  
