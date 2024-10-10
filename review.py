# iterating a string
city = "Vancouver"
vowel = ['a','e','o','u','i']

vowel_count = 0
for ch in city:
    # if ch in vowel:
    if ch in "AEIOUaeiou":
        vowel_count += 1

print(f"{city} has {vowel_count} vowels.")

#iterating a list

nums = [1, 34, 567, 49, 55, 30, 66]
even_count = 0
for num in nums:
    if num % 2 == 0:
        even_count += 1

print(f"{nums} list has {even_count} even numbers.")

# while loop with string
i = 0 # index
vowels = 0 # vowels count
while i < len(city):
    if city[i] in "AEIOUaeiou":
        vowels += 1
    i += 1

print(f"{city} has {vowels} vowels.")

# while loop with list
j = 0
even_cnt = 0
while j <len(nums):
    if  nums[j] % 2 == 0:
        even_cnt += 1
    j += 1
print(f"{nums} list has {even_cnt} even numbers.")


#while True
while True : 
    command = input("Enter the 'q to quit: ")
    if command == 'q':
        print("Bye")
        break
    elif command == "s":
        continue # continue 하면 그 다음 코드는 스킵하고 감 skip the rest
    print("Try agian")

Loop
