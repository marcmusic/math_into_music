from NumericSequenceGenerators import fibonacci
from NumericSequenceGenerators import pascal_triangle
from NumericSequenceGenerators import perrin_numbers
from NumericSequenceGenerators import prime_numbers
from NumericSequenceGenerators import happy_numbers
from NumericSequenceGenerators import lucky_numbers
from NumericSequenceGenerators import exponential_numbers

print(pascal_triangle.generate_sequence())
print(fibonacci.generate_sequence())
print(perrin_numbers.generate_sequence(10))
print(prime_numbers.generate_sequence(10))
print(happy_numbers.generate_sequence(10))
print(lucky_numbers.generate_sequence(10))
print(exponential_numbers.generate_sequence(10, 3))