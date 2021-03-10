namespace SpriteKind {
    export const spacePlane = SpriteKind.create()
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    projectile = sprites.createProjectileFromSprite(img`
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
        `, spacePlane2, 200, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy(effects.fire, 500)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    scene.cameraShake(4, 500)
    info.changeLifeBy(-1)
})
let bogey : Sprite = null
let projectile : Sprite = null
let spacePlane2 : Sprite = null
spacePlane2 = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(spacePlane2, 200, 200)
spacePlane2.setStayInScreen(true)
info.setLife(3)
game.onUpdateInterval(1000, function on_update_interval() {
    
    let mySprite : Sprite = null
    bogey = sprites.create(img`
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
        `, SpriteKind.Enemy)
    bogey.setVelocity(-100, 0)
    mySprite.setPosition(160, randint(5, 115))
    bogey.setFlag(SpriteFlag.AutoDestroy, true)
})
