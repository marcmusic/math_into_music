#! /usr/bin/python3
# Author: M.A.R.C Original Music

from .util.musical_sequence import MusicalSequence

global scale

def get_note(num):
	divisor = len(scale)
	modNum = num % divisor
	return scale[modNum]

def convert_sequence(num_sequence, music_scale) -> MusicalSequence:
	global scale 
	scale = music_scale[1]
	
	mus_sequence = []

	for num in num_sequence:
		music_note = get_note(num)
		mus_sequence.append(music_note)

	return MusicalSequence(mus_sequence, f'B10Mod{str(len(music_scale[1]))}{music_scale[0]}')
