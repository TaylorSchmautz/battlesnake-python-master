import bottle
import os
import random


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/gears.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': 'gold',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_type': 'tongue',
        'tail_type': 'fat-rattle',
        'name': 'GodKing'
    }


@bottle.post('/move')
def move():
    snakes = bottle.request.json[u'snakes']
    data = bottle.request.json
    food = bottle.request.json[u'food']
    myID = data[u'you']
    mysnake = [0]
    ffood = food[0]
    
    for snake in snakes:
        if snake[u'id'] == myID:
            mysnake = snake

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']
    #directionsList = {'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]}
          
    
    if mysnake['health_points'] >= 30:
        if data['turn'] % 4 == 0:
            return {
                'move': 'right'
            }
        if  data['turn'] % 4 == 1:
            return {
                'move': 'up',
                'taunt': 'Suck it, Mech Eng rules'
            }
        if  data['turn'] % 4 == 2:
            return {
                'move': 'left'
            }
        if  data['turn'] % 4 == 3:
            return {
                'move': 'down'
            }
    else:
        if ffood[0] < mysnake[0]:
            return {
                'move': 'down'
            } 
        elif ffood[0] < mysnake[0]:
            return {
                'move': 'up'
            }
        else:
            return{
                'move': 'right'
            }
        
    
# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
