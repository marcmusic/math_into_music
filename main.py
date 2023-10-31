import music_xml_generator.template as XmlGenerator
import transformer_algorithms.b10_mod_x as b10_mod_x
from transformer_algorithms.util.music_scales import MUSIC_SCALES

from numeric_sequence_generators import fibonacci
from numeric_sequence_generators import pascal_triangle
from numeric_sequence_generators import perrin_numbers
from numeric_sequence_generators import prime_numbers
from numeric_sequence_generators import happy_numbers
from numeric_sequence_generators import lucky_numbers
from numeric_sequence_generators import exponential_numbers
from numeric_sequence_generators import gen1
from numeric_sequence_generators import apo

sequences = [
    fibonacci.generate_sequence(100),
    pascal_triangle.generate_sequence(10),
    perrin_numbers.generate_sequence(100),
    exponential_numbers.generate_sequence(100, 2),
    exponential_numbers.generate_sequence(100, 3),
    exponential_numbers.generate_sequence(100, 4),
    prime_numbers.generate_sequence(100),
    happy_numbers.generate_sequence(100),
    lucky_numbers.generate_sequence(100),
    gen1.generate_sequence(),
    apo.generate_sequence(),
]

for sequence in sequences:
    for scale in MUSIC_SCALES.items():
        musical_sequence = b10_mod_x.convert_sequence(sequence.numeric_sequence, scale)

        with open(f'_test_exports/{sequence.id}.{musical_sequence.algorithm_id}.musicxml', 'w') as export_file:
            export_file.write(XmlGenerator.get_xml(f'{sequence.name} - {musical_sequence.algorithm_id}', sequence.description, f'{sequence.id}.{musical_sequence.algorithm_id}', musical_sequence.sequence))

