numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

def ReplaceNone(numbers):

    for number in range(len(numbers)):
        if numbers[number] is None:
            numbers[number] = 0
            numbers[number] = sum(numbers) / len(numbers)
            break
    return f"Измененный список: {numbers}"

print(ReplaceNone(numbers))