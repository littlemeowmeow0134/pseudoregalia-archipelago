from BaseClasses import CollectionState
from typing import Dict, Callable, TYPE_CHECKING
from worlds.generic.Rules import set_rule
from .constants.difficulties import NORMAL

if TYPE_CHECKING:
    from . import PseudoregaliaWorld
else:
    PseudoregaliaWorld = object


class PseudoregaliaRulesHelpers:
    world: PseudoregaliaWorld
    player: int
    region_rules: Dict[str, Callable[[CollectionState], bool]]
    location_rules: Dict[str, Callable[[CollectionState], bool]]
    required_small_keys: int = 6  # Set to 7 for Normal logic.

    def __init__(self, world: PseudoregaliaWorld) -> None:
        self.world = world
        self.player = world.player

        self.region_rules = {
            "Empty Bailey -> Castle Main": lambda state: True,
            "Empty Bailey -> Theatre Pillar": lambda state: True,
            "Empty Bailey -> Tower Remains": lambda state:
                self.has_gem(state)
                or state.has_all({"Slide", "Sunsetter"}, self.player)
                or self.get_kicks(state, 1),
            "Tower Remains -> Underbelly Little Guy": lambda state:
                self.has_plunge(state),
            "Tower Remains -> The Great Door": lambda state:
                self.has_gem(state) and self.get_kicks(state, 3),
            "Theatre Main -> Keep Main": lambda state:
                self.has_gem(state),
            "Theatre Pillar -> Theatre Main": lambda state:
                state.has_all({"Sunsetter", "Cling Gem"}, self.player)
                or self.has_plunge(state) and self.get_kicks(state, 4),
            "Theatre Outside Scythe Corridor -> Theatre Main": lambda state:
                self.has_gem(state) and self.get_kicks(state, 3)
                or self.has_gem(state) and self.can_slidejump(state),
        }

        self.location_rules = {
            "Empty Bailey - Solar Wind": lambda state:
                self.has_slide(state),
            "Empty Bailey - Cheese Bell": lambda state:
                self.can_slidejump(state) and self.get_kicks(state, 1) and self.has_plunge(state)
                or self.can_slidejump(state) and self.has_gem(state)
                or self.get_kicks(state, 3) and self.has_plunge(state),
            "Empty Bailey - Inside Building": lambda state:
                self.has_slide(state),
            "Empty Bailey - Center Steeple": lambda state:
                self.get_kicks(state, 3)
                or state.has_all({"Sunsetter", "Slide"}, self.player),
            "Empty Bailey - Guarded Hand": lambda state:
                self.has_plunge(state)
                or self.has_gem(state)
                or self.get_kicks(state, 3),
            "Twilight Theatre - Soul Cutter": lambda state:
                self.can_strikebreak(state),
            "Twilight Theatre - Corner Beam": lambda state:
                self.has_gem(state) and self.get_kicks(state, 3)
                or self.has_gem(state) and self.can_slidejump(state)
                or self.get_kicks(state, 3) and self.can_slidejump(state),
            "Twilight Theatre - Locked Door": lambda state:
                self.has_small_keys(state)
                and (
                    self.has_gem(state)
                    or self.get_kicks(state, 3)),
            "Twilight Theatre - Back Of Auditorium": lambda state:
                self.get_kicks(state, 3)
                or self.has_gem(state),
            "Twilight Theatre - Murderous Goat": lambda state: True,
            "Twilight Theatre - Center Stage": lambda state:
                self.can_soulcutter(state) and self.has_gem(state) and self.can_slidejump(state)
                or self.can_soulcutter(state) and self.has_gem(state) and self.get_kicks(state, 1),
            "Tower Remains - Cling Gem": lambda state:
                self.get_kicks(state, 3),
            "Tower Remains - Atop The Tower": lambda state: True,
        }

        if world.options.shuffle_goatlings:
            self.location_rules.update({
                # Goatlings
                # "Dilapidated Dungeon - the goatling who fell out his cage":
                # #Lock::None,
                # "Castle Sansa - the goatling lamenting the skill issue of players who need a map":
                # #Lock::None,
                # "Castle Sansa - the goatling who wants to lick the checkpoint":
                # #Lock::None,
                # "Castle Sansa - the goatling who wanted to see the armour display":
                # #Lock::None,
                "Castle Sansa - the goatling about to jump into the haze": lambda state:
                    self.has_breaker(state)
                    or (self.has_plunge(state)
                        and self.trick("Knowledge", "Normal")),  # TODO double check this is equivilant
                # Any(&[ // Just need to break the wall.. nothing new
                #     Powerup(A::DreamBreaker),
                #     All(&[
                #         Powerup(A::Sunsetter),
                #         Trick(T::Knowledge, D::Normal),
                #     ])
                # ]),
                "Castle Sansa - the goatling that calls you bubble girl": lambda state:
                    self.get_kicks(state, 1)
                    or self.has_gem(state, 4),
                # Any(&[
                #     Powerup(A::HeliacalPower),
                #     Powerup(A::ClingGem(4)),
                # ]),
                #  "Castle Sansa - the goatling in the gazebo":
                #  #Lock::None,
                #  "Sansa Keep - the goatling sad about the lack of furniture":
                #  #Lock::None,
                #  "Sansa Keep - the goatling collapsing out of reality":
                #  #Lock::None,
                "Empty Bailey - the goatling who's hiding": lambda state:
                    self.has_slide(state),
                # Powerup(A::Slide), // Theres another way to get TO the item, not putting it in since its a one way unless it is slide though...
                #  "Twilight Theatre - the goatling who can eat 20 beans at least":
                #  #Lock::None,
                #  "Twilight Theatre - the goatling who thought the theatre was safe":
                #  #Lock::None,
                #  "Twilight Theatre - the first goatling who really wanted to see the show":
                #  #Lock::None,
                #  "Twilight Theatre - the second goatling who really wanted to see the show":
                #  #Lock::None,
                "Twilight Theatre - the goatling that will kill again": lambda state:
                    any([
                        self.can_slidejump(state) and self.get_kicks(state, 1),
                        self.get_kicks(state, 3),
                        self.has_gem(state, 6),
                        ]),
                # Any(&[
                #     All(&[Powerup(A::SolarWind), Powerup(A::HeliacalPower)]),
                #     Powerup(A::SunGreaves),
                #     Powerup(A::ClingGem(6))
                # ]),
            })

        if world.options.shuffle_chairs:
            self.location_rules.update({
                # Chairs
                # "Castle Sansa - first chair next to the goatling who wants to lick the checkpoint":
                # # locks: Lock::None,
                # "Castle Sansa - second chair next to the goatling who wants to lick the checkpoint":
                # # locks: Lock::None,
                # "Castle Sansa - third chair next to the goatling who wants to lick the checkpoint":
                # # locks: Lock::None,
                # "Castle Sansa - the chair in the gazebo":
                # # locks: Lock::None,
                # "Listless Library - the chair at the entrance":
                # # locks: Lock::None,
                # "Listless Library - the chair after the normal sun greaves location":
                # # locks: Lock::None,
                "Listless Library - the chair next to the egg nest": lambda state:
                    any([
                        self.get_kicks(state, 3),
                        self.has_gem(state, 4),
                        self.can_slidejump(state)
                        ]),
                # locks: Any(&[
                #     Powerup(A::SunGreaves),
                #     Powerup(A::ClingGem(4)),
                #     Powerup(A::SolarWind),
                # ]),

                # "Sansa Keep - the chair collapsing out of reality":
                # # locks: Lock::None,

                "Sansa Keep - the chair in the middle of the parkour": lambda state:
                    any([
                        all([
                            self.can_bounce(state),
                            any([
                                all([
                                    self.has_gem(state, 4),
                                    any([self.has_plunge(state), self.get_kicks(state, 3)]),
                                    ]),
                                all([self.has_plunge(state), self.get_kicks(state, 3)])
                                ]),
                            ]),
                        all([
                            self.has_breaker(state),
                            self.has_slide(state),
                            self.can_slidejump(state),
                            self.has_plunge(state),
                            self.has_gem(state, 2),
                            self.get_kicks(state, 3),
                            ])
                        ]),
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

                # "Twilight Theatre - first chair around the table":
                # # TODO may need additional logic
                # # locks: Lock::None,
                # "Twilight Theatre - second chair around the table":
                # # TODO may need additional logic
                # # locks: Lock::None,
                # "Twilight Theatre - third chair around the table":
                # # TODO may need additional logic
                # # locks: Lock::None,
                # "Twilight Theatre - the chair next to the books":
                # # TODO may need additional logic
                # # locks: Lock::None,
                "Twilight Theatre - the chair near the courtyard": lambda state:
                    any([
                        self.has_gem(state, 4),
                        all([self.can_slidejump(state), self.get_kicks(state, 4)]),
                    ]),
                # TODO may need additional logic
                # locks: Any(&[
                #     Powerup(A::ClingGem(4)),
                #     All(&[Powerup(A::SolarWind), Powerup(A::HeliacalPower), Powerup(A::SunGreaves)]),
                # ]),

                "Twilight Theatre - the chair in the soul cutter zone": lambda state:
                    all([
                        self.can_strikebreak(state),
                        self.has_gem(state, 6),
                        any([
                            all([
                                self.can_strikebreak(state),
                                self.can_slidejump(state),
                                self.get_kicks(state, 4),
                                self.has_plunge(state),
                                self.trick("ClingAbuse", "Expert"),
                                self.trick("OneWall", "Expert"),
                                self.trick("Movement", "Insane"),
                                self.trick("Momentum", "Expert"),
                            ]),
                            all([
                                self.can_soulcutter(state),
                                any([
                                    self.get_kicks(state, 1),
                                    self.can_slidejump(state),
                                ]),
                            ]),
                        ]),
                    ]),
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
            })

        if world.options.shuffle_notes:
            self.location_rules.update({
                # Notes
                "Listless Library - the note next to the egg nest": lambda state:
                    any([
                        self.get_kicks(state, 3),
                        self.has_gem(state, 4),
                        self.can_slidejump(state),
                    ]),
                # locks: Any(&[
                #     Powerup(A::SunGreaves),
                #     Powerup(A::ClingGem(4)),
                #     Powerup(A::SolarWind),
                # ]),

                "The Underbelly - the note on a high ledge in the big room": lambda state:
                    all([
                        self.get_kicks(state, 1),
                        self.has_plunge(state),
                        any([
                            self.has_gem(state, 4),
                            self.get_kicks(state, 4),  # to account for the 1 already in the all clause
                            self.can_slidejump(state),
                        ]),
                    ]),
                # locks: All(&[ // Leaving as is for now.
                #     Powerup(A::HeliacalPower),
                #     Powerup(A::Sunsetter),
                #     Any(&[
                #         Powerup(A::ClingGem(6)),
                #         Powerup(A::SunGreaves),
                #         Powerup(A::SolarWind),
                #     ]),
                # ]),

                "The Underbelly - the note behind the locked door": lambda state:
                    self.has_small_keys(state),
                # locks: Lock::SmallKey,

                "The Underbelly - the note near the empty bailey entrance": lambda state:
                    any([
                        self.get_kicks(state, 3),
                        all([self.get_kicks(state, 1), self.has_plunge(state)]),
                        self.has_gem(state, 6),
                        self.can_bounce(state),
                        self.can_slidejump(state),
                        all([self.get_kicks(state, 1), self.trick("ReverseKick", "Normal")]),
                        all([self.has_plunge(state), self.trick("Movement", "Normal")]),
                    ]),
                # locks: Any(&[
                #     Powerup(A::SunGreaves),
                #     All(&[Powerup(A::HeliacalPower), Powerup(A::Sunsetter)]),
                #     Powerup(A::ClingGem(6)),
                #     Powerup(A::AscendantLight),
                #     Powerup(A::SolarWind),
                #     All(&[Powerup(A::HeliacalPower), Trick(T::ReverseKick, D::Normal)]),
                #     All(&[Powerup(A::Sunsetter), Trick(T::Movement, D::Normal)]),
                # ]),
            })

    def trick(self, category: str, difficullty: str):
        # will eventually check self.world.options for the correct values
        return True

    def has_breaker(self, state) -> bool:
        return state.has_any({"Dream Breaker", "Progressive Dream Breaker"}, self.player)

    def has_slide(self, state) -> bool:
        return state.has_any({"Slide", "Progressive Slide"}, self.player)

    def has_plunge(self, state) -> bool:
        return state.has("Sunsetter", self.player)

    def has_gem(self, state, count: int = 6) -> bool:
        clings: int = 0
        if state.has("Cling Gem", self.player):
            clings += 6
        clings += state.count("Progressive Cling", self.player)
        return clings >= count

    def can_bounce(self, state) -> bool:
        return self.has_breaker(state) and state.has("Ascendant Light", self.player)

    def can_attack(self, state) -> bool:
        """Used where either breaker or sunsetter will work, for example on switches.
        Using sunsetter is considered Obscure Logic by this method."""
        raise Exception("can_attack() was not set")

    def get_kicks(self, state, count: int) -> bool:
        kicks: int = 0
        if (state.has("Sun Greaves", self.player)):
            kicks += 3
        kicks += state.count("Heliacal Power", self.player)
        kicks += state.count("Air Kick", self.player)
        return kicks >= count

    def kick_or_plunge(self, state, count: int) -> bool:
        """Used where one air kick can be replaced with sunsetter.
        Input is the number of kicks needed without plunge."""
        total: int = 0
        if (state.has("Sun Greaves", self.player)):
            total += 3
        if (state.has("Sunsetter", self.player)):
            total += 1
        total += state.count("Heliacal Power", self.player)
        total += state.count("Air Kick", self.player)
        return total >= count

    def has_small_keys(self, state) -> bool:
        if not self.can_attack(state):
            return False
        return state.count("Small Key", self.player) >= self.required_small_keys

    def navigate_darkrooms(self, state) -> bool:
        # TODO: Update this to check obscure tricks for breaker only when logic rework nears completion
        return self.has_breaker(state) or state.has("Ascendant Light", self.player)

    def can_slidejump(self, state) -> bool:
        return (state.has_all({"Slide", "Solar Wind"}, self.player)
                or state.count("Progressive Slide", self.player) >= 2)

    def can_strikebreak(self, state) -> bool:
        return (state.has_all({"Dream Breaker", "Strikebreak"}, self.player)
                or state.count("Progressive Dream Breaker", self.player) >= 2)

    def can_soulcutter(self, state) -> bool:
        return (state.has_all({"Dream Breaker", "Strikebreak", "Soul Cutter"}, self.player)
                or state.count("Progressive Dream Breaker", self.player) >= 3)

    def knows_obscure(self, state) -> bool:
        return self.world.options.obscure_logic.value

    def set_pseudoregalia_rules(self) -> None:
        multiworld = self.world.multiworld
        split_kicks = bool(multiworld.split_sun_greaves[self.player])
        if bool(multiworld.obscure_logic[self.player]):
            self.knows_obscure = lambda state: True
            self.can_attack = lambda state: self.has_breaker(state) or self.has_plunge(state)
        else:
            self.knows_obscure = lambda state: False
            self.can_attack = lambda state: self.has_breaker(state)

        logic_level = multiworld.logic_level[self.player].value
        if logic_level == NORMAL:
            self.required_small_keys = 7

        for name, rule in self.region_rules.items():
            entrance = multiworld.get_entrance(name, self.player)
            set_rule(entrance, rule)
        for name, rule in self.location_rules.items():
            if name.startswith("Listless Library"):
                if split_kicks and name.endswith("Greaves"):
                    continue
                if not split_kicks and name[-1].isdigit():
                    continue
            location = multiworld.get_location(name, self.player)
            set_rule(location, rule)

        set_rule(multiworld.get_location("D S T RT ED M M O   Y", self.player), lambda state:
                 state.has_all({
                     "Major Key - Empty Bailey",
                     "Major Key - The Underbelly",
                     "Major Key - Tower Remains",
                     "Major Key - Sansa Keep",
                     "Major Key - Twilight Theatre",
                 }, self.player))
        multiworld.completion_condition[self.player] = lambda state: state.has(
            "Something Worth Being Awake For", self.player)
