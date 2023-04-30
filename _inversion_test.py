from transformer_algorithms.util import music_scales

for scale in music_scales.MUSIC_SCALES.items():
    print(scale[0] + '\n' +str(scale[1]))