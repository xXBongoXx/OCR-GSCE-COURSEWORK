import _passCheck,random                                  ## runs the passCheck file for encrypted Uns and Pws and random to choose songs

global songs,artists,un                                  ## allows these variables to be carried between sub-routines

## Fully comented code on my school computer 
## along with correctly alighned comments 
## because OCD... but it all works the same anyway.


def auth():                                              ## links to password checking

    un=input("Enter username.\n")
    pw=input("Enter password.\n")
    temp = _passCheck.checkUser(un,pw,True,"users")       ## checks for correct username and password and loops if false and continues if true
    print(temp)                                          ##
    if not temp:                                         ## 
        auth()                                           ##
    return un                                            ## 

def devAuth(): ## Should be called add() but I got lazy sooooo...

    inp1 = 'a'
    inp2 = 'b'
    inp3 = 'c'
    inp4 = 'd'
    while inp1 != inp3 or inp2 != inp4:
        inp1 = input("Song name.\n").title()
        inp2 = input("Artist name.\n").title()
        inp3 = input("Confirm Song name.\n").title()
        inp4 = input("Confirm Artist name.\n").title()
    addSong(inp1,inp2)
    getSongs()
    menu()

def getSongs():
    f = open("songs.txt","a")                            ## Append ensures that file is present
    f.close()                                            ##  

    
    f = open("songs.txt","r")                            ## Reads file for songs and artists
    songs=[]                                             ##
    artists=[]                                           ##
    while True:                                          ##
        n = f.readline()                                 ## 
        n = n.split(',')                                 ##
        if n[0] == '' or n[0] == '\n':                   ##
            break                                        ##
        songs.append(n[0])                               ##
        artists.append(n[1])                             ##
    return songs, artists

def addSong(song,artist):                                ## Add song to txt file
    f = open("songs.txt","a")                            ##
    f.write(song.title()+','+artist.title()+',\n')                         ##
    f.close()                                            ##

def chooseSong(songs,artists):                           ## Chooses a song and artist
    num = random.randint(0,len(songs)-1)                 ##
    return songs[num],artists[num]                       ##

def playRound(roundNum):
    temp = getSongs()
    songs = temp[0]
    artists = temp[1]                                  
    print("Round %s!\n" %(roundNum))                     ## Display round
    song = chooseSong(songs,artists)
    artist = song[1]
    song = song[0]
    temp = song.split(' ')                               ## Split song name into it's words
    temp2 = []
    for i in temp:
        temp2.append(i[0])                               ## Adds first letter of each word to temp2 array
    for i in range(len(temp)):
        for x in range(len(temp[i])-1):
            temp2[i] += "-"                              ## fills words in the temp2 array with dashes to shoew length
    songDisp = ''
    for i in temp2:
        songDisp += i+' '                                    ## adds each word in the temp2 array to the string that will be displayed
    guess = input("The song is called "+songDisp+" by "+artist+", guess the song's name.\n\n").title()
    if guess != song:
        print("Incorrect guess again - ", end='')
        guess = input("The song is called "+songDisp+" by "+artist+", guess the song's name.\n\n").title()
        if guess != song:
            return False                                 ## return the Loss status
        else:
            return 1                                     ## return the score granted
    else:
        return 3                                         ## return the score granted

def gameLoop(): ## COMMENTS NEEDED
    points = 0
    roundNum = 0 
    while True:
        roundNum += 1
        result = playRound(roundNum)
        if result == False:
            break
        points += int(result)
        input(str(result)+" points gained, current score is "+str(points)+".")
        print("\n"*48)
    input("Game over!\nYour final score was "+str(points)+".")
    end(points)

def end(points): ## COMMENTS NEEDED
    f = open("hs.txt","a")
    f.close()
    f = open("hs.txt","r")
    l = f.readline()
    pls=[]
    scs=[]
    if l == '' or l == '\n':
        hs = points
        
    else:
        while not(l == '' or l == '\n'):
            l = l.split(',')
            pls.append(l[0])
            scs.append(int(l[1]))
            l = f.readline()
        f.close()
        hs = -10
        for i in range(len(scs)):
            if scs[i] > hs:
                hs = scs[i]
        if points > hs:
            print("Congratulations, you have the new highscore!")
        elif points == hs:
            print("So close, you have the joint highscore!")
        else:
            print("You were %s points behind the highscore." %(hs-points))
    if un in pls:
        count = 0
        while pls[count] != un:
            count += 1
        scs[count] = points
    else:
        pls.append(un)
        scs.append(points)
    f = open("hs.txt","w")
    for i in range(len(pls)):
        f.write(pls[i]+","+str(scs[i])+",\n")
    f.close()

def menu(): ## COMMENTS NEEDED
    print("\n"*48)
    inp = input("Add,Play or Quit?\n").title()
    if inp[0] == 'A':
        devAuth()
    elif inp[0] == 'P':
        gameLoop()
    elif inp[0] == 'Q':
        input("\n\nThank you for playing!\n\n")
        quit()
    else:
        input("*Invalid entry, enter to continue*")
    menu()


un = auth()
menu()