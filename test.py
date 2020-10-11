    #!/usr/bin/env python3
import tcod
from engine import *
from foundation import Entity
from action_handlers import *

def main() -> None:
    screen_width = 80
    screen_height = 50  

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(name="Player", type="PLAYER", pos=[int(screen_width/2), int(screen_height/2)], char="@")
    npc = Entity(name="Jack", type="NPC", pos=[int(screen_width/2),int(screen_height/2)], char="&", color=(255,0,255))

    entities = {player, npc}

    engine = Engine(entities=entities, event_handler=event_handler, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)
            


if __name__ == "__main__":
    main()