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
    x=0
    y=0
    d="N"
    ns={}
    s={}
    json.load(logger.info(request.json))
    xaxis=request.json["arena"]["dims"][0]
    yaxis=request.json["arena"]["dims"][1]
    for player in request.json["arena"]["state"]:
        ex=request.json["arena"]["state"]["x"]
        ey=request.json["arena"]["state"]["y"]
        edir=request.json["arena"]["state"]["direction"]
        if( y==ey && math.abs(x - ex)<=3):
            ns.append(player)
    	if( x==ex && math.abs(y - ey)<=3):
    		s.append(player)
        distance_sq = math.pow( math.abs(x-ex), 2) + math.pow(math.abs(y- ey), 2)
//      distance = math.sqrt(distance_sq)
        while (distance<4 or distance==4):
            if(d=="E" and y=ey and ex-x<4 and ex>x):
                return "T"
            elif(d=="W" and y=ey and x-ex<4 and x>ex):
                return "T"
            elif(d=="N" and x=ex and y-ey<4 and y>ey):
                return "T"
            elif(d=="S" and x=ex and ey-y<4 and ey>y):
                return "T"
            else:
                move= "F"
                if d=="N":
                    for plyr in ns:
                        if d=="N" and plyr.x<x:
                            move="L"
                        if d=="N" and plyr.x>x:
                            move="R"
                        if d=="S" and plyr.x<x:
                            move="R"
                        if d=="S" and plyr.x>x:
                            move="L"
                        if move!="F":
                            return move
                if d=="S" and yaxis-y<4:
                        if xaxis/2>x:
                            move="L"
                        else:
                            move="R"
                if d=="N" and y<4:
                        if xaxis/2>x:
                            move="R"
                        else:
                            move="L"                            
                if d=="W" and x<4:
                        if yaxis/2>y:
                            move="L"
                        else:
                            move="R"            
                if d=="E" and xaxis-x<4:
                        if yaxis/2>y:
                            move="R"
                        else:
                            move="L"            
                        return move
    return moves[random.randrange(len(moves))]           
if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
