from BaseClasses import Location, MultiWorld
from typing import NamedTuple, Optional, Callable


class PseudoregaliaLocation(Location):
    game = "Pseudoregalia"


class PseudoregaliaLocationData(NamedTuple):
    region: str
    code: int = None
    can_create: Callable[[MultiWorld, int], bool] = lambda world: True
    locked_item: Optional[str] = None
    show_in_spoiler: bool = True


location_table = {
    # Sorted by greater region, then subregion
    # Then abilities first
    # Then alphabetically
    # Anything optional goes below the 50 base locations

    "Dilapidated Dungeon - Dream Breaker": PseudoregaliaLocationData(
        # Dream Breaker can't really be shuffled right now but I would like to later
        code=2365810001,
        region="Dungeon Mirror",
        locked_item="Dream Breaker"),
    "Dilapidated Dungeon - Slide": PseudoregaliaLocationData(
        code=2365810002,
        region="Dungeon Slide"),
    "Dilapidated Dungeon - Alcove Near Mirror": PseudoregaliaLocationData(
        code=2365810003,
        region="Dungeon => Castle",),
    "Dilapidated Dungeon - Dark Orbs": PseudoregaliaLocationData(
        code=2365810004,
        region="Dungeon Escape Upper",),
    "Dilapidated Dungeon - Past Poles": PseudoregaliaLocationData(
        code=2365810005,
        region="Dungeon Strong Eyes",),
    "Dilapidated Dungeon - Rafters": PseudoregaliaLocationData(
        code=2365810006,
        region="Dungeon Strong Eyes",),
    "Dilapidated Dungeon - Strong Eyes": PseudoregaliaLocationData(
        code=2365810007,
        region="Dungeon Strong Eyes",),

    "Castle Sansa - Indignation": PseudoregaliaLocationData(
        code=2365810008,
        region="Castle Main"),
    "Castle Sansa - Alcove Near Dungeon": PseudoregaliaLocationData(
        code=2365810009,
        region="Castle Main",),
    "Castle Sansa - Balcony": PseudoregaliaLocationData(
        code=2365810010,
        region="Castle Main",),
    "Castle Sansa - Corner Corridor": PseudoregaliaLocationData(
        code=2365810011,
        region="Castle Main",),
    "Castle Sansa - Floater In Courtyard": PseudoregaliaLocationData(
        code=2365810012,
        region="Castle Main",),
    "Castle Sansa - Locked Door": PseudoregaliaLocationData(
        code=2365810013,
        region="Castle Main",),
    "Castle Sansa - Platform In Main Halls": PseudoregaliaLocationData(
        code=2365810014,
        region="Castle Main",),
    "Castle Sansa - Tall Room Near Wheel Crawlers": PseudoregaliaLocationData(
        code=2365810015,
        region="Castle Main",),
    "Castle Sansa - Wheel Crawlers": PseudoregaliaLocationData(
        code=2365810016,
        region="Castle Main",),
    "Castle Sansa - High Climb From Courtyard": PseudoregaliaLocationData(
        code=2365810017,
        region="Castle High Climb",),
    "Castle Sansa - Alcove Near Scythe Corridor": PseudoregaliaLocationData(
        code=2365810018,
        region="Castle By Scythe Corridor",),
    "Castle Sansa - Near Theatre Front": PseudoregaliaLocationData(
        code=2365810019,
        region="Castle Moon Room",),

    "Sansa Keep - Strikebreak": PseudoregaliaLocationData(
        code=2365810020,
        region="Keep Main"),
    "Sansa Keep - Alcove Near Locked Door": PseudoregaliaLocationData(
        code=2365810021,
        region="Keep Locked Room",),
    "Sansa Keep - Levers Room": PseudoregaliaLocationData(
        code=2365810022,
        region="Keep Main",),
    "Sansa Keep - Lonely Throne": PseudoregaliaLocationData(
        code=2365810023,
        region="Keep Path To Throne",),
    "Sansa Keep - Near Theatre": PseudoregaliaLocationData(
        code=2365810024,
        region="Keep Main",),
    "Sansa Keep - Sunsetter": PseudoregaliaLocationData(
        code=2365810025,
        region="Keep Sunsetter"),

    "Listless Library - Sun Greaves": PseudoregaliaLocationData(
        code=2365810026,
        region="Library Greaves",
        can_create=lambda world: not bool(world.options.split_sun_greaves)),
    "Listless Library - Upper Back": PseudoregaliaLocationData(
        code=2365810027,
        region="Library Top",),
    "Listless Library - Locked Door Across": PseudoregaliaLocationData(
        code=2365810028,
        region="Library Locked",),
    "Listless Library - Locked Door Left": PseudoregaliaLocationData(
        code=2365810029,
        region="Library Locked",),

    "Twilight Theatre - Soul Cutter": PseudoregaliaLocationData(
        code=2365810030,
        region="Theatre Main"),
    "Twilight Theatre - Back Of Auditorium": PseudoregaliaLocationData(
        code=2365810031,
        region="Theatre Main",),
    "Twilight Theatre - Center Stage": PseudoregaliaLocationData(
        code=2365810032,
        region="Theatre Main",),
    "Twilight Theatre - Locked Door": PseudoregaliaLocationData(
        code=2365810033,
        region="Theatre Main",),
    "Twilight Theatre - Murderous Goat": PseudoregaliaLocationData(
        code=2365810034,
        region="Theatre Main",),
    "Twilight Theatre - Corner Beam": PseudoregaliaLocationData(
        code=2365810035,
        region="Theatre Pillar",),

    "Empty Bailey - Solar Wind": PseudoregaliaLocationData(
        code=2365810036,
        region="Empty Bailey",),
    "Empty Bailey - Center Steeple": PseudoregaliaLocationData(
        code=2365810037,
        region="Empty Bailey",),
    "Empty Bailey - Cheese Bell": PseudoregaliaLocationData(
        code=2365810038,
        region="Empty Bailey",),
    "Empty Bailey - Guarded Hand": PseudoregaliaLocationData(
        code=2365810039,
        region="Empty Bailey",),
    "Empty Bailey - Inside Building": PseudoregaliaLocationData(
        code=2365810040,
        region="Empty Bailey",),

    "The Underbelly - Ascendant Light": PseudoregaliaLocationData(
        code=2365810041,
        region="Underbelly Ascendant Light"),
    "The Underbelly - Alcove Near Light": PseudoregaliaLocationData(
        code=2365810042,
        region="Underbelly Light Pillar",),
    "The Underbelly - Building Near Little Guy": PseudoregaliaLocationData(
        code=2365810043,
        region="Underbelly Little Guy",),
    "The Underbelly - Locked Door": PseudoregaliaLocationData(
        code=2365810044,
        region="Underbelly By Heliacal",),
    "The Underbelly - Main Room": PseudoregaliaLocationData(
        code=2365810045,
        region="Underbelly Main Upper",),
    "The Underbelly - Rafters Near Keep": PseudoregaliaLocationData(
        code=2365810046,
        region="Underbelly => Keep",),
    "The Underbelly - Strikebreak Wall": PseudoregaliaLocationData(
        code=2365810047,
        region="Underbelly Main Upper",),
    "The Underbelly - Surrounded By Holes": PseudoregaliaLocationData(
        code=2365810048,
        region="Underbelly Hole",),

    "Tower Remains - Cling Gem": PseudoregaliaLocationData(
        code=2365810049,
        region="Tower Remains"),
    "Tower Remains - Atop The Tower": PseudoregaliaLocationData(
        code=2365810050,
        region="The Great Door",),

    # Split Greaves
    "Listless Library - Sun Greaves 1": PseudoregaliaLocationData(
        code=2365810051,
        region="Library Greaves",
        can_create=lambda world: bool(world.options.split_sun_greaves)),
    "Listless Library - Sun Greaves 2": PseudoregaliaLocationData(
        code=2365810052,
        region="Library Greaves",
        can_create=lambda world: bool(world.options.split_sun_greaves)),
    "Listless Library - Sun Greaves 3": PseudoregaliaLocationData(
        code=2365810053,
        region="Library Greaves",
        can_create=lambda world: bool(world.options.split_sun_greaves)),

    # Goatlings
    "Dilapidated Dungeon - the goatling who fell out his cage": PseudoregaliaLocationData(
        code=2365810054,
        region="Dungeon Mirror",
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Lock::None,
    "Castle Sansa - the goatling lamenting the skill issue of players who need a map": PseudoregaliaLocationData(
        code=2365810055,
        region="Castle Main",
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Lock::None,
    "Castle Sansa - the goatling who wants to lick the checkpoint": PseudoregaliaLocationData(
        code=2365810056,
        region="Castle Main",
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Lock::None,
    "Castle Sansa - the goatling who wanted to see the armour display": PseudoregaliaLocationData(
        code=2365810057,
        region="Castle Main",
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Lock::None,
    "Castle Sansa - the goatling about to jump into the haze": PseudoregaliaLocationData(
        code=2365810058,
        region="Castle By Scythe Corridor",
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Any(&[ // Just need to break the wall.. nothing new
    #    Powerup(A::DreamBreaker),
    #    All(&[
    #        Powerup(A::Sunsetter),
    #        Trick(T::Knowledge, D::Normal),
    #    ])
    #]),
    "Castle Sansa - the goatling that calls you bubble girl": PseudoregaliaLocationData(
        code=2365810059,
        region="Castle Main",
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Any(&[
    #    Powerup(A::HeliacalPower),
    #    Powerup(A::ClingGem(4)),
    #]),
    "Castle Sansa - the goatling in the gazebo": PseudoregaliaLocationData(
        code=2365810060,
        region="Castle Main",  # TODO double check
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Lock::None,
    "Sansa Keep - the goatling sad about the lack of furniture": PseudoregaliaLocationData(
        code=2365810061,
        region="Keep Main",
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Lock::None,
    "Sansa Keep - the goatling collapsing out of reality": PseudoregaliaLocationData(
        code=2365810062,
        region="Keep => Underbelly",  # pretty sure this is logically sound but should probably change
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Lock::None,
    "Empty Bailey - the goatling who's hiding": PseudoregaliaLocationData(
        code=2365810063,
        region="Empty Bailey",  # TODO don't know of this is right
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Powerup(A::Slide), // Theres another way to get TO the item, not putting it in since its a one way unless it is slide though...
    "Twilight Theatre - the goatling who can eat 20 beans at least": PseudoregaliaLocationData(
        code=2365810064,
        region="Castle => Theatre (Front)",
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Lock::None,
    "Twilight Theatre - the goatling who thought the theatre was safe": PseudoregaliaLocationData(
        code=2365810065,
        region="Castle => Theatre (Front)",
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Lock::None,
    "Twilight Theatre - the first goatling who really wanted to see the show": PseudoregaliaLocationData(
        code=2365810066,
        region="Castle => Theatre (Front)",
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Lock::None,
    "Twilight Theatre - the second goatling who really wanted to see the show": PseudoregaliaLocationData(
        code=2365810067,
        region="Castle => Theatre (Front)",
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Lock::None,
    "Twilight Theatre - the goatling that will kill again": PseudoregaliaLocationData(
        code=2365810068,
        region="Theatre Main",
        can_create=lambda world: bool(world.options.shuffle_goatlings)),
    #Any(&[
    #    All(&[Powerup(A::SolarWind), Powerup(A::HeliacalPower)]),
    #    Powerup(A::SunGreaves),
    #    Powerup(A::ClingGem(6))
    #]),

    # Notes
    "Listless Library - the note next to the egg nest": PseudoregaliaLocationData(
        code=2365810069,
        region="Library Main", # location: L::MainLibrary,
        can_create=lambda world: bool(world.options.shuffle_notes)),
    # locks: Any(&[
    #     Powerup(A::SunGreaves),
    #     Powerup(A::ClingGem(4)),
    #     Powerup(A::SolarWind),
    # ]),

    "The Underbelly - the note on a high ledge in the big room": PseudoregaliaLocationData(
        code=2365810070,
        region="Underbelly Main Upper",  # location: L::MainUnderbelly,
        # TODO: double check this region
        can_create=lambda world: bool(world.options.shuffle_notes)),
    # locks: All(&[ // Leaving as is for now.
    #     Powerup(A::HeliacalPower),
    #     Powerup(A::Sunsetter),
    #     Any(&[
    #         Powerup(A::ClingGem(6)),
    #         Powerup(A::SunGreaves),
    #         Powerup(A::SolarWind),
    #     ]),
    # ]),

    "The Underbelly - the note behind the locked door": PseudoregaliaLocationData(
        code=2365810071,
        region="Underbelly By Heliacal",  # location: L::HpSave,
        can_create=lambda world: bool(world.options.shuffle_notes)),
    # locks: Lock::SmallKey,

    "The Underbelly - the note near the empty bailey entrance": PseudoregaliaLocationData(
        code=2365810072,
        region="Underbelly Main Lower",  # location: L::BaileyHole,
        can_create=lambda world: bool(world.options.shuffle_notes)),
    # locks: Any(&[
    #     Powerup(A::SunGreaves),
    #     All(&[Powerup(A::HeliacalPower), Powerup(A::Sunsetter)]),
    #     Powerup(A::ClingGem(6)),
    #     Powerup(A::AscendantLight),
    #     Powerup(A::SolarWind),
    #     All(&[Powerup(A::HeliacalPower), Trick(T::ReverseKick, D::Normal)]),
    #     All(&[Powerup(A::Sunsetter), Trick(T::Movement, D::Normal)]),
    # ]),

    # Chairs
    "Castle Sansa - first chair next to the goatling who wants to lick the checkpoint": PseudoregaliaLocationData(
        code=2365810073,
        region="Castle Main",  # location: L::CsMain,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # locks: Lock::None,

    "Castle Sansa - second chair next to the goatling who wants to lick the checkpoint": PseudoregaliaLocationData(
        code=2365810074,
        region="Castle Main",  # location: L::CsMain,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # locks: Lock::None,

    "Castle Sansa - third chair next to the goatling who wants to lick the checkpoint": PseudoregaliaLocationData(
        code=2365810075,
        region="Castle Main",  # location: L::CsMain,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # locks: Lock::None,

    "Castle Sansa - the chair in the gazebo": PseudoregaliaLocationData(
        code=2365810076,
        region="Castle Main",  # location: L::CsMain,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # locks: Lock::None,

    "Listless Library - the chair at the entrance": PseudoregaliaLocationData(
        code=2365810077,
        region="Library Main",  # location: L::MainLibrary,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # locks: Lock::None,

    "Listless Library - the chair after the normal sun greaves location": PseudoregaliaLocationData(
        code=2365810078,
        region="Library Greaves",  # location: L::LibSaveNearGreaves,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # locks: Lock::None,

    "Listless Library - the chair next to the egg nest": PseudoregaliaLocationData(
        code=2365810079,
        region="Library Main",  # location: L::MainLibrary,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # locks: Any(&[
    #     Powerup(A::SunGreaves),
    #     Powerup(A::ClingGem(4)),
    #     Powerup(A::SolarWind),
    # ]),

    "Sansa Keep - the chair collapsing out of reality": PseudoregaliaLocationData(
        code=2365810080,
        region="Keep => Underbelly",  # location: L::SkCastleRampEntry,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # locks: Lock::None,

    "Sansa Keep - the chair in the middle of the parkour": PseudoregaliaLocationData(
        code=2365810081,
        region="Keep Main",  # location: L::SansaKeep,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # locks:  Any(&[
    #     All(&[
    #         Powerup(A::AscendantLight),
    #         Any(&[
    #             All(&[
    #                 Powerup(A::ClingGem(4)),
    #                 Any(&[Powerup(A::Sunsetter), Powerup(A::SunGreaves)]),
    #             ]),
    #             All(&[Powerup(A::Sunsetter), Powerup(A::SunGreaves)]),
    #         ]),
    #     ]),
    #     All(&[
    #         Powerup(A::DreamBreaker),
    #         Powerup(A::Slide),
    #         Powerup(A::SolarWind),
    #         Powerup(A::Sunsetter),
    #         Powerup(A::ClingGem(2)),
    #         Powerup(A::SunGreaves),
    #     ]),
    # ]),

    "Twilight Theatre - first chair around the table": PseudoregaliaLocationData(
        code=2365810082,
        region="Theatre Main",  # location: L::OtherTheatrePath,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # TODO may need additional logic
    # locks: Lock::None,

    "Twilight Theatre - second chair around the table": PseudoregaliaLocationData(
        code=2365810083,
        region="Theatre Main",  # location: L::OtherTheatrePath,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # TODO may need additional logic
    # locks: Lock::None,

    "Twilight Theatre - third chair around the table": PseudoregaliaLocationData(
        code=2365810084,
        region="Theatre Main",  # location: L::OtherTheatrePath,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # TODO may need additional logic
    # locks: Lock::None,

    "Twilight Theatre - the chair next to the books": PseudoregaliaLocationData(
        code=2365810085,
        region="Theatre Main",  # location: L::OtherTheatrePath,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # TODO may need additional logic
    # locks: Lock::None,

    "Twilight Theatre - the chair near the courtyard": PseudoregaliaLocationData(
        code=2365810086,
        region="Theatre Main",  # location: L::MainTheatre,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # TODO may need additional logic
    # locks: Any(&[
    #     Powerup(A::ClingGem(4)),
    #     All(&[Powerup(A::SolarWind), Powerup(A::HeliacalPower), Powerup(A::SunGreaves)]),
    # ]),

    "Twilight Theatre - the chair in the soul cutter zone": PseudoregaliaLocationData(
        code=2365810087,
        region="Theatre Main",  # location: L::MainTheatre,
        can_create=lambda world: bool(world.options.shuffle_chairs)),
    # locks:  All(&[
    #     Powerup(A::Strikebreak),
    #     Powerup(A::ClingGem(6)),
    #     Any(&[
    #         // Logic for soul cutter route w/o soulcutter
    #         All(&[
    #             Powerup(A::Strikebreak),
    #             Powerup(A::SolarWind),
    #             Powerup(A::HeliacalPower),
    #             Powerup(A::SunGreaves),
    #             Powerup(A::Sunsetter),
    #             Trick(T::ClingAbuse, D::Expert),
    #             Trick(T::OneWall, D::Expert),
    #             Trick(T::Movement, D::Insane),
    #             Trick(T::Momentum, D::Expert),
    #         ]),
    #         //with soul cutter.
    #         All(&[
    #             Powerup(A::SoulCutter),
    #             Any(&[
    #                 Powerup(A::HeliacalPower),
    #                 Powerup(A::SolarWind)
    #             ]),
    #         ]),
    #     ]),
    # ]),


    # Door Unlocks
    "Dilapidated Dungeon - Unlock Door": PseudoregaliaLocationData(
        region="Dungeon Strong Eyes",
        locked_item="Unlocked Door",
        show_in_spoiler=False),
    "Castle Sansa - Unlock Door (Professionalism)": PseudoregaliaLocationData(
        region="Castle Main",
        locked_item="Unlocked Door",
        show_in_spoiler=False),
    "Castle Sansa - Unlock Door (Sansa Keep)": PseudoregaliaLocationData(
        region="Castle Main",
        locked_item="Unlocked Door",
        show_in_spoiler=False),
    "Sansa Keep - Unlock Door": PseudoregaliaLocationData(
        region="Keep Main",
        locked_item="Unlocked Door",
        show_in_spoiler=False),
    "Listless Library - Unlock Door": PseudoregaliaLocationData(
        region="Library Main",
        locked_item="Unlocked Door",
        show_in_spoiler=False),
    "Twilight Theatre - Unlock Door": PseudoregaliaLocationData(
        region="Theatre Main",
        locked_item="Unlocked Door",
        show_in_spoiler=False),
    "The Underbelly - Unlock Door": PseudoregaliaLocationData(
        region="Underbelly By Heliacal",
        locked_item="Unlocked Door",
        show_in_spoiler=False),

    # Victory Location
    "D S T RT ED M M O   Y": PseudoregaliaLocationData(
        region="The Great Door",
        locked_item="Something Worth Being Awake For"),
}
