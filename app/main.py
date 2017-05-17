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
		'name': 'KingGod'
    	}


@bottle.post('/move')
def move():
	snakes = bottle.request.json[u'snakes']
	data = bottle.request.json
	myID = data[u'you']
	mysnake = [0]
	foods = bottle.request.json[u'food']
	headx = snakes[meIndex][u'coords'][0][0]
	heady = snakes[meIndex][u'coords'][0][1]
	meIndex = 0

	for snake in snakes:
		if snake[u'id'] == myID:
	    		mysnake = snake

	length = len(mysnake[u'coords'])        
	# TODO: Do things with data
	directions = ['up', 'down', 'left', 'right']
	directionDictionary = {'up':[0,-1],'down':[0,1],'right':[1,0], 'left':[-1,0]}
	waysToGo = ['up','down','right','left']

	for wayToGo in directions:
		SpotToCheck = [x+y for x, y in zip([headx, heady], directionDictionary[wayToGo])]
		#print(SpotToCheck)
		if occupied_check(SpotToCheck,snakes):
			if wayToGo in waysToGo:
			#print(wayToGo)
			waysToGo.remove(wayToGo)
		
	if mysnake['health_points'] >= 30:
		if data['turn'] % 7 <= 1:
			return {
			    'move': 'right'
			}
		    if  data['turn'] % 7 > 1 & data['turn'] % 7 <= 3:
			return {
			    'move': 'up',
			    'taunt': 'Suck it, Mech Eng rules'
			}
		    if  data['turn'] % 7 > 3 & data['turn'] % 7 <= 5:
			return {
			    'move': 'left'
			}
		    if  data['turn'] % 7 > 5:
			return {
			    'move': 'down'
			}
		else:
			return food_finder([headx,heady],foods)

	def occupied_check(spot, snakes):
		for snake in snakes:
			if spot in snake[u'coords']:
				return True
		return False


	def food_finder(head, foods):
		closest_food = []
		shortestDistance = 1000000
		food_direction = []
		for food in foods:
			distance = math.sqrt(sum(square([x-y for x, y in zip(food, head)])))
			if distance < shortestDistance:
				closest_food = food
		if len(closest_food) > 0:
			if([x-y for x, y in zip(food,head)][0] < 0):
				food_direction.append('left')
			elif([x-y for x, y in zip(food, head)][0] > 0):
				food_direction.append('right')
		if([x-y for x, y in zip(food, head)][1] < 0):
			food_direction.append('up')
		elif([x-y for x, y in zip(food, head)][1] > 0):
			food_direction.append('down')
	return food_direction
    
# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    	bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
