def find_most_common_characters(input_strings):
    most_common_characters_count = 0
    most_common_characters_string = ""
    for input_string in input_strings:
        character_count = {}
        for character in input_string:
            if character.isalnum():
                character_count[character] = character_count.get(character, 0) + 1
        if character_count:
            max_character, max_count = max(character_count.items(), key = lambda item: item[1])
            if max_count > most_common_characters_count:
                most_common_characters_count = max_count
                most_common_characters_string = input_string
    return most_common_characters_string
N = int(input("Кількість рядків: "))
input_strings = []
for i in range(N):
    input_string = input(f"Введіть рядок {i+1}: ")
    input_strings.append(input_string)
result = find_most_common_characters(input_strings)
if result:
    print(f"Найбільша кількість однакових символів: {result}")
else:
    print("У рядках немає символів.")