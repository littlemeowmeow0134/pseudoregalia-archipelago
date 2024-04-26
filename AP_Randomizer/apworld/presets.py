from typing import Dict, Any 
    # this is probly not importing anything atm/yet ?
    # I also haven't tested if any of this works, and got no clue how to code things
    # but could be a nice start to have once added as a supported game
from .options import * # think this is required for custom options ?
#from .constants.difficulties import NORMAL, HARD, EXPERT, LUNATIC # no clue if this is required ?

pseudoregalia_options_presets: Dict[str, Dict[str, Any]] = {
    # saw pseudoregalia_options, so this should follow the proper naming scheme ?
    
    # Extra easy settings
    "Easy": {
        "progression_balancing": 99,
        "logic_level": "normal",
    },
    
    # As vanilla as it can get
    "Normal": {
        "progression_balancing": 50,
        "logic_level": "normal",
    },
    
    # Bit less progression
    "Hard": {
        "progression_balancing": 40,
        "logic_level": "hard",
    },
    
    # low progression & split greaves, death link enabled as deaths are not that punishing
    "Expert": {
        "progression_balancing": 30,
        "logic_level": "expert",
        "obscure_logic": "true",
        "split_sun_greaves": "true",
        "death_link": "true",
    },
    
    # Think logic on its own should make up most of the challenge, even with similar settings to expert
    # 0-20 progression wouldn't really make it any harder
    "Lunatic": {
        "progression_balancing": 30,
        "logic_level": "lunatic",
        "obscure_logic": "true",
        "split_sun_greaves": "true",
        "death_link": "true",
    },

    # Everything randomized
    "All_random": {
        "progression_balancing": "random",
        "accessibility": "random",
        "logic_level": "random",
        "obscure_logic": "random",
        "progressive_breaker": "random",
        "progressive_slide": "random",
        "split_sun_greaves": "random",
        "death_link": "random",
    },
}