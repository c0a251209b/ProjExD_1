import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600)) #サイズ
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #画像読み込み　画像Surfaceの生成
    kk_img = pg.image.load("fig/3.png") #練習3；こうかとんSurfaceの作成
    kk_img = pg.transform.folip(kk_img, True , False) #練習３こうかとん左右反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0]) #作られたscreenのsurfaceの座標 0,0に貼り付け　貼り付けないと見えない。
        screen.blit(kk_img, [300, 200])        #練習4:こうかとんsurfaceの表示
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()