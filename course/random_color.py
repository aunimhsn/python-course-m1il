import random
from sty import fg


def generate_rgb() -> tuple[int]:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return red, green, blue

def generate_color(red:int, green:int, blue:int):
    return fg(red, green, blue)

red, green, blue = generate_rgb()
color = generate_color(red, green, blue)
# fg.rs : reset de la couleur
print(color, "Hello World!", fg.rs)