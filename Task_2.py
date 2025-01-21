from collections import deque

def is_palindrome(input_string):
    normalized_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    char_deque = deque(normalized_string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

if __name__ == "__main__":
    test_string = input("Введіть рядок для перевірки: ")
    if is_palindrome(test_string):
        print("Рядок є паліндромом.")
    else:
        print("Рядок не є паліндромом.")
