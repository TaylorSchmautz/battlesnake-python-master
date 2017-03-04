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
        'color': '#FFFFFF',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'King snake AKA Owen'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    food = bottle.request.json(u'food')
    snake = bottle.request.json(u'snakes')

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']
    if 'turn' %4 == 0:
        return{
                    'move': 'up',
                    'taunt': 'snake snake'
                }
     if 'turn' %4 == 1:
        return{
                    'move': 'right',
                    'taunt': 'snake snake'
                }
     if 'turn' %4 == 2:
        return{
                    'move': 'down',
                    'taunt': 'snake snake'
                }
     if 'turn' %4 == 3:
        return{
                    'move': 'left',
                    'taunt': 'snake snake'
                }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
