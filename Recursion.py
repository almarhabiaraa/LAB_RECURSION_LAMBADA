
def vowels(word: str) -> int:
    
    # 🔹 Base case
    if word == "":
        return 0
    
    # 🔹 Check first character
    if word[0].lower() in "aeiou":
        return 1 + vowels(word[1:])
    else:
        return vowels(word[1:])
    

print(vowels("I LOVE python"))