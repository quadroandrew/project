from app import frontend

print("\nTest for invalid words")

# Set up two tests: a good sentence and a bad sentence
good_test = "I see it"
bad_test = "I see Jane"

frontend.input_system(good_test)
frontend.input_system(bad_test)

print("\nTest for lowercasing")

# Set up two tests: a good sentence and a bad sentence
lower_test = "I SEE it"
print("'", lower_test, "'")
frontend.input_system(lower_test)
