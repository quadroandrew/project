# Get the frontend
from app.frontend import frontend

debug = False

front = frontend()

# This is going to allow the user to consistently try inputs until exit
while True:
    # Get the input
    input_words = input("Enter the sentence: ")

    ###
    # This will allow for printing extra lines
    if input_words == "-debug" or input_words == "debug":
        debug = not debug
        print("\nDebug: ", debug)
        continue

    # Close the while loop
    if input_words == "-exit" or input_words == "exit":
        break
    ###

    front.input_system(input_words)
