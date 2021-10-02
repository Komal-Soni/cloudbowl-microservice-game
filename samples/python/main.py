import os
import logging
import random
import math
import json
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
    d=self.direction
    json_object=json.load(logger.info(request.json))
    ex=json_object[0]["state"]["x"]
    ey=json_object[0]["state"]["y"]
    edir=json_object[0]["state"]["direction"]
    if((ex in range(x-4,x+5) or (ey in range(y-4,y+5))):
       i=1
       return moves[i]
    elif:
       if(edir=="N" and ex==x and ey<y):
          i=2       
       elif(edir=="S" and ex==x and ey>y):
          i=2
       elif(edir=="E" and ex<x and ey=y):
          i=2
       elif(edir=="W" and ex>x and ey=y):
          i=3
       else:
          i=0
       return moves[i]
    elif:       
       if d="S" and y==dims[-1] and x==0:
          i=2
       elif d="S" and y==dims[-1] and x==dims[0]:
          i=3
       elif d="E" and y==dims[-1] and x==dims[0]:
          i=2
       elif d="E" and y==0 and x==dims[0]:
          i=3
       elif d="W" and y==0 and x==0:
          i=2
       elif d="W" and y==dims[-1] and x==0:
          i=3
       elif d="N" and y==0 and x==0:
          i=3
       elif d="N" and y==0 and x==dims[0]:
          i=2
       else:
          i=0
       return moves[i]
    else:
       return moves[random.randrange(len(moves))]
if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
