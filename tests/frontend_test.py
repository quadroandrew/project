from app.frontend import frontend

print("\nTest for invalid words")

# Set up two tests: a good sentence and a bad sentence
good_test = "I see it"
bad_test = "I see Jane"

front = frontend()

good = front.input_system(good_test)
bad = front.input_system(bad_test)

for word_object in good:
    print(word_object.word, "is", word_object.ety)

for word_object in bad:
    print(word_object.word, "is", word_object.ety)

print("\nTest for lowercasing")

# Set up two tests: a good sentence and a bad sentence
lower_test = "I SEE it"
print("'", lower_test, "'")
for word_object in front.input_system(lower_test):
    print(word_object.word, "is", word_object.ety)
