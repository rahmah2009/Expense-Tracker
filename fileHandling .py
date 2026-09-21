# # Open file
# file = open("handling.txt", "r")

# Reading file
with open("handling.txt","r") as file:
    content = file.read()

print (content)

# Reading line by line

# with open("handling.txt", "r") as file:
#     for line in file:
#         print(line)

# Append file (add)
# with open("handling.txt", "a") as file:
#     file.write("\nZainab\n")