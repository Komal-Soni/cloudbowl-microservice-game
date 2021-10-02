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
    x=self.x
    y=self.y
    request.get_data()
    logger.info(request.json)
    while y<0 and x>0 and x>dims[0] and -y < (dims[-1]):
        if (direction=="N") and abs(state.y-y)<5 and abs(state.x-x)<5:
            if state.x > x and state.y = y:
                moves['T']
            elif state.x =x and state.y>y:
                moves['R']
                moves['T']
            elif state.x =x and state.y<y:
                moves['L']
                moves['T']
            elif state.x <x and state.y=y:
                moves['R']
                moves['R']
                moves['T']
            else:
                moves[random.randrange(len(moves))]
                moves['T']
        else:
            moves['F']
            moves['T']
        if (direction=="S") and abs(state.y-y)<5 and abs(state.x-x)<5:
            if state.x > x and state.y = y:
                moves['L']
                moves['L']
                moves['T']
            elif state.x =x and state.y>y:
                moves['R']
                moves['T']
            elif state.x =x and state.y<y:
                moves['L']
                moves['T']
            elif state.x < x and logger.y=y:
                moves['T']
            else:
                moves[random.randrange(len(moves))]
                moves['T']
        else:
            moves['F']
            moves['T']
        if (direction=="E") and abs(state.y-y)<5 and abs(state.x-x)<5:
            if state.x > x and state.y = y:
                moves['L']
                moves['T']
            elif state.x =x and state.y>y:
                moves['T']
            elif state.x =x and state.y<y:
                moves['L']
                moves['L']
                moves['T']
            elif state.x < x and state.y=y:
                moves['L']
                moves['T']
            else:
                moves[random.randrange(len(moves))]
                moves['T']
        else:
            moves['F']
            moves['T']
        if (direction=="W") and abs(state.y-y)<5 and abs(state.x-x)<5:
            if state.x > x and state.y = y:
                moves['R']
                moves['T']
            elif state.x =x and state.y>y:
                moves['R']
                moves['R']
                moves['T']
            elif state.x =x and state.y<y:
                moves['T']
            elif state.x < x and state.y=y:
                moves['R']
                moves['T']
            else:
                moves[random.randrange(len(moves))]
                moves['T']
        else:
            moves['F']
            moves['T']
        return moves[random.randrange(len(moves))]


if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
