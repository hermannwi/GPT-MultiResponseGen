import os
import openai
import csv
from datetime import date

# Sets the key for the openai api. You need to refer to the path where you saved your key.txt file
openai.api_key_path = "key.txt"

    # Generates a message based on the marker
# def generate_message(category):
#     vowels = ('a','e','i','o','u','A','E','I','O','U')
#     article = ""
#     if category[0] in vowels:
#         article = "an"
#     else:
#         article = "a"
#     return f"Write a 50 word plot summary for {article} potential {category} children's novel."



# Generates stories based on the user's input and writes them to a csv file
def generate_stories():
    messages = [ {"role": "system", "content": ""} ]
    
    # message = generate_message(category)
    message = input("Enter a prompt: ")

    # The user has to specify the number of stories to generate
    while True:
        n = int(input("Enter the number of replies to generate: "))
        # check if n is an integer
        if isinstance(n, int):
            break
        else:
            print("Please enter an integer")


    filename = input("Name the output csv file: ") + ".csv"

    # The user has to specify the temperature
    while True:
        temp = float(input("Enter the temperature: "))
        # check if temp is a float and between 0 and 1
        if isinstance(temp, float) and temp > 0 and temp <= 1:
            break
        else:
            print("Please enter a float between 0 and 1")


    # For loop that prompts chatgpt a specified number of times and for each iteration writes the prompt, reply, date and model to a csv file
    for i in range(n):
        with open (filename, "a", newline="") as f:
            writer = csv.DictWriter(f, delimiter=";", fieldnames=["prompt", "reply", "date", "modelname", "temperature"])
            # If the file is empty, it writes the fieldnames
            if os.stat(filename).st_size == 0:
                writer.writeheader()
            messages.append({"role": "user", "content": message},)
            # Creates a chatgpt model based on the previous prompts and replies
            chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=temp)
            # Removes the last prompt from the messages
            messages = messages[:-1]
            # A call to the chatgpt model that generates a reply
            reply = chat.choices[0].message.content
            unit = {"prompt": message, "reply": reply, "date": date.today(), "modelname": "gpt-3.5-turbo", "temperature": temp}
            # writes the prompt, reply, date and model to a csv file
            writer.writerow(unit)

    print(messages)
    # asks the user if they want to save the prompt
    save_prompt = input("Do you want to save the prompt? (y/n): ")
    if save_prompt == "y":
        prompt_filename = input("Name the prompt file: ")
        with open (prompt_filename + "prompt", "w", newline="") as f:
            f.write(message)
    else:
        pass
    
    # asks the user if they want to generate more stories
    more_stories = input("Do you want to generate more stories? (y/n): ")
    if more_stories == "y":
        generate_stories()
    else:
        pass


# Generate stories
stories = generate_stories()







