# Author: M.A.R.C Original Music

from .diatonic_mode import DiatonicMode


PENTATONIC_SCALE = ['C', 'D', 'F', 'G', 'A']
DIATONIC_SCALE = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
CHROMATIC_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# INVERSE_PENTATONIC_SCALE = ["D", "C", "A", "G", "F"]
# INVERSE_DIATONIC_SCALE = ["D", "C", "B", "A", "G", "F", "E"]
# INVERSE_CHROMATIC_SCALE = ["C#", "C", "B", "A#", "A", "G#", "G", "F#", "F", "E", "D#", "D"]

def offset_scale(music_scale, offset) -> list[int]:
    return music_scale[offset:] + music_scale[0:offset]

def invert_scale(music_scale) -> list[int]:
    music_scale.reverse()
    return offset_scale(music_scale, len(music_scale) -1)

MUSIC_SCALES = {
    "C-Pen": PENTATONIC_SCALE,
    "C-Ipen": invert_scale(PENTATONIC_SCALE[:]),
    "C-Dia": DIATONIC_SCALE,
    "C-Idia": invert_scale(DIATONIC_SCALE[:]),
    "C-Chr": CHROMATIC_SCALE,
    "C-Ichr": invert_scale(CHROMATIC_SCALE[:])
}

MODES = [
    DiatonicMode("Ionian", 0),
    DiatonicMode("Dorico", 1),
    DiatonicMode("Phrygian", 2),
    DiatonicMode("Lydian", 3),
    DiatonicMode("Mixolydian", 4),
    DiatonicMode("Aeolian", 5),
    DiatonicMode("Locrian", 6),
]

def get_modal_scale(diatonic_mode) -> list[int]:
    return offset_scale(DIATONIC_SCALE, diatonic_mode.offset)