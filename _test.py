from numeric_sequence_generators import fibonacci
from numeric_sequence_generators import pascal_triangle
from numeric_sequence_generators import perrin_numbers
from numeric_sequence_generators import prime_numbers
from numeric_sequence_generators import happy_numbers
from numeric_sequence_generators import lucky_numbers
from numeric_sequence_generators import exponential_numbers

print(pascal_triangle.generate_sequence())
print(fibonacci.generate_sequence())
print(perrin_numbers.generate_sequence(10))
print(prime_numbers.generate_sequence(10))
print(happy_numbers.generate_sequence(10))
print(lucky_numbers.generate_sequence(10))
print(exponential_numbers.generate_sequence(10, 3))