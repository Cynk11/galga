@namespace
class SpriteKind:
    spacePlane = SpriteKind.create()

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . 2 . . . . . 
                    . . . . . 8 1 1 1 2 2 . . . . . 
                    . . . . . . . . . . 2 . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        spacePlane2,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.fire, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    scene.camera_shake(4, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

bogey: Sprite = None
projectile: Sprite = None
spacePlane2: Sprite = None
spacePlane2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . 6 6 . . . . . . . . . . . . 
            . . 6 6 6 . . . . . . . . . . . 
            . . . 6 6 8 8 8 7 7 . . . . . . 
            . . . . 6 6 6 6 6 6 7 . . . . . 
            . . . . . . 6 6 6 . . . . . . . 
            . . . . . . 6 6 . . . . . . . . 
            . . . . . . 6 . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(spacePlane2, 200, 200)
spacePlane2.set_stay_in_screen(True)
info.set_life(3)

def on_update_interval():
    global bogey
    mySprite: Sprite = None
    bogey = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . 5 5 . . . . . . . . . . . . 
                    . . 5 5 5 . . . . . . . . . . . 
                    . . 5 5 5 2 2 2 2 . . . . . . . 
                    . . . . 5 5 5 5 5 2 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    bogey.set_velocity(-100, 0)
    mySprite.set_position(160, randint(5, 115))
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(1000, on_update_interval)
