import pygame
import random

# initialize pygame
pygame.init()

#set display size
gameDisplay = pygame.display.set_mode((800,600))

#name of display
pygame.display.set_caption("hello snake")


gameExit = False

clock = pygame.time.Clock()

start_x = 300
start_y = 300

start_x_change = 0
start_y_change = 0

snakeList = []

AppleX = round(random.randrange(0, 799)/10.0)*10.0
AppleY = round(random.randrange(0, 599)/10.0)*10.0


def snake(snakelist):	
	for xY in snakelist:
		pygame.draw.rect(gameDisplay, (255,255,255), [xY[0], xY[1], 10, 10])

		

#game loop
while not gameExit:
	#events handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				start_x_change = -20
				start_y_change = 0
			elif event.key == pygame.K_RIGHT:
				start_x_change = 20
				start_y_change = 0
			elif event.key == pygame.K_DOWN:
				start_y_change = 20
				start_x_change = 0
			elif event.key == pygame.K_UP:
				start_y_change = -20
				start_x_change = 0
				
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				start_x_change = -10
				start_y_change = 0
			elif event.key == pygame.K_RIGHT:
				start_x_change = 10
				start_y_change = 0
			elif event.key == pygame.K_DOWN:
				start_y_change = 10
				start_x_change = 0
			elif event.key == pygame.K_UP:
				start_y_change = -10
				start_x_change = 0
				
	if start_x >= 800 or start_x < 0 or start_y >= 600 or start_y < 0:
		gameExit = True
		print ("YOU SUCK")

				
	#snake continues moving
	start_x += start_x_change
	
	start_y += start_y_change

	
	#fill black display
	gameDisplay.fill((0,0,0))

	
	#draw apple
	pygame.draw.rect(gameDisplay, (255,0,0), [AppleX, AppleY, 10, 10])
	
	

	snakeHead = []
	snakeHead.append(start_x)
	snakeHead.append(start_y)
	snakeList.append(snakeHead)
	
	# if len
	
	snake(snakeList)
	
	
	#snake eats apple
	if start_x == AppleX and start_y == AppleY:
		AppleX = round(random.randrange(0, 799)/10.0)*10.0
		AppleY = round(random.randrange(0, 599)/10.0)*10.0
	
	
	
	pygame.display.update()
	
	#sets FPS
	clock.tick(15)


#quit pygame
pygame.quit()

#quit python
quit()