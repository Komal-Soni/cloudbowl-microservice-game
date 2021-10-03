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
def my_data(all_data):
    my_name = all_data['_links']['self']['href']
    my_coord = all_data["arena"]["state"][my_name]

    return my_coord, my_name

def get_command(my_direction, my_coord_x, my_coord_y, arena_x, arena_y, all_user_data):
    if my_direction == "N":
        # X axis constant
        # Y decreases as we move forward
        if my_coord_y == 0:
            return "R"
        elif is_someone_present([my_coord_x], [my_coord_y-1, my_coord_y-2, my_coord_y-3], all_user_data):
            return "T"
        else:
            return "F"

    elif my_direction == "S":
        # X axis constant
        # Y increases as we move forward
        if my_coord_y == arena_y - 1:
            return "R"
        elif is_someone_present([my_coord_x], [my_coord_y+1, my_coord_y+2, my_coord_y+3], all_user_data):
            return "T"
        else:
            return "F"

    elif my_direction == "E":
        # Y axis constant
        # X increases as we move forward
        if my_coord_x == arena_x - 1:
            return "R"
        elif is_someone_present([my_coord_x+1, my_coord_x+2, my_coord_x+3], [my_coord_y], all_user_data):
            return "T"
        else:
            return "F"

    elif my_direction == "W":
        # Y axis constant
        # X decreases as we move forward
        if my_coord_x == 0:
            return "R"
        elif is_someone_present([my_coord_x-1, my_coord_x-2, my_coord_x-3], [my_coord_y], all_user_data):
            return "T"
        else:
            return "F"
    else:
        return moves[random.randrange(len(moves))]


def is_someone_present(possible_points_x, possible_points_y, all_user_data):
    for _each_user_name, each_user_stats in all_user_data.items():
        if each_user_stats["x"] in possible_points_x and each_user_stats["y"] in possible_points_y:
            return True
    else:
        return False


@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    return moves[random.randrange(len(moves))]
    my_coord, my_name = my_data(request.json)
    arena_x, arena_y = request.json["arena"]["dims"]
    return get_command(my_coord['direction'], my_coord['x'], my_coord['y'], arena_x, arena_y, request.json["arena"]["state"])

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
