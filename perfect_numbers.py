def classify(number: int) -> str:
    """Determine if a number is perfect, abundant, or deficient based on Nicomachus' classification scheme
    for natural numbers."""
    if number <= 0:
        raise ValueError("Only positive integers!")
    else:
        s = sum(i for i in range(1, (number//2)+1) if not number % i)
    return "perfect" if s == number else "abundant" if s > number else "deficient"
