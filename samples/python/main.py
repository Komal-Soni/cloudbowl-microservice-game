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
    while(state.x,state.y in (x+4,y+4 or x+4,y-4 or x-4,y+4 or x-4,y-4)):
        return moves[1]
    return moves[random.randrange(len(moves))]
    

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
