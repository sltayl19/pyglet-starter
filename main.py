import pyglet # import the library
window = pyglet.window.Window() # create the window

pyglet.window.key.KeyStateHandler()
keys = pyglet.window.key.KeyStateHandler()

# Create some text
# label = pyglet.text.Label('Hello, world', x = 200, y = 200)

# Create a sprite
img = pyglet.image.load('assets/hero/Old hero.png')
cave = pyglet.image.load('assets/hero/sliced/idle-1.png')
log = pyglet.image.load('assets/gfx/log.png')
kick = pyglet.image.load('assets/hero/sliced/kick.png')
jump = pyglet.image.load('assets/hero/sliced/jump-1.png')




# Start the event loop
def update(dt):
    pass




@window.event
def on_draw():
    window.clear()
    img.blit(100, 200)
    cave.blit(50,300)
    log.blit(400,200)
    kick.blit(300,100)
    
    
pyglet.clock.schedule(update)
pyglet.app.run()