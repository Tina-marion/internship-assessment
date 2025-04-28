from typing import List

def collatz(n: int) -> List[int]:
    
    sequence = []
    while n != 1:
        sequence.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    sequence.append(1)  # Include the final 1
    return sequence

def distinct_numbers(numbers: List[int]) -> int:
   
    return len(set(numbers))