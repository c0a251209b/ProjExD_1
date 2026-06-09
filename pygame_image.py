import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600)) #サイズ
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #画像読み込み　画像Surfaceの生成
    bg_img2 = pg.transform.flip(bg_img, True , False) #練習8 背景画像の左右反転
    kk_img = pg.image.load("fig/3.png") #練習3；こうかとんSurfaceの作成
    kk_img = pg.transform.flip(kk_img, True , False) #練習３こうかとん左右反転
    kk_rct = kk_img.get_rect() #練習10-1:　こうかとんRectの取得
    kk_rct.center = 300, 200 # 練習10-2：　こうかとんRectに初期座標を設定
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = py.key.get_pressed() # 練習10-3 すべてのキーの押した状態の取得
        # print(key_lst)
        if key_lst[pg.K_UP]: #上矢印キーが押されたら
             kk_rct.move_ip(0,-1)
        if key_lst[pg.K_DOWN]: 
             kk_rct.move_ip(0,1)     
        if key_lst[pg.K_LEFT]: 
             kk_rct.move_ip(-1,0)
        if key_lst[pg.K_RIGHT]: 
             kk_rct.move_ip(1,0) 
            
        x = tmr %3200  
        
        screen.blit(bg_img, [-x, 0]) #作られたscreenのsurfaceの座標 0,0に貼り付け　貼り付けないと見えない。
        screen.blit(bg_img2, [-x+1600, 0])#練習7二枚目
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kk_img, kk_rct) # kk_rctでうごくこうかとんの実装
        #練習4:こうかとんsurfaceの表示
        pg.display.update()
        tmr += 1
                
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()