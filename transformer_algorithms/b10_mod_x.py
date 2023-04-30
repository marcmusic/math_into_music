#! /usr/bin/python3
# Author: M.A.R.C Original Music

from .util.musical_sequence import MusicalSequence

global scale

def get_note(num):
	divisor = len(scale)
	modNum = num % divisor
	return scale[modNum]

def convert_sequence(num_sequence, music_scale) -> MusicalSequence:
	mus_scale = music_scale[1]
	max_mus_scale_index = len(music_scale[1]) - 1

	global scale 
	# The music scale is shifted one value up, so C is index 1.
	scale = mus_scale[max_mus_scale_index:] + mus_scale[0:max_mus_scale_index]
	
	mus_sequence = []
	algorithm_id = f'B10Mod{str(len(music_scale[1]))}.{music_scale[0]}'

	for num in num_sequence:
		music_note = get_note(num)
		mus_sequence.append(music_note)

	return MusicalSequence(mus_sequence, algorithm_id)
