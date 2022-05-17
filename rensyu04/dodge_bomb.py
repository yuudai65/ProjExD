import pygame as pg
import sys
import random
from tkinter import messagebox
import tkinter as tk

key_delta = {
             pg.K_UP:[0, -3],
             pg.K_DOWN:[0, +3],
             pg.K_RIGHT:[+3, 0],
             pg.K_LEFT:[-3, 0],} #こうかとんの移動先と移動速度(数字の大きさ)


             
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

    #練習5
    bomb = pg.Surface((20, 20))  #爆弾用のSurface
    bomb.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10) #爆弾用Surfaceに円を描く
    bomb_rect = bomb.get_rect()  #爆弾用rect
    bomb_rect.centerx = random.randint(0, sc_rect.width)
    bomb_rect.centery = random.randint(0, sc_rect.height)
    screen.blit(bomb, bomb_rect) #爆弾用のsurfaceを画面用surfaceに張り付ける
    vx, vy = +5, +5 #爆弾の速さ

    while True:
        #練習2
        screen.blit(bg_img, bg_rect)
        for event in pg.event.get():
           if event.type == pg.QUIT: return #×ボタンでmain関数から戻る

        #練習4
        key_status = pg.key.get_pressed()#key_statusは256もの状態がある
        for key, delta in key_delta.items():
            if key_status[key] == True:
                tori_rect.centerx += delta[0]
                tori_rect.centery += delta[1]
                if check_bound(sc_rect, tori_rect) != (1,1):
                    tori_rect.centerx -= delta[0]
                    tori_rect.centery -= delta[1]
        screen.blit(tori_img, tori_rect)
    

        #練習6
        
        bomb_rect.move_ip(vx, vy)
        screen.blit(bomb, bomb_rect)
        x,y = check_bound(sc_rect, bomb_rect)
        vx *= x #横方向に画面外なら横方向速度の符号反転
        vy *= y #縦方向に画面外なら縦方向速度の符号反転


        #練習8
        if tori_rect.colliderect(bomb_rect):#こうかとん用のrectが爆弾用のrectと衝突したらreturn
            kesu = tk.Tk()#rootウィンドウを消すための作業
            kesu.withdraw()#ここでrootウィンドウを消してる
            messagebox.showerror('死亡', f'君は{keika}ミリ秒生き残った')
            return 



        pg.display.update()  #画面を更新
        clock.tick(1000)

def check_bound(sc_r, obj_r): #画面用rect, こうかとんか爆弾用rect
    #画面内:+1 /　画面外:-1
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right < obj_r.right: 
        x = -1 #画面外
    if obj_r.top < sc_r.top or sc_r.bottom < obj_r.bottom: 
        y = -1
    return x, y


if __name__ == "__main__":
    pg.init()
    kesu = tk.Tk()#rootウィンドウを消すための作業
    kesu.withdraw()#ここでrootウィンドウを消してる
    messagebox.showinfo('覚悟', '命を奪う覚悟はあるか？') #ゲームが始まる前に出てくる
    keika = pg.time.get_ticks()#生き残った時間を取得
    main()
    pg.quit()
    sys.exit()

#改造案
#爆弾増やす
#こうかとんの画像をランダムに
