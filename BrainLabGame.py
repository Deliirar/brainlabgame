print('''
  ,--""-.
 (_,=-   )
   `---#{
        `}
''')
print("Welcome to the brainlab.")
print("Your mission is to find the correct function of the suprachiasmatic nucleus (SpN).") 

#Write your code below this line 👇

perception = input("Do you think the SpN ir related to the perceptual process? Y or N ")
sleep = input("Do you think the SpN ir related to the sleep? Y or N ")
circadian = input("Do you think the SpN ir related to circadian rhythms system? Y or N ")

if perception=="N" and sleep=="Y" and circadian=="Y":
    print ("Perfect, you have a really god idea about the suprachiasmatic nucleus function")
else:
    print ("Oh sorry, you don't have clear the suprachiasmatic nucleus function, tho ")