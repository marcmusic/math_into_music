# Author: M.A.R.C Original Music

PENTATONIC_SCALE = ["A", "C", "D", "F", "G"]
DIATONIC_SCALE = ["B", "C", "D", "E", "F", "G", "A"]
CHROMATIC_SCALE = ["B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#"]

INVERSE_PENTATONIC_SCALE = ["D", "C", "A", "G", "F"]
INVERSE_DIATONIC_SCALE = ["D", "C", "B", "A", "G", "F", "E"]
INVERSE_CHROMATIC_SCALE = ["C#", "C", "B", "A#", "A", "G#", "G", "F#", "F", "E", "D#", "D"]

MUSIC_SCALES = {
    "C1Pen": PENTATONIC_SCALE,
    "C1iPen": INVERSE_PENTATONIC_SCALE,
    "C1Dia": DIATONIC_SCALE,
    "C1iDia": INVERSE_DIATONIC_SCALE,
    "C1Chro": CHROMATIC_SCALE,
    "C1iChro": INVERSE_CHROMATIC_SCALE
}