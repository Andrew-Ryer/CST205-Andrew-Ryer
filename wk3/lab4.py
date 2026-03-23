import pickle
import pprint

#Task 1
with open('tarantella.txt', 'r') as my_file:
    read_poem = my_file.readlines()
count= 0
for counter, line in enumerate(read_poem):
    count+=1
    #print(f'Line {counter}: {line}')
print(f'Lines: {count}')

print("\n")

#Task 2
with open('tarantella.txt', 'r') as my_file:
    read_poem2 = my_file.read()
    words = read_poem2.split()
    count2 = 0
    for word in words:
        #print(f'{count}: {word}')
        count2+=1
    print(f'Words: {count2}')

print("\n")

#Task 3
# Enter a reminder. (Enter 'n' if done.)
# brush teeth
# Enter a reminder. (Enter 'n' if done.)
# walk dog
# Enter a reminder. (Enter 'n' if done.)
# study Python
# Enter a reminder. (Enter 'n' if done.)
# n
# Here are your reminders:
# brush teeth
# walk dog
# study Python

reminders = []

user_input = ""

# Loop as long as the input is not 'n'
while user_input != 'n':
    # Prompt the user for input and update the variable
    user_input = input("Enter a reminder. (Enter 'n' if done.) ")
    if user_input != 'n':
        print(f"{user_input}")
        reminders.append(user_input)

print("\n")
print("Here are your reminders:")
for item in reminders:
    print(item)
print("\n")

# with open("reminders.txt", "w") as my_file:
#     my_file.write(str(reminders))

# # try to re-open as list
# with open("reminders.txt", "r") as my_file:
#     my_list = my_file.read()

# print(my_list)
# print(my_list[0])

#Task 4
#TODO-Still need to save changes applied when writing to file

# reminders = []

with open('reminders.txt', 'wb') as my_file2:
    # store pickled version of audio_formats
     pickle.dump(reminders, my_file2)

with open('reminders.txt', 'rb') as my_file2:
    my_list = pickle.load(my_file2)

print(f'From my txt file: {my_list}')