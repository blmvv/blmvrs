def is_palindrome(word):
    return word==word[::-1]
def find_shortest_palindrome(input_string):
    words=input_string.split()
    shortest_palindrome=None
    for word in words:
        if is_palindrome(word):
            if shortest_palindrome is None or len(word) < len(shortest_palindrome):
                shortest_palindrome = word
    if shortest_palindrome:
        return f"Слово-паліндром: {shortest_palindrome}"
    else:
        return "Немає слова-паліндрому."
input_string = input("Ввевідь слова: ")
result = find_shortest_palindrome(input_string)
print(result)