#step1:importing random module
import random

#step2:create a list of subjects,objects and actions of specific genres
genres= {
    "miscellaneous": {
        "subjects": ["varsha", "om", "chaitanya", "Narendra modi", "Draupadi Murumu", "Prime Minister", "nokia"],
        "actions": ["is dancing", "playing", "is working at", "tremendously facing financial condition downfall", "riding a", "wedding"],
        "objects": ["delhi", "new place", "banglore", "home", "rajajinagar", "bennergatta", "inside parliament"]
    },
     "politics": {
        "subjects": ["Narendra Modi", "Prime Minister", "Opposition Leader", "President"],
        "actions": ["is addressing", "is debating", "is signing", "is visiting"],
        "objects": ["the parliament", "a new policy", "an international summit", "the election rally"]
    },
    "sports": {
        "subjects": ["Virat Kohli", "Serena Williams", "LeBron James", "Roger Federer"],
        "actions": ["is scoring", "is training", "is winning", "is injured in"],
        "objects": ["the final match", "a practice session", "the championship", "a friendly game"]
    },
    "dance": {
        "subjects": ["Varsha", "Om", "Chaitanya", "The dance troupe", "Narendra Modi"],
        "actions": ["is performing", "is rehearsing", "is choreographing", "is leading", "is mastering"],
        "objects": ["a classical ballet", "a hip-hop routine", "a traditional folk dance", "a contemporary piece", "a wedding dance"]
    },
    "songs": {
        "subjects": ["The singer", "The band", "Narendra Modi", "Varsha", "Om"],
        "actions": ["released", "is composing", "is remixing", "is performing", "is recording"],
        "objects": ["a new pop song", "a soulful ballad", "a trending hip-hop track", "a patriotic anthem", "a wedding song"]
    },
    "films": {
        "subjects": ["The director", "The lead actor", "Narendra Modi", "Varsha", "Om"],
        "actions": ["is shooting", "is directing", "is starring in", "is producing", "is promoting"],
        "objects": ["a blockbuster movie", "a romantic comedy", "an action thriller", "a documentary film", "a wedding drama"]
    }
}
#user can pick genre of their choice
print("Available genres are:")
for genre in genres:
    print(f"-{genre}")

userchoice=input("choose a genre of your choice:").strip().lower()

if userchoice not in genres:
    print("Looks like you have chosen wrong genre,pick genre from the list above or default to miscellaneous")
    userchoice="miscellaneous"#default

#selecting the subject,object and actions of particular genre selected
subjects=genres[userchoice]["subjects"]
actions=genres[userchoice]["actions"]
objects=genres[userchoice]["objects"]

#step3:printing of headlines ,start the while loop
#open the headline in the write mode to save the output as textfile
with open("headlines.txt","a")as file:
    while True:
        subject=random.choice(subjects)#generating random subject from list of subjects
        action=random.choice(actions)#genearting random actions from list of actions
        object=random.choice(objects)#generating random objects from list of objects

        headline=f"BREAKING NEWS: {subject} {action} {object}"#string formatting
        print("\n"+headline)
        file.write(headline+"\n")#saving to the file
        
        #takes in he user input
        user_input=input("\nDo you want another headline to be generated?(yes/no)").strip().lower()
        if(user_input=="no"):#if user doesnt want another headline, exit
             break

print("\nThanks for using fake headline generator")