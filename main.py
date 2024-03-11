from engine import *
def main():
  pass
while __name__ == "__main__":
  if gamestate == GAMESTATES[0]:

    start_button = button(image=START_IMAGE, xpos=((screen.get_width()/2)-50), ypos=((screen.get_height()/2)-25))
    title_text = FONT.render('pong', True, 'white')

    while gamestate == GAMESTATES[0]:
      for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
          exit(0)

        if ev.type == pygame.MOUSEBUTTONDOWN:
          pos = pygame.mouse.get_pos()
          if pos[0] > ((screen.get_width()/2)-50) and pos[0] < ((screen.get_width()/2)+50) and pos[1] > ((screen.get_height()/2)-25) and pos[1] < ((screen.get_height()/2)+25):
            gamestate = GAMESTATES[1]
      screen.blit(BACKGROUND, (0,0))
      screen.blit(title_text, (((screen.get_width()/2)-(title_text.get_width()/2)), 100))
      screen.blit(start_button.image, (start_button.posX, start_button.posY))
      pygame.display.flip()


  if gamestate == GAMESTATES[1]:
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

    while gamestate == GAMESTATES[1]:

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


      for item in ALLSPRITES.sprites():
        if item != gameball:
          if pygame.sprite.collide_rect(item, gameball):
            gameball.flip()
            for subitem in ALLSPRITES.sprites():
              if subitem != gameball:
                subitem.accelSpeed += subitem.accelSpeed/4
      

      if gameball.rect.x > screen.get_width():
        score = gameball.reset(score, 'right')
        for item in ALLSPRITES.sprites():
          if item != gameball:
            item.accelSpeed = item.defaultAccelSpeed
      if gameball.rect.x < 0:
        score = gameball.reset(score, 'left')
        for item in ALLSPRITES.sprites():
          if item != gameball:
            item.accelSpeed = item.defaultAccelSpeed



      ALLSPRITES.update()
      

      scoreDisp = FONT.render(f'{score[0]} : {score[1]}', True, 'white')

      screen.blit(BACKGROUND, (0,0))
      screen.blit(scoreDisp, ((screen.get_width()/2)-(scoreDisp.get_width()/2), 25))
      ALLSPRITES.draw(screen)

      pygame.display.flip()
      Clock.tick(FRAMERATE)