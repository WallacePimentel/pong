from PPlay.window import *
from PPlay.sprite import *

#Janelas
janela = Window(600, 600)
janela.set_background_color([0, 0, 0])
janela.set_title("Wallace Pimentel")

#Sprites
ball = Sprite("ball.png")
pad1 = Sprite("pad.png")
pad2 = Sprite("pad.png")

#Tecla geral
tecla = Window.get_keyboard()

#Coordenadas
start_x = janela.width / 2 - ball.width / 2
end_x = janela.height / 2 - ball.height / 2
pad1x = pad1.width
pad2x = janela.width - 2 * pad1.width
pady = janela.height / 2

#Posições
pad1.set_position(pad1x, pady)
pad2.set_position(pad2x,pady)
ball.set_position(start_x, end_x)

#Velocidade dos objetos
vx, vy = 400, 400
v_up1, v_down1, v_up2, v_down2 = 500, 500, 500, 500

#Pontuação dos jogadores
p1 = 0
p2 = 0

#Gameloop
while True:
    #Velocidade dinâmica da bola
    ball.x = ball.x + vx * janela.delta_time()
    ball.y = ball.y + vy * janela.delta_time()

    #Colisões
    if ball.x >= janela.width - ball.width:                             #Parede direita
        p1 += 1
        ball.set_position(start_x, end_x)
        vx, vy = 0, 0

    if ball.x <= 0:                                                     #Parede esquerda
        p2 += 1
        ball.set_position(start_x, end_x)
        vx, vy = 0, 0

    #Colisão dos pads com o teto
    if pad1.y <= 10:
        v_up1 = 0
    if pad1.y >= janela.height- pad1.height -10:
        v_down1 = 0
    if pad2.y <= 10:
        v_up2 = 0
    if pad2.y >= janela.height- pad1.height -10:
        v_down2 = 0

    if tecla.key_pressed("space"):                                      #Recomeçar o movimento da bola
        vx, vy = 400, 400

    #Inversões de velocidade quando a bola tocar o teto e os pads
    if ball.y >= janela.height - ball.height:
        ball.y = janela.height - ball.height
        vy *= -1

    if ball.y <= 0:
        ball.y = 0
        vy *= -1

    if(ball.collided(pad1) or ball.collided(pad2)):
         vx *= -1

    #Movimentação dos pads
    ##Pad 1
    if(tecla.key_pressed("w")):
        v_down2 = 500
        pad1.y = pad1.y - v_up1 * janela.delta_time()
    if(tecla.key_pressed("s")):
        v_up2 = 500
        pad1.y = pad1.y + v_down1 * janela.delta_time()

    ##Pad 2
    if(tecla.key_pressed("up")):
        v_down1 = 500
        pad2.y = pad2.y - v_up2 * janela.delta_time()
    if(tecla.key_pressed("down")):
        v_up1 = 500
        pad2.y = pad2.y + v_down2 * janela.delta_time()

    #Marcando a pontuação e desenhando o jogo
    pont1 = str(p1)
    pont2 = str(p2)
    janela.set_background_color([0, 0, 0])
    janela.draw_text(pont1, janela.width / 2 - 50, pad1.height / 2, size=50, color=(50, 100, 200), font_name="Arial", bold=True, italic=False)
    janela.draw_text(pont2, janela.width / 2 + 50, pad1.height / 2, size=50, color=(50, 100, 200), font_name="Arial", bold=True, italic=False)
    ball.draw()
    pad1.draw()
    pad2.draw()
    janela.update()