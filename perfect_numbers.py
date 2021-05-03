def classify(number: int) -> str:
    aliquot_sum = 0
    if number > 0:
        for n in range(1, number):
            if number % n == 0:
                aliquot_sum += n

        if aliquot_sum == number:
            return "perfect"
        elif aliquot_sum > number:
            return "abundant"
        elif aliquot_sum < number:
            return "deficient"
    else:
        raise ValueError(r".+")
