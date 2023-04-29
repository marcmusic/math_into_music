# Author: M.A.R.C Original Music

PENTATONIC_SCALE = ["A", "C", "D", "F", "G"]
DIATONIC_SCALE = ["B", "C", "D", "E", "F", "G", "A"]
CHROMATIC_SCALE = ["B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#"]

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