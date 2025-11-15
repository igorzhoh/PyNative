# Task: String slicing

sentence = "Python programming is fun!"

# Slice the first word
part1 = sentence[0:6]          # from 0 to 5
print("Word 1:", part1)

# Slice the second word
part2 = sentence[7:18]         # from 7 to 17
print("Word 2:", part2)

# Last word
part3 = sentence[-4:]          # last 4 simbols
print("Last word:", part3)

# Every second character
every_second = sentence[::2]   # step = 2
print("Every 2nd char:", every_second)

# Reverse the sentence
reversed_sentence = sentence[::-1]
print("Reversed:", reversed_sentence)




# Format - Strings



# Upper Case / Lower Case / Remove Whitespace / Replace String / Split String

text = "hello world"
upper_text = text.upper()
print(upper_text)  # "HELLO WORLD"



text = "PYTHON"
lower_text = text.lower()
print(lower_text)  # "python"



text = "   data science   "
clean_text = text.strip()
print(clean_text)  # "data science"



text = "Good morning"
new_text = text.replace("morning", "evening")
print(new_text)  # "Good evening"



text = "Python is fun"
words = text.split()
print(words)  # ['Python', 'is', 'fun']





#Escape Characters


# Task:

#"Once upon a time," she said, "there was a coder named Dmitry."
#	He would often say:
#		'Python makes programming fun!'
#End of story.


story = "\"Once upon a time,\" she said, \"there was a coder named Dmitry.\"\n" \
        "\tHe would often say:\n" \
        "\t\t'Python makes programming fun!'\n" \
        "End of story."

print(story)
