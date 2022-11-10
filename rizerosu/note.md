# リゼロスの自動化

## 起動コマンド

emulator @Pixel_4_API_33 -no-boot-anim -no-snapshot-load -no-snapshot-save 

コールドブート（再起動的なやつ）したい時には次のオプション指定
-no-snapshot-load

状態のセーブをしない
-no-snapshot-save 

起動アニメーションを除いて、高速に起動するオプション
-no-boot-anim

## 終了コマンド

adb -s emulator-5554 emu kill

## グランドアリーナの自動化


