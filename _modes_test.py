from transformer_algorithms.util import music_scales

for mode in music_scales.MODES:
    print(str(music_scales.get_modal_scale(mode)) + mode.name)