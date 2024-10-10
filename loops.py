# 1
for x in "Python":
    print(x)
# 2
vowels_cnt = 0
for x in "data science":
    if x in "AEIUOaeiou":
        vowels_cnt += 1
print("data science has ", vowels_cnt)

# 3
rever = ""
for c in "hello world":
    rever = c + rever
print(rever)


# 4
for x in "coding":
    print(ord(x))


# 5
e_cnt = 0
for ee in "experience":
    if ee == "e":
        e_cnt += 1
print("experience has e", e_cnt)

# 6
edu = ""
for u in "education":
    if u in "AEIUOaeiou":
        edu = edu + "*"
    else:
        edu = edu + u
print(edu)

# 7
loop = "looping"
for x in range(0,len(loop),2):
    print(loop[x])

# 8
map = {}
cnt = 0
for ch in "swiss":
    map[ch] = map.get(ch,0)+ 1
    if map[ch] == 2:
        print (ch)
        break

# 9 
upper_sen = ""
for x in "machine learning is fun":
    upper_sen = upper_sen + x.upper() 
print(upper_sen)

# 10
word = "racecar"
re_word = "".join(reversed(word))
for f in range(len(word)):
    if word[f] != re_word[f]:
        error = 1
        break
    else :
        error = 0
if error == 1:
    print("this is not match")
else:
    print("This is same forwards and backwards.")
