from .. import (weapons)
from .. import features as feats
from .classes import CharClass


class Sorceror(CharClass):
    class_name = 'Sorceror'
    hit_dice_faces = 6
    saving_throw_proficiencies = ('constitution', 'charisma')
    _proficiencies_text = ('daggers', 'darts', 'slings',
                           'quarterstaffs', 'light crossbows')
    weapon_proficiencies = (weapons.Dagger, weapons.Dart,
                            weapons.Sling, weapons.Quarterstaff,
                            weapons.LightCrossbow)
    class_skill_choices = ('Arcana', 'Deception', 'Insight',
                           'Intimidation', 'Persuasion', 'Religion')
    spellcasting_ability = 'charisma'
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (4, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (4, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (4, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        4:  (5, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        5:  (5, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        6:  (5, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        7:  (5, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        8:  (5, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        9:  (5, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        10: (6, 4, 3, 3, 3, 2, 0, 0, 0, 0),
        11: (6, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        12: (6, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        13: (6, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        14: (6, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        15: (6, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        16: (6, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        17: (6, 4, 3, 3, 3, 2, 1, 1, 1, 1),
        18: (6, 4, 3, 3, 3, 3, 1, 1, 1, 1),
        19: (6, 4, 3, 3, 3, 3, 2, 1, 1, 1),
        20: (6, 4, 3, 3, 3, 3, 2, 2, 1, 1),
    }