import pygame as pg
import sys


def main():
    clock = pg.time.Clock()
    #練習1
    pg.display.set_caption("逃げろ!こうかとん")
    screen = pg.display.set_mode((1600, 900)) #画面用surface
    sc_rect = screen.get_rect()               #画面用rect
    bg_img = pg.image.load("fig/pg_bg.jpg")   #背景画像用のsurface
    bg_rect = bg_img.get_rect()               #背景画像用のrect
    screen.blit(bg_img, bg_rect)              #背景画像用surfaceを画面用surfaceに貼り付けているイメージ
    pg.display.update()
    clock.tick(0.5)

    while True:
        #練習2
        screen.blit(bg_img, bg_rect)
        for event in pg.event.get():
           if event.type == pg.QUIT: return #×ボタンでmain関数から戻る
        pg.display.update()  #画面を更新
        clock.tick(1000)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
