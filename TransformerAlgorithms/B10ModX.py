#! /usr/bin/python3
# Author: M.A.R.C Original Music

scale = []

def get_note(num):
	divisor = len(scale)
	modNum = num % divisor
	return scale[modNum]

def convert_sequence(sequence, musical_scale) -> list[int]:
	musical_sequence = []
	scale = musical_scale

	for num in sequence:
		music_note = get_note(num)
		musical_sequence.append(music_note)

	return musical_sequence
