from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from actions import EscapeAction, MovementAction
from foundation import Entity
from action_handlers import EventHandler


class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            if isinstance(action, MovementAction):
                for ent in self.entities :
                    if(ent.type == "PLAYER"):
                        ent.move(byX=action.dx, byY=action.dy)

            elif isinstance(action, EscapeAction):
                raise SystemExit()

    def renderMap(self, console: Console, context: Context):
        for ent in self.entities :
            if(ent.type == "MAP"):
                for tile in ent.inventory :
                    if(tile.type == "TILE"):
                        console.print(tile.pos[0], tile.pos[1], tile.char, fg=tile.color)

    def render(self, console: Console, context: Context) -> None:
        for entity in self.entities:
            if(entity.type == "MAP"):
                for tile in entity.inventory :
                    if(tile.type == "TILE"):
                        console.print(tile.pos[0], tile.pos[1], tile.char, fg=tile.color)
            else :
                console.print(entity.pos[0], entity.pos[1], entity.char, fg=entity.color)

        context.present(console)

        console.clear()