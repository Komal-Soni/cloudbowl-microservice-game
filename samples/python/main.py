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
    for key in json_object:
        ex=json_object[0]["state"]["x"]
        ey=json_object[0]["state"]["y"]
        edir=json_object[0]["state"]["direction"]
        if((ex in range(x-4,x+5) or (ey in range(y-4,y+5))):
           if (d=="N"):
                if(ey < y and ex == x):
                    return moves[1]
                elif (ey == y and ex > x):
                    d="E"
                    return moves[1]
                elif (ey == y and ex < x):
                    d="W"
                    return moves[1]
                elif (ey > y and ex == x):
                    d="S"
                    return moves[1]
                else:
                    return moves[0]
           elif (d=="S"):
                if(ey < y and ex == x):
                    d="N"
                    return moves[1]
                elif (ey == y and ex > x):
                    d="E"
                    return moves[1]
                elif (ey == y and ex < x):
                    d="W"
                    return moves[1]
                elif (ey > y and ex == x):
                    return moves[1]
                else:
                    return moves[0]
           elif (d=="E"):
                if(ey < y and ex == x):
                    d="N"
                    return moves[1]
                elif (ey == y and ex > x):
                    return moves[1]
                elif (ey == y and ex < x):
                    d="W"
                    return moves[1]
                elif (ey > y and ex == x):
                    d="S"
                    return moves[1]
                else:
                    return moves[0]
           elif (d=="W"):
                if(ey < y and ex == x):
                    d="N"
                    return moves[1]
                elif (ey == y and ex > x):
                    d="E"
                    return moves[1]
                elif (ey == y and ex < x):
                    return moves[1]
                elif (ey > y and ex == x):
                    d="S"
                    return moves[1]
                else:
                    return moves[0]
        elif:
           if(edir=="N" and ex==x and ey<y):
                try:
                    return moves[2]
                catch:
                    return moves[3]
           elif(edir=="S" and ex==x and ey>y):
                try:
                    return moves[2]
                catch:
                    return moves[3]
           elif(edir=="E" and ex<x and ey=y):
                try:
                    return moves[2]
                catch:
                    return moves[3]
           elif(edir=="W" and ex>x and ey=y):
                try:
                    return moves[2]
                catch:
                    return moves[3]
           else:
                return moves[0]
        elif:       
           if d="S" and y==dims[-1] and x==0:
                return moves[2]
           elif d="S" and y==dims[-1] and x==dims[0]:
                return moves[2]
           elif d="E" and y==dims[-1] and x==dims[0]:
                return moves[2]
           elif d="E" and y==0 and x==dims[0]:
                return moves[3]
           elif d="W" and y==0 and x==0:
                return moves[2]
           elif d="W" and y==dims[-1] and x==0:
                return moves[3]
           elif d="N" and y==0 and x==0:
                return moves[3]
           elif d="N" and y==0 and x==dims[0]:
                return moves[2]
           else:
                return moves[0]
        else:
           return moves[random.randrange(len(moves))]           
if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
