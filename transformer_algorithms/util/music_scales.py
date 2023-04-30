# Author: M.A.R.C Original Music

from .diatonic_mode import DiatonicMode


PENTATONIC_SCALE = ["C", "D", "F", "G", "A"]
DIATONIC_SCALE = ["C", "D", "E", "F", "G", "A", "B"]
CHROMATIC_SCALE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

INVERSE_PENTATONIC_SCALE = ["D", "C", "A", "G", "F"]
INVERSE_DIATONIC_SCALE = ["D", "C", "B", "A", "G", "F", "E"]
INVERSE_CHROMATIC_SCALE = ["C#", "C", "B", "A#", "A", "G#", "G", "F#", "F", "E", "D#", "D"]

MUSIC_SCALES = {
    "C-Pen": PENTATONIC_SCALE,
    "C-Ipen": INVERSE_PENTATONIC_SCALE,
    "C-Dia": DIATONIC_SCALE,
    "C-Idia": INVERSE_DIATONIC_SCALE,
    "C-Chr": CHROMATIC_SCALE,
    "C-Ichr": INVERSE_CHROMATIC_SCALE
}

MODES = [
    DiatonicMode("Ionian", 6),
    DiatonicMode("Dorico", 0),
    DiatonicMode("Phrygian", 1),
    DiatonicMode("Lydian", 2),
    DiatonicMode("Mixolydian", 3),
    DiatonicMode("Aeolian", 4),
    DiatonicMode("Locrian", 5),
]

def get_modal_scale(diatonic_mode) -> list[int]:
    return DIATONIC_SCALE[diatonic_mode.offset:] + DIATONIC_SCALE[0:diatonic_mode.offset]
