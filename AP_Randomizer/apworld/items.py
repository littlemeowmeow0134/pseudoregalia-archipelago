from BaseClasses import Item, ItemClassification, MultiWorld
from typing import NamedTuple, Dict, Set, Callable


class PseudoregaliaItem(Item):
    game = "Pseudoregalia"


class PseudoregaliaItemData(NamedTuple):
    code: int = None
    classification: ItemClassification = ItemClassification.filler
    can_create: Callable[[MultiWorld, int], bool] = lambda world: True


item_table: Dict[str, PseudoregaliaItemData] = {
    "Dream Breaker": PseudoregaliaItemData(
        code=2365810001,
        classification=ItemClassification.progression,
        can_create=lambda world: not bool(world.options.progressive_breaker)),
    "Indignation": PseudoregaliaItemData(
        code=2365810002,
        classification=ItemClassification.useful),
    "Sun Greaves": PseudoregaliaItemData(
        code=2365810003,
        classification=ItemClassification.progression,
        can_create=lambda world: not bool(world.options.split_sun_greaves)),
    "Slide": PseudoregaliaItemData(
        code=2365810004,
        classification=ItemClassification.progression,
        can_create=lambda world: not bool(world.options.progressive_slide)),
    "Solar Wind": PseudoregaliaItemData(
        code=2365810005,
        classification=ItemClassification.progression,
        can_create=lambda world: not bool(world.options.progressive_slide)),
    "Sunsetter": PseudoregaliaItemData(
        code=2365810006,
        classification=ItemClassification.progression),
    "Strikebreak": PseudoregaliaItemData(
        code=2365810007,
        classification=ItemClassification.progression,
        can_create=lambda world: not bool(world.options.progressive_breaker)),
    "Cling Gem": PseudoregaliaItemData(
        code=2365810008,
        classification=ItemClassification.progression,
        can_create=lambda world: not bool(world.options.split_gem)),
    "Ascendant Light": PseudoregaliaItemData(
        code=2365810009,
        classification=ItemClassification.progression),
    "Soul Cutter": PseudoregaliaItemData(
        code=2365810010,
        classification=ItemClassification.progression,
        can_create=lambda world: not bool(world.options.progressive_breaker)),

    "Heliacal Power": PseudoregaliaItemData(
        code=2365810011,
        classification=ItemClassification.progression,
        can_create=lambda world: not bool(world.options.split_sun_greaves)),
    "Aerial Finesse": PseudoregaliaItemData(
        code=2365810012,
        classification=ItemClassification.filler),
    "Pilgrimage": PseudoregaliaItemData(
        code=2365810013,
        classification=ItemClassification.filler),
    "Empathy": PseudoregaliaItemData(
        code=2365810014,
        classification=ItemClassification.filler),
    "Good Graces": PseudoregaliaItemData(
        code=2365810015,
        classification=ItemClassification.useful),
    "Martial Prowess": PseudoregaliaItemData(
        code=2365810016,
        classification=ItemClassification.useful),
    "Clear Mind": PseudoregaliaItemData(
        code=2365810017,
        classification=ItemClassification.filler),
    "Professionalism": PseudoregaliaItemData(
        code=2365810018,
        classification=ItemClassification.filler),

    "Health Piece": PseudoregaliaItemData(
        code=2365810019,
        classification=ItemClassification.useful),
    "Small Key": PseudoregaliaItemData(
        code=2365810020,
        classification=ItemClassification.progression),

    "Major Key - Empty Bailey": PseudoregaliaItemData(
        code=2365810021,
        classification=ItemClassification.progression),
    "Major Key - The Underbelly": PseudoregaliaItemData(
        code=2365810022,
        classification=ItemClassification.progression),
    "Major Key - Tower Remains": PseudoregaliaItemData(
        code=2365810023,
        classification=ItemClassification.progression),
    "Major Key - Sansa Keep": PseudoregaliaItemData(
        code=2365810024,
        classification=ItemClassification.progression),
    "Major Key - Twilight Theatre": PseudoregaliaItemData(
        code=2365810025,
        classification=ItemClassification.progression),

    "Progressive Slide": PseudoregaliaItemData(
        code=2365810026,
        classification=ItemClassification.progression,
        can_create=lambda world: bool(world.options.progressive_slide)),
    "Air Kick": PseudoregaliaItemData(
        code=2365810027,
        classification=ItemClassification.progression,
        can_create=lambda world: bool(world.options.split_sun_greaves)),
    "Progressive Dream Breaker": PseudoregaliaItemData(
        code=2365810028,
        classification=ItemClassification.progression,
        can_create=lambda world: bool(world.options.progressive_breaker)),
    "Progressive Cling": PseudoregaliaItemData(
        code=2365810029,
        classification=ItemClassification.progression,
        can_create=lambda world: bool(world.options.split_gem)),

    "Unlocked Door": PseudoregaliaItemData(
        classification=ItemClassification.useful),

    "Something Worth Being Awake For": PseudoregaliaItemData(
        classification=ItemClassification.progression),
}

item_frequencies = {
    "Empathy": 2,
    "Good Graces": 2,
    "Clear Mind": 3,
    "Small Key": 7,
    "Health Piece": 16,
    "Progressive Slide": 2,
    "Air Kick": 4,
    "Progressive Cling": 6,
    "Progressive Dream Breaker": 2,  # Will need to change this later when dream breaker stops being locked to vanilla
}

item_groups: Dict[str, Set[str]] = {
    "major keys": {"Major Key - Empty Bailey",
                   "Major Key - The Underbelly",
                   "Major Key - Tower Remains",
                   "Major Key - Sansa Keep",
                   "Major Key - Twilight Theatre"},
    "plunge": {"Sunsetter"},
    "air kicks": {"Sun Greaves"},
    "nike kicks": {"Sun Greaves"},
    "charge": {"Strikebreak"},
    "projectile": {"Soul Cutter"},
    "slidejump": {"Solar Wind"},
    "wallride": {"Cling Gem"},
    "pogo": {"Ascendant Light"},
    "floof": {"Professionalism"},
    "heliacal power": {"Air Kick"},
    "aspects": {"Indignation",  # some nice to have groups when sorting local/non local items in yaml etc, does not include "Memento" aka new map powerup
                "Aerial Finesse",
                "Pilgrimage",
                "Empathy",
                "Martial Prowess",
                "Clear Mind",
                "Professionalism",
                "Good Graces"},
    "mobility": {"Sun Greaves",
                 "Slide",
                 "Solar Wind",
                 "Ascendant Light",
                 "Heliacal Power",
                 "Progressive Slide",
                 "Sunsetter",
                 "Air Kick",
                 "Cling Gem"},
    "collectables": {"Health Piece",
                     "Small Key"},
    #"weapon": {"Dream Breaker",
    #           "Progressive Dream Breaker",
    #           "Strikebreak",
    #           "Soul Cutter"},
    #"attire": {"Professional", # Castle Sansa trial
    #           "Soldier", # Empty Bailey trial
    #           "Guardian", # Sansa Keep trial
    #           "Sol Sister", # Dilapidated Dungeon trial
    #           "Classy", # Twilight Theatre trial
    #           "XIX", # Underbelly trial
    #           "Sleepytime", # Listless Library trial
    #           "Bleeding Heart}, # Tower Remains trial  
}
