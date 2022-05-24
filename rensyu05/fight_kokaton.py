import pygame as pg
import sys
import random
from tkinter import messagebox
import tkinter as tk


class Gameover:
    def __init__(self, fn, wh, r):
        self.width, self.height = wh
        self.image = pg.image.load(fn)#ゲームオーバー画像のロード
        self.disp = pg.display.set_mode((self.width, self.height)) # Surface
        self.image = pg.transform.rotozoom(self.image, 0, r) #ゲームオーバー画像が小さいので大きくする用
        self.rect = self.disp.get_rect()#ゲームオーバー画像の形


class Screen:
    def __init__(self, fn, wh, title):
        #fn:背景画像のパス、　wh:幅高さのタプル、title：画面のタイトル        
        pg.display.set_caption(title)
        self.width, self.height = wh #wh1はタプルの予定　例(1000, 900)
        self.disp = pg.display.set_mode((self.width, self.height)) #Surface
        self.rect= self.disp.get_rect() #Rect
        self.image = pg.image.load(fn) #Surfaceクラス


class Bird(pg.sprite.Sprite):
    key_delta = {pg.K_UP   : [0, -1],
             pg.K_DOWN : [0, +1],
             pg.K_LEFT : [-1, 0],
             pg.K_RIGHT: [+1, 0],
             }
    def __init__(self, fn, r, xy):
        #fn:画像用　r:拡大率　xy:こうかとんの初期位置
        super().__init__() #基底クラスの初期化
        self.image = pg.image.load(fn) #Surface
        self.image = pg.transform.rotozoom(self.image, 0, r) 
        self.rect = self.image.get_rect()
        self.rect.center = xy

    def update(self, screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key] == True:
                self.rect.centerx += delta[0]
                self.rect.centery += delta[1]
                # 練習7
                if check_bound(screen.rect, self.rect) != (1,1): 
                    self.rect.centerx -= delta[0]
                    self.rect.centery -= delta[1]




class Bomb(pg.sprite.Sprite):
    def __init__(self,color,r, vxy, screen):
        #color：爆弾のいろ　r:爆弾円の速度のタプル、 screen:描画用：Screenオブジェクト 
        super().__init__()
        self.image = pg.Surface((2*r,2*r))                     # 爆弾用のSurface
        self.image.set_colorkey((0,0,0))                     # 黒色部分を透過する
        pg.draw.circle(self.image, color, (r,r), r)   # 爆弾用Surfaceに円を描く
        self.rect = self.image.get_rect()   # 爆弾用Rect
        self.rect.centerx = random.randint(0, screen.rect.width)
        self.rect.centery = random.randint(0, screen.rect.height)
        self.vx, self.vy = vxy

    def update(self, screen):
        self.rect.move_ip(self.vx, self.vy)
        x, y = check_bound(screen.rect, self.rect)
        self.vx *= x
        self.vy *= y


def pic():#ランダムでこうかとんの画像の名前を返す
    a = random.randint(0, 9)
    img_lst = [(f"fig/{i}.png") for i in range(10)] #内包表記  
    return img_lst[a]


def main():
    clock = pg.time.Clock()
    
    # 練習1
    screen = Screen("fig/pg_bg.jpg", (1600, 900), "逃げろこうかとん")
    #pg.display.set_caption("逃げろ！こうかとん")
    #screen = pg.display.set_mode((1600, 900))      # 画面用のSurface
    #sc_rect= screen.get_rect()                     # 画面用のRect
    #bg_img = pg.image.load("fig/pg_bg.jpg")        # 背景画像用のSurface
    #bg_rect= bg_img.get_rect()                     # 背景画像用のRect
    #bg_rect.center = (1500,500)
    screen.disp.blit(screen.image, (0,0))           # 背景画像用Surfaceを画面用Surfaceに貼り付ける

    # 練習3
    tori = Bird(pic(), 2, (900, 400))
    screen.disp.blit(tori.image, tori.rect)               # こうかとん画像用のSurfaceを画面用Surfaceに貼り付ける
    tori = pg.sprite.Group()
    tori.add(Bird(pic(), 2, (900, 400)))

    # 練習5
    #bomb = Bomb((255, 0, 0), 10, (+2, +2), screen)
    #screen.disp.blit(bomb.image, bomb.rect)                   # 爆弾用のSurfaceを画面用Surfaceに貼り付ける
    bombs = pg.sprite.Group()
    for _ in range(5):#使わないのでアンダースコアを使っている　爆弾のインスタンスを五個生成
        bombs.add(Bomb((255, 0, 0), 10, (+2, +2), screen))

    while True:
        # 練習2
        screen.disp.blit(screen.image, (0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT: return       # ✕ボタンでmain関数から戻る

        # 練習4
        tori.update(screen)
        #screen.disp.blit(tori.image, tori.rect)
        #screen.blit(tori_img, tori_rect)
        tori.draw(screen.disp)

        # 練習6
        bombs.update(screen)
        #screen.disp.blit(bomb.image, bomb.rect)
        bombs.draw(screen.disp) #bombsはグループクラスのインスタンス


        # 練習8
        if len(pg.sprite.groupcollide(tori, bombs, False, False)) != 0:
            gameover = Gameover("fig/ゲームオーバー.jpeg", (1600, 900), 3.3) #ゲームオーバークラスの呼び出し
            screen.disp.blit(gameover.image, gameover.rect) #こうかとん死亡時にゲーム画面にゲームオーバー画像を表示させる
            pg.display.update()     # 画面の更新
            clock.tick(0.5)
            kesu = tk.Tk()#rootウィンドウを消すための作業
            kesu.withdraw()#ここでrootウィンドウを消してる
            pg.mixer.music.stop()#BGMの停止
            messagebox.showerror('死亡', f'君のスコアは{keika}点')
            return
        # こうかとん用のRectが爆弾用のRectと衝突していたらreturn
        #if pg.sprite.collide_rect(tori, bomb): return
        #collide_rect(spriteクラスのインスタンス,spriteクラスのインスタンス)
        pg.display.update()  # 画面の更新
        clock.tick(1000) 
    
# 練習7
def check_bound(sc_r, obj_r): # 画面用Rect, ｛こうかとん，爆弾｝Rect
    # 画面内：+1 / 画面外：-1
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right  < obj_r.right : x = -1
    if obj_r.top  < sc_r.top  or sc_r.bottom < obj_r.bottom: y = -1
    return x, y


def BGM(): #BGMの再生
    pg.mixer.music.load("BGM/08-ラフメイカー.mp3") #曲のロード
    pg.mixer.music.play(loops=-1, start=0.0)#ロードした音楽の再生


if __name__ == "__main__":
    pg.init() 
    kesu = tk.Tk()#rootウィンドウを消すための作業
    kesu.withdraw()#ここでrootウィンドウを消してる
    messagebox.showinfo('覚悟', '命を奪う覚悟はあるか？')
    keika = pg.time.get_ticks()
    BGM()    #音楽の再生用
    main()
    pg.quit()
    sys.exit()