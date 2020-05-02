import pyxel

from game.game_world import PyxelTronGameWorld, Action
from render.constants import TILESET, TILESET_PATH, SHIP_PATH, SHIP, PICO8_PALETTE, COLOR_BLACK, CAPTION
from settings import DEBUG


class PyxelTron:
    def __init__(self):
        pyxel.init(160, 120, caption=CAPTION, palette=PICO8_PALETTE)
        pyxel.image(TILESET).load(0, 0, TILESET_PATH)
        pyxel.image(SHIP).load(0, 0, SHIP_PATH)
        self.world = PyxelTronGameWorld()
        self.world.initialize()
        pyxel.run(self.update, self.draw)
        self.collisions = False

    def render_world(self):
        for entity in self.world.entities:
            if entity.render:
                pyxel.blt(
                    entity.x,
                    entity.y,
                    entity.render.IMAGE_BANK,
                    entity.render.u,
                    entity.render.v,
                    entity.render.WIDTH,
                    entity.render.HEIGHT,
                    COLOR_BLACK
                )

    def _handle_input(self):
        action = None
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_LEFT):
            action = Action.MOVE_LEFT
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            action = Action.MOVE_RIGHT
        elif pyxel.btnp(pyxel.KEY_UP):
            action = Action.MOVE_UP
        elif pyxel.btnp(pyxel.KEY_DOWN):
            action = Action.MOVE_DOWN
        elif pyxel.btnp(pyxel.KEY_SPACE):
            action = Action.SHOOT
        self.world.update_scenario(action)

    def update(self):
        self._handle_input()
        self.collisions = self.world.update_collisions()

    def draw(self):
        pyxel.cls(0)
        self.render_world()
        if DEBUG and self.collisions:
            pyxel.text(140, 110, 'PUM', 4)


if __name__ == '__main__':
    PyxelTron()
