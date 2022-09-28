from ai import HostileEnemy
from fighter import Fighter
from entity import Actor

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

drone = Actor(
    char="D",
    color=(63, 127, 63),
    name="Drone Bug",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
)
soldier = Actor(
    char="S",
    color=(0, 127, 0),
    name="Soldier Bug",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
)
