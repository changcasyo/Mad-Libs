#Mad Libs is a type of word play
#Story taken from google search: https://g.christianbook.com/g/slideshow/1/173796/main/173796_5_sam.jpg and edited

print("Let's play a game! It is called Mad Libs")
player = input("What's your name?")
print("Hello " + player + "! Our story today is called Apology Letter ;)")

print("I need you to input some basic answers, whatever you can think of sky's the limit! \n Let's go!")

last_name = input("Person's last name: ")
adj1 = input("Adjective: ")
noun1 = input("Noun: ")
place1 = input("Place: ")
verb1 = input("Verb ending in -ing: ")
color1 = input("Color: ")
noun2 = input("Noun: ")
body_part1 = input("Body Part: ")
verb2 = input("Verb: ")
body_part2 = input("Body Part (plural): ")
word1 = input("Silly Word: ")
adj2 = input("Adjective: ")
noun3 = input("Noun: ")
verb3 = input("Verb: ")
noun4 = input("Plural Noun: ")
noun5 = input("Noun: ")
adj3 = input("Adjective: ")


print("\n \n \n Apology Letter \n \n")
print("Dear Mrs. " + last_name + ",")
print("       I am extremely " + adj1 + " for causing a commotion in the class on the topic of " + noun1 + " tribes of " + place1 + ".")
print("It was rude of me to burst out " + verb1 + " when you told us that the leader wore a/an " + color1 + " back shield in the shape of a winged " + noun2 + " on his " + body_part1 + ".")
print("And my action to " + verb2 + " in a circle with my " + body_part2 + " outstretched while chanting ")
chant = "%s ! %s !" % (word1, word1)
print(chant + " was extremely inappropriate, I was only trying to do the " + adj2 + " dance.")
print("I understand that I could have though of my actions especially for that kind of " + noun3 + ".")
print("I know that you " + verb3 + " very hard as a teacher and deserve respect for teaching me and my " + noun4 + " every day.")
print("I hope you accept my sincere " + noun5 + " and believe I will never do such " + adj3 + " judgement again.")
print("\n Sincerely, \n " +player)
