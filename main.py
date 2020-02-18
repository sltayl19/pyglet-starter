import pyglet # import the library
window = pyglet.window.Window() # create the window

# Create a sprite
img = pyglet.image.load('assets/hero/Old hero.png')
idle = pyglet.image.load('assets/hero/sliced/idle-1.png')
log = pyglet.image.load('assets/gfx/log.png')
kick = pyglet.image.load('assets/hero/sliced/kick.png')
jump = pyglet.image.load('assets/hero/sliced/jump-1.png')






keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

spr = pyglet.sprite.Sprite(img, x = 200, y = 200)
spr.draw()

# Start the event loop
def update(dt):
 if keys[pyglet.window.key.LEFT]:
  spr.x -= 1
 if keys[pyglet.window.key.RIGHT]:
  spr.x += 1


@window.event
def on_draw():
    window.clear()
    img.blit(100, 200)
    log.blit(400,200)
    kick.blit(300,100)
    jump.blit (200,100)
    

pyglet.clock.schedule(update)
pyglet.app.run()