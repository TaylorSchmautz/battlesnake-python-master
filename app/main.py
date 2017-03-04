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

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'King snake AKA Owen'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    food = bottle.request.json(u'food')
    snake = bottle.request.json(u'snakes')
    me = data[u'you']
    
    var = food[0]
    
    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']    
    if data['turn'] == 4:
        return {
            'move': 'up',
            'taunt': 'battlesnake-python!'
        }
    else:
        return {
            'move': 'left',
            'taunt': 'battlesnake-python!'
        }
    

  
# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
