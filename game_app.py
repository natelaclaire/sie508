from Game import Game
from Avatar import Avatar

mario = Avatar('mario', 'brown', 5, 'running')
mario.name
mario.Animate()

toad = Avatar('toad', 'white', 4, 'running')
toad.name

mygame = Game('supermario', 10)
mygame.startGame()
mygame.addAvatar(mario)
mygame.addAvatar(toad)
mygame.Animate()
mygame.stopGame()


tetris = Game('tetris', 5)
tetris.startGame()
tetris.addAvatar(mario)
tetris.addAvatar(toad)
tetris.Animate()

orangeRicky = Avatar('orange ricky', 'orange', 4, 'running')
blueRicky = Avatar('blue ricky', 'orange', 4, 'running')
hero = Avatar('hero', 'orange', 4, 'running')
tetris.addAvatar(orangeRicky)
tetris.addAvatar(blueRicky)
tetris.addAvatar(hero)
tetris.Animate()
tetris.stopGame()
