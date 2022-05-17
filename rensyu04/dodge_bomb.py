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
    #練習3
    tori_img = pg.image.load("fig/3.png")     #こうかとん画像用のsurface
    tori_img = pg.transform.rotozoom(tori_img, 0, 2)
    tori_rect = tori_img.get_rect()           #こうかとん画像用のrect
    tori_rect.center = 900, 400               #こうかとん画像用surfaceを画像用surfaceに貼り付ける
    screen.blit(tori_img, tori_rect)

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
