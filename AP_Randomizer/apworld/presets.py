from typing import Dict, Any 
    # this is probly not importing anything atm/yet ?
    # I also haven't tested if any of this works, and got no clue how to code things
    # but could be a nice start to have once added as a supported game
from .options import * # think this is required for custom options ?
#from .constants.difficulties import NORMAL, HARD, EXPERT, LUNATIC # no clue if this is required ?

pseudoregalia_options_presets: Dict[str, Dict[str, Any]] = {
    # saw pseudoregalia_options, so this should follow the proper naming scheme ?
    
    # As vanilla as it can get
    "Normal": {
        "logic_level": "normal",
    },
    
    # Bit less progression
    "Hard": {
        "logic_level": "hard",
    },
    
    # split greaves for 1-2 kick tricks
    "Expert": {
        "logic_level": "expert",
        "obscure_logic": "true",
        "split_sun_greaves": "true",
    },
    
    # Think logic on its own should make up most of the challenge, even with similar settings to expert
    "Lunatic": {
        "logic_level": "lunatic",
        "obscure_logic": "true",
        "split_sun_greaves": "true",
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
    },
}
