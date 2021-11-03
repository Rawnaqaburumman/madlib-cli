
import re
def read_template(bath):
      """
    This function is used to read the files.
    """


    
      with open(bath)as file:
            return file.read()

#---------------------------------------------------------------------------------------
def parse_template(item):
 """
This function used to parse the file content into usable parts
 """

 testing=re.findall(r'{(.*?)}',item)
 x= tuple(testing)
 testing1=re.sub(r'{(.*?)}',"{}",item)   
 return testing1,x

#--------------------------------------------------------------------------------------

def merge(file:str,x):
    """
    This function used to insert the values from input to the text that we want to change it.
    """
    arbit=file.format(*x)
    return arbit


def write_new_file(texxt: str):
    
    with open('assets/video_game_result.txt', 'w') as video_game:
        video_game.write(texxt)


#--------------------------------------------------------------------------------

if __name__=="__main__":

    print("Welcome to Madlib Game At this Game we will ask you to enter some words ... Lets start !")

    sample=read_template("assets/vedio_game.txt")

    testing=re.findall(r'{(.*?)}',sample)
    modifiedarray1=[]

    for i in testing:
        userInput=input(f'Please enter a {i} ')
        modifiedarray1.append(userInput)

    modifedArray=tuple(modifiedarray1)

  

    texteddited=re.sub(r'{(.*?)}',"{}",sample)

   
    print(merge(texteddited,modifedArray))
    write_new_file(merge(texteddited,modifedArray))



