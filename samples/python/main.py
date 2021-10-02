
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
    while True:
        for i in range(10000):
            moves['R']
            moves['T']
            moves['L']
            moves['T']
            moves['F']
            moves['T']
    return moves['T']
    '''while True:
        if x==0:
            return moves['R','F','T']
        if y=0:
            return moves['L','F','T']
        if LOGLEVEL<=4:
            return moves['T']
        else:
            for i in range(LOGLEVEL):
                return moves['F','T']
        m=moves[random.randrange(len(moves))]
            if m='L':
                return moves['T']
            if m='R':
                return moves['T']   
            if m='F':
                return moves['T']
            else:
                return moves['T']
        
        
        #return moves['T']

    #return moves[random.randrange(len(moves))]'''

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
