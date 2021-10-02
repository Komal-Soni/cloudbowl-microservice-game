import os
import logging
import random
import math
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['POST'])
def move(self):
    request.get_data()
    logger.info(request.json)
    x=self.x
    y=self.y
    while x,-y in dims:
        if (direction=="N") and abs(state.y-y)<5 or abs(state.x-x)<5:
            if state.y > y and state.x == x:
                return moves[1]
            elif state.y==y and state.x>x:
                direction=="E"
                return moves[1]
            elif state.y==y and state.x<x:
                direction=="W"
                return moves[1]
            elif state.y <y and state.x==x:
                direction=="S"
                return moves[1]
            else:
                return moves[random.randrange(len(moves))]
        elif (direction=="S") and abs(state.y-y)<5 or abs(state.x-x)<5:
            if state.y > y and state.x ==x:
                direction=="N"
                return moves[1]
            elif state.y ==y and state.x>x:
                direction=="E"
                return moves[1]
            elif state.y==y and state.x<x:
                direction=="W"
                return moves[1]
            elif state.y < y and state.x==x:
                return moves[1]
            else:
                return moves[random.randrange(len(moves))]
        elif (direction=="E") and abs(state.y-y)<5 or abs(state.x-x)<5:
            if state.y > y and state.x = x:
                direction=="N"
                return moves[1]
            elif state.y =y and state.x>x:
                return moves[1]
            elif state.y =y and state.x<x:
                direction=="W"
                return moves[1]
            elif state.y < y and state.x=x:
                direction=="S"
                return moves[1]
            else:
                return moves[random.randrange(len(moves))]
        elif (direction=="W") and abs(state.y-y)<5 or abs(state.x-x)<5:
            if state.y > y and state.x = x:
                direction=="N"
                return moves[1]
            elif state.y=y and state.x>x:
                direction=="E"
                return moves[1]
            elif state.y =y and state.x<x:
                return moves[1]
            elif state.y < y and state.x=x:
                direction=="S"
                return moves[1]
            else:
                return moves[random.randrange(len(moves))]
        else:
            return moves[random.randrange(len(moves))]
    

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
