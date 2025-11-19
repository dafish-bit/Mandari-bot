from PIL import Image
from datetime import datetime

hour = datetime.now().hour

hunger = 100
thirst = 100
fun = 100
not_tired = 100
is_sleeping = False
is_dead = False
hd = (1280, 720)

class img:
    def __init__(self, x, y, image_dir):
        self.x = x
        self.y = y
        self.image = Image.open(image_dir)

bg = img(0, 0, "game/images/back.jpg")
help = img(0, 0, "game/images/mmikh.png")
dous = {
    "normal" :img(450, 30, "game/images/dou.png"),
    "eat" : img(450, 30, "game/images/delicius aple.png"),
    "drink" : img(450, 30, "game/images/wotir.png"),
    "sleep": img(450, 30, "game/images/sleep.png"),
    "play": img(450, 30, "game/images/fun.png"),
    "dead" : img(450, 30, "game/images/dead.png")}
def make_image(back, main):
    to_return = Image.new("RGBA", hd)
    to_return.paste(back.image, (0, 0))
    to_return.paste(main.image, (main.x, main.y), main.image)
    return to_return
def dou_exist(action="aaa"):
    global hunger, fun, thirst, not_tired, is_sleeping, dous, bg
    if not is_sleeping:
        if 8 <= hour <= 20:
            hunger -= .01
            thirst -= .02
            not_tired -= .01
            fun -= .05
        else:
            not_tired -=.01
            fun -= .01
            hunger -= .02
            thirst -= .03
    else:
        not_tired += .001
        if not_tired >=100:
            is_sleeping = False
    if (hunger<=0)or(thirst<=0):
        is_dead = True
    if action != "aaa":
        if not is_dead:
            match action:
                case "feed":
                    hunger = 100
                    return (make_image(bg, dous["eat"]))
                case "drink":
                    thirst = 100
                    return (make_image(bg, dous["drink"]))
                case "sleep":
                    is_sleeping = True
                    return (make_image(bg, dous["sleep"]))
                case "play":
                    fun += 10
                    return (make_image(bg, dous["play"]))
                case "nothing":
                    if is_sleeping:
                        return (make_image(bg, dous["sleep"]))
                    else: 
                        return (make_image(bg, dous["normal"]))
    else:
        return (make_image(bg, dous["dead"]))
    return make_image(help, help)
