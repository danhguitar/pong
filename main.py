from engine import *
def main():
  pass
if __name__ == "--main__":
  main()


if gamestate == GAMESTATES[2]:
  Clock = pygame.time.Clock()
  pygame.display.set_caption("pong")

  playerApaddle = paddle(PADDLE.get_width(), ((screen.get_height()/2)-(PADDLE.get_height()/2)), .1)
  playerBpaddle = paddle((screen.get_width()-PADDLE.get_width()*2), ((screen.get_height()/2)-(PADDLE.get_height()/2)), .1)
  gameball = ball(((screen.get_width()/2-BALL.get_width()/2)), ((screen.get_height()/2)-BALL.get_height()/2), 'right', 'up', 1, .1)

  ALLSPRITES = pygame.sprite.Group()
  ALLSPRITES.add(playerApaddle)
  ALLSPRITES.add(playerBpaddle)
  ALLSPRITES.add(gameball)

  score = [0,0]

  scoreDisp = FONT.render(f'{score[0]} : {score[1]}', True, 'white')

  while True:

    for ev in pygame.event.get():
      if ev.type == pygame.QUIT:
        exit(0)


    if score[0] == 7 or score[1] == 7:
      time.sleep(3)

      playerApaddle.rect.x = playerApaddle.defaultX
      playerApaddle.rect.y = playerApaddle.defaultY
      playerBpaddle.rect.x = playerBpaddle.defaultX
      playerBpaddle.rect.y = playerBpaddle.defaultY

      score = [0,0]


    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
      playerApaddle.accelY -= playerApaddle.accelSpeed
    if keys[pygame.K_s]:
      playerApaddle.accelY += playerApaddle.accelSpeed
    if keys[pygame.K_UP]:
      playerBpaddle.accelY -= playerBpaddle.accelSpeed
    if keys[pygame.K_DOWN]:
      playerBpaddle.accelY += playerBpaddle.accelSpeed

    if keys[pygame.K_r]:
      playerApaddle.rect.x = playerApaddle.defaultX
      playerApaddle.rect.y = playerApaddle.defaultY
      playerBpaddle.rect.x = playerBpaddle.defaultX
      playerBpaddle.rect.y = playerBpaddle.defaultY

      score = gameball.reset(None, None)


    for i in ALLSPRITES.sprites():
      if i != gameball:
        if pygame.sprite.collide_rect(i, gameball):
          gameball.flip()
    

    if gameball.rect.x > screen.get_width():
      score = gameball.reset(score, 'right')
    if gameball.rect.x < 0:
      score = gameball.reset(score, 'left')



    ALLSPRITES.update()
    

    scoreDisp = FONT.render(f'{score[0]} : {score[1]}', True, 'white')

    screen.blit(BACKGROUND, (0,0))
    screen.blit(scoreDisp, ((screen.get_width()/2)-(scoreDisp.get_width()/2), 25))
    ALLSPRITES.draw(screen)

    pygame.display.flip()
    Clock.tick(FRAMERATE)