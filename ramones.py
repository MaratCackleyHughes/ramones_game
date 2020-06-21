__author__ = 'Marat Cackley-Hughes'
# This is a simple game to play and test my skills in Python
# You enter your favorite member of the band The Ramones and you receive some information about their career in the band.

# Input list members, fav_ramone, albums_played
# Output list  fav_ramone, albums_played

# Global variables
#Declare String members[size] = "joey","johnny","tommy","dee dee","marky" 
members = ["joey","johnny","tommy","dee dee","marky" ]
# //Main Module
# Declare module main
# Declare string fav_ramone
# Declare string albums_played
# Declare string keepGoing
# Set keepGoing = "y"
# While keepGoing == "y" then
#  Set fav_ramone to input_program(fav_ramone)
#  Call function input_program
#  Set albums_played to album_program
#  Call function album_program
#  Display " Do you want to play again?"
#  Set keepGoing
#  Input keepGoing
#  Display "Enter y for yes."
# End module
def main():
 fav_ramone = ""
 albums_played = ""
 found = False
 index = 0
 size = len(members)
 keepGoing = "y"
 while keepGoing == "y":
  fav_ramone = input_program(fav_ramone,index,found,members,size)
  albums_played = album_program(fav_ramone, members)
  output_program(fav_ramone, albums_played, members)
  print("Do you want to play again?")
  keepGoing = input("Enter y for yes: ").lower()

# //Input function
# Define input_program(fav_ramone)
# Display "Welcome to The Ramones game."
# Display ("Here you enter information about your favorite Ramone")
# Display ("and receive data in return.")
# Display ("Please choose either Joey, Johnny, Dee Dee, Tommy, or if you must, Marky.")
# Set fav_ramone to input
# Display "Please enter your favorite Ramone here: "
# While fav_ramone NOT = JOEY AND fav_ramone NOT = JOHNNY AND fav_ramone NOT = TOMMY AND fav_ramone NOT = MARKY AND fav_ramone NOT = DD THEN
# Display(fav_ramone,"is not valid")
# Set fav_ramone to input
# Display "Please enter your favorite Ramone here: "
# Return fav_ramone
# End function
def input_program(fav_ramone,index,found,members,size):
    print("Welcome to The Ramones game.")
    print("Here you enter information about your favorite Ramone")
    print("and receive data in return.")
    print("Please enter either Joey, Johnny, Dee Dee, Tommy, or if you must, Marky.")
    fav_ramone = input("Please enter your favorite Ramone here: ").lower()
    while found == False and index <= size:
     if members[index].lower() == fav_ramone:
      found = True
     else:
      index = index + 1 
    return fav_ramone 

# //Album function
# Declare function album_program(fav_ramone,members)
# Declare String albums[] = "all the records", "Ramones, Leave Home, and Rocket to Russia.", "all the records until the release of Brain Drain in 1989", ""
#  If fav_ramone = members[0] then
#   Set albums_played = albums[0]
#  Else if fav_ramone = members[1] then
#   Set albums_played = albums[0]
#  Else if fav_ramone = members[2] then
#   Set albums_played = albums[1]
# Else if fav_ramone = members[3] then
#   Set albums_played = albums[2]
# End if
# Return albums_played
# End function
def album_program(fav_ramone, members):
    albums = ["all the records", "Ramones, Leave Home, and Rocket to Russia.", "all the records until the release of Brain Drain in 1989", ""]  
    if fav_ramone == members[0]:
        albums_played = albums[0]
    elif fav_ramone == members[1]:
        albums_played = albums[0]
    elif fav_ramone == members[2]:
        albums_played = albums[1]
    elif fav_ramone == members[3]:
        albums_played = albums[2]
    elif fav_ramone == members[4]:
        albums_played = ""
    return albums_played


 # //Output module

# Declare module output_program(fav_ramone, albums_played,members)
# If fav_ramone = members[0] then
#  Display fav_ramone "sang on", albums_played
# Else if fav_ramone = members[1] then
#  Display fav_ramone "played guitar on ", albums_played
# Else if fav_ramone = members[2] then
#  Display fav_ramone "played drums on ", albums_played
# Else if fav_ramone = members[3] then
#  Display fav_ramone "played bass on ", albums_played
# Else if fav_ramone = members[4] then
#  Display fav_ramone "doen't count"
# End if
# End module
def output_program(fav_ramone, albums_played,members):
    if fav_ramone == members[0]:
        print(fav_ramone.title(), "sang on", albums_played)
    elif fav_ramone == members[1]:
        print(fav_ramone.title(), "played guitar on", albums_played)
    elif fav_ramone == members[2]:
        print(fav_ramone.title(), "played drums on", albums_played)    
    elif fav_ramone == members[3]:
        print(fav_ramone.title(), "played bass on", albums_played)
    elif fav_ramone == members[4]:
        print(fav_ramone.title(), "doesn't count ", albums_played)


main()
