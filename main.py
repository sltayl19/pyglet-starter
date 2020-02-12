import pyglet # import the library
window = pyglet.window.Window() # create the window

# Create some text
# label = pyglet.text.Label('Hello, world', x = 200, y = 200)

# Create a sprite
img = pyglet.image.load('assets/hero/Old hero.png')
cave = pyglet.image.load('assets/gfx/cave.png')

# Start the event loop
def update(dt):
    pass

@window.event
def on_draw():
    window.clear()
    img.blit(100, 200)
    img.blit(50,300)

pyglet.clock.schedule(update)
pyglet.app.run()