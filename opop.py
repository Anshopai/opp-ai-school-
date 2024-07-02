import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib
import os 
import random 
gg = int(input('Enter 0 if you want the voice to be males and enter 1 if you want the sound to be of a girl   '))

arandom = ('rock','paper','scisors')

word = random.choice(arandom)
brandom = ('1','2','3','4','5','6','7','8','9','10')
word2 = random.choice(brandom)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[gg].id)

crandom = ('heads','tales')
word3 = random.choice(crandom)

drandom = ('Why dont scientists trust atoms?   ,,,Because they make up everything!','Why did the scarecrow win an award?,,    ,,Because he was outstanding in his field')
word4 = random.choice(drandom)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def search_wikipedia(query):
    try:

        result = wikipedia.summary(query)
    except wikipedia.exceptions.DisambiguationError as e:
        
        result = wikipedia.summary(e.options[0])
    except wikipedia.exceptions.PageError:
        
        result = "No page found for the query."
    
    return result






def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print('Good Morning!')

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        print("Good Afternoon!")
        
    else:
        speak("Good Evening!")  
        print('Good Evening!')

     


speak ('if you are a male enter m and if you are a female enter f   ')


qq = input('if you are a male enter m and if you are a female enter f    ')

if qq == 'm' :

    wishMe()

    speak ('Sir')

    print ('Sir')

    speak (" I am an ai model created by Ansh bhatia You can ask me to do a lot of things so  Please tell me how may I help you")

    print (" I am an ai model created by Ansh bhatia You can ask me to do a lot of things so  Please tell me how may I help you")      




elif qq == 'f' :

    wishMe()

    print('Mam')

    speak('Mam')

    print (" I am an ai model created by Ansh bhatia You can ask me to do a lot of things so  Please tell me how may I help you")

    speak  (" I am an ai model created by Ansh bhatia You can ask me to do a lot of things so  Please tell me how may I help you")


    







def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anahopff2312@gmail.com,', 'vishnu@2312')
    server.sendmail('anahopff2312@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    

    # if 1:
        
        speak ('What do you want me to do ')

        query = input(('What do you want me to do '))

        


        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            
            # speak('Searching Wikipedia...')
            
            # ans =  input ("wikipedia", "")
            
            # results = wikipedia.summary(ans, sentences=2)
            
            # speak("According to Wikipedia")
            
            # print(results)
            
            # speak(results)

            zx =  (input('Enter the thing you want to search '))
            
            speak ('Enter the thing you want to search ')


            print(search_wikipedia(zx))


            speak(search_wikipedia(zx))



        elif 'youtube' in query:

            webbrowser.open("youtube.com")




        elif 'google' in query:
          
            webbrowser.open("google.com")



        elif 'stackoverflow' in query:
          
            webbrowser.open("stackoverflow.com")   




        elif 'music' in query:
           
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
           
            songs = str('Sorry this function is not available on this divice is not available right now ')
          
            print (songs)  
         
            speak (songs)  
        


        elif 'song'  in query :
            
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'

            print   ('Sorry this function is not available on this divice is not available right now ')

            speak ('Sorry this function is not available on this divice is not available right now ')






        elif 'time' in query:
           
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    

            print('{strTime}')
           
            speak(f"Sir, the time is {strTime}")






        # elif 'code' in query:
        
        #     codePath = 'C:\Users\Dell\OneDrive\Desktop\my ai'  
                    
        #     os.startfile(codePath)







        elif 'email' in query:
            try:
                speak("What should I say?")
              
                content = (input('Enter what do you want me to send '))

                speak ('Enter the gmail you want me to send this to ')
               
                to = (input('Enter the gmail of the person to which you want me to send this '))    
               
                sendEmail(to, content)
              
                speak("Email has been sent!")
           
            except Exception as e:
            
                print(e)
           
                speak("Sorry Mr ansh . I am not able to send this email")   
       










        elif  'currency converter ' in query :
            
            print ("currency converter has started ")
            
            speak ("currency converter has started ")
            
            speak ("1st currency will be converted to 2nd currency ")
            
            print("1st currency will be converted to 2nd currency ") 
            
            d = (input("Enter the 1st currency "))
            
            e = (input ("Enter the 2nd currency "))
            
            f = int(input("Enter the amount ") )
            
            if d == 'INR' :
                
                if e == 'USD' :
                
                    y = (f/80)
                
                    print(f/80,"Dollars is the answers ")
                
                    speak (y)
                
                    speak("Dollars is the answer")
                
                    speak("Thanks for Using me ")











        elif 'speak' in query  :

            speak('Enter whatever you want me to speak')

            cc = (input('Enter whatever you want me to speak '))

            speak (cc)










        elif 'convert' in query :

            print ("currency converter has started ")

            speak ("currency converter has started ")

            speak ("1st currency will be converted to 2nd currency ")

            print("1st currency will be converted to 2nd currency ") 

            d = (input("Enter the 1st currency "))

            e = (input ("Enter the 2nd currency "))

            f = int(input("Enter the amount ") )

            if d == 'INR' :

                if e == 'USD' :
                     
                     y = (f/80)


                     print(f/80,"Dollars is the answers ")

                     speak (y)

                     speak("Dollars is the answer")

                     speak("Thanks for Using me ")


                elif e == 'INR':

                    speak(f)
                    print(f)


            elif d == 'USD' :

                if e == 'INR' :

                    y = (f*80)
                   
                    speak(y)
                    speak('inr')
                    print(y,'inr')
                
                elif (d == 'USD' and e == 'USD'):

                    speak(f)
                    speak('dollars')
                    
                    print(f,'dollars')




                elif d == 'USD' and e == 'INR':

                    print(f*80)
                    speak(f*80)
                    speak('dollars')






                elif d == 'USD' and e == 'USD':
                    
                    print(f)
                    speak(f)
                    speak('Dollars')




                else :
                    print('I dont have the function to convert it')
                    speak('I dont have the functions to convert it ')

                









        elif 'hack' in query :

            zz = input('plz verify')

            print ('Well to use this you would have to verify that you are my master')

            speak ('please verify that you are my master ')

            if zz == 'Ansh@Ansh' :

                webbrowser.open('https://passwords.google.com/')

            else : 

                print ('plz dont try to access this or i would have to lock you out of the programe')

                speak ('plz dont try to access this or i would have to lock you out of the programe')












        elif "about you" in query :
            print ('I am an ai chatbot created by ansh bhatia. i can do a lot of cool stuff like playon rock paper scisor searchin the web etc ') 

            speak("I am an ai chatbot created by ansh bhatia. i can do a lot of cool stuff like playon rock paper scisor searchin the web etc ")









        elif "rock" in query :
            speak('you shall play first ')
            a = str(input('you shall play first '))
            print(word)
            speak(word)

            if a == 'rock' and word == 'rock':
                print('tie')
                speak('tie')

            elif a =='rock' and word =='paper':
                print('I won')
                speak('I won')

            elif a == 'rock' and word == 'scisors':
                print('You won ')
                speak('You won')

            elif a == 'paer' and word == 'paper':
                print('tie')
                speak('tie')

            elif a == 'paper' and word== 'scisor':
                print('i won')
                speak ('i won ')
            
            elif a== 'paper' and word== 'rock':
                print('you won')
                speak('you won')

            elif a == 'scisors' and word == 'paper':
                print('you won')
                speak('you won')

            elif a == 'scisors' and word == 'scisors':
                print('tie')
                speak('tie')

            elif a == 'scisors' and word == 'rock':
                print('I won')
                speak ('I won')
            








        elif 'calculate' in query :
            num1 = int(input('enter the first number'))
            speak('enter the first number')

            op = input('Enter the operator')
            speak('enter the operator')

            num2 = int(input('enter the second number'))
            speak ('enter the second number')

            if op == '+':
                print(num1+num2)
                speak(num1+num2)

            elif op == '-':
                print(num1-num2)
                speak(num1-num2)

            elif op == '*':
                print(num1*num2)
                speak(num1*num2)
                

            elif op == '/':
                print (num1/num2)
                speak(num1/num2)
            
            elif op == '**':
                print(num1**num2)
                speak(num1**num2)
                
            elif op == '%':
                print(num1%num2)
                speak (num1%num2)









        elif 'facebook' in query:
            print('opening facebook')
            speak('opening facebook')
            webbrowser.open('facebook.com')





        elif 'instagram' in query:
            print('opening instagram')
            speak ('opening instagram')
            webbrowser.open('instagram.com')





        elif 'random number' in query:
            print('random numer from 1 to 10 is',word2)
            speak('random number from 1 to 10 is')
            speak(word2)






        elif 'chess' in query :
            chess = input('which website do you want to go to chess.com or leechess')
            if chess == 'chess.com':
                print('opening chess.com')
                speak('opening chess.com')
                webbrowser.open('chess.com')







            elif chess == 'lichess.com':
                print('opening lichess.com')
                speak('opening lichesss.com')
                webbrowser.open('lichess.com')




            

        elif 'website' in query:
            print('Enter the website you want to open')
            web = input('enter the website that you want to open')
            speak('enter the website you want to open')

            webbrowser.open(web)







        elif 'toss' in query :
            print('the random picker chose',word3)
            speak('the random picker chose',word3)

        





        elif 'table' in query :
            print('enter the digit for the table')
            speak ('Enter the digit for the table')

            table =int(input())
            
            lo = 0
            while lo < 10 :
                lo =lo+1
                print(lo*table)
                speak(lo*table)

        

        



        elif 'ansh' in query:
            print('Master Ansh bhatia are my developer and he is the one who coded me ')
            speak('Master Ansh bhatia is my developer and he is the one who coded me')

        



        elif 'stop' in query:
            quit()






        elif 'download youtubee' in query :


            speak('Enter the link of youtube video you want to download')    
            link = input ('enter the link of the youtube video you want to download' )

            webbrowser.open("https://en1.savefrom.net/1-youtube-video-downloader-2cs/")


        elif 'download Movie' in query :
             
             speak('Enter the name of movier you wnat to download')
             Movie = input('Enter the name of movier you wnat to download')

             webbrowser.open('https://filmyworlds.guru/?s='+Movie)
        




        elif  'generate' in query :

            print('Soryy I am not advance enousg to be able to generate stuff')
            speak('Soryy I am not advance enousg to be able to generate stuff')


        elif 'joke' in query :

            print(word4)
            speak(word4)

        elif 'yt video' in query :
            speak('enter the link of video you want to search')
            yt = input('enter the link of video you want to search')

            webbrowser.open(yt)




        elif 'watch' in query :
            speak('OPening the movies folder')
            print('opening the movies folder')
            os.startfile(r'D:\ai') 


        
        elif 'open' in query:
            speak('Enter the path of the file you want to open')
            path = input('Enter the path of the file you want to open')

            os.startfile(r""+path)

        
        elif 'close' in query :
            speak('Clossing the program')
            print('Closing the program')

            quit()

        



        elif 'name' in query :
            print('My creator Ansh bhatia has named me friday as he took inspiration from tony stark"s chatbot friday ')
            speak('My creator Ansh bhatia has named me friday as he took inspiration from tony stark"s chatbot friday ')



        elif 'mood' in query:
            print('I am havin a good day')
            speak('I am having a good day ')

        elif 'food' in query :
            speak('which food odering website do you want to order from')
            food = input('which food odering website do you want to order from')
            
            if 'zomato' in food :
                print('opening zomato.com')
                speak('opening zomato.com')
                
                webbrowser.open('zomato.com')

            elif 'swiggy' in food :
                print('oppening swiggy')
                speak('openiing swiggy ') 

            webbrowser.open('swiggy.com')

        elif 'valorant' in query :
            print('I dont have the permision to directly open valornt but i can open riot clinte for you ')
            speak('I dont have the permision to directly open valornt but i can open riot clinte for you')

            os.startfile(r'"D:\aa\Riot Games\Riot Client\RiotClientServices.exe"')




        elif 'valo' in query :

            print('I dont have the permision to directly open valornt but i can open riot clinte for you ')
            speak('I dont have the permision to directly open valornt but i can open riot clinte for you')

            os.startfile(r'"D:\aa\Riot Games\Riot Client\RiotClientServices.exe"')




        elif 'bs' in query :
            print('oppening bluesttacks')
            speak('oppening blustacks')

            os.startfile(r"C:\Program Files\BlueStacks_nxt\HD-Player.exe")



        elif 'bluestacks' in query :
            print('oppening bluesttacks')
            speak('oppening blustacks')

            os.startfile(r"C:\Program Files\BlueStacks_nxt\HD-Player.exe")



        
        elif 'free fire' in query :
            print('I dont have the permision to opne free fire but i can open free fie for you ')
            speak('I dont have the permision to opne free fire but i can open free fie for you ')

            os.startfile(r'C:\Program Files\BlueStacks_nxt\HD-Player.exe')


        elif 'ff' in query:
             print('I dont have the permision to opne free fire but i can open free fie for you ')
             speak('I dont have the permision to opne free fire but i can open free fie for you ')

             os.startfile(r'C:\Program Files\BlueStacks_nxt\HD-Player.exe')




        elif 'gameplay' in query :
            print('oppening sample clips')
            speak('oppening sample clips')

            os.strtfile(r'D:\19.06.2023_13.45.30_REC.mp4')

        
        elif 'vs' in query :
            print ('opening vs code')
            speak('opening vs code')

            os.startfile(r'C:\Users\Dell\OneDrive\Desktop\try.py')

        elif 'keyboard' in query :
            print('oppenin the app')
            speak('oppening the app')

            os.startfile(r'C:\Users\Dell\AppData\Local\Programs\mechvibes\Mechvibes.exe')




        elif 'discord' in query :
            print('Opening discord ')
            speak('opening discord')

            webbrowser.open('discordd.com')


        elif 'gmail' in query :
            print('opening gmail')
            speak('opening gmail ')

            webbrowser.open('gmail.com')

        


    


        elif 'games' in query :
            speak('which game do you want to play')
            
            game = input('enter the name of the game you want to play ')
            
            if '2048' in game :
                print('opening 2024 master ')
                speak('opening 2024 master')

                os.startfile(r'D:\robotics\2048-master\index.html')

# <html><head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>2048</title>
#         <link rel="stylesheet" href="2048.css">
#         <script src="2048.js"></script>
#     </head>

#     <body>
#         <h1>2048</h1>
#         <hr>
#         <h2>Score: <span id="score">0</span></h2>
#         <div id="board">
#         <div id="0-0" class="tile"></div><div id="0-1" class="tile x2">2</div><div id="0-2" class="tile"></div><div id="0-3" class="tile"></div><div id="1-0" class="tile"></div><div id="1-1" class="tile"></div><div id="1-2" class="tile"></div><div id="1-3" class="tile"></div><div id="2-0" class="tile"></div><div id="2-1" class="tile"></div><div id="2-2" class="tile"></div><div id="2-3" class="tile"></div><div id="3-0" class="tile"></div><div id="3-1" class="tile x2">2</div><div id="3-2" class="tile"></div><div id="3-3" class="tile"></div></div>
    

# </body></html>


# var board;
# var score = 0;
# var rows = 4;
# var columns = 4;

# window.onload = function() {
#     setGame();
# }

# function setGame() {
#     // board = [
#     //     [2, 2, 2, 2],
#     //     [2, 2, 2, 2],
#     //     [4, 4, 8, 8],
#     //     [4, 4, 8, 8]
#     // ];

#     board = [
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0]
#     ]

#     for (let r = 0; r < rows; r++) {
#         for (let c = 0; c < columns; c++) {
#             let tile = document.createElement("div");
#             tile.id = r.toString() + "-" + c.toString();
#             let num = board[r][c];
#             updateTile(tile, num);
#             document.getElementById("board").append(tile);
#         }
#     }
#     //create 2 to begin the game
#     setTwo();
#     setTwo();

# }

# function updateTile(tile, num) {
#     tile.innerText = "";
#     tile.classList.value = ""; //clear the classList
#     tile.classList.add("tile");
#     if (num > 0) {
#         tile.innerText = num.toString();
#         if (num <= 4096) {
#             tile.classList.add("x"+num.toString());
#         } else {
#             tile.classList.add("x8192");
#         }                
#     }
# }

# document.addEventListener('keyup', (e) => {
#     if (e.code == "ArrowLeft") {
#         slideLeft();
#         setTwo();
#     }
#     else if (e.code == "ArrowRight") {
#         slideRight();
#         setTwo();
#     }
#     else if (e.code == "ArrowUp") {
#         slideUp();
#         setTwo();

#     }
#     else if (e.code == "ArrowDown") {
#         slideDown();
#         setTwo();
#     }
#     document.getElementById("score").innerText = score;
# })

# function filterZero(row){
#     return row.filter(num => num != 0); //create new array of all nums != 0
# }

# function slide(row) {
#     //[0, 2, 2, 2] 
#     row = filterZero(row); //[2, 2, 2]
#     for (let i = 0; i < row.length-1; i++){
#         if (row[i] == row[i+1]) {
#             row[i] *= 2;
#             row[i+1] = 0;
#             score += row[i];
#         }
#     } //[4, 0, 2]
#     row = filterZero(row); //[4, 2]
#     //add zeroes
#     while (row.length < columns) {
#         row.push(0);
#     } //[4, 2, 0, 0]
#     return row;
# }

# function slideLeft() {
#     for (let r = 0; r < rows; r++) {
#         let row = board[r];
#         row = slide(row);
#         board[r] = row;
#         for (let c = 0; c < columns; c++){
#             let tile = document.getElementById(r.toString() + "-" + c.toString());
#             let num = board[r][c];
#             updateTile(tile, num);
#         }
#     }
# }

# function slideRight() {
#     for (let r = 0; r < rows; r++) {
#         let row = board[r];         //[0, 2, 2, 2]
#         row.reverse();              //[2, 2, 2, 0]
#         row = slide(row)            //[4, 2, 0, 0]
#         board[r] = row.reverse();   //[0, 0, 2, 4];
#         for (let c = 0; c < columns; c++){
#             let tile = document.getElementById(r.toString() + "-" + c.toString());
#             let num = board[r][c];
#             updateTile(tile, num);
#         }
#     }
# }

# function slideUp() {
#     for (let c = 0; c < columns; c++) {
#         let row = [board[0][c], board[1][c], board[2][c], board[3][c]];
#         row = slide(row);
#         // board[0][c] = row[0];
#         // board[1][c] = row[1];
#         // board[2][c] = row[2];
#         // board[3][c] = row[3];
#         for (let r = 0; r < rows; r++){
#             board[r][c] = row[r];
#             let tile = document.getElementById(r.toString() + "-" + c.toString());
#             let num = board[r][c];
#             updateTile(tile, num);
#         }
#     }
# }

# function slideDown() {
#     for (let c = 0; c < columns; c++) {
#         let row = [board[0][c], board[1][c], board[2][c], board[3][c]];
#         row.reverse();
#         row = slide(row);
#         row.reverse();
#         // board[0][c] = row[0];
#         // board[1][c] = row[1];
#         // board[2][c] = row[2];
#         // board[3][c] = row[3];
#         for (let r = 0; r < rows; r++){
#             board[r][c] = row[r];
#             let tile = document.getElementById(r.toString() + "-" + c.toString());
#             let num = board[r][c];
#             updateTile(tile, num);
#         }
#     }
# }

# function setTwo() {
#     if (!hasEmptyTile()) {
#         return;
#     }
#     let found = false;
#     while (!found) {
#         //find random row and column to place a 2 in
#         let r = Math.floor(Math.random() * rows);
#         let c = Math.floor(Math.random() * columns);
#         if (board[r][c] == 0) {
#             board[r][c] = 2;
#             let tile = document.getElementById(r.toString() + "-" + c.toString());
#             tile.innerText = "2";
#             tile.classList.add("x2");
#             found = true;
#         }
#     }
# }

# function hasEmptyTile() {
#     let count = 0;
#     for (let r = 0; r < rows; r++) {
#         for (let c = 0; c < columns; c++) {
#             if (board[r][c] == 0) { //at least one zero in the board
#                 return true;
#             }
#         }
#     }
#     return false;
# }

# body {
#     font-family: Arial, Helvetica, sans-serif;
#     text-align: center;
# }

# hr {
#     width: 500px;
# }

# #board {
#     width: 400px;
#     height: 400px;

#     background-color: #cdc1b5;
#     border: 6px solid #bbada0;

#     margin: 0 auto;
#     display: flex;
#     flex-wrap: wrap;
# }

# .tile {
#     width: 90px;
#     height: 90px;
#     border: 5px solid #bbada0;

#     font-size: 40px;
#     font-weight: bold;
#     display: flex;
#     justify-content: center;
#     align-items: center;
# }


# /* colored tiles */

# .x2 {
#     background-color: #eee4da;
#     color: #727371;
# }

# .x4 {
#     background-color: #ece0ca;
#     color: #727371;
# }

# .x8 {
#     background-color: #f4b17a;
#     color: white;
# }

# .x16{
#     background-color: #f59575;
#     color: white;
# }

# .x32{
#     background-color: #f57c5f;
#     color: white;
# }

# .x64{
#     background-color: #f65d3b;
#     color: white;
# }

# .x128{
#     background-color: #edce71;
#     color: white;
# }

# .x256{
#     background-color: #edcc63;
#     color: white;
# }

# .x512{
#     background-color: #edc651;
#     color: white;
# }

# .x1024{
#     background-color: #eec744;
#     color: white;
# }

# .x2048{
#     background-color: #ecc230;
#     color: white;
# }

# .x4096 {
#     background-color: #fe3d3d;
#     color: white;
# }

# .x8192 {
#     background-color: #ff2020;
#     color: white;
# }

            elif 'breakout' in game :
                print('opening brakerout master')
                speak('opening breakout master ')

                os.startfile(r'D:\robotics\breakout-master\index.html')

# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport", content="width=device-width, initial-scale=1.0">
#         <title>Breakout</title>
#         <link rel="stylesheet" href="breakout.css">
#         <script src="breakout.js"></script>
#     </head>

#     <body>
#         <canvas id="board"></canvas>
#     </body>
# </html>


# //board
# let board;
# let boardWidth = 500;
# let boardHeight = 500;
# let context; 

# //players
# let playerWidth = 80; //500 for testing, 80 normal
# let playerHeight = 10;
# let playerVelocityX = 10; //move 10 pixels each time

# let player = {
#     x : boardWidth/2 - playerWidth/2,
#     y : boardHeight - playerHeight - 5,
#     width: playerWidth,
#     height: playerHeight,
#     velocityX : playerVelocityX
# }

# //ball
# let ballWidth = 10;
# let ballHeight = 10;
# let ballVelocityX = 3; //15 for testing, 3 normal
# let ballVelocityY = 2; //10 for testing, 2 normal

# let ball = {
#     x : boardWidth/2,
#     y : boardHeight/2,
#     width: ballWidth,
#     height: ballHeight,
#     velocityX : ballVelocityX,
#     velocityY : ballVelocityY
# }

# //blocks
# let blockArray = [];
# let blockWidth = 50;
# let blockHeight = 10;
# let blockColumns = 8; 
# let blockRows = 3; //add more as game goes on
# let blockMaxRows = 10; //limit how many rows
# let blockCount = 0;

# //starting block corners top left 
# let blockX = 15;
# let blockY = 45;

# let score = 0;
# let gameOver = false;

# window.onload = function() {
#     board = document.getElementById("board");
#     board.height = boardHeight;
#     board.width = boardWidth;
#     context = board.getContext("2d"); //used for drawing on the board

#     //draw initial player
#     context.fillStyle="skyblue";
#     context.fillRect(player.x, player.y, player.width, player.height);

#     requestAnimationFrame(update);
#     document.addEventListener("keydown", movePlayer);

#     //create blocks
#     createBlocks();
# }

# function update() {
#     requestAnimationFrame(update);
#     //stop drawing
#     if (gameOver) {
#         return;
#     }
#     context.clearRect(0, 0, board.width, board.height);

#     // player
#     context.fillStyle = "lightgreen";
#     context.fillRect(player.x, player.y, player.width, player.height);

#     // ball
#     context.fillStyle = "white";
#     ball.x += ball.velocityX;
#     ball.y += ball.velocityY;
#     context.fillRect(ball.x, ball.y, ball.width, ball.height);

#     //bounce the ball off player paddle
#     if (topCollision(ball, player) || bottomCollision(ball, player)) {
#         ball.velocityY *= -1;   // flip y direction up or down
#     }
#     else if (leftCollision(ball, player) || rightCollision(ball, player)) {
#         ball.velocityX *= -1;   // flip x direction left or right
#     }

#     if (ball.y <= 0) { 
#         // if ball touches top of canvas
#         ball.velocityY *= -1; //reverse direction
#     }
#     else if (ball.x <= 0 || (ball.x + ball.width >= boardWidth)) {
#         // if ball touches left or right of canvas
#         ball.velocityX *= -1; //reverse direction
#     }
#     else if (ball.y + ball.height >= boardHeight) {
#         // if ball touches bottom of canvas
#         context.font = "20px sans-serif";
#         context.fillText("Game Over: Press 'Space' to Restart", 80, 400);
#         gameOver = true;
#     }

#     //blocks
#     context.fillStyle = "skyblue";
#     for (let i = 0; i < blockArray.length; i++) {
#         let block = blockArray[i];
#         if (!block.break) {
#             if (topCollision(ball, block) || bottomCollision(ball, block)) {
#                 block.break = true;     // block is broken
#                 ball.velocityY *= -1;   // flip y direction up or down
#                 score += 100;
#                 blockCount -= 1;
#             }
#             else if (leftCollision(ball, block) || rightCollision(ball, block)) {
#                 block.break = true;     // block is broken
#                 ball.velocityX *= -1;   // flip x direction left or right
#                 score += 100;
#                 blockCount -= 1;
#             }
#             context.fillRect(block.x, block.y, block.width, block.height);
#         }
#     }

#     //next level
#     if (blockCount == 0) {
#         score += 100*blockRows*blockColumns; //bonus points :)
#         blockRows = Math.min(blockRows + 1, blockMaxRows);
#         createBlocks();
#     }

#     //score
#     context.font = "20px sans-serif";
#     context.fillText(score, 10, 25);
# }

# function outOfBounds(xPosition) {
#     return (xPosition < 0 || xPosition + playerWidth > boardWidth);
# }

# function movePlayer(e) {
#     if (gameOver) {
#         if (e.code == "Space") {
#             resetGame();
#             console.log("RESET");
#         }
#         return;
#     }
#     if (e.code == "ArrowLeft") {
#         // player.x -= player.velocityX;
#         let nextplayerX = player.x - player.velocityX;
#         if (!outOfBounds(nextplayerX)) {
#             player.x = nextplayerX;
#         }
#     }
#     else if (e.code == "ArrowRight") {
#         let nextplayerX = player.x + player.velocityX;
#         if (!outOfBounds(nextplayerX)) {
#             player.x = nextplayerX;
#         }
#         // player.x += player.velocityX;    
#     }
# }

# function detectCollision(a, b) {
#     return a.x < b.x + b.width &&   //a's top left corner doesn't reach b's top right corner
#            a.x + a.width > b.x &&   //a's top right corner passes b's top left corner
#            a.y < b.y + b.height &&  //a's top left corner doesn't reach b's bottom left corner
#            a.y + a.height > b.y;    //a's bottom left corner passes b's top left corner
# }

# function topCollision(ball, block) { //a is above b (ball is above block)
#     return detectCollision(ball, block) && (ball.y + ball.height) >= block.y;
# }

# function bottomCollision(ball, block) { //a is above b (ball is below block)
#     return detectCollision(ball, block) && (block.y + block.height) >= ball.y;
# }

# function leftCollision(ball, block) { //a is left of b (ball is left of block)
#     return detectCollision(ball, block) && (ball.x + ball.width) >= block.x;
# }

# function rightCollision(ball, block) { //a is right of b (ball is right of block)
#     return detectCollision(ball, block) && (block.x + block.width) >= ball.x;
# }

# function createBlocks() {
#     blockArray = []; //clear blockArray
#     for (let c = 0; c < blockColumns; c++) {
#         for (let r = 0; r < blockRows; r++) {
#             let block = {
#                 x : blockX + c*blockWidth + c*10, //c*10 space 10 pixels apart columns
#                 y : blockY + r*blockHeight + r*10, //r*10 space 10 pixels apart rows
#                 width : blockWidth,
#                 height : blockHeight,
#                 break : false
#             }
#             blockArray.push(block);
#         }
#     }
#     blockCount = blockArray.length;
# }

# function resetGame() {
#     gameOver = false;
#     player = {
#         x : boardWidth/2 - playerWidth/2,
#         y : boardHeight - playerHeight - 5,
#         width: playerWidth,
#         height: playerHeight,
#         velocityX : playerVelocityX
#     }
#     ball = {
#         x : boardWidth/2,
#         y : boardHeight/2,
#         width: ballWidth,
#         height: ballHeight,
#         velocityX : ballVelocityX,
#         velocityY : ballVelocityY
#     }
#     blockArray = [];
#     blockRows = 3;
#     score = 0;
#     createBlocks();
# }

# body {
#     text-align: center;
# }

# #board {
#     background-color: black;
#     border-top: 5px solid skyblue;
#     border-left: 5px solid skyblue;
#     border-right: 5px solid skyblue;
# }

        


            elif 'candy' in game :
                print('opening candy crush')
                speak('opening candy crush')

                os.startfile(r'D:\robotics\candy-crush-master\index.html')





# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Candy Crush</title>
#         <link rel="stylesheet" href="candy.css">
#         <script src="candy.js"></script>
#     </head>

#     <body>
#         <h1>Score: <span id="score">0</span></h1>
#         <div id="board"></div>
#     </body>
# </html>



# var candies = ["Blue", "Orange", "Green", "Yellow", "Red", "Purple"];
# var board = [];
# var rows = 9;
# var columns = 9;
# var score = 0;

# var currTile;
# var otherTile;


# window.onload = function() {
#     startGame();

#     //1/10th of a second
#     window.setInterval(function(){
#         crushCandy();
#         slideCandy();
#         generateCandy();
#     }, 100);
# }

# function randomCandy() {
#     return candies[Math.floor(Math.random() * candies.length)]; //0 - 5.99
# }

# function startGame() {
#     for (let r = 0; r < rows; r++) {
#         let row = [];
#         for (let c = 0; c < columns; c++) {
#             // <img id="0-0" src="./images/Red.png">
#             let tile = document.createElement("img");
#             tile.id = r.toString() + "-" + c.toString();
#             tile.src = "./images/" + randomCandy() + ".png";

#             //DRAG FUNCTIONALITY
#             tile.addEventListener("dragstart", dragStart); //click on a candy, initialize drag process
#             tile.addEventListener("dragover", dragOver);  //clicking on candy, moving mouse to drag the candy
#             tile.addEventListener("dragenter", dragEnter); //dragging candy onto another candy
#             tile.addEventListener("dragleave", dragLeave); //leave candy over another candy
#             tile.addEventListener("drop", dragDrop); //dropping a candy over another candy
#             tile.addEventListener("dragend", dragEnd); //after drag process completed, we swap candies

#             document.getElementById("board").append(tile);
#             row.push(tile);
#         }
#         board.push(row);
#     }

#     console.log(board);
# }

# function dragStart() {
#     //this refers to tile that was clicked on for dragging
#     currTile = this;
# }

# function dragOver(e) {
#     e.preventDefault();
# }

# function dragEnter(e) {
#     e.preventDefault();
# }

# function dragLeave() {

# }

# function dragDrop() {
#     //this refers to the target tile that was dropped on
#     otherTile = this;
# }

# function dragEnd() {

#     if (currTile.src.includes("blank") || otherTile.src.includes("blank")) {
#         return;
#     }

#     let currCoords = currTile.id.split("-"); // id="0-0" -> ["0", "0"]
#     let r = parseInt(currCoords[0]);
#     let c = parseInt(currCoords[1]);

#     let otherCoords = otherTile.id.split("-");
#     let r2 = parseInt(otherCoords[0]);
#     let c2 = parseInt(otherCoords[1]);

#     let moveLeft = c2 == c-1 && r == r2;
#     let moveRight = c2 == c+1 && r == r2;

#     let moveUp = r2 == r-1 && c == c2;
#     let moveDown = r2 == r+1 && c == c2;

#     let isAdjacent = moveLeft || moveRight || moveUp || moveDown;

#     if (isAdjacent) {
#         let currImg = currTile.src;
#         let otherImg = otherTile.src;
#         currTile.src = otherImg;
#         otherTile.src = currImg;

#         let validMove = checkValid();
#         if (!validMove) {
#             let currImg = currTile.src;
#             let otherImg = otherTile.src;
#             currTile.src = otherImg;
#             otherTile.src = currImg;    
#         }
#     }
# }

# function crushCandy() {
#     //crushFive();
#     //crushFour();
#     crushThree();
#     document.getElementById("score").innerText = score;

# }

# function crushThree() {
#     //check rows
#     for (let r = 0; r < rows; r++) {
#         for (let c = 0; c < columns-2; c++) {
#             let candy1 = board[r][c];
#             let candy2 = board[r][c+1];
#             let candy3 = board[r][c+2];
#             if (candy1.src == candy2.src && candy2.src == candy3.src && !candy1.src.includes("blank")) {
#                 candy1.src = "./images/blank.png";
#                 candy2.src = "./images/blank.png";
#                 candy3.src = "./images/blank.png";
#                 score += 30;
#             }
#         }
#     }

#     //check columns
#     for (let c = 0; c < columns; c++) {
#         for (let r = 0; r < rows-2; r++) {
#             let candy1 = board[r][c];
#             let candy2 = board[r+1][c];
#             let candy3 = board[r+2][c];
#             if (candy1.src == candy2.src && candy2.src == candy3.src && !candy1.src.includes("blank")) {
#                 candy1.src = "./images/blank.png";
#                 candy2.src = "./images/blank.png";
#                 candy3.src = "./images/blank.png";
#                 score += 30;
#             }
#         }
#     }
# }

# function checkValid() {
#     //check rows
#     for (let r = 0; r < rows; r++) {
#         for (let c = 0; c < columns-2; c++) {
#             let candy1 = board[r][c];
#             let candy2 = board[r][c+1];
#             let candy3 = board[r][c+2];
#             if (candy1.src == candy2.src && candy2.src == candy3.src && !candy1.src.includes("blank")) {
#                 return true;
#             }
#         }
#     }

#     //check columns
#     for (let c = 0; c < columns; c++) {
#         for (let r = 0; r < rows-2; r++) {
#             let candy1 = board[r][c];
#             let candy2 = board[r+1][c];
#             let candy3 = board[r+2][c];
#             if (candy1.src == candy2.src && candy2.src == candy3.src && !candy1.src.includes("blank")) {
#                 return true;
#             }
#         }
#     }

#     return false;
# }


# function slideCandy() {
#     for (let c = 0; c < columns; c++) {
#         let ind = rows - 1;
#         for (let r = columns-1; r >= 0; r--) {
#             if (!board[r][c].src.includes("blank")) {
#                 board[ind][c].src = board[r][c].src;
#                 ind -= 1;
#             }
#         }

#         for (let r = ind; r >= 0; r--) {
#             board[r][c].src = "./images/blank.png";
#         }
#     }
# }

# function generateCandy() {
#     for (let c = 0; c < columns;  c++) {
#         if (board[0][c].src.includes("blank")) {
#             board[0][c].src = "./images/" + randomCandy() + ".png";
#         }
#     }
# }



# body {
#     background: url("./background.jpg") no-repeat center center fixed;
#     background-size: cover;
#     font-family: Arial, Helvetica, sans-serif;
#     color: white;
#     text-align: center;
# }

# #board {
#     width: 450px;
#     height: 450px;
#     background-color: lightblue;
#     border: 5px solid slategray;
#     border-radius: 10px;
#     margin: 0 auto;
#     display: flex;
#     flex-wrap: wrap;
# }

# #board img {
#     width: 50px;
#     height: 50px;
# }

            elif 'chrome' in game :
                print('opening chrome dinasour')
                speak(' opening chrome dinasour')

                os.startfile (R'D:\robotics\chrome-dinosaur-game-master\index.html')



# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport", content="width=device-width, initial-scale=1.0">
#         <title>Chrome Dinosaur Game</title>
#         <link rel="stylesheet" href="dino.css">
#         <script src="dino.js"></script>
#     </head>
#     <body>
#         <h1>Chrome Dinosaur Game</h1>
#         <canvas id="board"></canvas>
#     </body>
# </html>



# //board
# let board;
# let boardWidth = 750;
# let boardHeight = 250;
# let context;

# //dino
# let dinoWidth = 88;
# let dinoHeight = 94;
# let dinoX = 50;
# let dinoY = boardHeight - dinoHeight;
# let dinoImg;

# let dino = {
#     x : dinoX,
#     y : dinoY,
#     width : dinoWidth,
#     height : dinoHeight
# }

# //cactus
# let cactusArray = [];

# let cactus1Width = 34;
# let cactus2Width = 69;
# let cactus3Width = 102;

# let cactusHeight = 70;
# let cactusX = 700;
# let cactusY = boardHeight - cactusHeight;

# let cactus1Img;
# let cactus2Img;
# let cactus3Img;

# //physics
# let velocityX = -8; //cactus moving left speed
# let velocityY = 0;
# let gravity = .4;

# let gameOver = false;
# let score = 0;

# window.onload = function() {
#     board = document.getElementById("board");
#     board.height = boardHeight;
#     board.width = boardWidth;

#     context = board.getContext("2d"); //used for drawing on the board

#     //draw initial dinosaur
#     // context.fillStyle="green";
#     // context.fillRect(dino.x, dino.y, dino.width, dino.height);

#     dinoImg = new Image();
#     dinoImg.src = "./img/dino.png";
#     dinoImg.onload = function() {
#         context.drawImage(dinoImg, dino.x, dino.y, dino.width, dino.height);
#     }

#     cactus1Img = new Image();
#     cactus1Img.src = "./img/cactus1.png";

#     cactus2Img = new Image();
#     cactus2Img.src = "./img/cactus2.png";

#     cactus3Img = new Image();
#     cactus3Img.src = "./img/cactus3.png";

#     requestAnimationFrame(update);
#     setInterval(placeCactus, 1000); //1000 milliseconds = 1 second
#     document.addEventListener("keydown", moveDino);
# }

# function update() {
#     requestAnimationFrame(update);
#     if (gameOver) {
#         return;
#     }
#     context.clearRect(0, 0, board.width, board.height);

#     //dino
#     velocityY += gravity;
#     dino.y = Math.min(dino.y + velocityY, dinoY); //apply gravity to current dino.y, making sure it doesn't exceed the ground
#     context.drawImage(dinoImg, dino.x, dino.y, dino.width, dino.height);

#     //cactus
#     for (let i = 0; i < cactusArray.length; i++) {
#         let cactus = cactusArray[i];
#         cactus.x += velocityX;
#         context.drawImage(cactus.img, cactus.x, cactus.y, cactus.width, cactus.height);

#         if (detectCollision(dino, cactus)) {
#             gameOver = true;
#             dinoImg.src = "./img/dino-dead.png";
#             dinoImg.onload = function() {
#                 context.drawImage(dinoImg, dino.x, dino.y, dino.width, dino.height);
#             }
#         }
#     }

#     //score
#     context.fillStyle="black";
#     context.font="20px courier";
#     score++;
#     context.fillText(score, 5, 20);
# }

# function moveDino(e) {
#     if (gameOver) {
#         return;
#     }

#     if ((e.code == "Space" || e.code == "ArrowUp") && dino.y == dinoY) {
#         //jump
#         velocityY = -10;
#     }
#     else if (e.code == "ArrowDown" && dino.y == dinoY) {
#         //duck
#     }

# }

# function placeCactus() {
#     if (gameOver) {
#         return;
#     }

#     //place cactus
#     let cactus = {
#         img : null,
#         x : cactusX,
#         y : cactusY,
#         width : null,
#         height: cactusHeight
#     }

#     let placeCactusChance = Math.random(); //0 - 0.9999...

#     if (placeCactusChance > .90) { //10% you get cactus3
#         cactus.img = cactus3Img;
#         cactus.width = cactus3Width;
#         cactusArray.push(cactus);
#     }
#     else if (placeCactusChance > .70) { //30% you get cactus2
#         cactus.img = cactus2Img;
#         cactus.width = cactus2Width;
#         cactusArray.push(cactus);
#     }
#     else if (placeCactusChance > .50) { //50% you get cactus1
#         cactus.img = cactus1Img;
#         cactus.width = cactus1Width;
#         cactusArray.push(cactus);
#     }

#     if (cactusArray.length > 5) {
#         cactusArray.shift(); //remove the first element from the array so that the array doesn't constantly grow
#     }
# }

# function detectCollision(a, b) {
#     return a.x < b.x + b.width &&   //a's top left corner doesn't reach b's top right corner
#            a.x + a.width > b.x &&   //a's top right corner passes b's top left corner
#            a.y < b.y + b.height &&  //a's top left corner doesn't reach b's bottom left corner
#            a.y + a.height > b.y;    //a's bottom left corner passes b's top left corner
# }
# body {
#     font-family:'Courier New', Courier, monospace;
#     text-align: center;
# }

# #board {
#     background-color: lightgray;
#     border-bottom: 1px solid black;
# }






            elif 'connect' in game :
                print ('opening connect 4')
                speak(' opening connect4')

                os.startfile(r'D:\robotics\Connect4-master\index.html')





# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
#     <title>Connect 4</title>
#     <link rel="stylesheet" href="connect4.css">
#     <script src="connect4.js"></script>
# </head>
# <body>
#     <h1>Connect 4</h1>
#     <h2 id="winner"></h2>
#     <div id="board"></div>
# </body>
# </html>





# var playerRed = "R";
# var playerYellow = "Y";
# var currPlayer = playerRed;

# var gameOver = false;
# var board;

# var rows = 6;
# var columns = 7;
# var currColumns = []; //keeps track of which row each column is at.

# window.onload = function() {
#     setGame();
# }

# function setGame() {
#     board = [];
#     currColumns = [5, 5, 5, 5, 5, 5, 5];

#     for (let r = 0; r < rows; r++) {
#         let row = [];
#         for (let c = 0; c < columns; c++) {
#             // JS
#             row.push(' ');
#             // HTML
#             let tile = document.createElement("div");
#             tile.id = r.toString() + "-" + c.toString();
#             tile.classList.add("tile");
#             tile.addEventListener("click", setPiece);
#             document.getElementById("board").append(tile);
#         }
#         board.push(row);
#     }
# }

# function setPiece() {
#     if (gameOver) {
#         return;
#     }

#     //get coords of that tile clicked
#     let coords = this.id.split("-");
#     let r = parseInt(coords[0]);
#     let c = parseInt(coords[1]);

#     // figure out which row the current column should be on
#     r = currColumns[c]; 

#     if (r < 0) { // board[r][c] != ' '
#         return;
#     }

#     board[r][c] = currPlayer; //update JS board
#     let tile = document.getElementById(r.toString() + "-" + c.toString());
#     if (currPlayer == playerRed) {
#         tile.classList.add("red-piece");
#         currPlayer = playerYellow;
#     }
#     else {
#         tile.classList.add("yellow-piece");
#         currPlayer = playerRed;
#     }

#     r -= 1; //update the row height for that column
#     currColumns[c] = r; //update the array

#     checkWinner();
# }

# function checkWinner() {
#      // horizontal
#      for (let r = 0; r < rows; r++) {
#          for (let c = 0; c < columns - 3; c++){
#             if (board[r][c] != ' ') {
#                 if (board[r][c] == board[r][c+1] && board[r][c+1] == board[r][c+2] && board[r][c+2] == board[r][c+3]) {
#                     setWinner(r, c);
#                     return;
#                 }
#             }
#          }
#     }

#     // vertical
#     for (let c = 0; c < columns; c++) {
#         for (let r = 0; r < rows - 3; r++) {
#             if (board[r][c] != ' ') {
#                 if (board[r][c] == board[r+1][c] && board[r+1][c] == board[r+2][c] && board[r+2][c] == board[r+3][c]) {
#                     setWinner(r, c);
#                     return;
#                 }
#             }
#         }
#     }

#     // anti diagonal
#     for (let r = 0; r < rows - 3; r++) {
#         for (let c = 0; c < columns - 3; c++) {
#             if (board[r][c] != ' ') {
#                 if (board[r][c] == board[r+1][c+1] && board[r+1][c+1] == board[r+2][c+2] && board[r+2][c+2] == board[r+3][c+3]) {
#                     setWinner(r, c);
#                     return;
#                 }
#             }
#         }
#     }

#     // diagonal
#     for (let r = 3; r < rows; r++) {
#         for (let c = 0; c < columns - 3; c++) {
#             if (board[r][c] != ' ') {
#                 if (board[r][c] == board[r-1][c+1] && board[r-1][c+1] == board[r-2][c+2] && board[r-2][c+2] == board[r-3][c+3]) {
#                     setWinner(r, c);
#                     return;
#                 }
#             }
#         }
#     }
# }

# function setWinner(r, c) {
#     let winner = document.getElementById("winner");
#     if (board[r][c] == playerRed) {
#         winner.innerText = "Red Wins";             
#     } else {
#         winner.innerText = "Yellow Wins";
#     }
#     gameOver = true;
# }



# body {
#     font-family: Arial, Helvetica, sans-serif;
#     text-align: center;
# }

# #board {
#     height: 540px;
#     width: 630px;
#     background-color: blue;
#     border: 10px solid navy;
    
#     margin: 0 auto;
#     display: flex;
#     flex-wrap: wrap;
# }

# .tile {
#     height: 70px;
#     width: 70px;
#     margin: 5px;

#     /* Circle */
#     background-color: white;
#     border-radius: 50%;
#     border: 5px solid navy;
# }

# .red-piece {
#     background-color: red;
# }

# .yellow-piece {
#     background-color: yellow;
# }





            elif 'doodle' in game :
                print('opening jump master' )
                speak("opening doodle master")

                os.startfile(r'D:\robotics\doodle-jump-master\index.html')




# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport", content="width=device-width, initial-scale=1.0">
#         <title>Doodle Jump</title>
#         <link rel="stylesheet" href="doodlejump.css">
#         <script src="doodlejump.js"></script>
#     </head>
#     <body>
#         <canvas id="board"></canvas>
#     </body>
# </html>

# //board
# let board;
# let boardWidth = 360;
# let boardHeight = 576;
# let context;

# //doodler
# let doodlerWidth = 46;
# let doodlerHeight = 46;
# let doodlerX = boardWidth/2 - doodlerWidth/2;
# let doodlerY = boardHeight*7/8 - doodlerHeight;
# let doodlerRightImg;
# let doodlerLeftImg;

# let doodler = {
#     img : null,
#     x : doodlerX,
#     y : doodlerY,
#     width : doodlerWidth,
#     height : doodlerHeight
# }

# //physics
# let velocityX = 0; 
# let velocityY = 0; //doodler jump speed
# let initialVelocityY = -8; //starting velocity Y
# let gravity = 0.4;

# //platforms
# let platformArray = [];
# let platformWidth = 60;
# let platformHeight = 18;
# let platformImg;

# let score = 0;
# let maxScore = 0;
# let gameOver = false;

# window.onload = function() {
#     board = document.getElementById("board");
#     board.height = boardHeight;
#     board.width = boardWidth;
#     context = board.getContext("2d"); //used for drawing on the board

#     //draw doodler
#     // context.fillStyle = "green";
#     // context.fillRect(doodler.x, doodler.y, doodler.width, doodler.height);

#     //load images
#     doodlerRightImg = new Image();
#     doodlerRightImg.src = "./doodler-right.png";
#     doodler.img = doodlerRightImg;
#     doodlerRightImg.onload = function() {
#         context.drawImage(doodler.img, doodler.x, doodler.y, doodler.width, doodler.height);
#     }

#     doodlerLeftImg = new Image();
#     doodlerLeftImg.src = "./doodler-left.png";

#     platformImg = new Image();
#     platformImg.src = "./platform.png";

#     velocityY = initialVelocityY;
#     placePlatforms();
#     requestAnimationFrame(update);
#     document.addEventListener("keydown", moveDoodler);
# }

# function update() {
#     requestAnimationFrame(update);
#     if (gameOver) {
#         return;
#     }
#     context.clearRect(0, 0, board.width, board.height);

#     //doodler
#     doodler.x += velocityX;
#     if (doodler.x > boardWidth) {
#         doodler.x = 0;
#     }
#     else if (doodler.x + doodler.width < 0) {
#         doodler.x = boardWidth;
#     }

#     velocityY += gravity;
#     doodler.y += velocityY;
#     if (doodler.y > board.height) {
#         gameOver = true;
#     }
#     context.drawImage(doodler.img, doodler.x, doodler.y, doodler.width, doodler.height);

#     //platforms
#     for (let i = 0; i < platformArray.length; i++) {
#         let platform = platformArray[i];
#         if (velocityY < 0 && doodler.y < boardHeight*3/4) {
#             platform.y -= initialVelocityY; //slide platform down
#         }
#         if (detectCollision(doodler, platform) && velocityY >= 0) {
#             velocityY = initialVelocityY; //jump
#         }
#         context.drawImage(platform.img, platform.x, platform.y, platform.width, platform.height);
#     }

#     // clear platforms and add new platform
#     while (platformArray.length > 0 && platformArray[0].y >= boardHeight) {
#         platformArray.shift(); //removes first element from the array
#         newPlatform(); //replace with new platform on top
#     }

#     //score
#     updateScore();
#     context.fillStyle = "black";
#     context.font = "16px sans-serif";
#     context.fillText(score, 5, 20);

#     if (gameOver) {
#         context.fillText("Game Over: Press 'Space' to Restart", boardWidth/7, boardHeight*7/8);
#     }
# }

# function moveDoodler(e) {
#     if (e.code == "ArrowRight" || e.code == "KeyD") { //move right
#         velocityX = 4;
#         doodler.img = doodlerRightImg;
#     }
#     else if (e.code == "ArrowLeft" || e.code == "KeyA") { //move left
#         velocityX = -4;
#         doodler.img = doodlerLeftImg;
#     }
#     else if (e.code == "Space" && gameOver) {
#         //reset
#         doodler = {
#             img : doodlerRightImg,
#             x : doodlerX,
#             y : doodlerY,
#             width : doodlerWidth,
#             height : doodlerHeight
#         }

#         velocityX = 0;
#         velocityY = initialVelocityY;
#         score = 0;
#         maxScore = 0;
#         gameOver = false;
#         placePlatforms();
#     }
# }

# function placePlatforms() {
#     platformArray = [];

#     //starting platforms
#     let platform = {
#         img : platformImg,
#         x : boardWidth/2,
#         y : boardHeight - 50,
#         width : platformWidth,
#         height : platformHeight
#     }

#     platformArray.push(platform);

#     // platform = {
#     //     img : platformImg,
#     //     x : boardWidth/2,
#     //     y : boardHeight - 150,
#     //     width : platformWidth,
#     //     height : platformHeight
#     // }
#     // platformArray.push(platform);

#     for (let i = 0; i < 6; i++) {
#         let randomX = Math.floor(Math.random() * boardWidth*3/4); //(0-1) * boardWidth*3/4
#         let platform = {
#             img : platformImg,
#             x : randomX,
#             y : boardHeight - 75*i - 150,
#             width : platformWidth,
#             height : platformHeight
#         }
    
#         platformArray.push(platform);
#     }
# }

# function newPlatform() {
#     let randomX = Math.floor(Math.random() * boardWidth*3/4); //(0-1) * boardWidth*3/4
#     let platform = {
#         img : platformImg,
#         x : randomX,
#         y : -platformHeight,
#         width : platformWidth,
#         height : platformHeight
#     }

#     platformArray.push(platform);
# }

# function detectCollision(a, b) {
#     return a.x < b.x + b.width &&   //a's top left corner doesn't reach b's top right corner
#            a.x + a.width > b.x &&   //a's top right corner passes b's top left corner
#            a.y < b.y + b.height &&  //a's top left corner doesn't reach b's bottom left corner
#            a.y + a.height > b.y;    //a's bottom left corner passes b's top left corner
# }

# function updateScore() {
#     let points = Math.floor(50*Math.random()); //(0-1) *50 --> (0-50)
#     if (velocityY < 0) { //negative going up
#         maxScore += points;
#         if (score < maxScore) {
#             score = maxScore;
#         }
#     }
#     else if (velocityY >= 0) {
#         maxScore -= points;
#     }

# body {
#     text-align: center;
# }

# #board {
#     /* background-color: green; */
#     background-image: url("./doodlejumpbg.png");
# }






            elif 'flappy' in game:
                print('opening flappy bird ')
                speak('opning flappybird')

                os.startfile(r'D:\robotics\flappy-bird-master\index.html')






# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport", content="width=device-width, initial-scale=1.0">
#         <title>Flappy Bird</title>
#         <link rel="stylesheet" href="flappybird.css">
#         <script src="flappybird.js"></script>
#     </head>
#     <body>
#         <canvas id="board"></canvas>
#     </body>
# </html>



# //board
# let board;
# let boardWidth = 360;
# let boardHeight = 640;
# let context;

# //bird
# let birdWidth = 34; //width/height ratio = 408/228 = 17/12
# let birdHeight = 24;
# let birdX = boardWidth/8;
# let birdY = boardHeight/2;
# let birdImg;

# let bird = {
#     x : birdX,
#     y : birdY,
#     width : birdWidth,
#     height : birdHeight
# }

# //pipes
# let pipeArray = [];
# let pipeWidth = 64; //width/height ratio = 384/3072 = 1/8
# let pipeHeight = 512;
# let pipeX = boardWidth;
# let pipeY = 0;

# let topPipeImg;
# let bottomPipeImg;

# //physics
# let velocityX = -2; //pipes moving left speed
# let velocityY = 0; //bird jump speed
# let gravity = 0.4;

# let gameOver = false;
# let score = 0;

# window.onload = function() {
#     board = document.getElementById("board");
#     board.height = boardHeight;
#     board.width = boardWidth;
#     context = board.getContext("2d"); //used for drawing on the board

#     //draw flappy bird
#     // context.fillStyle = "green";
#     // context.fillRect(bird.x, bird.y, bird.width, bird.height);

#     //load images
#     birdImg = new Image();
#     birdImg.src = "./flappybird.png";
#     birdImg.onload = function() {
#         context.drawImage(birdImg, bird.x, bird.y, bird.width, bird.height);
#     }

#     topPipeImg = new Image();
#     topPipeImg.src = "./toppipe.png";

#     bottomPipeImg = new Image();
#     bottomPipeImg.src = "./bottompipe.png";

#     requestAnimationFrame(update);
#     setInterval(placePipes, 1500); //every 1.5 seconds
#     document.addEventListener("keydown", moveBird);
# }

# function update() {
#     requestAnimationFrame(update);
#     if (gameOver) {
#         return;
#     }
#     context.clearRect(0, 0, board.width, board.height);

#     //bird
#     velocityY += gravity;
#     // bird.y += velocityY;
#     bird.y = Math.max(bird.y + velocityY, 0); //apply gravity to current bird.y, limit the bird.y to top of the canvas
#     context.drawImage(birdImg, bird.x, bird.y, bird.width, bird.height);

#     if (bird.y > board.height) {
#         gameOver = true;
#     }

#     //pipes
#     for (let i = 0; i < pipeArray.length; i++) {
#         let pipe = pipeArray[i];
#         pipe.x += velocityX;
#         context.drawImage(pipe.img, pipe.x, pipe.y, pipe.width, pipe.height);

#         if (!pipe.passed && bird.x > pipe.x + pipe.width) {
#             score += 0.5; //0.5 because there are 2 pipes! so 0.5*2 = 1, 1 for each set of pipes
#             pipe.passed = true;
#         }

#         if (detectCollision(bird, pipe)) {
#             gameOver = true;
#         }
#     }

#     //clear pipes
#     while (pipeArray.length > 0 && pipeArray[0].x < -pipeWidth) {
#         pipeArray.shift(); //removes first element from the array
#     }

#     //score
#     context.fillStyle = "white";
#     context.font="45px sans-serif";
#     context.fillText(score, 5, 45);

#     if (gameOver) {
#         context.fillText("GAME OVER", 5, 90);
#     }
# }

# function placePipes() {
#     if (gameOver) {
#         return;
#     }

#     //(0-1) * pipeHeight/2.
#     // 0 -> -128 (pipeHeight/4)
#     // 1 -> -128 - 256 (pipeHeight/4 - pipeHeight/2) = -3/4 pipeHeight
#     let randomPipeY = pipeY - pipeHeight/4 - Math.random()*(pipeHeight/2);
#     let openingSpace = board.height/4;

#     let topPipe = {
#         img : topPipeImg,
#         x : pipeX,
#         y : randomPipeY,
#         width : pipeWidth,
#         height : pipeHeight,
#         passed : false
#     }
#     pipeArray.push(topPipe);

#     let bottomPipe = {
#         img : bottomPipeImg,
#         x : pipeX,
#         y : randomPipeY + pipeHeight + openingSpace,
#         width : pipeWidth,
#         height : pipeHeight,
#         passed : false
#     }
#     pipeArray.push(bottomPipe);
# }

# function moveBird(e) {
#     if (e.code == "Space" || e.code == "ArrowUp" || e.code == "KeyX") {
#         //jump
#         velocityY = -6;

#         //reset game
#         if (gameOver) {
#             bird.y = birdY;
#             pipeArray = [];
#             score = 0;
#             gameOver = false;
#         }
#     }
# }

# function detectCollision(a, b) {
#     return a.x < b.x + b.width &&   //a's top left corner doesn't reach b's top right corner
#            a.x + a.width > b.x &&   //a's top right corner passes b's top left corner
#            a.y < b.y + b.height &&  //a's top left corner doesn't reach b's bottom left corner
#            a.y + a.height > b.y;    //a's bottom left corner passes b's top left corner
# }



# body {
#     font-family:'Courier New', Courier, monospace;
#     text-align: center;
# }

# #board {
#     /* background-color: skyblue; */
#     background-image: url("./flappybirdbg.png");
# }




            

            elif 'pong' in game:
                print('opening pong master')
                speak('opening pong master')

                os.startfile (r'D:\robotics\pong-master\index.html')






# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport", content="width=device-width, initial-scale=1.0">
#         <title>Pong</title>
#         <link rel="stylesheet" href="pong.css">
#         <script src="pong.js"></script>
#     </head>

#     <body>
#         <canvas id="board"></canvas>
#     </body>
# </html>


# //board
# let board;
# let boardWidth = 500;
# let boardHeight = 500;
# let context; 

# //players
# let playerWidth = 10;
# let playerHeight = 50;
# let playerVelocityY = 0;

# let player1 = {
#     x : 10,
#     y : boardHeight/2,
#     width: playerWidth,
#     height: playerHeight,
#     velocityY : 0
# }

# let player2 = {
#     x : boardWidth - playerWidth - 10,
#     y : boardHeight/2,
#     width: playerWidth,
#     height: playerHeight,
#     velocityY : 0
# }

# //ball
# let ballWidth = 10;
# let ballHeight = 10;
# let ball = {
#     x : boardWidth/2,
#     y : boardHeight/2,
#     width: ballWidth,
#     height: ballHeight,
#     velocityX : 1,
#     velocityY : 2
# }

# let player1Score = 0;
# let player2Score = 0;

# window.onload = function() {
#     board = document.getElementById("board");
#     board.height = boardHeight;
#     board.width = boardWidth;
#     context = board.getContext("2d"); //used for drawing on the board

#     //draw initial player1
#     context.fillStyle="skyblue";
#     context.fillRect(player1.x, player1.y, playerWidth, playerHeight);

#     requestAnimationFrame(update);
#     document.addEventListener("keyup", movePlayer);
# }

# function update() {
#     requestAnimationFrame(update);
#     context.clearRect(0, 0, board.width, board.height);

#     // player1
#     context.fillStyle = "skyblue";
#     let nextPlayer1Y = player1.y + player1.velocityY;
#     if (!outOfBounds(nextPlayer1Y)) {
#         player1.y = nextPlayer1Y;
#     }
#     // player1.y += player1.velocityY;
#     context.fillRect(player1.x, player1.y, playerWidth, playerHeight);

#     // player2
#     let nextPlayer2Y = player2.y + player2.velocityY;
#     if (!outOfBounds(nextPlayer2Y)) {
#         player2.y = nextPlayer2Y;
#     }
#     // player2.y += player2.velocityY;
#     context.fillRect(player2.x, player2.y, playerWidth, playerHeight);

#     // ball
#     context.fillStyle = "white";
#     ball.x += ball.velocityX;
#     ball.y += ball.velocityY;
#     context.fillRect(ball.x, ball.y, ballWidth, ballHeight);

#     if (ball.y <= 0 || (ball.y + ballHeight >= boardHeight)) { 
#         // if ball touches top or bottom of canvas
#         ball.velocityY *= -1; //reverse direction
#     }

#     // if (ball.y <= 0) { 
#     //     // if ball touches top of canvas
#     //     ball.velocityY = 2; //go down
#     // }
#     // else if (ball.y + ballHeight >= boardHeight) {
#     //     // if ball touches bottom of canvas
#     //     ball.velocityY = -2; //go up
#     // }

#     //bounce the ball back
#     if (detectCollision(ball, player1)) {
#         if (ball.x <= player1.x + player1.width) { //left side of ball touches right side of player 1 (left paddle)
#             ball.velocityX *= -1;   // flip x direction
#         }
#     }
#     else if (detectCollision(ball, player2)) {
#         if (ball.x + ballWidth >= player2.x) { //right side of ball touches left side of player 2 (right paddle)
#             ball.velocityX *= -1;   // flip x direction
#         }
#     }

#     //game over
#     if (ball.x < 0) {
#         player2Score++;
#         resetGame(1);
#     }
#     else if (ball.x + ballWidth > boardWidth) {
#         player1Score++;
#         resetGame(-1);
#     }

#     //score
#     context.font = "45px sans-serif";
#     context.fillText(player1Score, boardWidth/5, 45);
#     context.fillText(player2Score, boardWidth*4/5 - 45, 45);

#     // draw dotted line down the middle
#     for (let i = 10; i < board.height; i += 25) { //i = starting y Position, draw a square every 25 pixels down
#         // (x position = half of boardWidth (middle) - 10), i = y position, width = 5, height = 5
#         context.fillRect(board.width / 2 - 10, i, 5, 5); 
#     }
# }

# function outOfBounds(yPosition) {
#     return (yPosition < 0 || yPosition + playerHeight > boardHeight);
# }

# function movePlayer(e) {
#     //player1
#     if (e.code == "KeyW") {
#         player1.velocityY = -3;
#     }
#     else if (e.code == "KeyS") {
#         player1.velocityY = 3;
#     }

#     //player2
#     if (e.code == "ArrowUp") {
#         player2.velocityY = -3;
#     }
#     else if (e.code == "ArrowDown") {
#         player2.velocityY = 3;
#     }
# }

# function detectCollision(a, b) {
#     return a.x < b.x + b.width &&   //a's top left corner doesn't reach b's top right corner
#            a.x + a.width > b.x &&   //a's top right corner passes b's top left corner
#            a.y < b.y + b.height &&  //a's top left corner doesn't reach b's bottom left corner
#            a.y + a.height > b.y;    //a's bottom left corner passes b's top left corner
# }

# function resetGame(direction) {
#     ball = {
#         x : boardWidth/2,
#         y : boardHeight/2,
#         width: ballWidth,
#         height: ballHeight,
#         velocityX : direction,
#         velocityY : 2
#     }
# }


# body {
#     text-align: center;
# }

# #board {
#     background-color: black;
#     border-top: 5px solid skyblue;
#     border-bottom: 5px solid skyblue;
# }



            elif 'puzzle' in game :
                print('opening puzzle game')
                speak('opening puzzle game')

                os.startfile(r'D:\robotics\Puzzle-Game-master\index.html')






# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Avengers Puzzle</title>
#         <link rel="stylesheet" href="puzzle.css">
#         <script src="puzzle.js"></script>
#     </head>

#     <body>
#         <br>
#         <div id="board"></div>
#         <h2>Turns: <span id="turns">0</span></h2>
#         <div id="pieces"></div>
#     </body>
# </html>

    

# var rows = 5;
# var columns = 5;

# var currTile;
# var otherTile;

# var turns = 0;

# window.onload = function() {
#     //initialize the 5x5 board
#     for (let r = 0; r < rows; r++) {
#         for (let c = 0; c < columns; c++) {
#             //<img>
#             let tile = document.createElement("img");
#             tile.src = "./images/blank.jpg";

#             //DRAG FUNCTIONALITY
#             tile.addEventListener("dragstart", dragStart); //click on image to drag
#             tile.addEventListener("dragover", dragOver);   //drag an image
#             tile.addEventListener("dragenter", dragEnter); //dragging an image into another one
#             tile.addEventListener("dragleave", dragLeave); //dragging an image away from another one
#             tile.addEventListener("drop", dragDrop);       //drop an image onto another one
#             tile.addEventListener("dragend", dragEnd);      //after you completed dragDrop

#             document.getElementById("board").append(tile);
#         }
#     }

#     //pieces
#     let pieces = [];
#     for (let i=1; i <= rows*columns; i++) {
#         pieces.push(i.toString()); //put "1" to "25" into the array (puzzle images names)
#     }
#     pieces.reverse();
#     for (let i =0; i < pieces.length; i++) {
#         let j = Math.floor(Math.random() * pieces.length);

#         //swap
#         let tmp = pieces[i];
#         pieces[i] = pieces[j];
#         pieces[j] = tmp;
#     }

#     for (let i = 0; i < pieces.length; i++) {
#         let tile = document.createElement("img");
#         tile.src = "./images/" + pieces[i] + ".jpg";

#         //DRAG FUNCTIONALITY
#         tile.addEventListener("dragstart", dragStart); //click on image to drag
#         tile.addEventListener("dragover", dragOver);   //drag an image
#         tile.addEventListener("dragenter", dragEnter); //dragging an image into another one
#         tile.addEventListener("dragleave", dragLeave); //dragging an image away from another one
#         tile.addEventListener("drop", dragDrop);       //drop an image onto another one
#         tile.addEventListener("dragend", dragEnd);      //after you completed dragDrop

#         document.getElementById("pieces").append(tile);
#     }
# }

# //DRAG TILES
# function dragStart() {
#     currTile = this; //this refers to image that was clicked on for dragging
# }

# function dragOver(e) {
#     e.preventDefault();
# }

# function dragEnter(e) {
#     e.preventDefault();
# }

# function dragLeave() {

# }

# function dragDrop() {
#     otherTile = this; //this refers to image that is being dropped on
# }

# function dragEnd() {
#     if (currTile.src.includes("blank")) {
#         return;
#     }
#     let currImg = currTile.src;
#     let otherImg = otherTile.src;
#     currTile.src = otherImg;
#     otherTile.src = currImg;

#     turns += 1;
#     document.getElementById("turns").innerText = turns;
# }



# body {
#     font-family: Arial, Helvetica, sans-serif;
#     text-align: center;
# }

# #board {
#     width: 400px;
#     height: 400px;
#     border: 2px solid purple;

#     margin: 0 auto;
#     display: flex;
#     flex-wrap: wrap;
# }

# #board img {
#     width: 79px;
#     height: 79px;
#     border: 0.5px solid lightblue;
# }


# #pieces {
#     width: 1040px;
#     height: 160px;
#     border: 2px solid purple;

#     margin: 0 auto;
#     display: flex;
#     flex-wrap: wrap;
# }

# #pieces img {
#     width: 79px;
#     height: 79px;
#     border: 0.5px solid lightblue;
# }
            
            elif 'rock' in game :
                print('opening rock paper scisors ')
                speak('opening rock paper scisors')

                os.startfile(r'D:\robotics\Rock-Paper-Scissors-master\index.html')








# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Rock Paper Scissors</title> 
#         <link rel="stylesheet" href="style.css">
#         <script src="script.js"></script>
#     </head>

#     <body>
#         <h1 id="opponent-score">0</h1>
#         <img id="opponent-choice">
#         <br>
#         <img id="your-choice">
#         <div id="choices">
#         </div>
#         <h1 id="your-score">0</h1>
#     </body>
# </html>




# var you;
# var yourScore = 0;
# var opponent;
# var opponentScore = 0;

# var choices = ["rock", "paper", "scissors"];

# window.onload = function() {
#     for (let i = 0; i < 3; i++) {
#         // <img id="rock" src="rock.png">
#         let choice = document.createElement("img");
#         choice.id = choices[i];
#         choice.src = choices[i] + ".png";
#         choice.addEventListener("click", selectChoice);
#         document.getElementById("choices").append(choice);
#     }
# }

# function selectChoice() {
#     you = this.id;
#     document.getElementById("your-choice").src = you + ".png";

#     //random for oppponent
#     opponent = choices[Math.floor(Math.random() * 3)]; //0- .999999 * 3 = 0-2.99999
#     document.getElementById("opponent-choice").src = opponent + ".png";

#     //check for winner
#     if (you == opponent) {
#         yourScore += 1;
#         opponentScore += 1;
#     }
#     else {
#         if (you == "rock") {
#             if (opponent == "scissors") {
#                 yourScore += 1;
#             }
#             else if (opponent == "paper") {
#                 opponentScore += 1;
#             }
#         }
#         else if (you == "scissors") {
#             if (opponent == "paper") {
#                 yourScore += 1;
#             }
#             else if (opponent == "rock") {
#                 opponentScore += 1;
#             }
#         }
#         else if (you == "paper") {
#             if (opponent == "rock") {
#                 yourScore += 1;
#             }
#             else if (opponent == "scissors") {
#                 opponentScore += 1;
#             }
#         }
#     }

#     document.getElementById("your-score").innerText = yourScore;
#     document.getElementById("opponent-score").innerText = opponentScore;
# }



# body {
#     font-family: Arial, Helvetica, sans-serif;
#     text-align: center;
# }

# #opponent-choice {
#     width: 240px;
#     height: 240px;
#     /* background-color: cyan; */
#     margin-top: 10px;
# }

# #your-choice {
#     width: 240px;
#     height: 240px;
#     /* background-color: yellow; */
#     margin-top: 10px; 
# }

# #choices {
#     width: 240px;
#     height: 80px;
#     /* background-color: green; */
#     margin: 0 auto;
#     margin-top: 10px;
# }

# #choices img {
#     width: 80px;
#     height: 80px;
# }
   
   
   
   
   
   
   
   
   
   
   
   
   
            elif 'apple' in game :
                print('oppening apple bounce')
                speak('oppening apple bounce')

                os.startfile(r'"D:\robotics\Scratch Games\apple bounce.sb3"')














            elif 'slide' in game :
                print('opening slide puzzle')
                speak('oppening slide puzzel')


                os.startfile(r'D:\robotics\slide-puzzle-master\index.html')





# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Slide Puzzle</title>
#         <link rel="stylesheet" href="puzzle.css">
#         <script src="puzzle.js"></script>
#     </head>

#     <body>
#         <img id="title" src="./logo.png">
#         <div id="board">
#         </div>
#         <h1>Turns: <span id="turns">0</span></h1>
#     </body>
# </html>





# var rows = 3;
# var columns = 3;

# var currTile;
# var otherTile; //blank tile

# var turns = 0;

# // var imgOrder = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
# var imgOrder = ["4", "2", "8", "5", "1", "6", "7", "9", "3"];

# window.onload = function() {
#     for (let r=0; r < rows; r++) {
#         for (let c=0; c < columns; c++) {

#             //<img id="0-0" src="1.jpg">
#             let tile = document.createElement("img");
#             tile.id = r.toString() + "-" + c.toString();
#             tile.src = imgOrder.shift() + ".jpg";

#             //DRAG FUNCTIONALITY
#             tile.addEventListener("dragstart", dragStart);  //click an image to drag
#             tile.addEventListener("dragover", dragOver);    //moving image around while clicked
#             tile.addEventListener("dragenter", dragEnter);  //dragging image onto another one
#             tile.addEventListener("dragleave", dragLeave);  //dragged image leaving anohter image
#             tile.addEventListener("drop", dragDrop);        //drag an image over another image, drop the image
#             tile.addEventListener("dragend", dragEnd);      //after drag drop, swap the two tiles

#             document.getElementById("board").append(tile);

#         }
#     }
# }

# function dragStart() {
#     currTile = this; //this refers to the img tile being dragged
# }

# function dragOver(e) {
#     e.preventDefault();
# }

# function dragEnter(e) {
#     e.preventDefault();
# }

# function dragLeave() {

# }

# function dragDrop() {
#     otherTile = this; //this refers to the img tile being dropped on
# }

# function dragEnd() {
#     if (!otherTile.src.includes("3.jpg")) {
#         return;
#     }

#     let currCoords = currTile.id.split("-"); //ex) "0-0" -> ["0", "0"]
#     let r = parseInt(currCoords[0]);
#     let c = parseInt(currCoords[1]);

#     let otherCoords = otherTile.id.split("-");
#     let r2 = parseInt(otherCoords[0]);
#     let c2 = parseInt(otherCoords[1]);

#     let moveLeft = r == r2 && c2 == c-1;
#     let moveRight = r == r2 && c2 == c+1;

#     let moveUp = c == c2 && r2 == r-1;
#     let moveDown = c == c2 && r2 == r+1;

#     let isAdjacent = moveLeft || moveRight || moveUp || moveDown;

#     if (isAdjacent) {
#         let currImg = currTile.src;
#         let otherImg = otherTile.src;

#         currTile.src = otherImg;
#         otherTile.src = currImg;

#         turns += 1;
#         document.getElementById("turns").innerText = turns;
#     }


# }



# body {
#     font-family: Arial, Helvetica, sans-serif;
#     text-align: center;
#     color: #0c67ae;
# }

# #title {
#     height: 150px;
#     width: 400px;
# }

# #board {
#     width: 360px;
#     height: 360px;
#     background-color: lightblue;
#     border: 10px solid #0c67ae;

#     margin: 0 auto;
#     display: flex;
#     flex-wrap: wrap;
# }

# #board img {
#     width: 118px;
#     height: 118px;
#     border: 1px solid #0c67ae;
# }




        


            elif 'snake' in game:
                print ('opening snake game')
                speak('opening snake game')

                os.startfile(r'D:\robotics\snake-master\index.html')


# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport", content="width=device-width, initial-scale=1.0">
#         <title>Snake</title>
#         <link rel="stylesheet" href="snake.css">
#         <script src="snake.js"></script>
#     </head>

#     <body>
#         <h1>Snake</h1>
#         <canvas id="board"></canvas>
#     </body>
# </html>



# //board
# var blockSize = 25;
# var rows = 20;
# var cols = 20;
# var board;
# var context; 

# //snake head
# var snakeX = blockSize * 5;
# var snakeY = blockSize * 5;

# var velocityX = 0;
# var velocityY = 0;

# var snakeBody = [];

# //food
# var foodX;
# var foodY;

# var gameOver = false;

# window.onload = function() {
#     board = document.getElementById("board");
#     board.height = rows * blockSize;
#     board.width = cols * blockSize;
#     context = board.getContext("2d"); //used for drawing on the board

#     placeFood();
#     document.addEventListener("keyup", changeDirection);
#     // update();
#     setInterval(update, 1000/10); //100 milliseconds
# }

# function update() {
#     if (gameOver) {
#         return;
#     }

#     context.fillStyle="black";
#     context.fillRect(0, 0, board.width, board.height);

#     context.fillStyle="red";
#     context.fillRect(foodX, foodY, blockSize, blockSize);

#     if (snakeX == foodX && snakeY == foodY) {
#         snakeBody.push([foodX, foodY]);
#         placeFood();
#     }

#     for (let i = snakeBody.length-1; i > 0; i--) {
#         snakeBody[i] = snakeBody[i-1];
#     }
#     if (snakeBody.length) {
#         snakeBody[0] = [snakeX, snakeY];
#     }

#     context.fillStyle="lime";
#     snakeX += velocityX * blockSize;
#     snakeY += velocityY * blockSize;
#     context.fillRect(snakeX, snakeY, blockSize, blockSize);
#     for (let i = 0; i < snakeBody.length; i++) {
#         context.fillRect(snakeBody[i][0], snakeBody[i][1], blockSize, blockSize);
#     }

#     //game over conditions
#     if (snakeX < 0 || snakeX > cols*blockSize || snakeY < 0 || snakeY > rows*blockSize) {
#         gameOver = true;
#         alert("Game Over");
#     }

#     for (let i = 0; i < snakeBody.length; i++) {
#         if (snakeX == snakeBody[i][0] && snakeY == snakeBody[i][1]) {
#             gameOver = true;
#             alert("Game Over");
#         }
#     }
# }

# function changeDirection(e) {
#     if (e.code == "ArrowUp" && velocityY != 1) {
#         velocityX = 0;
#         velocityY = -1;
#     }
#     else if (e.code == "ArrowDown" && velocityY != -1) {
#         velocityX = 0;
#         velocityY = 1;
#     }
#     else if (e.code == "ArrowLeft" && velocityX != 1) {
#         velocityX = -1;
#         velocityY = 0;
#     }
#     else if (e.code == "ArrowRight" && velocityX != -1) {
#         velocityX = 1;
#         velocityY = 0;
#     }
# }


# function placeFood() {
#     //(0-1) * cols -> (0-19.9999) -> (0-19) * 25
#     foodX = Math.floor(Math.random() * cols) * blockSize;
#     foodY = Math.floor(Math.random() * rows) * blockSize;
# }


# body {
#     font-family: 'Courier New', Courier, monospace;
#     text-align: center;
# }







            elif 'space' in game :
                print('opening space invader')
                speak('opening space invadors')

                os.startfile(r'D:\robotics\space-invaders-master\index.html')





# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport", content="width=device-width, initial-scale=1.0">
#         <title>Space Invaders</title>
#         <link rel="stylesheet" href="space.css">
#         <script src="space.js"></script>
#     </head>

#     <body>
#         <h1>Space Invaders</h1>
#         <canvas id="board"></canvas>
#     </body>
# </html>

# //board
# let tileSize = 32;
# let rows = 16;
# let columns = 16;

# let board;
# let boardWidth = tileSize * columns; // 32 * 16
# let boardHeight = tileSize * rows; // 32 * 16
# let context;

# //ship
# let shipWidth = tileSize*2;
# let shipHeight = tileSize;
# let shipX = tileSize * columns/2 - tileSize;
# let shipY = tileSize * rows - tileSize*2;

# let ship = {
#     x : shipX,
#     y : shipY,
#     width : shipWidth,
#     height : shipHeight
# }

# let shipImg;
# let shipVelocityX = tileSize; //ship moving speed

# //aliens
# let alienArray = [];
# let alienWidth = tileSize*2;
# let alienHeight = tileSize;
# let alienX = tileSize;
# let alienY = tileSize;
# let alienImg;

# let alienRows = 2;
# let alienColumns = 3;
# let alienCount = 0; //number of aliens to defeat
# let alienVelocityX = 1; //alien moving speed

# //bullets
# let bulletArray = [];
# let bulletVelocityY = -10; //bullet moving speed

# let score = 0;
# let gameOver = false;

# window.onload = function() {
#     board = document.getElementById("board");
#     board.width = boardWidth;
#     board.height = boardHeight;
#     context = board.getContext("2d"); //used for drawing on the board

#     //draw initial ship
#     // context.fillStyle="green";
#     // context.fillRect(ship.x, ship.y, ship.width, ship.height);

#     //load images
#     shipImg = new Image();
#     shipImg.src = "./ship.png";
#     shipImg.onload = function() {
#         context.drawImage(shipImg, ship.x, ship.y, ship.width, ship.height);
#     }

#     alienImg = new Image();
#     alienImg.src = "./alien.png";
#     createAliens();

#     requestAnimationFrame(update);
#     document.addEventListener("keydown", moveShip);
#     document.addEventListener("keyup", shoot);
# }

# function update() {
#     requestAnimationFrame(update);

#     if (gameOver) {
#         return;
#     }

#     context.clearRect(0, 0, board.width, board.height);

#     //ship
#     context.drawImage(shipImg, ship.x, ship.y, ship.width, ship.height);

#     //alien
#     for (let i = 0; i < alienArray.length; i++) {
#         let alien = alienArray[i];
#         if (alien.alive) {
#             alien.x += alienVelocityX;

#             //if alien touches the borders
#             if (alien.x + alien.width >= board.width || alien.x <= 0) {
#                 alienVelocityX *= -1;
#                 alien.x += alienVelocityX*2;

#                 //move all aliens up by one row
#                 for (let j = 0; j < alienArray.length; j++) {
#                     alienArray[j].y += alienHeight;
#                 }
#             }
#             context.drawImage(alienImg, alien.x, alien.y, alien.width, alien.height);

#             if (alien.y >= ship.y) {
#                 gameOver = true;
#             }
#         }
#     }

#     //bullets
#     for (let i = 0; i < bulletArray.length; i++) {
#         let bullet = bulletArray[i];
#         bullet.y += bulletVelocityY;
#         context.fillStyle="white";
#         context.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);

#         //bullet collision with aliens
#         for (let j = 0; j < alienArray.length; j++) {
#             let alien = alienArray[j];
#             if (!bullet.used && alien.alive && detectCollision(bullet, alien)) {
#                 bullet.used = true;
#                 alien.alive = false;
#                 alienCount--;
#                 score += 100;
#             }
#         }
#     }

#     //clear bullets
#     while (bulletArray.length > 0 && (bulletArray[0].used || bulletArray[0].y < 0)) {
#         bulletArray.shift(); //removes the first element of the array
#     }

#     //next level
#     if (alienCount == 0) {
#         //increase the number of aliens in columns and rows by 1
#         score += alienColumns * alienRows * 100; //bonus points :)
#         alienColumns = Math.min(alienColumns + 1, columns/2 -2); //cap at 16/2 -2 = 6
#         alienRows = Math.min(alienRows + 1, rows-4);  //cap at 16-4 = 12
#         if (alienVelocityX > 0) {
#             alienVelocityX += 0.2; //increase the alien movement speed towards the right
#         }
#         else {
#             alienVelocityX -= 0.2; //increase the alien movement speed towards the left
#         }
#         alienArray = [];
#         bulletArray = [];
#         createAliens();
#     }

#     //score
#     context.fillStyle="white";
#     context.font="16px courier";
#     context.fillText(score, 5, 20);
# }

# function moveShip(e) {
#     if (gameOver) {
#         return;
#     }

#     if (e.code == "ArrowLeft" && ship.x - shipVelocityX >= 0) {
#         ship.x -= shipVelocityX; //move left one tile
#     }
#     else if (e.code == "ArrowRight" && ship.x + shipVelocityX + ship.width <= board.width) {
#         ship.x += shipVelocityX; //move right one tile
#     }
# }

# function createAliens() {
#     for (let c = 0; c < alienColumns; c++) {
#         for (let r = 0; r < alienRows; r++) {
#             let alien = {
#                 img : alienImg,
#                 x : alienX + c*alienWidth,
#                 y : alienY + r*alienHeight,
#                 width : alienWidth,
#                 height : alienHeight,
#                 alive : true
#             }
#             alienArray.push(alien);
#         }
#     }
#     alienCount = alienArray.length;
# }

# function shoot(e) {
#     if (gameOver) {
#         return;
#     }

#     if (e.code == "Space") {
#         //shoot
#         let bullet = {
#             x : ship.x + shipWidth*15/32,
#             y : ship.y,
#             width : tileSize/8,
#             height : tileSize/2,
#             used : false
#         }
#         bulletArray.push(bullet);
#     }
# }

# function detectCollision(a, b) {
#     return a.x < b.x + b.width &&   //a's top left corner doesn't reach b's top right corner
#            a.x + a.width > b.x &&   //a's top right corner passes b's top left corner
#            a.y < b.y + b.height &&  //a's top left corner doesn't reach b's bottom left corner
#            a.y + a.height > b.y;    //a's bottom left corner passes b's top left corner
# }


# body {
#     font-family:'Courier New', Courier, monospace;
#     text-align: center;
# }

# #board {
#     background-color: black;
# }





            elif 'sudoku' in game :
                print('opening sudoku master')
                speak('opening sudoku master')

                os.startfile(r'D:\robotics\Sudoku-master\index.html')



# <html>
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width initial-scale=1.0 user-scalable=no">
#         <title>Sudoku</title>

#         <link rel="stylesheet" href="sudoku.css">
#         <script src="sudoku.js"></script>
#     </head>

#     <body>
#         <h1>Sudoku</h1>
#         <hr>
#         <h2 id="errors">0</h2>

#         <!-- 9x9 board -->
#         <div id="board"></div>
#         <br>
#         <div id="digits">
#         </div>

#     </body>


# </html>
   
   
   

# var numSelected = null;
# var tileSelected = null;

# var errors = 0;

# var board = [
#     "--74916-5",
#     "2---6-3-9",
#     "-----7-1-",
#     "-586----4",
#     "--3----9-",
#     "--62--187",
#     "9-4-7---2",
#     "67-83----",
#     "81--45---"
# ]

# var solution = [
#     "387491625",
#     "241568379",
#     "569327418",
#     "758619234",
#     "123784596",
#     "496253187",
#     "934176852",
#     "675832941",
#     "812945763"
# ]

# window.onload = function() {
#     setGame();
# }

# function setGame() {
#     // Digits 1-9
#     for (let i = 1; i <= 9; i++) {
#         //<div id="1" class="number">1</div>
#         let number = document.createElement("div");
#         number.id = i
#         number.innerText = i;
#         number.addEventListener("click", selectNumber);
#         number.classList.add("number");
#         document.getElementById("digits").appendChild(number);
#     }

#     // Board 9x9
#     for (let r = 0; r < 9; r++) {
#         for (let c = 0; c < 9; c++) {
#             let tile = document.createElement("div");
#             tile.id = r.toString() + "-" + c.toString();
#             if (board[r][c] != "-") {
#                 tile.innerText = board[r][c];
#                 tile.classList.add("tile-start");
#             }
#             if (r == 2 || r == 5) {
#                 tile.classList.add("horizontal-line");
#             }
#             if (c == 2 || c == 5) {
#                 tile.classList.add("vertical-line");
#             }
#             tile.addEventListener("click", selectTile);
#             tile.classList.add("tile");
#             document.getElementById("board").append(tile);
#         }
#     }
# }

# function selectNumber(){
#     if (numSelected != null) {
#         numSelected.classList.remove("number-selected");
#     }
#     numSelected = this;
#     numSelected.classList.add("number-selected");
# }

# function selectTile() {
#     if (numSelected) {
#         if (this.innerText != "") {
#             return;
#         }

#         // "0-0" "0-1" .. "3-1"
#         let coords = this.id.split("-"); //["0", "0"]
#         let r = parseInt(coords[0]);
#         let c = parseInt(coords[1]);

#         if (solution[r][c] == numSelected.id) {
#             this.innerText = numSelected.id;
#         }
#         else {
#             errors += 1;
#             document.getElementById("errors").innerText = errors;
#         }
#     }
# }

   
# body {
#     font-family: Arial, Helvetica, sans-serif;
#     text-align: center;
# }

# hr {
#     width: 500px;
# }

# #errors {
#     color: coral;
# }

# #board {
#     width: 450px;
#     height: 450px;

#     margin: 0 auto;
#     display: flex;
#     flex-wrap: wrap;
# }

# .tile {
#     width: 48px; 
#     height: 48px;
#     border: 1px solid lightgray;

#     /* Text */
#     font-size: 20px;
#     font-weight: bold;
#     display: flex;
#     justify-content: center;
#     align-items: center;
# }

# #digits {
#     width: 450px;
#     height: 50px;

#     margin: 0 auto;
#     display: flex;
#     flex-wrap: wrap;
# }

# .number {
#     width: 44px; 
#     height: 44px;
#     border: 1px solid black;
#     margin: 2px;

#     /* Text */
#     font-size: 20px;
#     font-weight: bold;
#     display: flex;
#     justify-content: center;
#     align-items: center;
# }

# .number-selected {
#     background-color: gray;
# }

# .tile-start {
#     background-color: whitesmoke;
# }

# .horizontal-line {
#     border-bottom: 1px solid black;
# }

# .vertical-line {
#     border-right: 1px solid black;
# }   
   
   
   
   
   
            elif 'tic' in game :
                print('opening tic tac toe')
                speak('opening tic tac toe')

                os.startfile(r'D:\robotics\Tic-Tac-Toe-master\index.html')



# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Tic Tac Toe</title>
#     <link rel="stylesheet" href="tictactoe.css">
#     <script src="tictactoe.js"></script>
# </head>
# <body>
#     <h1>Tic Tac Toe</h1>
#     <hr>
#     <br>
#     <!-- 3x3 -->
#     <div id="board">
#     </div>
# </body>
# </html>


# var board;
# var playerO = "O";
# var playerX = "X";
# var currPlayer = playerO;
# var gameOver = false;

# window.onload = function() {
#     setGame();
# }

# function setGame() {
#     board = [
#                 [' ', ' ', ' '],
#                 [' ', ' ', ' '],
#                 [' ', ' ', ' ']
#             ]

#     for (let r = 0; r < 3; r++) {
#         for (let c = 0; c < 3; c++) {
#             let tile = document.createElement("div");
#             tile.id = r.toString() + "-" + c.toString();
#             tile.classList.add("tile");
#             if (r == 0 || r == 1) {
#                 tile.classList.add("horizontal-line");
#             }
#             if (c == 0 || c == 1) {
#                 tile.classList.add("vertical-line");
#             }
#             tile.innerText = "";
#             tile.addEventListener("click", setTile);
#             document.getElementById("board").appendChild(tile);
#         }
#     }
# }

# function setTile() {
#     if (gameOver) {
#         return;
#     }

#     let coords = this.id.split("-");    //ex) "1-2" -> ["1", "2'"]
#     let r = parseInt(coords[0]);
#     let c = parseInt(coords[1]);

#     if (board[r][c] != ' ') { 
#         //already taken spot
#         return;
#     }
    
#     board[r][c] = currPlayer; //mark the board
#     this.innerText = currPlayer; //mark the board on html

#     //change players
#     if (currPlayer == playerO) {
#         currPlayer = playerX;
#     }
#     else {
#         currPlayer = playerO;
#     }

#     //check winner
#     checkWinner();
# }


# function checkWinner() {
#     //horizontally, check 3 rows
#     for (let r = 0; r < 3; r++) {
#         if (board[r][0] == board[r][1] && board[r][1] == board[r][2] && board[r][0] != ' ') {
#             //if we found the winning row
#             //apply the winner style to that row
#             for (let i = 0; i < 3; i++) {
#                 let tile = document.getElementById(r.toString() + "-" + i.toString());
#                 tile.classList.add("winner");
#             }
#             gameOver = true;
#             return;
#         }
#     }

#     //vertically, check 3 columns
#     for (let c = 0; c < 3; c++) {
#         if (board[0][c] == board[1][c] && board[1][c] ==  board[2][c] && board[0][c] != ' ') {
#             //if we found the winning col
#             //apply the winner style to that col
#             for (let i = 0; i < 3; i++) {
#                 let tile = document.getElementById(i.toString() + "-" + c.toString());                
#                 tile.classList.add("winner");
#             }
#             gameOver = true;
#             return;
#         }
#     }

#     //diagonally
#     if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ' ') {
#         for (let i = 0; i < 3; i++) {
#             let tile = document.getElementById(i.toString() + "-" + i.toString());                
#             tile.classList.add("winner");
#         }
#         gameOver = true;
#         return;
#     }

#     //anti-diagonally
#     if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != ' ') {
#         //0-2
#         let tile = document.getElementById("0-2");                
#         tile.classList.add("winner");

#         //1-1
#         tile = document.getElementById("1-1");                
#         tile.classList.add("winner");

#         //2-0
#         tile = document.getElementById("2-0");                
#         tile.classList.add("winner");
#         gameOver = true;
#         return;
#     }
# }





# body {
#     font-family: Arial, Helvetica, sans-serif;
#     text-align: center;
# }

# hr {
#     width: 500px;
#     height: 2px;
#     background-color: black;
# }


# #board {
#     width: 450px;
#     height: 450px;
#     /* background-color: gray; */
#     margin: 0 auto;
#     display: flex;
#     flex-wrap: wrap;
# }

# .tile {
#     width: 147px;
#     height: 147px;
    
#     /* Text */
#     font-size: 150px;
#     display: flex;
#     justify-content: center; 
#     align-items: center;    
# }

# .winner {
#     background-color: lightgray;
#     color: red;
# }


# .horizontal-line {
#     border-bottom: 3px solid black;
# }

# .vertical-line {
#     border-right: 3px solid black;
# }






            elif 'whac' in game :
                print('opening whac a mole')
                speak('opening whac a mole')

                os.startfile(r'D:\robotics\whac-a-mole-master\index.html')


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Whac a Mole</title>
#     <link rel="stylesheet" href="mole.css">
#     <script src="mole.js"></script>
# </head>
# <body>
#     <h1>Whac a Mole</h1>
#     <h2 id="score">0</h2>
#     <!-- 3x3 -->
#     <div id="board">
#     </div>
# </body>
# </html>






# let currMoleTile;
# let currPlantTile;
# let score = 0;
# let gameOver = false;

# window.onload = function() {
#     setGame();
# }

# function setGame() {
#     //set up the grid in html
#     for (let i = 0; i < 9; i++) { //i goes from 0 to 8, stops at 9
#         //<div id="0-8"></div>
#         let tile = document.createElement("div");
#         tile.id = i.toString();
#         tile.addEventListener("click", selectTile);
#         document.getElementById("board").appendChild(tile);
#     }
#     setInterval(setMole, 1000); // 1000 miliseconds = 1 second, every 1 second call setMole
#     setInterval(setPlant, 2000); // 2000 miliseconds = 2 seconds, every 2 second call setPlant
# }

# function getRandomTile() {
#     //math.random --> 0-1 --> (0-1) * 9 = (0-9) --> round down to (0-8) integers
#     let num = Math.floor(Math.random() * 9);
#     return num.toString();
# }

# function setMole() {
#     if (gameOver) {
#         return;
#     }
#     if (currMoleTile) {
#         currMoleTile.innerHTML = "";
#     }
#     let mole = document.createElement("img");
#     mole.src = "./monty-mole.png";

#     let num = getRandomTile();
#     if (currPlantTile && currPlantTile.id == num) {
#         return;
#     }
#     currMoleTile = document.getElementById(num);
#     currMoleTile.appendChild(mole);
# }

# function setPlant() {
#     if (gameOver) {
#         return;
#     }
#     if (currPlantTile) {
#         currPlantTile.innerHTML = "";
#     }
#     let plant = document.createElement("img");
#     plant.src = "./piranha-plant.png";

#     let num = getRandomTile();
#     if (currMoleTile && currMoleTile.id == num) {
#         return;
#     }
#     currPlantTile = document.getElementById(num);
#     currPlantTile.appendChild(plant);
# }

# function selectTile() {
#     if (gameOver) {
#         return;
#     }
#     if (this == currMoleTile) {
# #         score += 10;
# #         document.getElementById("score").innerText = score.toString(); //update score html
# #     }
# #     else if (this == currPlantTile) {
# #         document.getElementById("score").innerText = "GAME OVER: " + score.toString(); //update score html
# #         gameOver = true;
# #     }
# # }


#    body {
#     font-family: Arial, Helvetica, sans-serif;
#     text-align: center;
#     background: url("./mario-bg.jpg");
#     background-size: cover;
# }

# #board {
#     width: 540px;
#     height: 540px;
#     /* background-color: green; */

#     margin: 0 auto;
#     display: flex;
#     flex-wrap: wrap;

#     background: url("./soil.png");
#     background-size: cover;
#     border: 3px solid white;
#     border-radius: 25px;
# }

# #board div {
#     /* board = 540 x 540, divide into 3x3 tiles --> 180 x 180 per div */
#     width: 180px; 
#     height: 180px;
#     background-image: url("./pipe.png");
#     background-size: cover;
# }

# #board div img {
#     /* all img tags inside tiles */
#     width: 100px;
#     height: 100px;

#     user-select: none;
#     -moz-user-select: none;
#     -webkit-user-drag: none;
#     -webkit-user-select: none;
#     -ms-user-select: none;
# }         
   
   
   
   
   
   
   
   
   
   
   
            elif 'wordle' in game :
                print('opening wordle master')
                speak('opening wordle master')

                os.startfile(r'D:\robotics\Wordle-master\index.html')






# <html>
#     <head>
#         <title>Wordle</title>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale = 1.0">

#         <link rel="stylesheet" href="wordle.css">
#         <script src="wordle.js"></script>
#     </head>

#     <body>
#         <h1 id="title">Wordle</h1>
#         <hr>
#         <br>
#         <div id="board">
#         </div>

# #         <br>
# #         <h1 id="answer"></h1>
# #     </body>
# # </html>

# var height = 6;
# //number of guesses
# var width = 5;
# //length of the word

# var row = 0;
# //current guess (attempt #)
# var col = 0;
# //current letter for that attempt

# var gameOver = false;
# // var word = "SQUID";
# var wordList = ["cigar", "rebut", "sissy", "humph", "awake", "blush", "focal", "evade", "naval", "serve", "heath", "dwarf", "model", "karma", "stink", "grade", "quiet", "bench", "abate", "feign", "major", "death", "fresh", "crust", "stool", "colon", "abase", "marry", "react", "batty", "pride", "floss", "helix", "croak", "staff", "paper", "unfed", "whelp", "trawl", "outdo", "adobe", "crazy", "sower", "repay", "digit", "crate", "cluck", "spike", "mimic", "pound", "maxim", "linen", "unmet", "flesh", "booby", "forth", "first", "stand", "belly", "ivory", "seedy", "print", "yearn", "drain", "bribe", "stout", "panel", "crass", "flume", "offal", "agree", "error", "swirl", "argue", "bleed", "delta", "flick", "totem", "wooer", "front", "shrub", "parry", "biome", "lapel", "start", "greet", "goner", "golem", "lusty", "loopy", "round", "audit", "lying", "gamma", "labor", "islet", "civic", "forge", "corny", "moult", "basic", "salad", "agate", "spicy", "spray", "essay", "fjord", "spend", "kebab", "guild", "aback", "motor", "alone", "hatch", "hyper", "thumb", "dowry", "ought", "belch", "dutch", "pilot", "tweed", "comet", "jaunt", "enema", "steed", "abyss", "growl", "fling", "dozen", "boozy", "erode", "world", "gouge", "click", "briar", "great", "altar", "pulpy", "blurt", "coast", "duchy", "groin", "fixer", "group", "rogue", "badly", "smart", "pithy", "gaudy", "chill", "heron", "vodka", "finer", "surer", "radio", "rouge", "perch", "retch", "wrote", "clock", "tilde", "store", "prove", "bring", "solve", "cheat", "grime", "exult", "usher", "epoch", "triad", "break", "rhino", "viral", "conic", "masse", "sonic", "vital", "trace", "using", "peach", "champ", "baton", "brake", "pluck", "craze", "gripe", "weary", "picky", "acute", "ferry", "aside", "tapir", "troll", "unify", "rebus", "boost", "truss", "siege", "tiger", "banal", "slump", "crank", "gorge", "query", "drink", "favor", "abbey", "tangy", "panic", "solar", "shire", "proxy", "point", "robot", "prick", "wince", "crimp", "knoll", "sugar", "whack", "mount", "perky", "could", "wrung", "light", "those", "moist", "shard", "pleat", "aloft", "skill", "elder", "frame", "humor", "pause", "ulcer", "ultra", "robin", "cynic", "aroma", "caulk", "shake", "dodge", "swill", "tacit", "other", "thorn", "trove", "bloke", "vivid", "spill", "chant", "choke", "rupee", "nasty", "mourn", "ahead", "brine", "cloth", "hoard", "sweet", "month", "lapse", "watch", "today", "focus", "smelt", "tease", "cater", "movie", "saute", "allow", "renew", "their", "slosh", "purge", "chest", "depot", "epoxy", "nymph", "found", "shall", "harry", "stove", "lowly", "snout", "trope", "fewer", "shawl", "natal", "comma", "foray", "scare", "stair", "black", "squad", "royal", "chunk", "mince", "shame", "cheek", "ample", "flair", "foyer", "cargo", "oxide", "plant", "olive", "inert", "askew", "heist", "shown", "zesty", "hasty", "trash", "fella", "larva", "forgo", "story", "hairy", "train", "homer", "badge", "midst", "canny", "fetus", "butch", "farce", "slung", "tipsy", "metal", "yield", "delve", "being", "scour", "glass", "gamer", "scrap", "money", "hinge", "album", "vouch", "asset", "tiara", "crept", "bayou", "atoll", "manor", "creak", "showy", "phase", "froth", "depth", "gloom", "flood", "trait", "girth", "piety", "payer", "goose", "float", "donor", "atone", "primo", "apron", "blown", "cacao", "loser", "input", "gloat", "awful", "brink", "smite", "beady", "rusty", "retro", "droll", "gawky", "hutch", "pinto", "gaily", "egret", "lilac", "sever", "field", "fluff", "hydro", "flack", "agape", "voice", "stead", "stalk", "berth", "madam", "night", "bland", "liver", "wedge", "augur", "roomy", "wacky", "flock", "angry", "bobby", "trite", "aphid", "tryst", "midge", "power", "elope", "cinch", "motto", "stomp", "upset", "bluff", "cramp", "quart", "coyly", "youth", "rhyme", "buggy", "alien", "smear", "unfit", "patty", "cling", "glean", "label", "hunky", "khaki", "poker", "gruel", "twice", "twang", "shrug", "treat", "unlit", "waste", "merit", "woven", "octal", "needy", "clown", "widow", "irony", "ruder", "gauze", "chief", "onset", "prize", "fungi", "charm", "gully", "inter", "whoop", "taunt", "leery", "class", "theme", "lofty", "tibia", "booze", "alpha", "thyme", "eclat", "doubt", "parer", "chute", "stick", "trice", "alike", "sooth", "recap", "saint", "liege", "glory", "grate", "admit", "brisk", "soggy", "usurp", "scald", "scorn", "leave", "twine", "sting", "bough", "marsh", "sloth", "dandy", "vigor", "howdy", "enjoy", "valid", "ionic", "equal", "unset", "floor", "catch", "spade", "stein", "exist", "quirk", "denim", "grove", "spiel", "mummy", "fault", "foggy", "flout", "carry", "sneak", "libel", "waltz", "aptly", "piney", "inept", "aloud", "photo", "dream", "stale", "vomit", "ombre", "fanny", "unite", "snarl", "baker", "there", "glyph", "pooch", "hippy", "spell", "folly", "louse", "gulch", "vault", "godly", "threw", "fleet", "grave", "inane", "shock", "crave", "spite", "valve", "skimp", "claim", "rainy", "musty", "pique", "daddy", "quasi", "arise", "aging", "valet", "opium", "avert", "stuck", "recut", "mulch", "genre", "plume", "rifle", "count", "incur", "total", "wrest", "mocha", "deter", "study", "lover", "safer", "rivet", "funny", "smoke", "mound", "undue", "sedan", "pagan", "swine", "guile", "gusty", "equip", "tough", "canoe", "chaos", "covet", "human", "udder", "lunch", "blast", "stray", "manga", "melee", "lefty", "quick", "paste", "given", "octet", "risen", "groan", "leaky", "grind", "carve", "loose", "sadly", "spilt", "apple", "slack", "honey", "final", "sheen", "eerie", "minty", "slick", "derby", "wharf", "spelt", "coach", "erupt", "singe", "price", "spawn", "fairy", "jiffy", "filmy", "stack", "chose", "sleep", "ardor", "nanny", "niece", "woozy", "handy", "grace", "ditto", "stank", "cream", "usual", "diode", "valor", "angle", "ninja", "muddy", "chase", "reply", "prone", "spoil", "heart", "shade", "diner", "arson", "onion", "sleet", "dowel", "couch", "palsy", "bowel", "smile", "evoke", "creek", "lance", "eagle", "idiot", "siren", "built", "embed", "award", "dross", "annul", "goody", "frown", "patio", "laden", "humid", "elite", "lymph", "edify", "might", "reset", "visit", "gusto", "purse", "vapor", "crock", "write", "sunny", "loath", "chaff", "slide", "queer", "venom", "stamp", "sorry", "still", "acorn", "aping", "pushy", "tamer", "hater", "mania", "awoke", "brawn", "swift", "exile", "birch", "lucky", "freer", "risky", "ghost", "plier", "lunar", "winch", "snare", "nurse", "house", "borax", "nicer", "lurch", "exalt", "about", "savvy", "toxin", "tunic", "pried", "inlay", "chump", "lanky", "cress", "eater", "elude", "cycle", "kitty", "boule", "moron", "tenet", "place", "lobby", "plush", "vigil", "index", "blink", "clung", "qualm", "croup", "clink", "juicy", "stage", "decay", "nerve", "flier", "shaft", "crook", "clean", "china", "ridge", "vowel", "gnome", "snuck", "icing", "spiny", "rigor", "snail", "flown", "rabid", "prose", "thank", "poppy", "budge", "fiber", "moldy", "dowdy", "kneel", "track", "caddy", "quell", "dumpy", "paler", "swore", "rebar", "scuba", "splat", "flyer", "horny", "mason", "doing", "ozone", "amply", "molar", "ovary", "beset", "queue", "cliff", "magic", "truce", "sport", "fritz", "edict", "twirl", "verse", "llama", "eaten", "range", "whisk", "hovel", "rehab", "macaw", "sigma", "spout", "verve", "sushi", "dying", "fetid", "brain", "buddy", "thump", "scion", "candy", "chord", "basin", "march", "crowd", "arbor", "gayly", "musky", "stain", "dally", "bless", "bravo", "stung", "title", "ruler", "kiosk", "blond", "ennui", "layer", "fluid", "tatty", "score", "cutie", "zebra", "barge", "matey", "bluer", "aider", "shook", "river", "privy", "betel", "frisk", "bongo", "begun", "azure", "weave", "genie", "sound", "glove", "braid", "scope", "wryly", "rover", "assay", "ocean", "bloom", "irate", "later", "woken", "silky", "wreck", "dwelt", "slate", "smack", "solid", "amaze", "hazel", "wrist", "jolly", "globe", "flint", "rouse", "civil", "vista", "relax", "cover", "alive", "beech", "jetty", "bliss", "vocal", "often", "dolly", "eight", "joker", "since", "event", "ensue", "shunt", "diver", "poser", "worst", "sweep", "alley", "creed", "anime", "leafy", "bosom", "dunce", "stare", "pudgy", "waive", "choir", "stood", "spoke", "outgo", "delay", "bilge", "ideal", "clasp", "seize", "hotly", "laugh", "sieve", "block", "meant", "grape", "noose", "hardy", "shied", "drawl", "daisy", "putty", "strut", "burnt", "tulip", "crick", "idyll", "vixen", "furor", "geeky", "cough", "naive", "shoal", "stork", "bathe", "aunty", "check", "prime", "brass", "outer", "furry", "razor", "elect", "evict", "imply", "demur", "quota", "haven", "cavil", "swear", "crump", "dough", "gavel", "wagon", "salon", "nudge", "harem", "pitch", "sworn", "pupil", "excel", "stony", "cabin", "unzip", "queen", "trout", "polyp", "earth", "storm", "until", "taper", "enter", "child", "adopt", "minor", "fatty", "husky", "brave", "filet", "slime", "glint", "tread", "steal", "regal", "guest", "every", "murky", "share", "spore", "hoist", "buxom", "inner", "otter", "dimly", "level", "sumac", "donut", "stilt", "arena", "sheet", "scrub", "fancy", "slimy", "pearl", "silly", "porch", "dingo", "sepia", "amble", "shady", "bread", "friar", "reign", "dairy", "quill", "cross", "brood", "tuber", "shear", "posit", "blank", "villa", "shank", "piggy", "freak", "which", "among", "fecal", "shell", "would", "algae", "large", "rabbi", "agony", "amuse", "bushy", "copse", "swoon", "knife", "pouch", "ascot", "plane", "crown", "urban", "snide", "relay", "abide", "viola", "rajah", "straw", "dilly", "crash", "amass", "third", "trick", "tutor", "woody", "blurb", "grief", "disco", "where", "sassy", "beach", "sauna", "comic", "clued", "creep", "caste", "graze", "snuff", "frock", "gonad", "drunk", "prong", "lurid", "steel", "halve", "buyer", "vinyl", "utile", "smell", "adage", "worry", "tasty", "local", "trade", "finch", "ashen", "modal", "gaunt", "clove", "enact", "adorn", "roast", "speck", "sheik", "missy", "grunt", "snoop", "party", "touch", "mafia", "emcee", "array", "south", "vapid", "jelly", "skulk", "angst", "tubal", "lower", "crest", "sweat", "cyber", "adore", "tardy", "swami", "notch", "groom", "roach", "hitch", "young", "align", "ready", "frond", "strap", "puree", "realm", "venue", "swarm", "offer", "seven", "dryer", "diary", "dryly", "drank", "acrid", "heady", "theta", "junto", "pixie", "quoth", "bonus", "shalt", "penne", "amend", "datum", "build", "piano", "shelf", "lodge", "suing", "rearm", "coral", "ramen", "worth", "psalm", "infer", "overt", "mayor", "ovoid", "glide", "usage", "poise", "randy", "chuck", "prank", "fishy", "tooth", "ether", "drove", "idler", "swath", "stint", "while", "begat", "apply", "slang", "tarot", "radar", "credo", "aware", "canon", "shift", "timer", "bylaw", "serum", "three", "steak", "iliac", "shirk", "blunt", "puppy", "penal", "joist", "bunny", "shape", "beget", "wheel", "adept", "stunt", "stole", "topaz", "chore", "fluke", "afoot", "bloat", "bully", "dense", "caper", "sneer", "boxer", "jumbo", "lunge", "space", "avail", "short", "slurp", "loyal", "flirt", "pizza", "conch", "tempo", "droop", "plate", "bible", "plunk", "afoul", "savoy", "steep", "agile", "stake", "dwell", "knave", "beard", "arose", "motif", "smash", "broil", "glare", "shove", "baggy", "mammy", "swamp", "along", "rugby", "wager", "quack", "squat", "snaky", "debit", "mange", "skate", "ninth", "joust", "tramp", "spurn", "medal", "micro", "rebel", "flank", "learn", "nadir", "maple", "comfy", "remit", "gruff", "ester", "least", "mogul", "fetch", "cause", "oaken", "aglow", "meaty", "gaffe", "shyly", "racer", "prowl", "thief", "stern", "poesy", "rocky", "tweet", "waist", "spire", "grope", "havoc", "patsy", "truly", "forty", "deity", "uncle", "swish", "giver", "preen", "bevel", "lemur", "draft", "slope", "annoy", "lingo", "bleak", "ditty", "curly", "cedar", "dirge", "grown", "horde", "drool", "shuck", "crypt", "cumin", "stock", "gravy", "locus", "wider", "breed", "quite", "chafe", "cache", "blimp", "deign", "fiend", "logic", "cheap", "elide", "rigid", "false", "renal", "pence", "rowdy", "shoot", "blaze", "envoy", "posse", "brief", "never", "abort", "mouse", "mucky", "sulky", "fiery", "media", "trunk", "yeast", "clear", "skunk", "scalp", "bitty", "cider", "koala", "duvet", "segue", "creme", "super", "grill", "after", "owner", "ember", "reach", "nobly", "empty", "speed", "gipsy", "recur", "smock", "dread", "merge", "burst", "kappa", "amity", "shaky", "hover", "carol", "snort", "synod", "faint", "haunt", "flour", "chair", "detox", "shrew", "tense", "plied", "quark", "burly", "novel", "waxen", "stoic", "jerky", "blitz", "beefy", "lyric", "hussy", "towel", "quilt", "below", "bingo", "wispy", "brash", "scone", "toast", "easel", "saucy", "value", "spice", "honor", "route", "sharp", "bawdy", "radii", "skull", "phony", "issue", "lager", "swell", "urine", "gassy", "trial", "flora", "upper", "latch", "wight", "brick", "retry", "holly", "decal", "grass", "shack", "dogma", "mover", "defer", "sober", "optic", "crier", "vying", "nomad", "flute", "hippo", "shark", "drier", "obese", "bugle", "tawny", "chalk", "feast", "ruddy", "pedal", "scarf", "cruel", "bleat", "tidal", "slush", "semen", "windy", "dusty", "sally", "igloo", "nerdy", "jewel", "shone", "whale", "hymen", "abuse", "fugue", "elbow", "crumb", "pansy", "welsh", "syrup", "terse", "suave", "gamut", "swung", "drake", "freed", "afire", "shirt", "grout", "oddly", "tithe", "plaid", "dummy", "broom", "blind", "torch", "enemy", "again", "tying", "pesky", "alter", "gazer", "noble", "ethos", "bride", "extol", "decor", "hobby", "beast", "idiom", "utter", "these", "sixth", "alarm", "erase", "elegy", "spunk", "piper", "scaly", "scold", "hefty", "chick", "sooty", "canal", "whiny", "slash", "quake", "joint", "swept", "prude", "heavy", "wield", "femme", "lasso", "maize", "shale", "screw", "spree", "smoky", "whiff", "scent", "glade", "spent", "prism", "stoke", "riper", "orbit", "cocoa", "guilt", "humus", "shush", "table", "smirk", "wrong", "noisy", "alert", "shiny", "elate", "resin", "whole", "hunch", "pixel", "polar", "hotel", "sword", "cleat", "mango", "rumba", "puffy", "filly", "billy", "leash", "clout", "dance", "ovate", "facet", "chili", "paint", "liner", "curio", "salty", "audio", "snake", "fable", "cloak", "navel", "spurt", "pesto", "balmy", "flash", "unwed", "early", "churn", "weedy", "stump", "lease", "witty", "wimpy", "spoof", "saner", "blend", "salsa", "thick", "warty", "manic", "blare", "squib", "spoon", "probe", "crepe", "knack", "force", "debut", "order", "haste", "teeth", "agent", "widen", "icily", "slice", "ingot", "clash", "juror", "blood", "abode", "throw", "unity", "pivot", "slept", "troop", "spare", "sewer", "parse", "morph", "cacti", "tacky", "spool", "demon", "moody", "annex", "begin", "fuzzy", "patch", "water", "lumpy", "admin", "omega", "limit", "tabby", "macho", "aisle", "skiff", "basis", "plank", "verge", "botch", "crawl", "lousy", "slain", "cubic", "raise", "wrack", "guide", "foist", "cameo", "under", "actor", "revue", "fraud", "harpy", "scoop", "climb", "refer", "olden", "clerk", "debar", "tally", "ethic", "cairn", "tulle", "ghoul", "hilly", "crude", "apart", "scale", "older", "plain", "sperm", "briny", "abbot", "rerun", "quest", "crisp", "bound", "befit", "drawn", "suite", "itchy", "cheer", "bagel", "guess", "broad", "axiom", "chard", "caput", "leant", "harsh", "curse", "proud", "swing", "opine", "taste", "lupus", "gumbo", "miner", "green", "chasm", "lipid", "topic", "armor", "brush", "crane", "mural", "abled", "habit", "bossy", "maker", "dusky", "dizzy", "lithe", "brook", "jazzy", "fifty", "sense", "giant", "surly", "legal", "fatal", "flunk", "began", "prune", "small", "slant", "scoff", "torus", "ninny", "covey", "viper", "taken", "moral", "vogue", "owing", "token", "entry", "booth", "voter", "chide", "elfin", "ebony", "neigh", "minim", "melon", "kneed", "decoy", "voila", "ankle", "arrow", "mushy", "tribe", "cease", "eager", "birth", "graph", "odder", "terra", "weird", "tried", "clack", "color", "rough", "weigh", "uncut", "ladle", "strip", "craft", "minus", "dicey", "titan", "lucid", "vicar", "dress", "ditch", "gypsy", "pasta", "taffy", "flame", "swoop", "aloof", "sight", "broke", "teary", "chart", "sixty", "wordy", "sheer", "leper", "nosey", "bulge", "savor", "clamp", "funky", "foamy", "toxic", "brand", "plumb", "dingy", "butte", "drill", "tripe", "bicep", "tenor", "krill", "worse", "drama", "hyena", "think", "ratio", "cobra", "basil", "scrum", "bused", "phone", "court", "camel", "proof", "heard", "angel", "petal", "pouty", "throb", "maybe", "fetal", "sprig", "spine", "shout", "cadet", "macro", "dodgy", "satyr", "rarer", "binge", "trend", "nutty", "leapt", "amiss", "split", "myrrh", "width", "sonar", "tower", "baron", "fever", "waver", "spark", "belie", "sloop", "expel", "smote", "baler", "above", "north", "wafer", "scant", "frill", "awash", "snack", "scowl", "frail", "drift", "limbo", "fence", "motel", "ounce", "wreak", "revel", "talon", "prior", "knelt", "cello", "flake", "debug", "anode", "crime", "salve", "scout", "imbue", "pinky", "stave", "vague", "chock", "fight", "video", "stone", "teach", "cleft", "frost", "prawn", "booty", "twist", "apnea", "stiff", "plaza", "ledge", "tweak", "board", "grant", "medic", "bacon", "cable", "brawl", "slunk", "raspy", "forum", "drone", "women", "mucus", "boast", "toddy", "coven", "tumor", "truer", "wrath", "stall", "steam", "axial", "purer", "daily", "trail", "niche", "mealy", "juice", "nylon", "plump", "merry", "flail", "papal", "wheat", "berry", "cower", "erect", "brute", "leggy", "snipe", "sinew", "skier", "penny", "jumpy", "rally", "umbra", "scary", "modem", "gross", "avian", "greed", "satin", "tonic", "parka", "sniff", "livid", "stark", "trump", "giddy", "reuse", "taboo", "avoid", "quote", "devil", "liken", "gloss", "gayer", "beret", "noise", "gland", "dealt", "sling", "rumor", "opera", "thigh", "tonga", "flare", "wound", "white", "bulky", "etude", "horse", "circa", "paddy", "inbox", "fizzy", "grain", "exert", "surge", "gleam", "belle", "salvo", "crush", "fruit", "sappy", "taker", "tract", "ovine", "spiky", "frank", "reedy", "filth", "spasm", "heave", "mambo", "right", "clank", "trust", "lumen", "borne", "spook", "sauce", "amber", "lathe", "carat", "corer", "dirty", "slyly", "affix", "alloy", "taint", "sheep", "kinky", "wooly", "mauve", "flung", "yacht", "fried", "quail", "brunt", "grimy", "curvy", "cagey", "rinse", "deuce", "state", "grasp", "milky", "bison", "graft", "sandy", "baste", "flask", "hedge", "girly", "swash", "boney", "coupe", "endow", "abhor", "welch", "blade", "tight", "geese", "miser", "mirth", "cloud", "cabal", "leech", "close", "tenth", "pecan", "droit", "grail", "clone", "guise", "ralph", "tango", "biddy", "smith", "mower", "payee", "serif", "drape", "fifth", "spank", "glaze", "allot", "truck", "kayak", "virus", "testy", "tepee", "fully", "zonal", "metro", "curry", "grand", "banjo", "axion", "bezel", "occur", "chain", "nasal", "gooey", "filer", "brace", "allay", "pubic", "raven", "plead", "gnash", "flaky", "munch", "dully", "eking", "thing", "slink", "hurry", "theft", "shorn", "pygmy", "ranch", "wring", "lemon", "shore", "mamma", "froze", "newer", "style", "moose", "antic", "drown", "vegan", "chess", "guppy", "union", "lever", "lorry", "image", "cabby", "druid", "exact", "truth", "dopey", "spear", "cried", "chime", "crony", "stunk", "timid", "batch", "gauge", "rotor", "crack", "curve", "latte", "witch", "bunch", "repel", "anvil", "soapy", "meter", "broth", "madly", "dried", "scene", "known", "magma", "roost", "woman", "thong", "punch", "pasty", "downy", "knead", "whirl", "rapid", "clang", "anger", "drive", "goofy", "email", "music", "stuff", "bleep", "rider", "mecca", "folio", "setup", "verso", "quash", "fauna", "gummy", "happy", "newly", "fussy", "relic", "guava", "ratty", "fudge", "femur", "chirp", "forte", "alibi", "whine", "petty", "golly", "plait", "fleck", "felon", "gourd", "brown", "thrum", "ficus", "stash", "decry", "wiser", "junta", "visor", "daunt", "scree", "impel", "await", "press", "whose", "turbo", "stoop", "speak", "mangy", "eying", "inlet", "crone", "pulse", "mossy", "staid", "hence", "pinch", "teddy", "sully", "snore", "ripen", "snowy", "attic", "going", "leach", "mouth", "hound", "clump", "tonal", "bigot", "peril", "piece", "blame", "haute", "spied", "undid", "intro", "basal", "shine", "gecko", "rodeo", "guard", "steer", "loamy", "scamp", "scram", "manly", "hello", "vaunt", "organ", "feral", "knock", "extra", "condo", "adapt", "willy", "polka", "rayon", "skirt", "faith", "torso", "match", "mercy", "tepid", "sleek", "riser", "twixt", "peace", "flush", "catty", "login", "eject", "roger", "rival", "untie", "refit", "aorta", "adult", "judge", "rower", "artsy", "rural", "shave"]

# var guessList = ["aahed", "aalii", "aargh", "aarti", "abaca", "abaci", "abacs", "abaft", "abaka", "abamp", "aband", "abash", "abask", "abaya", "abbas", "abbed", "abbes", "abcee", "abeam", "abear", "abele", "abers", "abets", "abies", "abler", "ables", "ablet", "ablow", "abmho", "abohm", "aboil", "aboma", "aboon", "abord", "abore", "abram", "abray", "abrim", "abrin", "abris", "absey", "absit", "abuna", "abune", "abuts", "abuzz", "abyes", "abysm", "acais", "acari", "accas", "accoy", "acerb", "acers", "aceta", "achar", "ached", "aches", "achoo", "acids", "acidy", "acing", "acini", "ackee", "acker", "acmes", "acmic", "acned", "acnes", "acock", "acold", "acred", "acres", "acros", "acted", "actin", "acton", "acyls", "adaws", "adays", "adbot", "addax", "added", "adder", "addio", "addle", "adeem", "adhan", "adieu", "adios", "adits", "adman", "admen", "admix", "adobo", "adown", "adoze", "adrad", "adred", "adsum", "aduki", "adunc", "adust", "advew", "adyta", "adzed", "adzes", "aecia", "aedes", "aegis", "aeons", "aerie", "aeros", "aesir", "afald", "afara", "afars", "afear", "aflaj", "afore", "afrit", "afros", "agama", "agami", "agars", "agast", "agave", "agaze", "agene", "agers", "agger", "aggie", "aggri", "aggro", "aggry", "aghas", "agila", "agios", "agism", "agist", "agita", "aglee", "aglet", "agley", "agloo", "aglus", "agmas", "agoge", "agone", "agons", "agood", "agria", "agrin", "agros", "agued", "agues", "aguna", "aguti", "aheap", "ahent", "ahigh", "ahind", "ahing", "ahint", "ahold", "ahull", "ahuru", "aidas", "aided", "aides", "aidoi", "aidos", "aiery", "aigas", "aight", "ailed", "aimed", "aimer", "ainee", "ainga", "aioli", "aired", "airer", "airns", "airth", "airts", "aitch", "aitus", "aiver", "aiyee", "aizle", "ajies", "ajiva", "ajuga", "ajwan", "akees", "akela", "akene", "aking", "akita", "akkas", "alaap", "alack", "alamo", "aland", "alane", "alang", "alans", "alant", "alapa", "alaps", "alary", "alate", "alays", "albas", "albee", "alcid", "alcos", "aldea", "alder", "aldol", "aleck", "alecs", "alefs", "aleft", "aleph", "alews", "aleye", "alfas", "algal", "algas", "algid", "algin", "algor", "algum", "alias", "alifs", "aline", "alist", "aliya", "alkie", "alkos", "alkyd", "alkyl", "allee", "allel", "allis", "allod", "allyl", "almah", "almas", "almeh", "almes", "almud", "almug", "alods", "aloed", "aloes", "aloha", "aloin", "aloos", "alowe", "altho", "altos", "alula", "alums", "alure", "alvar", "alway", "amahs", "amain", "amate", "amaut", "amban", "ambit", "ambos", "ambry", "ameba", "ameer", "amene", "amens", "ament", "amias", "amice", "amici", "amide", "amido", "amids", "amies", "amiga", "amigo", "amine", "amino", "amins", "amirs", "amlas", "amman", "ammon", "ammos", "amnia", "amnic", "amnio", "amoks", "amole", "amort", "amour", "amove", "amowt", "amped", "ampul", "amrit", "amuck", "amyls", "anana", "anata", "ancho", "ancle", "ancon", "andro", "anear", "anele", "anent", "angas", "anglo", "anigh", "anile", "anils", "anima", "animi", "anion", "anise", "anker", "ankhs", "ankus", "anlas", "annal", "annas", "annat", "anoas", "anole", "anomy", "ansae", "antae", "antar", "antas", "anted", "antes", "antis", "antra", "antre", "antsy", "anura", "anyon", "apace", "apage", "apaid", "apayd", "apays", "apeak", "apeek", "apers", "apert", "apery", "apgar", "aphis", "apian", "apiol", "apish", "apism", "apode", "apods", "apoop", "aport", "appal", "appay", "appel", "appro", "appui", "appuy", "apres", "apses", "apsis", "apsos", "apted", "apter", "aquae", "aquas", "araba", "araks", "arame", "arars", "arbas", "arced", "archi", "arcos", "arcus", "ardeb", "ardri", "aread", "areae", "areal", "arear", "areas", "areca", "aredd", "arede", "arefy", "areic", "arene", "arepa", "arere", "arete", "arets", "arett", "argal", "argan", "argil", "argle", "argol", "argon", "argot", "argus", "arhat", "arias", "ariel", "ariki", "arils", "ariot", "arish", "arked", "arled", "arles", "armed", "armer", "armet", "armil", "arnas", "arnut", "aroba", "aroha", "aroid", "arpas", "arpen", "arrah", "arras", "arret", "arris", "arroz", "arsed", "arses", "arsey", "arsis", "artal", "artel", "artic", "artis", "aruhe", "arums", "arval", "arvee", "arvos", "aryls", "asana", "ascon", "ascus", "asdic", "ashed", "ashes", "ashet", "asked", "asker", "askoi", "askos", "aspen", "asper", "aspic", "aspie", "aspis", "aspro", "assai", "assam", "asses", "assez", "assot", "aster", "astir", "astun", "asura", "asway", "aswim", "asyla", "ataps", "ataxy", "atigi", "atilt", "atimy", "atlas", "atman", "atmas", "atmos", "atocs", "atoke", "atoks", "atoms", "atomy", "atony", "atopy", "atria", "atrip", "attap", "attar", "atuas", "audad", "auger", "aught", "aulas", "aulic", "auloi", "aulos", "aumil", "aunes", "aunts", "aurae", "aural", "aurar", "auras", "aurei", "aures", "auric", "auris", "aurum", "autos", "auxin", "avale", "avant", "avast", "avels", "avens", "avers", "avgas", "avine", "avion", "avise", "aviso", "avize", "avows", "avyze", "awarn", "awato", "awave", "aways", "awdls", "aweel", "aweto", "awing", "awmry", "awned", "awner", "awols", "awork", "axels", "axile", "axils", "axing", "axite", "axled", "axles", "axman", "axmen", "axoid", "axone", "axons", "ayahs", "ayaya", "ayelp", "aygre", "ayins", "ayont", "ayres", "ayrie", "azans", "azide", "azido", "azine", "azlon", "azoic", "azole", "azons", "azote", "azoth", "azuki", "azurn", "azury", "azygy", "azyme", "azyms", "baaed", "baals", "babas", "babel", "babes", "babka", "baboo", "babul", "babus", "bacca", "bacco", "baccy", "bacha", "bachs", "backs", "baddy", "baels", "baffs", "baffy", "bafts", "baghs", "bagie", "bahts", "bahus", "bahut", "bails", "bairn", "baisa", "baith", "baits", "baiza", "baize", "bajan", "bajra", "bajri", "bajus", "baked", "baken", "bakes", "bakra", "balas", "balds", "baldy", "baled", "bales", "balks", "balky", "balls", "bally", "balms", "baloo", "balsa", "balti", "balun", "balus", "bambi", "banak", "banco", "bancs", "banda", "bandh", "bands", "bandy", "baned", "banes", "bangs", "bania", "banks", "banns", "bants", "bantu", "banty", "banya", "bapus", "barbe", "barbs", "barby", "barca", "barde", "bardo", "bards", "bardy", "bared", "barer", "bares", "barfi", "barfs", "baric", "barks", "barky", "barms", "barmy", "barns", "barny", "barps", "barra", "barre", "barro", "barry", "barye", "basan", "based", "basen", "baser", "bases", "basho", "basij", "basks", "bason", "basse", "bassi", "basso", "bassy", "basta", "basti", "basto", "basts", "bated", "bates", "baths", "batik", "batta", "batts", "battu", "bauds", "bauks", "baulk", "baurs", "bavin", "bawds", "bawks", "bawls", "bawns", "bawrs", "bawty", "bayed", "bayer", "bayes", "bayle", "bayts", "bazar", "bazoo", "beads", "beaks", "beaky", "beals", "beams", "beamy", "beano", "beans", "beany", "beare", "bears", "beath", "beats", "beaty", "beaus", "beaut", "beaux", "bebop", "becap", "becke", "becks", "bedad", "bedel", "bedes", "bedew", "bedim", "bedye", "beedi", "beefs", "beeps", "beers", "beery", "beets", "befog", "begad", "begar", "begem", "begot", "begum", "beige", "beigy", "beins", "bekah", "belah", "belar", "belay", "belee", "belga", "bells", "belon", "belts", "bemad", "bemas", "bemix", "bemud", "bends", "bendy", "benes", "benet", "benga", "benis", "benne", "benni", "benny", "bento", "bents", "benty", "bepat", "beray", "beres", "bergs", "berko", "berks", "berme", "berms", "berob", "beryl", "besat", "besaw", "besee", "beses", "besit", "besom", "besot", "besti", "bests", "betas", "beted", "betes", "beths", "betid", "beton", "betta", "betty", "bever", "bevor", "bevue", "bevvy", "bewet", "bewig", "bezes", "bezil", "bezzy", "bhais", "bhaji", "bhang", "bhats", "bhels", "bhoot", "bhuna", "bhuts", "biach", "biali", "bialy", "bibbs", "bibes", "biccy", "bices", "bided", "bider", "bides", "bidet", "bidis", "bidon", "bield", "biers", "biffo", "biffs", "biffy", "bifid", "bigae", "biggs", "biggy", "bigha", "bight", "bigly", "bigos", "bijou", "biked", "biker", "bikes", "bikie", "bilbo", "bilby", "biled", "biles", "bilgy", "bilks", "bills", "bimah", "bimas", "bimbo", "binal", "bindi", "binds", "biner", "bines", "bings", "bingy", "binit", "binks", "bints", "biogs", "biont", "biota", "biped", "bipod", "birds", "birks", "birle", "birls", "biros", "birrs", "birse", "birsy", "bises", "bisks", "bisom", "biter", "bites", "bitos", "bitou", "bitsy", "bitte", "bitts", "bivia", "bivvy", "bizes", "bizzo", "bizzy", "blabs", "blads", "blady", "blaer", "blaes", "blaff", "blags", "blahs", "blain", "blams", "blart", "blase", "blash", "blate", "blats", "blatt", "blaud", "blawn", "blaws", "blays", "blear", "blebs", "blech", "blees", "blent", "blert", "blest", "blets", "bleys", "blimy", "bling", "blini", "blins", "bliny", "blips", "blist", "blite", "blits", "blive", "blobs", "blocs", "blogs", "blook", "bloop", "blore", "blots", "blows", "blowy", "blubs", "blude", "bluds", "bludy", "blued", "blues", "bluet", "bluey", "bluid", "blume", "blunk", "blurs", "blype", "boabs", "boaks", "boars", "boart", "boats", "bobac", "bobak", "bobas", "bobol", "bobos", "bocca", "bocce", "bocci", "boche", "bocks", "boded", "bodes", "bodge", "bodhi", "bodle", "boeps", "boets", "boeuf", "boffo", "boffs", "bogan", "bogey", "boggy", "bogie", "bogle", "bogue", "bogus", "bohea", "bohos", "boils", "boing", "boink", "boite", "boked", "bokeh", "bokes", "bokos", "bolar", "bolas", "bolds", "boles", "bolix", "bolls", "bolos", "bolts", "bolus", "bomas", "bombe", "bombo", "bombs", "bonce", "bonds", "boned", "boner", "bones", "bongs", "bonie", "bonks", "bonne", "bonny", "bonza", "bonze", "booai", "booay", "boobs", "boody", "booed", "boofy", "boogy", "boohs", "books", "booky", "bools", "booms", "boomy", "boong", "boons", "boord", "boors", "boose", "boots", "boppy", "borak", "boral", "boras", "borde", "bords", "bored", "boree", "borel", "borer", "bores", "borgo", "boric", "borks", "borms", "borna", "boron", "borts", "borty", "bortz", "bosie", "bosks", "bosky", "boson", "bosun", "botas", "botel", "botes", "bothy", "botte", "botts", "botty", "bouge", "bouks", "boult", "bouns", "bourd", "bourg", "bourn", "bouse", "bousy", "bouts", "bovid", "bowat", "bowed", "bower", "bowes", "bowet", "bowie", "bowls", "bowne", "bowrs", "bowse", "boxed", "boxen", "boxes", "boxla", "boxty", "boyar", "boyau", "boyed", "boyfs", "boygs", "boyla", "boyos", "boysy", "bozos", "braai", "brach", "brack", "bract", "brads", "braes", "brags", "brail", "braks", "braky", "brame", "brane", "brank", "brans", "brant", "brast", "brats", "brava", "bravi", "braws", "braxy", "brays", "braza", "braze", "bream", "brede", "breds", "breem", "breer", "brees", "breid", "breis", "breme", "brens", "brent", "brere", "brers", "breve", "brews", "breys", "brier", "bries", "brigs", "briki", "briks", "brill", "brims", "brins", "brios", "brise", "briss", "brith", "brits", "britt", "brize", "broch", "brock", "brods", "brogh", "brogs", "brome", "bromo", "bronc", "brond", "brool", "broos", "brose", "brosy", "brows", "brugh", "bruin", "bruit", "brule", "brume", "brung", "brusk", "brust", "bruts", "buats", "buaze", "bubal", "bubas", "bubba", "bubbe", "bubby", "bubus", "buchu", "bucko", "bucks", "bucku", "budas", "budis", "budos", "buffa", "buffe", "buffi", "buffo", "buffs", "buffy", "bufos", "bufty", "buhls", "buhrs", "buiks", "buist", "bukes", "bulbs", "bulgy", "bulks", "bulla", "bulls", "bulse", "bumbo", "bumfs", "bumph", "bumps", "bumpy", "bunas", "bunce", "bunco", "bunde", "bundh", "bunds", "bundt", "bundu", "bundy", "bungs", "bungy", "bunia", "bunje", "bunjy", "bunko", "bunks", "bunns", "bunts", "bunty", "bunya", "buoys", "buppy", "buran", "buras", "burbs", "burds", "buret", "burfi", "burgh", "burgs", "burin", "burka", "burke", "burks", "burls", "burns", "buroo", "burps", "burqa", "burro", "burrs", "burry", "bursa", "burse", "busby", "buses", "busks", "busky", "bussu", "busti", "busts", "busty", "buteo", "butes", "butle", "butoh", "butts", "butty", "butut", "butyl", "buzzy", "bwana", "bwazi", "byded", "bydes", "byked", "bykes", "byres", "byrls", "byssi", "bytes", "byway", "caaed", "cabas", "caber", "cabob", "caboc", "cabre", "cacas", "cacks", "cacky", "cadee", "cades", "cadge", "cadgy", "cadie", "cadis", "cadre", "caeca", "caese", "cafes", "caffs", "caged", "cager", "cages", "cagot", "cahow", "caids", "cains", "caird", "cajon", "cajun", "caked", "cakes", "cakey", "calfs", "calid", "calif", "calix", "calks", "calla", "calls", "calms", "calmy", "calos", "calpa", "calps", "calve", "calyx", "caman", "camas", "cames", "camis", "camos", "campi", "campo", "camps", "campy", "camus", "caned", "caneh", "caner", "canes", "cangs", "canid", "canna", "canns", "canso", "canst", "canto", "cants", "canty", "capas", "caped", "capes", "capex", "caphs", "capiz", "caple", "capon", "capos", "capot", "capri", "capul", "carap", "carbo", "carbs", "carby", "cardi", "cards", "cardy", "cared", "carer", "cares", "caret", "carex", "carks", "carle", "carls", "carns", "carny", "carob", "carom", "caron", "carpi", "carps", "carrs", "carse", "carta", "carte", "carts", "carvy", "casas", "casco", "cased", "cases", "casks", "casky", "casts", "casus", "cates", "cauda", "cauks", "cauld", "cauls", "caums", "caups", "cauri", "causa", "cavas", "caved", "cavel", "caver", "caves", "cavie", "cawed", "cawks", "caxon", "ceaze", "cebid", "cecal", "cecum", "ceded", "ceder", "cedes", "cedis", "ceiba", "ceili", "ceils", "celeb", "cella", "celli", "cells", "celom", "celts", "cense", "cento", "cents", "centu", "ceorl", "cepes", "cerci", "cered", "ceres", "cerge", "ceria", "ceric", "cerne", "ceroc", "ceros", "certs", "certy", "cesse", "cesta", "cesti", "cetes", "cetyl", "cezve", "chace", "chack", "chaco", "chado", "chads", "chaft", "chais", "chals", "chams", "chana", "chang", "chank", "chape", "chaps", "chapt", "chara", "chare", "chark", "charr", "chars", "chary", "chats", "chave", "chavs", "chawk", "chaws", "chaya", "chays", "cheep", "chefs", "cheka", "chela", "chelp", "chemo", "chems", "chere", "chert", "cheth", "chevy", "chews", "chewy", "chiao", "chias", "chibs", "chica", "chich", "chico", "chics", "chiel", "chiks", "chile", "chimb", "chimo", "chimp", "chine", "ching", "chino", "chins", "chips", "chirk", "chirl", "chirm", "chiro", "chirr", "chirt", "chiru", "chits", "chive", "chivs", "chivy", "chizz", "choco", "chocs", "chode", "chogs", "choil", "choko", "choky", "chola", "choli", "cholo", "chomp", "chons", "choof", "chook", "choom", "choon", "chops", "chota", "chott", "chout", "choux", "chowk", "chows", "chubs", "chufa", "chuff", "chugs", "chums", "churl", "churr", "chuse", "chuts", "chyle", "chyme", "chynd", "cibol", "cided", "cides", "ciels", "ciggy", "cilia", "cills", "cimar", "cimex", "cinct", "cines", "cinqs", "cions", "cippi", "circs", "cires", "cirls", "cirri", "cisco", "cissy", "cists", "cital", "cited", "citer", "cites", "cives", "civet", "civie", "civvy", "clach", "clade", "clads", "claes", "clags", "clame", "clams", "clans", "claps", "clapt", "claro", "clart", "clary", "clast", "clats", "claut", "clave", "clavi", "claws", "clays", "cleck", "cleek", "cleep", "clefs", "clegs", "cleik", "clems", "clepe", "clept", "cleve", "clews", "clied", "clies", "clift", "clime", "cline", "clint", "clipe", "clips", "clipt", "clits", "cloam", "clods", "cloff", "clogs", "cloke", "clomb", "clomp", "clonk", "clons", "cloop", "cloot", "clops", "clote", "clots", "clour", "clous", "clows", "cloye", "cloys", "cloze", "clubs", "clues", "cluey", "clunk", "clype", "cnida", "coact", "coady", "coala", "coals", "coaly", "coapt", "coarb", "coate", "coati", "coats", "cobbs", "cobby", "cobia", "coble", "cobza", "cocas", "cocci", "cocco", "cocks", "cocky", "cocos", "codas", "codec", "coded", "coden", "coder", "codes", "codex", "codon", "coeds", "coffs", "cogie", "cogon", "cogue", "cohab", "cohen", "cohoe", "cohog", "cohos", "coifs", "coign", "coils", "coins", "coirs", "coits", "coked", "cokes", "colas", "colby", "colds", "coled", "coles", "coley", "colic", "colin", "colls", "colly", "colog", "colts", "colza", "comae", "comal", "comas", "combe", "combi", "combo", "combs", "comby", "comer", "comes", "comix", "commo", "comms", "commy", "compo", "comps", "compt", "comte", "comus", "coned", "cones", "coney", "confs", "conga", "conge", "congo", "conia", "conin", "conks", "conky", "conne", "conns", "conte", "conto", "conus", "convo", "cooch", "cooed", "cooee", "cooer", "cooey", "coofs", "cooks", "cooky", "cools", "cooly", "coomb", "cooms", "coomy", "coops", "coopt", "coost", "coots", "cooze", "copal", "copay", "coped", "copen", "coper", "copes", "coppy", "copra", "copsy", "coqui", "coram", "corbe", "corby", "cords", "cored", "cores", "corey", "corgi", "coria", "corks", "corky", "corms", "corni", "corno", "corns", "cornu", "corps", "corse", "corso", "cosec", "cosed", "coses", "coset", "cosey", "cosie", "costa", "coste", "costs", "cotan", "coted", "cotes", "coths", "cotta", "cotts", "coude", "coups", "courb", "courd", "coure", "cours", "couta", "couth", "coved", "coves", "covin", "cowal", "cowan", "cowed", "cowks", "cowls", "cowps", "cowry", "coxae", "coxal", "coxed", "coxes", "coxib", "coyau", "coyed", "coyer", "coypu", "cozed", "cozen", "cozes", "cozey", "cozie", "craal", "crabs", "crags", "craic", "craig", "crake", "crame", "crams", "crans", "crape", "craps", "crapy", "crare", "craws", "crays", "creds", "creel", "crees", "crems", "crena", "creps", "crepy", "crewe", "crews", "crias", "cribs", "cries", "crims", "crine", "crios", "cripe", "crips", "crise", "crith", "crits", "croci", "crocs", "croft", "crogs", "cromb", "crome", "cronk", "crons", "crool", "croon", "crops", "crore", "crost", "crout", "crows", "croze", "cruck", "crudo", "cruds", "crudy", "crues", "cruet", "cruft", "crunk", "cruor", "crura", "cruse", "crusy", "cruve", "crwth", "cryer", "ctene", "cubby", "cubeb", "cubed", "cuber", "cubes", "cubit", "cuddy", "cuffo", "cuffs", "cuifs", "cuing", "cuish", "cuits", "cukes", "culch", "culet", "culex", "culls", "cully", "culms", "culpa", "culti", "cults", "culty", "cumec", "cundy", "cunei", "cunit", "cunts", "cupel", "cupid", "cuppa", "cuppy", "curat", "curbs", "curch", "curds", "curdy", "cured", "curer", "cures", "curet", "curfs", "curia", "curie", "curli", "curls", "curns", "curny", "currs", "cursi", "curst", "cusec", "cushy", "cusks", "cusps", "cuspy", "cusso", "cusum", "cutch", "cuter", "cutes", "cutey", "cutin", "cutis", "cutto", "cutty", "cutup", "cuvee", "cuzes", "cwtch", "cyano", "cyans", "cycad", "cycas", "cyclo", "cyder", "cylix", "cymae", "cymar", "cymas", "cymes", "cymol", "cysts", "cytes", "cyton", "czars", "daals", "dabba", "daces", "dacha", "dacks", "dadah", "dadas", "dados", "daffs", "daffy", "dagga", "daggy", "dagos", "dahls", "daiko", "daine", "daint", "daker", "daled", "dales", "dalis", "dalle", "dalts", "daman", "damar", "dames", "damme", "damns", "damps", "dampy", "dancy", "dangs", "danio", "danks", "danny", "dants", "daraf", "darbs", "darcy", "dared", "darer", "dares", "darga", "dargs", "daric", "daris", "darks", "darns", "darre", "darts", "darzi", "dashi", "dashy", "datal", "dated", "dater", "dates", "datos", "datto", "daube", "daubs", "dauby", "dauds", "dault", "daurs", "dauts", "daven", "davit", "dawah", "dawds", "dawed", "dawen", "dawks", "dawns", "dawts", "dayan", "daych", "daynt", "dazed", "dazer", "dazes", "deads", "deair", "deals", "deans", "deare", "dearn", "dears", "deary", "deash", "deave", "deaws", "deawy", "debag", "debby", "debel", "debes", "debts", "debud", "debur", "debus", "debye", "decad", "decaf", "decan", "decko", "decks", "decos", "dedal", "deeds", "deedy", "deely", "deems", "deens", "deeps", "deere", "deers", "deets", "deeve", "deevs", "defat", "deffo", "defis", "defog", "degas", "degum", "degus", "deice", "deids", "deify", "deils", "deism", "deist", "deked", "dekes", "dekko", "deled", "deles", "delfs", "delft", "delis", "dells", "delly", "delos", "delph", "delts", "deman", "demes", "demic", "demit", "demob", "demoi", "demos", "dempt", "denar", "denay", "dench", "denes", "denet", "denis", "dents", "deoxy", "derat", "deray", "dered", "deres", "derig", "derma", "derms", "derns", "derny", "deros", "derro", "derry", "derth", "dervs", "desex", "deshi", "desis", "desks", "desse", "devas", "devel", "devis", "devon", "devos", "devot", "dewan", "dewar", "dewax", "dewed", "dexes", "dexie", "dhaba", "dhaks", "dhals", "dhikr", "dhobi", "dhole", "dholl", "dhols", "dhoti", "dhows", "dhuti", "diact", "dials", "diane", "diazo", "dibbs", "diced", "dicer", "dices", "dicht", "dicks", "dicky", "dicot", "dicta", "dicts", "dicty", "diddy", "didie", "didos", "didst", "diebs", "diels", "diene", "diets", "diffs", "dight", "dikas", "diked", "diker", "dikes", "dikey", "dildo", "dilli", "dills", "dimbo", "dimer", "dimes", "dimps", "dinar", "dined", "dines", "dinge", "dings", "dinic", "dinks", "dinky", "dinna", "dinos", "dints", "diols", "diota", "dippy", "dipso", "diram", "direr", "dirke", "dirks", "dirls", "dirts", "disas", "disci", "discs", "dishy", "disks", "disme", "dital", "ditas", "dited", "dites", "ditsy", "ditts", "ditzy", "divan", "divas", "dived", "dives", "divis", "divna", "divos", "divot", "divvy", "diwan", "dixie", "dixit", "diyas", "dizen", "djinn", "djins", "doabs", "doats", "dobby", "dobes", "dobie", "dobla", "dobra", "dobro", "docht", "docks", "docos", "docus", "doddy", "dodos", "doeks", "doers", "doest", "doeth", "doffs", "dogan", "doges", "dogey", "doggo", "doggy", "dogie", "dohyo", "doilt", "doily", "doits", "dojos", "dolce", "dolci", "doled", "doles", "dolia", "dolls", "dolma", "dolor", "dolos", "dolts", "domal", "domed", "domes", "domic", "donah", "donas", "donee", "doner", "donga", "dongs", "donko", "donna", "donne", "donny", "donsy", "doobs", "dooce", "doody", "dooks", "doole", "dools", "dooly", "dooms", "doomy", "doona", "doorn", "doors", "doozy", "dopas", "doped", "doper", "dopes", "dorad", "dorba", "dorbs", "doree", "dores", "doric", "doris", "dorks", "dorky", "dorms", "dormy", "dorps", "dorrs", "dorsa", "dorse", "dorts", "dorty", "dosai", "dosas", "dosed", "doseh", "doser", "doses", "dosha", "dotal", "doted", "doter", "dotes", "dotty", "douar", "douce", "doucs", "douks", "doula", "douma", "doums", "doups", "doura", "douse", "douts", "doved", "doven", "dover", "doves", "dovie", "dowar", "dowds", "dowed", "dower", "dowie", "dowle", "dowls", "dowly", "downa", "downs", "dowps", "dowse", "dowts", "doxed", "doxes", "doxie", "doyen", "doyly", "dozed", "dozer", "dozes", "drabs", "drack", "draco", "draff", "drags", "drail", "drams", "drant", "draps", "drats", "drave", "draws", "drays", "drear", "dreck", "dreed", "dreer", "drees", "dregs", "dreks", "drent", "drere", "drest", "dreys", "dribs", "drice", "dries", "drily", "drips", "dript", "droid", "droil", "droke", "drole", "drome", "drony", "droob", "droog", "drook", "drops", "dropt", "drouk", "drows", "drubs", "drugs", "drums", "drupe", "druse", "drusy", "druxy", "dryad", "dryas", "dsobo", "dsomo", "duads", "duals", "duans", "duars", "dubbo", "ducal", "ducat", "duces", "ducks", "ducky", "ducts", "duddy", "duded", "dudes", "duels", "duets", "duett", "duffs", "dufus", "duing", "duits", "dukas", "duked", "dukes", "dukka", "dulce", "dules", "dulia", "dulls", "dulse", "dumas", "dumbo", "dumbs", "dumka", "dumky", "dumps", "dunam", "dunch", "dunes", "dungs", "dungy", "dunks", "dunno", "dunny", "dunsh", "dunts", "duomi", "duomo", "duped", "duper", "dupes", "duple", "duply", "duppy", "dural", "duras", "dured", "dures", "durgy", "durns", "duroc", "duros", "duroy", "durra", "durrs", "durry", "durst", "durum", "durzi", "dusks", "dusts", "duxes", "dwaal", "dwale", "dwalm", "dwams", "dwang", "dwaum", "dweeb", "dwile", "dwine", "dyads", "dyers", "dykon", "dynel", "dynes", "dzhos", "eagre", "ealed", "eales", "eaned", "eards", "eared", "earls", "earns", "earnt", "earst", "eased", "easer", "eases", "easle", "easts", "eathe", "eaved", "eaves", "ebbed", "ebbet", "ebons", "ebook", "ecads", "eched", "eches", "echos", "ecrus", "edema", "edged", "edger", "edges", "edile", "edits", "educe", "educt", "eejit", "eensy", "eeven", "eevns", "effed", "egads", "egers", "egest", "eggar", "egged", "egger", "egmas", "ehing", "eider", "eidos", "eigne", "eiked", "eikon", "eilds", "eisel", "ejido", "ekkas", "elain", "eland", "elans", "elchi", "eldin", "elemi", "elfed", "eliad", "elint", "elmen", "eloge", "elogy", "eloin", "elops", "elpee", "elsin", "elute", "elvan", "elven", "elver", "elves", "emacs", "embar", "embay", "embog", "embow", "embox", "embus", "emeer", "emend", "emerg", "emery", "emeus", "emics", "emirs", "emits", "emmas", "emmer", "emmet", "emmew", "emmys", "emoji", "emong", "emote", "emove", "empts", "emule", "emure", "emyde", "emyds", "enarm", "enate", "ended", "ender", "endew", "endue", "enews", "enfix", "eniac", "enlit", "enmew", "ennog", "enoki", "enols", "enorm", "enows", "enrol", "ensew", "ensky", "entia", "enure", "enurn", "envoi", "enzym", "eorls", "eosin", "epact", "epees", "ephah", "ephas", "ephod", "ephor", "epics", "epode", "epopt", "epris", "eques", "equid", "erbia", "erevs", "ergon", "ergos", "ergot", "erhus", "erica", "erick", "erics", "ering", "erned", "ernes", "erose", "erred", "erses", "eruct", "erugo", "eruvs", "erven", "ervil", "escar", "escot", "esile", "eskar", "esker", "esnes", "esses", "estoc", "estop", "estro", "etage", "etape", "etats", "etens", "ethal", "ethne", "ethyl", "etics", "etnas", "ettin", "ettle", "etuis", "etwee", "etyma", "eughs", "euked", "eupad", "euros", "eusol", "evens", "evert", "evets", "evhoe", "evils", "evite", "evohe", "ewers", "ewest", "ewhow", "ewked", "exams", "exeat", "execs", "exeem", "exeme", "exfil", "exies", "exine", "exing", "exits", "exode", "exome", "exons", "expat", "expos", "exude", "exuls", "exurb", "eyass", "eyers", "eyots", "eyras", "eyres", "eyrie", "eyrir", "ezine", "fabby", "faced", "facer", "faces", "facia", "facta", "facts", "faddy", "faded", "fader", "fades", "fadge", "fados", "faena", "faery", "faffs", "faffy", "fagin", "faiks", "fails", "faine", "fains", "fairs", "faked", "faker", "fakes", "fakey", "fakie", "fakir", "falaj", "falls", "famed", "fames", "fanal", "fands", "fanes", "fanga", "fango", "fangs", "fanks", "fanon", "fanos", "fanum", "faqir", "farad", "farci", "farcy", "fards", "fared", "farer", "fares", "farle", "farls", "farms", "faros", "farro", "farse", "farts", "fasci", "fasti", "fasts", "fated", "fates", "fatly", "fatso", "fatwa", "faugh", "fauld", "fauns", "faurd", "fauts", "fauve", "favas", "favel", "faver", "faves", "favus", "fawns", "fawny", "faxed", "faxes", "fayed", "fayer", "fayne", "fayre", "fazed", "fazes", "feals", "feare", "fears", "feart", "fease", "feats", "feaze", "feces", "fecht", "fecit", "fecks", "fedex", "feebs", "feeds", "feels", "feens", "feers", "feese", "feeze", "fehme", "feint", "feist", "felch", "felid", "fells", "felly", "felts", "felty", "femal", "femes", "femmy", "fends", "fendy", "fenis", "fenks", "fenny", "fents", "feods", "feoff", "ferer", "feres", "feria", "ferly", "fermi", "ferms", "ferns", "ferny", "fesse", "festa", "fests", "festy", "fetas", "feted", "fetes", "fetor", "fetta", "fetts", "fetwa", "feuar", "feuds", "feued", "feyed", "feyer", "feyly", "fezes", "fezzy", "fiars", "fiats", "fibro", "fices", "fiche", "fichu", "ficin", "ficos", "fides", "fidge", "fidos", "fiefs", "fient", "fiere", "fiers", "fiest", "fifed", "fifer", "fifes", "fifis", "figgy", "figos", "fiked", "fikes", "filar", "filch", "filed", "files", "filii", "filks", "fille", "fillo", "fills", "filmi", "films", "filos", "filum", "finca", "finds", "fined", "fines", "finis", "finks", "finny", "finos", "fiord", "fiqhs", "fique", "fired", "firer", "fires", "firie", "firks", "firms", "firns", "firry", "firth", "fiscs", "fisks", "fists", "fisty", "fitch", "fitly", "fitna", "fitte", "fitts", "fiver", "fives", "fixed", "fixes", "fixit", "fjeld", "flabs", "flaff", "flags", "flaks", "flamm", "flams", "flamy", "flane", "flans", "flaps", "flary", "flats", "flava", "flawn", "flaws", "flawy", "flaxy", "flays", "fleam", "fleas", "fleek", "fleer", "flees", "flegs", "fleme", "fleur", "flews", "flexi", "flexo", "fleys", "flics", "flied", "flies", "flimp", "flims", "flips", "flirs", "flisk", "flite", "flits", "flitt", "flobs", "flocs", "floes", "flogs", "flong", "flops", "flors", "flory", "flosh", "flota", "flote", "flows", "flubs", "flued", "flues", "fluey", "fluky", "flump", "fluor", "flurr", "fluty", "fluyt", "flyby", "flype", "flyte", "foals", "foams", "foehn", "fogey", "fogie", "fogle", "fogou", "fohns", "foids", "foils", "foins", "folds", "foley", "folia", "folic", "folie", "folks", "folky", "fomes", "fonda", "fonds", "fondu", "fones", "fonly", "fonts", "foods", "foody", "fools", "foots", "footy", "foram", "forbs", "forby", "fordo", "fords", "forel", "fores", "forex", "forks", "forky", "forme", "forms", "forts", "forza", "forze", "fossa", "fosse", "fouat", "fouds", "fouer", "fouet", "foule", "fouls", "fount", "fours", "fouth", "fovea", "fowls", "fowth", "foxed", "foxes", "foxie", "foyle", "foyne", "frabs", "frack", "fract", "frags", "fraim", "franc", "frape", "fraps", "frass", "frate", "frati", "frats", "fraus", "frays", "frees", "freet", "freit", "fremd", "frena", "freon", "frere", "frets", "fribs", "frier", "fries", "frigs", "frise", "frist", "frith", "frits", "fritt", "frize", "frizz", "froes", "frogs", "frons", "frore", "frorn", "frory", "frosh", "frows", "frowy", "frugs", "frump", "frush", "frust", "fryer", "fubar", "fubby", "fubsy", "fucks", "fucus", "fuddy", "fudgy", "fuels", "fuero", "fuffs", "fuffy", "fugal", "fuggy", "fugie", "fugio", "fugle", "fugly", "fugus", "fujis", "fulls", "fumed", "fumer", "fumes", "fumet", "fundi", "funds", "fundy", "fungo", "fungs", "funks", "fural", "furan", "furca", "furls", "furol", "furrs", "furth", "furze", "furzy", "fused", "fusee", "fusel", "fuses", "fusil", "fusks", "fusts", "fusty", "futon", "fuzed", "fuzee", "fuzes", "fuzil", "fyces", "fyked", "fykes", "fyles", "fyrds", "fytte", "gabba", "gabby", "gable", "gaddi", "gades", "gadge", "gadid", "gadis", "gadje", "gadjo", "gadso", "gaffs", "gaged", "gager", "gages", "gaids", "gains", "gairs", "gaita", "gaits", "gaitt", "gajos", "galah", "galas", "galax", "galea", "galed", "gales", "galls", "gally", "galop", "galut", "galvo", "gamas", "gamay", "gamba", "gambe", "gambo", "gambs", "gamed", "games", "gamey", "gamic", "gamin", "gamme", "gammy", "gamps", "ganch", "gandy", "ganef", "ganev", "gangs", "ganja", "ganof", "gants", "gaols", "gaped", "gaper", "gapes", "gapos", "gappy", "garbe", "garbo", "garbs", "garda", "gares", "garis", "garms", "garni", "garre", "garth", "garum", "gases", "gasps", "gaspy", "gasts", "gatch", "gated", "gater", "gates", "gaths", "gator", "gauch", "gaucy", "gauds", "gauje", "gault", "gaums", "gaumy", "gaups", "gaurs", "gauss", "gauzy", "gavot", "gawcy", "gawds", "gawks", "gawps", "gawsy", "gayal", "gazal", "gazar", "gazed", "gazes", "gazon", "gazoo", "geals", "geans", "geare", "gears", "geats", "gebur", "gecks", "geeks", "geeps", "geest", "geist", "geits", "gelds", "gelee", "gelid", "gelly", "gelts", "gemel", "gemma", "gemmy", "gemot", "genal", "genas", "genes", "genet", "genic", "genii", "genip", "genny", "genoa", "genom", "genro", "gents", "genty", "genua", "genus", "geode", "geoid", "gerah", "gerbe", "geres", "gerle", "germs", "germy", "gerne", "gesse", "gesso", "geste", "gests", "getas", "getup", "geums", "geyan", "geyer", "ghast", "ghats", "ghaut", "ghazi", "ghees", "ghest", "ghyll", "gibed", "gibel", "giber", "gibes", "gibli", "gibus", "gifts", "gigas", "gighe", "gigot", "gigue", "gilas", "gilds", "gilet", "gills", "gilly", "gilpy", "gilts", "gimel", "gimme", "gimps", "gimpy", "ginch", "ginge", "gings", "ginks", "ginny", "ginzo", "gipon", "gippo", "gippy", "girds", "girls", "girns", "giron", "giros", "girrs", "girsh", "girts", "gismo", "gisms", "gists", "gitch", "gites", "giust", "gived", "gives", "gizmo", "glace", "glads", "glady", "glaik", "glair", "glams", "glans", "glary", "glaum", "glaur", "glazy", "gleba", "glebe", "gleby", "glede", "gleds", "gleed", "gleek", "glees", "gleet", "gleis", "glens", "glent", "gleys", "glial", "glias", "glibs", "gliff", "glift", "glike", "glime", "glims", "glisk", "glits", "glitz", "gloam", "globi", "globs", "globy", "glode", "glogg", "gloms", "gloop", "glops", "glost", "glout", "glows", "gloze", "glued", "gluer", "glues", "gluey", "glugs", "glume", "glums", "gluon", "glute", "gluts", "gnarl", "gnarr", "gnars", "gnats", "gnawn", "gnaws", "gnows", "goads", "goafs", "goals", "goary", "goats", "goaty", "goban", "gobar", "gobbi", "gobbo", "gobby", "gobis", "gobos", "godet", "godso", "goels", "goers", "goest", "goeth", "goety", "gofer", "goffs", "gogga", "gogos", "goier", "gojis", "golds", "goldy", "goles", "golfs", "golpe", "golps", "gombo", "gomer", "gompa", "gonch", "gonef", "gongs", "gonia", "gonif", "gonks", "gonna", "gonof", "gonys", "gonzo", "gooby", "goods", "goofs", "googs", "gooky", "goold", "gools", "gooly", "goons", "goony", "goops", "goopy", "goors", "goory", "goosy", "gopak", "gopik", "goral", "goras", "gored", "gores", "goris", "gorms", "gormy", "gorps", "gorse", "gorsy", "gosht", "gosse", "gotch", "goths", "gothy", "gotta", "gouch", "gouks", "goura", "gouts", "gouty", "gowan", "gowds", "gowfs", "gowks", "gowls", "gowns", "goxes", "goyim", "goyle", "graal", "grabs", "grads", "graff", "graip", "grama", "grame", "gramp", "grams", "grana", "grans", "grapy", "gravs", "grays", "grebe", "grebo", "grece", "greek", "grees", "grege", "grego", "grein", "grens", "grese", "greve", "grews", "greys", "grice", "gride", "grids", "griff", "grift", "grigs", "grike", "grins", "griot", "grips", "gript", "gripy", "grise", "grist", "grisy", "grith", "grits", "grize", "groat", "grody", "grogs", "groks", "groma", "grone", "groof", "grosz", "grots", "grouf", "grovy", "grows", "grrls", "grrrl", "grubs", "grued", "grues", "grufe", "grume", "grump", "grund", "gryce", "gryde", "gryke", "grype", "grypt", "guaco", "guana", "guano", "guans", "guars", "gucks", "gucky", "gudes", "guffs", "gugas", "guids", "guimp", "guiro", "gulag", "gular", "gulas", "gules", "gulet", "gulfs", "gulfy", "gulls", "gulph", "gulps", "gulpy", "gumma", "gummi", "gumps", "gundy", "gunge", "gungy", "gunks", "gunky", "gunny", "guqin", "gurdy", "gurge", "gurls", "gurly", "gurns", "gurry", "gursh", "gurus", "gushy", "gusla", "gusle", "gusli", "gussy", "gusts", "gutsy", "gutta", "gutty", "guyed", "guyle", "guyot", "guyse", "gwine", "gyals", "gyans", "gybed", "gybes", "gyeld", "gymps", "gynae", "gynie", "gynny", "gynos", "gyoza", "gypos", "gyppo", "gyppy", "gyral", "gyred", "gyres", "gyron", "gyros", "gyrus", "gytes", "gyved", "gyves", "haafs", "haars", "hable", "habus", "hacek", "hacks", "hadal", "haded", "hades", "hadji", "hadst", "haems", "haets", "haffs", "hafiz", "hafts", "haggs", "hahas", "haick", "haika", "haiks", "haiku", "hails", "haily", "hains", "haint", "hairs", "haith", "hajes", "hajis", "hajji", "hakam", "hakas", "hakea", "hakes", "hakim", "hakus", "halal", "haled", "haler", "hales", "halfa", "halfs", "halid", "hallo", "halls", "halma", "halms", "halon", "halos", "halse", "halts", "halva", "halwa", "hamal", "hamba", "hamed", "hames", "hammy", "hamza", "hanap", "hance", "hanch", "hands", "hangi", "hangs", "hanks", "hanky", "hansa", "hanse", "hants", "haole", "haoma", "hapax", "haply", "happi", "hapus", "haram", "hards", "hared", "hares", "harim", "harks", "harls", "harms", "harns", "haros", "harps", "harts", "hashy", "hasks", "hasps", "hasta", "hated", "hates", "hatha", "hauds", "haufs", "haugh", "hauld", "haulm", "hauls", "hault", "hauns", "hause", "haver", "haves", "hawed", "hawks", "hawms", "hawse", "hayed", "hayer", "hayey", "hayle", "hazan", "hazed", "hazer", "hazes", "heads", "heald", "heals", "heame", "heaps", "heapy", "heare", "hears", "heast", "heats", "heben", "hebes", "hecht", "hecks", "heder", "hedgy", "heeds", "heedy", "heels", "heeze", "hefte", "hefts", "heids", "heigh", "heils", "heirs", "hejab", "hejra", "heled", "heles", "helio", "hells", "helms", "helos", "helot", "helps", "helve", "hemal", "hemes", "hemic", "hemin", "hemps", "hempy", "hench", "hends", "henge", "henna", "henny", "henry", "hents", "hepar", "herbs", "herby", "herds", "heres", "herls", "herma", "herms", "herns", "heros", "herry", "herse", "hertz", "herye", "hesps", "hests", "hetes", "heths", "heuch", "heugh", "hevea", "hewed", "hewer", "hewgh", "hexad", "hexed", "hexer", "hexes", "hexyl", "heyed", "hiant", "hicks", "hided", "hider", "hides", "hiems", "highs", "hight", "hijab", "hijra", "hiked", "hiker", "hikes", "hikoi", "hilar", "hilch", "hillo", "hills", "hilts", "hilum", "hilus", "himbo", "hinau", "hinds", "hings", "hinky", "hinny", "hints", "hiois", "hiply", "hired", "hiree", "hirer", "hires", "hissy", "hists", "hithe", "hived", "hiver", "hives", "hizen", "hoaed", "hoagy", "hoars", "hoary", "hoast", "hobos", "hocks", "hocus", "hodad", "hodja", "hoers", "hogan", "hogen", "hoggs", "hoghs", "hohed", "hoick", "hoied", "hoiks", "hoing", "hoise", "hokas", "hoked", "hokes", "hokey", "hokis", "hokku", "hokum", "holds", "holed", "holes", "holey", "holks", "holla", "hollo", "holme", "holms", "holon", "holos", "holts", "homas", "homed", "homes", "homey", "homie", "homme", "honan", "honda", "honds", "honed", "honer", "hones", "hongi", "hongs", "honks", "honky", "hooch", "hoods", "hoody", "hooey", "hoofs", "hooka", "hooks", "hooky", "hooly", "hoons", "hoops", "hoord", "hoors", "hoosh", "hoots", "hooty", "hoove", "hopak", "hoped", "hoper", "hopes", "hoppy", "horah", "horal", "horas", "horis", "horks", "horme", "horns", "horst", "horsy", "hosed", "hosel", "hosen", "hoser", "hoses", "hosey", "hosta", "hosts", "hotch", "hoten", "hotty", "houff", "houfs", "hough", "houri", "hours", "houts", "hovea", "hoved", "hoven", "hoves", "howbe", "howes", "howff", "howfs", "howks", "howls", "howre", "howso", "hoxed", "hoxes", "hoyas", "hoyed", "hoyle", "hubby", "hucks", "hudna", "hudud", "huers", "huffs", "huffy", "huger", "huggy", "huhus", "huias", "hulas", "hules", "hulks", "hulky", "hullo", "hulls", "hully", "humas", "humfs", "humic", "humps", "humpy", "hunks", "hunts", "hurds", "hurls", "hurly", "hurra", "hurst", "hurts", "hushy", "husks", "husos", "hutia", "huzza", "huzzy", "hwyls", "hydra", "hyens", "hygge", "hying", "hykes", "hylas", "hyleg", "hyles", "hylic", "hymns", "hynde", "hyoid", "hyped", "hypes", "hypha", "hyphy", "hypos", "hyrax", "hyson", "hythe", "iambi", "iambs", "ibrik", "icers", "iched", "iches", "ichor", "icier", "icker", "ickle", "icons", "ictal", "ictic", "ictus", "idant", "ideas", "idees", "ident", "idled", "idles", "idola", "idols", "idyls", "iftar", "igapo", "igged", "iglus", "ihram", "ikans", "ikats", "ikons", "ileac", "ileal", "ileum", "ileus", "iliad", "ilial", "ilium", "iller", "illth", "imago", "imams", "imari", "imaum", "imbar", "imbed", "imide", "imido", "imids", "imine", "imino", "immew", "immit", "immix", "imped", "impis", "impot", "impro", "imshi", "imshy", "inapt", "inarm", "inbye", "incel", "incle", "incog", "incus", "incut", "indew", "india", "indie", "indol", "indow", "indri", "indue", "inerm", "infix", "infos", "infra", "ingan", "ingle", "inion", "inked", "inker", "inkle", "inned", "innit", "inorb", "inrun", "inset", "inspo", "intel", "intil", "intis", "intra", "inula", "inure", "inurn", "inust", "invar", "inwit", "iodic", "iodid", "iodin", "iotas", "ippon", "irade", "irids", "iring", "irked", "iroko", "irone", "irons", "isbas", "ishes", "isled", "isles", "isnae", "issei", "istle", "items", "ither", "ivied", "ivies", "ixias", "ixnay", "ixora", "ixtle", "izard", "izars", "izzat", "jaaps", "jabot", "jacal", "jacks", "jacky", "jaded", "jades", "jafas", "jaffa", "jagas", "jager", "jaggs", "jaggy", "jagir", "jagra", "jails", "jaker", "jakes", "jakey", "jalap", "jalop", "jambe", "jambo", "jambs", "jambu", "james", "jammy", "jamon", "janes", "janns", "janny", "janty", "japan", "japed", "japer", "japes", "jarks", "jarls", "jarps", "jarta", "jarul", "jasey", "jaspe", "jasps", "jatos", "jauks", "jaups", "javas", "javel", "jawan", "jawed", "jaxie", "jeans", "jeats", "jebel", "jedis", "jeels", "jeely", "jeeps", "jeers", "jeeze", "jefes", "jeffs", "jehad", "jehus", "jelab", "jello", "jells", "jembe", "jemmy", "jenny", "jeons", "jerid", "jerks", "jerry", "jesse", "jests", "jesus", "jetes", "jeton", "jeune", "jewed", "jewie", "jhala", "jiaos", "jibba", "jibbs", "jibed", "jiber", "jibes", "jiffs", "jiggy", "jigot", "jihad", "jills", "jilts", "jimmy", "jimpy", "jingo", "jinks", "jinne", "jinni", "jinns", "jirds", "jirga", "jirre", "jisms", "jived", "jiver", "jives", "jivey", "jnana", "jobed", "jobes", "jocko", "jocks", "jocky", "jocos", "jodel", "joeys", "johns", "joins", "joked", "jokes", "jokey", "jokol", "joled", "joles", "jolls", "jolts", "jolty", "jomon", "jomos", "jones", "jongs", "jonty", "jooks", "joram", "jorum", "jotas", "jotty", "jotun", "joual", "jougs", "jouks", "joule", "jours", "jowar", "jowed", "jowls", "jowly", "joyed", "jubas", "jubes", "jucos", "judas", "judgy", "judos", "jugal", "jugum", "jujus", "juked", "jukes", "jukus", "julep", "jumar", "jumby", "jumps", "junco", "junks", "junky", "jupes", "jupon", "jural", "jurat", "jurel", "jures", "justs", "jutes", "jutty", "juves", "juvie", "kaama", "kabab", "kabar", "kabob", "kacha", "kacks", "kadai", "kades", "kadis", "kafir", "kagos", "kagus", "kahal", "kaiak", "kaids", "kaies", "kaifs", "kaika", "kaiks", "kails", "kaims", "kaing", "kains", "kakas", "kakis", "kalam", "kales", "kalif", "kalis", "kalpa", "kamas", "kames", "kamik", "kamis", "kamme", "kanae", "kanas", "kandy", "kaneh", "kanes", "kanga", "kangs", "kanji", "kants", "kanzu", "kaons", "kapas", "kaphs", "kapok", "kapow", "kapus", "kaput", "karas", "karat", "karks", "karns", "karoo", "karos", "karri", "karst", "karsy", "karts", "karzy", "kasha", "kasme", "katal", "katas", "katis", "katti", "kaugh", "kauri", "kauru", "kaury", "kaval", "kavas", "kawas", "kawau", "kawed", "kayle", "kayos", "kazis", "kazoo", "kbars", "kebar", "kebob", "kecks", "kedge", "kedgy", "keech", "keefs", "keeks", "keels", "keema", "keeno", "keens", "keeps", "keets", "keeve", "kefir", "kehua", "keirs", "kelep", "kelim", "kells", "kelly", "kelps", "kelpy", "kelts", "kelty", "kembo", "kembs", "kemps", "kempt", "kempy", "kenaf", "kench", "kendo", "kenos", "kente", "kents", "kepis", "kerbs", "kerel", "kerfs", "kerky", "kerma", "kerne", "kerns", "keros", "kerry", "kerve", "kesar", "kests", "ketas", "ketch", "ketes", "ketol", "kevel", "kevil", "kexes", "keyed", "keyer", "khadi", "khafs", "khans", "khaph", "khats", "khaya", "khazi", "kheda", "kheth", "khets", "khoja", "khors", "khoum", "khuds", "kiaat", "kiack", "kiang", "kibbe", "kibbi", "kibei", "kibes", "kibla", "kicks", "kicky", "kiddo", "kiddy", "kidel", "kidge", "kiefs", "kiers", "kieve", "kievs", "kight", "kikoi", "kiley", "kilim", "kills", "kilns", "kilos", "kilps", "kilts", "kilty", "kimbo", "kinas", "kinda", "kinds", "kindy", "kines", "kings", "kinin", "kinks", "kinos", "kiore", "kipes", "kippa", "kipps", "kirby", "kirks", "kirns", "kirri", "kisan", "kissy", "kists", "kited", "kiter", "kites", "kithe", "kiths", "kitul", "kivas", "kiwis", "klang", "klaps", "klett", "klick", "klieg", "kliks", "klong", "kloof", "kluge", "klutz", "knags", "knaps", "knarl", "knars", "knaur", "knawe", "knees", "knell", "knish", "knits", "knive", "knobs", "knops", "knosp", "knots", "knout", "knowe", "knows", "knubs", "knurl", "knurr", "knurs", "knuts", "koans", "koaps", "koban", "kobos", "koels", "koffs", "kofta", "kogal", "kohas", "kohen", "kohls", "koine", "kojis", "kokam", "kokas", "koker", "kokra", "kokum", "kolas", "kolos", "kombu", "konbu", "kondo", "konks", "kooks", "kooky", "koori", "kopek", "kophs", "kopje", "koppa", "korai", "koras", "korat", "kores", "korma", "koros", "korun", "korus", "koses", "kotch", "kotos", "kotow", "koura", "kraal", "krabs", "kraft", "krais", "krait", "krang", "krans", "kranz", "kraut", "krays", "kreep", "kreng", "krewe", "krona", "krone", "kroon", "krubi", "krunk", "ksars", "kubie", "kudos", "kudus", "kudzu", "kufis", "kugel", "kuias", "kukri", "kukus", "kulak", "kulan", "kulas", "kulfi", "kumis", "kumys", "kuris", "kurre", "kurta", "kurus", "kusso", "kutas", "kutch", "kutis", "kutus", "kuzus", "kvass", "kvell", "kwela", "kyack", "kyaks", "kyang", "kyars", "kyats", "kybos", "kydst", "kyles", "kylie", "kylin", "kylix", "kyloe", "kynde", "kynds", "kypes", "kyrie", "kytes", "kythe", "laari", "labda", "labia", "labis", "labra", "laced", "lacer", "laces", "lacet", "lacey", "lacks", "laddy", "laded", "lader", "lades", "laers", "laevo", "lagan", "lahal", "lahar", "laich", "laics", "laids", "laigh", "laika", "laiks", "laird", "lairs", "lairy", "laith", "laity", "laked", "laker", "lakes", "lakhs", "lakin", "laksa", "laldy", "lalls", "lamas", "lambs", "lamby", "lamed", "lamer", "lames", "lamia", "lammy", "lamps", "lanai", "lanas", "lanch", "lande", "lands", "lanes", "lanks", "lants", "lapin", "lapis", "lapje", "larch", "lards", "lardy", "laree", "lares", "largo", "laris", "larks", "larky", "larns", "larnt", "larum", "lased", "laser", "lases", "lassi", "lassu", "lassy", "lasts", "latah", "lated", "laten", "latex", "lathi", "laths", "lathy", "latke", "latus", "lauan", "lauch", "lauds", "laufs", "laund", "laura", "laval", "lavas", "laved", "laver", "laves", "lavra", "lavvy", "lawed", "lawer", "lawin", "lawks", "lawns", "lawny", "laxed", "laxer", "laxes", "laxly", "layed", "layin", "layup", "lazar", "lazed", "lazes", "lazos", "lazzi", "lazzo", "leads", "leady", "leafs", "leaks", "leams", "leans", "leany", "leaps", "leare", "lears", "leary", "leats", "leavy", "leaze", "leben", "leccy", "ledes", "ledgy", "ledum", "leear", "leeks", "leeps", "leers", "leese", "leets", "leeze", "lefte", "lefts", "leger", "leges", "legge", "leggo", "legit", "lehrs", "lehua", "leirs", "leish", "leman", "lemed", "lemel", "lemes", "lemma", "lemme", "lends", "lenes", "lengs", "lenis", "lenos", "lense", "lenti", "lento", "leone", "lepid", "lepra", "lepta", "lered", "leres", "lerps", "leses", "lests", "letch", "lethe", "letup", "leuch", "leuco", "leuds", "leugh", "levas", "levee", "leves", "levin", "levis", "lewis", "lexes", "lexis", "lezes", "lezza", "lezzy", "liana", "liane", "liang", "liard", "liars", "liart", "liber", "libra", "libri", "lichi", "licht", "licit", "licks", "lidar", "lidos", "liefs", "liens", "liers", "lieus", "lieve", "lifer", "lifes", "lifts", "ligan", "liger", "ligge", "ligne", "liked", "liker", "likes", "likin", "lills", "lilos", "lilts", "liman", "limas", "limax", "limba", "limbi", "limbs", "limby", "limed", "limen", "limes", "limey", "limma", "limns", "limos", "limpa", "limps", "linac", "linch", "linds", "lindy", "lined", "lines", "liney", "linga", "lings", "lingy", "linin", "links", "linky", "linns", "linny", "linos", "lints", "linty", "linum", "linux", "lions", "lipas", "lipes", "lipin", "lipos", "lippy", "liras", "lirks", "lirot", "lisks", "lisle", "lisps", "lists", "litai", "litas", "lited", "liter", "lites", "litho", "liths", "litre", "lived", "liven", "lives", "livor", "livre", "llano", "loach", "loads", "loafs", "loams", "loans", "loast", "loave", "lobar", "lobed", "lobes", "lobos", "lobus", "loche", "lochs", "locie", "locis", "locks", "locos", "locum", "loden", "lodes", "loess", "lofts", "logan", "loges", "loggy", "logia", "logie", "logoi", "logon", "logos", "lohan", "loids", "loins", "loipe", "loirs", "lokes", "lolls", "lolly", "lolog", "lomas", "lomed", "lomes", "loner", "longa", "longe", "longs", "looby", "looed", "looey", "loofa", "loofs", "looie", "looks", "looky", "looms", "loons", "loony", "loops", "loord", "loots", "loped", "loper", "lopes", "loppy", "loral", "loran", "lords", "lordy", "lorel", "lores", "loric", "loris", "losed", "losel", "losen", "loses", "lossy", "lotah", "lotas", "lotes", "lotic", "lotos", "lotsa", "lotta", "lotte", "lotto", "lotus", "loued", "lough", "louie", "louis", "louma", "lound", "louns", "loupe", "loups", "loure", "lours", "loury", "louts", "lovat", "loved", "loves", "lovey", "lovie", "lowan", "lowed", "lowes", "lownd", "lowne", "lowns", "lowps", "lowry", "lowse", "lowts", "loxed", "loxes", "lozen", "luach", "luaus", "lubed", "lubes", "lubra", "luces", "lucks", "lucre", "ludes", "ludic", "ludos", "luffa", "luffs", "luged", "luger", "luges", "lulls", "lulus", "lumas", "lumbi", "lumme", "lummy", "lumps", "lunas", "lunes", "lunet", "lungi", "lungs", "lunks", "lunts", "lupin", "lured", "lurer", "lures", "lurex", "lurgi", "lurgy", "lurks", "lurry", "lurve", "luser", "lushy", "lusks", "lusts", "lusus", "lutea", "luted", "luter", "lutes", "luvvy", "luxed", "luxer", "luxes", "lweis", "lyams", "lyard", "lyart", "lyase", "lycea", "lycee", "lycra", "lymes", "lynes", "lyres", "lysed", "lyses", "lysin", "lysis", "lysol", "lyssa", "lyted", "lytes", "lythe", "lytic", "lytta", "maaed", "maare", "maars", "mabes", "macas", "maced", "macer", "maces", "mache", "machi", "machs", "macks", "macle", "macon", "madge", "madid", "madre", "maerl", "mafic", "mages", "maggs", "magot", "magus", "mahoe", "mahua", "mahwa", "maids", "maiko", "maiks", "maile", "maill", "mails", "maims", "mains", "maire", "mairs", "maise", "maist", "makar", "makes", "makis", "makos", "malam", "malar", "malas", "malax", "males", "malic", "malik", "malis", "malls", "malms", "malmy", "malts", "malty", "malus", "malva", "malwa", "mamas", "mamba", "mamee", "mamey", "mamie", "manas", "manat", "mandi", "maneb", "maned", "maneh", "manes", "manet", "mangs", "manis", "manky", "manna", "manos", "manse", "manta", "manto", "manty", "manul", "manus", "mapau", "maqui", "marae", "marah", "maras", "marcs", "mardy", "mares", "marge", "margs", "maria", "marid", "marka", "marks", "marle", "marls", "marly", "marms", "maron", "maror", "marra", "marri", "marse", "marts", "marvy", "masas", "mased", "maser", "mases", "mashy", "masks", "massa", "massy", "masts", "masty", "masus", "matai", "mated", "mater", "mates", "maths", "matin", "matlo", "matte", "matts", "matza", "matzo", "mauby", "mauds", "mauls", "maund", "mauri", "mausy", "mauts", "mauzy", "maven", "mavie", "mavin", "mavis", "mawed", "mawks", "mawky", "mawns", "mawrs", "maxed", "maxes", "maxis", "mayan", "mayas", "mayed", "mayos", "mayst", "mazed", "mazer", "mazes", "mazey", "mazut", "mbira", "meads", "meals", "meane", "means", "meany", "meare", "mease", "meath", "meats", "mebos", "mechs", "mecks", "medii", "medle", "meeds", "meers", "meets", "meffs", "meins", "meint", "meiny", "meith", "mekka", "melas", "melba", "melds", "melic", "melik", "mells", "melts", "melty", "memes", "memos", "menad", "mends", "mened", "menes", "menge", "mengs", "mensa", "mense", "mensh", "menta", "mento", "menus", "meous", "meows", "merch", "mercs", "merde", "mered", "merel", "merer", "meres", "meril", "meris", "merks", "merle", "merls", "merse", "mesal", "mesas", "mesel", "meses", "meshy", "mesic", "mesne", "meson", "messy", "mesto", "meted", "metes", "metho", "meths", "metic", "metif", "metis", "metol", "metre", "meuse", "meved", "meves", "mewed", "mewls", "meynt", "mezes", "mezze", "mezzo", "mhorr", "miaou", "miaow", "miasm", "miaul", "micas", "miche", "micht", "micks", "micky", "micos", "micra", "middy", "midgy", "midis", "miens", "mieve", "miffs", "miffy", "mifty", "miggs", "mihas", "mihis", "miked", "mikes", "mikra", "mikva", "milch", "milds", "miler", "miles", "milfs", "milia", "milko", "milks", "mille", "mills", "milor", "milos", "milpa", "milts", "milty", "miltz", "mimed", "mimeo", "mimer", "mimes", "mimsy", "minae", "minar", "minas", "mincy", "minds", "mined", "mines", "minge", "mings", "mingy", "minis", "minke", "minks", "minny", "minos", "mints", "mired", "mires", "mirex", "mirid", "mirin", "mirks", "mirky", "mirly", "miros", "mirvs", "mirza", "misch", "misdo", "mises", "misgo", "misos", "missa", "mists", "misty", "mitch", "miter", "mites", "mitis", "mitre", "mitts", "mixed", "mixen", "mixer", "mixes", "mixte", "mixup", "mizen", "mizzy", "mneme", "moans", "moats", "mobby", "mobes", "mobey", "mobie", "moble", "mochi", "mochs", "mochy", "mocks", "moder", "modes", "modge", "modii", "modus", "moers", "mofos", "moggy", "mohel", "mohos", "mohrs", "mohua", "mohur", "moile", "moils", "moira", "moire", "moits", "mojos", "mokes", "mokis", "mokos", "molal", "molas", "molds", "moled", "moles", "molla", "molls", "molly", "molto", "molts", "molys", "momes", "momma", "mommy", "momus", "monad", "monal", "monas", "monde", "mondo", "moner", "mongo", "mongs", "monic", "monie", "monks", "monos", "monte", "monty", "moobs", "mooch", "moods", "mooed", "mooks", "moola", "mooli", "mools", "mooly", "moong", "moons", "moony", "moops", "moors", "moory", "moots", "moove", "moped", "moper", "mopes", "mopey", "moppy", "mopsy", "mopus", "morae", "moras", "morat", "moray", "morel", "mores", "moria", "morne", "morns", "morra", "morro", "morse", "morts", "mosed", "moses", "mosey", "mosks", "mosso", "moste", "mosts", "moted", "moten", "motes", "motet", "motey", "moths", "mothy", "motis", "motte", "motts", "motty", "motus", "motza", "mouch", "moues", "mould", "mouls", "moups", "moust", "mousy", "moved", "moves", "mowas", "mowed", "mowra", "moxas", "moxie", "moyas", "moyle", "moyls", "mozed", "mozes", "mozos", "mpret", "mucho", "mucic", "mucid", "mucin", "mucks", "mucor", "mucro", "mudge", "mudir", "mudra", "muffs", "mufti", "mugga", "muggs", "muggy", "muhly", "muids", "muils", "muirs", "muist", "mujik", "mulct", "muled", "mules", "muley", "mulga", "mulie", "mulla", "mulls", "mulse", "mulsh", "mumms", "mumps", "mumsy", "mumus", "munga", "munge", "mungo", "mungs", "munis", "munts", "muntu", "muons", "muras", "mured", "mures", "murex", "murid", "murks", "murls", "murly", "murra", "murre", "murri", "murrs", "murry", "murti", "murva", "musar", "musca", "mused", "muser", "muses", "muset", "musha", "musit", "musks", "musos", "musse", "mussy", "musth", "musts", "mutch", "muted", "muter", "mutes", "mutha", "mutis", "muton", "mutts", "muxed", "muxes", "muzak", "muzzy", "mvule", "myall", "mylar", "mynah", "mynas", "myoid", "myoma", "myope", "myops", "myopy", "mysid", "mythi", "myths", "mythy", "myxos", "mzees", "naams", "naans", "nabes", "nabis", "nabks", "nabla", "nabob", "nache", "nacho", "nacre", "nadas", "naeve", "naevi", "naffs", "nagas", "naggy", "nagor", "nahal", "naiad", "naifs", "naiks", "nails", "naira", "nairu", "naked", "naker", "nakfa", "nalas", "naled", "nalla", "named", "namer", "names", "namma", "namus", "nanas", "nance", "nancy", "nandu", "nanna", "nanos", "nanua", "napas", "naped", "napes", "napoo", "nappa", "nappe", "nappy", "naras", "narco", "narcs", "nards", "nares", "naric", "naris", "narks", "narky", "narre", "nashi", "natch", "nates", "natis", "natty", "nauch", "naunt", "navar", "naves", "navew", "navvy", "nawab", "nazes", "nazir", "nazis", "nduja", "neafe", "neals", "neaps", "nears", "neath", "neats", "nebek", "nebel", "necks", "neddy", "needs", "neeld", "neele", "neemb", "neems", "neeps", "neese", "neeze", "negro", "negus", "neifs", "neist", "neive", "nelis", "nelly", "nemas", "nemns", "nempt", "nenes", "neons", "neper", "nepit", "neral", "nerds", "nerka", "nerks", "nerol", "nerts", "nertz", "nervy", "nests", "netes", "netop", "netts", "netty", "neuks", "neume", "neums", "nevel", "neves", "nevus", "newbs", "newed", "newel", "newie", "newsy", "newts", "nexts", "nexus", "ngaio", "ngana", "ngati", "ngoma", "ngwee", "nicad", "nicht", "nicks", "nicol", "nidal", "nided", "nides", "nidor", "nidus", "niefs", "nieve", "nifes", "niffs", "niffy", "nifty", "niger", "nighs", "nihil", "nikab", "nikah", "nikau", "nills", "nimbi", "nimbs", "nimps", "niner", "nines", "ninon", "nipas", "nippy", "niqab", "nirls", "nirly", "nisei", "nisse", "nisus", "niter", "nites", "nitid", "niton", "nitre", "nitro", "nitry", "nitty", "nival", "nixed", "nixer", "nixes", "nixie", "nizam", "nkosi", "noahs", "nobby", "nocks", "nodal", "noddy", "nodes", "nodus", "noels", "noggs", "nohow", "noils", "noily", "noint", "noirs", "noles", "nolls", "nolos", "nomas", "nomen", "nomes", "nomic", "nomoi", "nomos", "nonas", "nonce", "nones", "nonet", "nongs", "nonis", "nonny", "nonyl", "noobs", "nooit", "nooks", "nooky", "noons", "noops", "nopal", "noria", "noris", "norks", "norma", "norms", "nosed", "noser", "noses", "notal", "noted", "noter", "notes", "notum", "nould", "noule", "nouls", "nouns", "nouny", "noups", "novae", "novas", "novum", "noway", "nowed", "nowls", "nowts", "nowty", "noxal", "noxes", "noyau", "noyed", "noyes", "nubby", "nubia", "nucha", "nuddy", "nuder", "nudes", "nudie", "nudzh", "nuffs", "nugae", "nuked", "nukes", "nulla", "nulls", "numbs", "numen", "nummy", "nunny", "nurds", "nurdy", "nurls", "nurrs", "nutso", "nutsy", "nyaff", "nyala", "nying", "nyssa", "oaked", "oaker", "oakum", "oared", "oases", "oasis", "oasts", "oaten", "oater", "oaths", "oaves", "obang", "obeah", "obeli", "obeys", "obias", "obied", "obiit", "obits", "objet", "oboes", "obole", "oboli", "obols", "occam", "ocher", "oches", "ochre", "ochry", "ocker", "ocrea", "octad", "octan", "octas", "octyl", "oculi", "odahs", "odals", "odeon", "odeum", "odism", "odist", "odium", "odors", "odour", "odyle", "odyls", "ofays", "offed", "offie", "oflag", "ofter", "ogams", "ogeed", "ogees", "oggin", "ogham", "ogive", "ogled", "ogler", "ogles", "ogmic", "ogres", "ohias", "ohing", "ohmic", "ohone", "oidia", "oiled", "oiler", "oinks", "oints", "ojime", "okapi", "okays", "okehs", "okras", "oktas", "oldie", "oleic", "olein", "olent", "oleos", "oleum", "olios", "ollas", "ollav", "oller", "ollie", "ology", "olpae", "olpes", "omasa", "omber", "ombus", "omens", "omers", "omits", "omlah", "omovs", "omrah", "oncer", "onces", "oncet", "oncus", "onely", "oners", "onery", "onium", "onkus", "onlay", "onned", "ontic", "oobit", "oohed", "oomph", "oonts", "ooped", "oorie", "ooses", "ootid", "oozed", "oozes", "opahs", "opals", "opens", "opepe", "oping", "oppos", "opsin", "opted", "opter", "orach", "oracy", "orals", "orang", "orant", "orate", "orbed", "orcas", "orcin", "ordos", "oread", "orfes", "orgia", "orgic", "orgue", "oribi", "oriel", "orixa", "orles", "orlon", "orlop", "ormer", "ornis", "orpin", "orris", "ortho", "orval", "orzos", "oscar", "oshac", "osier", "osmic", "osmol", "ossia", "ostia", "otaku", "otary", "ottar", "ottos", "oubit", "oucht", "ouens", "ouija", "oulks", "oumas", "oundy", "oupas", "ouped", "ouphe", "ouphs", "ourie", "ousel", "ousts", "outby", "outed", "outre", "outro", "outta", "ouzel", "ouzos", "ovals", "ovels", "ovens", "overs", "ovist", "ovoli", "ovolo", "ovule", "owche", "owies", "owled", "owler", "owlet", "owned", "owres", "owrie", "owsen", "oxbow", "oxers", "oxeye", "oxids", "oxies", "oxime", "oxims", "oxlip", "oxter", "oyers", "ozeki", "ozzie", "paals", "paans", "pacas", "paced", "pacer", "paces", "pacey", "pacha", "packs", "pacos", "pacta", "pacts", "padis", "padle", "padma", "padre", "padri", "paean", "paedo", "paeon", "paged", "pager", "pages", "pagle", "pagod", "pagri", "paiks", "pails", "pains", "paire", "pairs", "paisa", "paise", "pakka", "palas", "palay", "palea", "paled", "pales", "palet", "palis", "palki", "palla", "palls", "pally", "palms", "palmy", "palpi", "palps", "palsa", "pampa", "panax", "pance", "panda", "pands", "pandy", "paned", "panes", "panga", "pangs", "panim", "panko", "panne", "panni", "panto", "pants", "panty", "paoli", "paolo", "papas", "papaw", "papes", "pappi", "pappy", "parae", "paras", "parch", "pardi", "pards", "pardy", "pared", "paren", "pareo", "pares", "pareu", "parev", "parge", "pargo", "paris", "parki", "parks", "parky", "parle", "parly", "parma", "parol", "parps", "parra", "parrs", "parti", "parts", "parve", "parvo", "paseo", "pases", "pasha", "pashm", "paska", "paspy", "passe", "pasts", "pated", "paten", "pater", "pates", "paths", "patin", "patka", "patly", "patte", "patus", "pauas", "pauls", "pavan", "paved", "paven", "paver", "paves", "pavid", "pavin", "pavis", "pawas", "pawaw", "pawed", "pawer", "pawks", "pawky", "pawls", "pawns", "paxes", "payed", "payor", "paysd", "peage", "peags", "peaks", "peaky", "peals", "peans", "peare", "pears", "peart", "pease", "peats", "peaty", "peavy", "peaze", "pebas", "pechs", "pecke", "pecks", "pecky", "pedes", "pedis", "pedro", "peece", "peeks", "peels", "peens", "peeoy", "peepe", "peeps", "peers", "peery", "peeve", "peggy", "peghs", "peins", "peise", "peize", "pekan", "pekes", "pekin", "pekoe", "pelas", "pelau", "peles", "pelfs", "pells", "pelma", "pelon", "pelta", "pelts", "pends", "pendu", "pened", "penes", "pengo", "penie", "penis", "penks", "penna", "penni", "pents", "peons", "peony", "pepla", "pepos", "peppy", "pepsi", "perai", "perce", "percs", "perdu", "perdy", "perea", "peres", "peris", "perks", "perms", "perns", "perog", "perps", "perry", "perse", "perst", "perts", "perve", "pervo", "pervs", "pervy", "pesos", "pests", "pesty", "petar", "peter", "petit", "petre", "petri", "petti", "petto", "pewee", "pewit", "peyse", "phage", "phang", "phare", "pharm", "pheer", "phene", "pheon", "phese", "phial", "phish", "phizz", "phlox", "phoca", "phono", "phons", "phots", "phpht", "phuts", "phyla", "phyle", "piani", "pians", "pibal", "pical", "picas", "piccy", "picks", "picot", "picra", "picul", "piend", "piers", "piert", "pieta", "piets", "piezo", "pight", "pigmy", "piing", "pikas", "pikau", "piked", "piker", "pikes", "pikey", "pikis", "pikul", "pilae", "pilaf", "pilao", "pilar", "pilau", "pilaw", "pilch", "pilea", "piled", "pilei", "piler", "piles", "pilis", "pills", "pilow", "pilum", "pilus", "pimas", "pimps", "pinas", "pined", "pines", "pingo", "pings", "pinko", "pinks", "pinna", "pinny", "pinon", "pinot", "pinta", "pints", "pinup", "pions", "piony", "pious", "pioye", "pioys", "pipal", "pipas", "piped", "pipes", "pipet", "pipis", "pipit", "pippy", "pipul", "pirai", "pirls", "pirns", "pirog", "pisco", "pises", "pisky", "pisos", "pissy", "piste", "pitas", "piths", "piton", "pitot", "pitta", "piums", "pixes", "pized", "pizes", "plaas", "plack", "plage", "plans", "plaps", "plash", "plasm", "plast", "plats", "platt", "platy", "playa", "plays", "pleas", "plebe", "plebs", "plena", "pleon", "plesh", "plews", "plica", "plies", "plims", "pling", "plink", "ploat", "plods", "plong", "plonk", "plook", "plops", "plots", "plotz", "plouk", "plows", "ploye", "ploys", "plues", "pluff", "plugs", "plums", "plumy", "pluot", "pluto", "plyer", "poach", "poaka", "poake", "poboy", "pocks", "pocky", "podal", "poddy", "podex", "podge", "podgy", "podia", "poems", "poeps", "poets", "pogey", "pogge", "pogos", "pohed", "poilu", "poind", "pokal", "poked", "pokes", "pokey", "pokie", "poled", "poler", "poles", "poley", "polio", "polis", "polje", "polks", "polls", "polly", "polos", "polts", "polys", "pombe", "pomes", "pommy", "pomos", "pomps", "ponce", "poncy", "ponds", "pones", "poney", "ponga", "pongo", "pongs", "pongy", "ponks", "ponts", "ponty", "ponzu", "poods", "pooed", "poofs", "poofy", "poohs", "pooja", "pooka", "pooks", "pools", "poons", "poops", "poopy", "poori", "poort", "poots", "poove", "poovy", "popes", "poppa", "popsy", "porae", "poral", "pored", "porer", "pores", "porge", "porgy", "porin", "porks", "porky", "porno", "porns", "porny", "porta", "ports", "porty", "posed", "poses", "posey", "posho", "posts", "potae", "potch", "poted", "potes", "potin", "potoo", "potsy", "potto", "potts", "potty", "pouff", "poufs", "pouke", "pouks", "poule", "poulp", "poult", "poupe", "poupt", "pours", "pouts", "powan", "powin", "pownd", "powns", "powny", "powre", "poxed", "poxes", "poynt", "poyou", "poyse", "pozzy", "praam", "prads", "prahu", "prams", "prana", "prang", "praos", "prase", "prate", "prats", "pratt", "praty", "praus", "prays", "predy", "preed", "prees", "preif", "prems", "premy", "prent", "preon", "preop", "preps", "presa", "prese", "prest", "preve", "prexy", "preys", "prial", "pricy", "prief", "prier", "pries", "prigs", "prill", "prima", "primi", "primp", "prims", "primy", "prink", "prion", "prise", "priss", "proas", "probs", "prods", "proem", "profs", "progs", "proin", "proke", "prole", "proll", "promo", "proms", "pronk", "props", "prore", "proso", "pross", "prost", "prosy", "proto", "proul", "prows", "proyn", "prunt", "pruta", "pryer", "pryse", "pseud", "pshaw", "psion", "psoae", "psoai", "psoas", "psora", "psych", "psyop", "pubco", "pubes", "pubis", "pucan", "pucer", "puces", "pucka", "pucks", "puddy", "pudge", "pudic", "pudor", "pudsy", "pudus", "puers", "puffa", "puffs", "puggy", "pugil", "puhas", "pujah", "pujas", "pukas", "puked", "puker", "pukes", "pukey", "pukka", "pukus", "pulao", "pulas", "puled", "puler", "pules", "pulik", "pulis", "pulka", "pulks", "pulli", "pulls", "pully", "pulmo", "pulps", "pulus", "pumas", "pumie", "pumps", "punas", "punce", "punga", "pungs", "punji", "punka", "punks", "punky", "punny", "punto", "punts", "punty", "pupae", "pupas", "pupus", "purda", "pured", "pures", "purin", "puris", "purls", "purpy", "purrs", "pursy", "purty", "puses", "pusle", "putid", "puton", "putti", "putto", "putts", "puzel", "pwned", "pyats", "pyets", "pygal", "pyins", "pylon", "pyned", "pynes", "pyoid", "pyots", "pyral", "pyran", "pyres", "pyrex", "pyric", "pyros", "pyxed", "pyxes", "pyxie", "pyxis", "pzazz", "qadis", "qaids", "qajaq", "qanat", "qapik", "qibla", "qophs", "qorma", "quads", "quaff", "quags", "quair", "quais", "quaky", "quale", "quant", "quare", "quass", "quate", "quats", "quayd", "quays", "qubit", "quean", "queme", "quena", "quern", "queyn", "queys", "quich", "quids", "quiff", "quims", "quina", "quine", "quino", "quins", "quint", "quipo", "quips", "quipu", "quire", "quirt", "quist", "quits", "quoad", "quods", "quoif", "quoin", "quoit", "quoll", "quonk", "quops", "qursh", "quyte", "rabat", "rabic", "rabis", "raced", "races", "rache", "racks", "racon", "radge", "radix", "radon", "raffs", "rafts", "ragas", "ragde", "raged", "ragee", "rager", "rages", "ragga", "raggs", "raggy", "ragis", "ragus", "rahed", "rahui", "raias", "raids", "raiks", "raile", "rails", "raine", "rains", "raird", "raita", "raits", "rajas", "rajes", "raked", "rakee", "raker", "rakes", "rakia", "rakis", "rakus", "rales", "ramal", "ramee", "ramet", "ramie", "ramin", "ramis", "rammy", "ramps", "ramus", "ranas", "rance", "rands", "ranee", "ranga", "rangi", "rangs", "rangy", "ranid", "ranis", "ranke", "ranks", "rants", "raped", "raper", "rapes", "raphe", "rappe", "rared", "raree", "rares", "rarks", "rased", "raser", "rases", "rasps", "rasse", "rasta", "ratal", "ratan", "ratas", "ratch", "rated", "ratel", "rater", "rates", "ratha", "rathe", "raths", "ratoo", "ratos", "ratus", "rauns", "raupo", "raved", "ravel", "raver", "raves", "ravey", "ravin", "rawer", "rawin", "rawly", "rawns", "raxed", "raxes", "rayah", "rayas", "rayed", "rayle", "rayne", "razed", "razee", "razer", "razes", "razoo", "readd", "reads", "reais", "reaks", "realo", "reals", "reame", "reams", "reamy", "reans", "reaps", "rears", "reast", "reata", "reate", "reave", "rebbe", "rebec", "rebid", "rebit", "rebop", "rebuy", "recal", "recce", "recco", "reccy", "recit", "recks", "recon", "recta", "recti", "recto", "redan", "redds", "reddy", "reded", "redes", "redia", "redid", "redip", "redly", "redon", "redos", "redox", "redry", "redub", "redux", "redye", "reech", "reede", "reeds", "reefs", "reefy", "reeks", "reeky", "reels", "reens", "reest", "reeve", "refed", "refel", "reffo", "refis", "refix", "refly", "refry", "regar", "reges", "reggo", "regie", "regma", "regna", "regos", "regur", "rehem", "reifs", "reify", "reiki", "reiks", "reink", "reins", "reird", "reist", "reive", "rejig", "rejon", "reked", "rekes", "rekey", "relet", "relie", "relit", "rello", "reman", "remap", "remen", "remet", "remex", "remix", "renay", "rends", "reney", "renga", "renig", "renin", "renne", "renos", "rente", "rents", "reoil", "reorg", "repeg", "repin", "repla", "repos", "repot", "repps", "repro", "reran", "rerig", "resat", "resaw", "resay", "resee", "reses", "resew", "resid", "resit", "resod", "resow", "resto", "rests", "resty", "resus", "retag", "retax", "retem", "retia", "retie", "retox", "revet", "revie", "rewan", "rewax", "rewed", "rewet", "rewin", "rewon", "rewth", "rexes", "rezes", "rheas", "rheme", "rheum", "rhies", "rhime", "rhine", "rhody", "rhomb", "rhone", "rhumb", "rhyne", "rhyta", "riads", "rials", "riant", "riata", "ribas", "ribby", "ribes", "riced", "ricer", "rices", "ricey", "richt", "ricin", "ricks", "rides", "ridgy", "ridic", "riels", "riems", "rieve", "rifer", "riffs", "rifte", "rifts", "rifty", "riggs", "rigol", "riled", "riles", "riley", "rille", "rills", "rimae", "rimed", "rimer", "rimes", "rimus", "rinds", "rindy", "rines", "rings", "rinks", "rioja", "riots", "riped", "ripes", "ripps", "rises", "rishi", "risks", "risps", "risus", "rites", "ritts", "ritzy", "rivas", "rived", "rivel", "riven", "rives", "riyal", "rizas", "roads", "roams", "roans", "roars", "roary", "roate", "robed", "robes", "roble", "rocks", "roded", "rodes", "roguy", "rohes", "roids", "roils", "roily", "roins", "roist", "rojak", "rojis", "roked", "roker", "rokes", "rolag", "roles", "rolfs", "rolls", "romal", "roman", "romeo", "romps", "ronde", "rondo", "roneo", "rones", "ronin", "ronne", "ronte", "ronts", "roods", "roofs", "roofy", "rooks", "rooky", "rooms", "roons", "roops", "roopy", "roosa", "roose", "roots", "rooty", "roped", "roper", "ropes", "ropey", "roque", "roral", "rores", "roric", "rorid", "rorie", "rorts", "rorty", "rosed", "roses", "roset", "roshi", "rosin", "rosit", "rosti", "rosts", "rotal", "rotan", "rotas", "rotch", "roted", "rotes", "rotis", "rotls", "roton", "rotos", "rotte", "rouen", "roues", "roule", "rouls", "roums", "roups", "roupy", "roust", "routh", "routs", "roved", "roven", "roves", "rowan", "rowed", "rowel", "rowen", "rowie", "rowme", "rownd", "rowth", "rowts", "royne", "royst", "rozet", "rozit", "ruana", "rubai", "rubby", "rubel", "rubes", "rubin", "ruble", "rubli", "rubus", "ruche", "rucks", "rudas", "rudds", "rudes", "rudie", "rudis", "rueda", "ruers", "ruffe", "ruffs", "rugae", "rugal", "ruggy", "ruing", "ruins", "rukhs", "ruled", "rules", "rumal", "rumbo", "rumen", "rumes", "rumly", "rummy", "rumpo", "rumps", "rumpy", "runch", "runds", "runed", "runes", "rungs", "runic", "runny", "runts", "runty", "rupia", "rurps", "rurus", "rusas", "ruses", "rushy", "rusks", "rusma", "russe", "rusts", "ruths", "rutin", "rutty", "ryals", "rybat", "ryked", "rykes", "rymme", "rynds", "ryots", "ryper", "saags", "sabal", "sabed", "saber", "sabes", "sabha", "sabin", "sabir", "sable", "sabot", "sabra", "sabre", "sacks", "sacra", "saddo", "sades", "sadhe", "sadhu", "sadis", "sados", "sadza", "safed", "safes", "sagas", "sager", "sages", "saggy", "sagos", "sagum", "saheb", "sahib", "saice", "saick", "saics", "saids", "saiga", "sails", "saims", "saine", "sains", "sairs", "saist", "saith", "sajou", "sakai", "saker", "sakes", "sakia", "sakis", "sakti", "salal", "salat", "salep", "sales", "salet", "salic", "salix", "salle", "salmi", "salol", "salop", "salpa", "salps", "salse", "salto", "salts", "salue", "salut", "saman", "samas", "samba", "sambo", "samek", "samel", "samen", "sames", "samey", "samfu", "sammy", "sampi", "samps", "sands", "saned", "sanes", "sanga", "sangh", "sango", "sangs", "sanko", "sansa", "santo", "sants", "saola", "sapan", "sapid", "sapor", "saran", "sards", "sared", "saree", "sarge", "sargo", "sarin", "saris", "sarks", "sarky", "sarod", "saros", "sarus", "saser", "sasin", "sasse", "satai", "satay", "sated", "satem", "sates", "satis", "sauba", "sauch", "saugh", "sauls", "sault", "saunt", "saury", "sauts", "saved", "saver", "saves", "savey", "savin", "sawah", "sawed", "sawer", "saxes", "sayed", "sayer", "sayid", "sayne", "sayon", "sayst", "sazes", "scabs", "scads", "scaff", "scags", "scail", "scala", "scall", "scams", "scand", "scans", "scapa", "scape", "scapi", "scarp", "scars", "scart", "scath", "scats", "scatt", "scaud", "scaup", "scaur", "scaws", "sceat", "scena", "scend", "schav", "schmo", "schul", "schwa", "sclim", "scody", "scogs", "scoog", "scoot", "scopa", "scops", "scots", "scoug", "scoup", "scowp", "scows", "scrab", "scrae", "scrag", "scran", "scrat", "scraw", "scray", "scrim", "scrip", "scrob", "scrod", "scrog", "scrow", "scudi", "scudo", "scuds", "scuff", "scuft", "scugs", "sculk", "scull", "sculp", "sculs", "scums", "scups", "scurf", "scurs", "scuse", "scuta", "scute", "scuts", "scuzz", "scyes", "sdayn", "sdein", "seals", "seame", "seams", "seamy", "seans", "seare", "sears", "sease", "seats", "seaze", "sebum", "secco", "sechs", "sects", "seder", "sedes", "sedge", "sedgy", "sedum", "seeds", "seeks", "seeld", "seels", "seely", "seems", "seeps", "seepy", "seers", "sefer", "segar", "segni", "segno", "segol", "segos", "sehri", "seifs", "seils", "seine", "seirs", "seise", "seism", "seity", "seiza", "sekos", "sekts", "selah", "seles", "selfs", "sella", "selle", "sells", "selva", "semee", "semes", "semie", "semis", "senas", "sends", "senes", "sengi", "senna", "senor", "sensa", "sensi", "sente", "senti", "sents", "senvy", "senza", "sepad", "sepal", "sepic", "sepoy", "septa", "septs", "serac", "serai", "seral", "sered", "serer", "seres", "serfs", "serge", "seric", "serin", "serks", "seron", "serow", "serra", "serre", "serrs", "serry", "servo", "sesey", "sessa", "setae", "setal", "seton", "setts", "sewan", "sewar", "sewed", "sewel", "sewen", "sewin", "sexed", "sexer", "sexes", "sexto", "sexts", "seyen", "shads", "shags", "shahs", "shako", "shakt", "shalm", "shaly", "shama", "shams", "shand", "shans", "shaps", "sharn", "shash", "shaul", "shawm", "shawn", "shaws", "shaya", "shays", "shchi", "sheaf", "sheal", "sheas", "sheds", "sheel", "shend", "shent", "sheol", "sherd", "shere", "shero", "shets", "sheva", "shewn", "shews", "shiai", "shiel", "shier", "shies", "shill", "shily", "shims", "shins", "ships", "shirr", "shirs", "shish", "shiso", "shist", "shite", "shits", "shiur", "shiva", "shive", "shivs", "shlep", "shlub", "shmek", "shmoe", "shoat", "shoed", "shoer", "shoes", "shogi", "shogs", "shoji", "shojo", "shola", "shool", "shoon", "shoos", "shope", "shops", "shorl", "shote", "shots", "shott", "showd", "shows", "shoyu", "shred", "shris", "shrow", "shtik", "shtum", "shtup", "shule", "shuln", "shuls", "shuns", "shura", "shute", "shuts", "shwas", "shyer", "sials", "sibbs", "sibyl", "sices", "sicht", "sicko", "sicks", "sicky", "sidas", "sided", "sider", "sides", "sidha", "sidhe", "sidle", "sield", "siens", "sient", "sieth", "sieur", "sifts", "sighs", "sigil", "sigla", "signa", "signs", "sijos", "sikas", "siker", "sikes", "silds", "siled", "silen", "siler", "siles", "silex", "silks", "sills", "silos", "silts", "silty", "silva", "simar", "simas", "simba", "simis", "simps", "simul", "sinds", "sined", "sines", "sings", "sinhs", "sinks", "sinky", "sinus", "siped", "sipes", "sippy", "sired", "siree", "sires", "sirih", "siris", "siroc", "sirra", "sirup", "sisal", "sises", "sista", "sists", "sitar", "sited", "sites", "sithe", "sitka", "situp", "situs", "siver", "sixer", "sixes", "sixmo", "sixte", "sizar", "sized", "sizel", "sizer", "sizes", "skags", "skail", "skald", "skank", "skart", "skats", "skatt", "skaws", "skean", "skear", "skeds", "skeed", "skeef", "skeen", "skeer", "skees", "skeet", "skegg", "skegs", "skein", "skelf", "skell", "skelm", "skelp", "skene", "skens", "skeos", "skeps", "skers", "skets", "skews", "skids", "skied", "skies", "skiey", "skimo", "skims", "skink", "skins", "skint", "skios", "skips", "skirl", "skirr", "skite", "skits", "skive", "skivy", "sklim", "skoal", "skody", "skoff", "skogs", "skols", "skool", "skort", "skosh", "skran", "skrik", "skuas", "skugs", "skyed", "skyer", "skyey", "skyfs", "skyre", "skyrs", "skyte", "slabs", "slade", "slaes", "slags", "slaid", "slake", "slams", "slane", "slank", "slaps", "slart", "slats", "slaty", "slaws", "slays", "slebs", "sleds", "sleer", "slews", "sleys", "slier", "slily", "slims", "slipe", "slips", "slipt", "slish", "slits", "slive", "sloan", "slobs", "sloes", "slogs", "sloid", "slojd", "slomo", "sloom", "sloot", "slops", "slopy", "slorm", "slots", "slove", "slows", "sloyd", "slubb", "slubs", "slued", "slues", "sluff", "slugs", "sluit", "slums", "slurb", "slurs", "sluse", "slyer", "slype", "smaak", "smaik", "smalm", "smalt", "smarm", "smaze", "smeek", "smees", "smeik", "smeke", "smerk", "smews", "smirr", "smirs", "smits", "smogs", "smoko", "smolt", "smoor", "smoot", "smore", "smorg", "smout", "smowt", "smugs", "smurs", "smush", "smuts", "snabs", "snafu", "snags", "snaps", "snarf", "snark", "snars", "snary", "snash", "snath", "snaws", "snead", "sneap", "snebs", "sneck", "sneds", "sneed", "snees", "snell", "snibs", "snick", "snies", "snift", "snigs", "snips", "snipy", "snirt", "snits", "snobs", "snods", "snoek", "snoep", "snogs", "snoke", "snood", "snook", "snool", "snoot", "snots", "snowk", "snows", "snubs", "snugs", "snush", "snyes", "soaks", "soaps", "soare", "soars", "soave", "sobas", "socas", "soces", "socko", "socks", "socle", "sodas", "soddy", "sodic", "sodom", "sofar", "sofas", "softa", "softs", "softy", "soger", "sohur", "soils", "soily", "sojas", "sojus", "sokah", "soken", "sokes", "sokol", "solah", "solan", "solas", "solde", "soldi", "soldo", "solds", "soled", "solei", "soler", "soles", "solon", "solos", "solum", "solus", "soman", "somas", "sonce", "sonde", "sones", "songs", "sonly", "sonne", "sonny", "sonse", "sonsy", "sooey", "sooks", "sooky", "soole", "sools", "sooms", "soops", "soote", "soots", "sophs", "sophy", "sopor", "soppy", "sopra", "soral", "soras", "sorbo", "sorbs", "sorda", "sordo", "sords", "sored", "soree", "sorel", "sorer", "sores", "sorex", "sorgo", "sorns", "sorra", "sorta", "sorts", "sorus", "soths", "sotol", "souce", "souct", "sough", "souks", "souls", "soums", "soups", "soupy", "sours", "souse", "souts", "sowar", "sowce", "sowed", "sowff", "sowfs", "sowle", "sowls", "sowms", "sownd", "sowne", "sowps", "sowse", "sowth", "soyas", "soyle", "soyuz", "sozin", "spacy", "spado", "spaed", "spaer", "spaes", "spags", "spahi", "spail", "spain", "spait", "spake", "spald", "spale", "spall", "spalt", "spams", "spane", "spang", "spans", "spard", "spars", "spart", "spate", "spats", "spaul", "spawl", "spaws", "spayd", "spays", "spaza", "spazz", "speal", "spean", "speat", "specs", "spect", "speel", "speer", "speil", "speir", "speks", "speld", "spelk", "speos", "spets", "speug", "spews", "spewy", "spial", "spica", "spide", "spier", "spies", "spiff", "spifs", "spile", "spims", "spina", "spink", "spins", "spirt", "spiry", "spits", "spitz", "spivs", "splay", "splog", "spode", "spods", "spoom", "spoor", "spoot", "spork", "sposh", "spots", "sprad", "sprag", "sprat", "spred", "sprew", "sprit", "sprod", "sprog", "sprue", "sprug", "spuds", "spued", "spuer", "spues", "spugs", "spule", "spume", "spumy", "spurs", "sputa", "spyal", "spyre", "squab", "squaw", "squeg", "squid", "squit", "squiz", "stabs", "stade", "stags", "stagy", "staig", "stane", "stang", "staph", "staps", "starn", "starr", "stars", "stats", "staun", "staws", "stays", "stean", "stear", "stedd", "stede", "steds", "steek", "steem", "steen", "steil", "stela", "stele", "stell", "steme", "stems", "stend", "steno", "stens", "stent", "steps", "stept", "stere", "stets", "stews", "stewy", "steys", "stich", "stied", "sties", "stilb", "stile", "stime", "stims", "stimy", "stipa", "stipe", "stire", "stirk", "stirp", "stirs", "stive", "stivy", "stoae", "stoai", "stoas", "stoat", "stobs", "stoep", "stogy", "stoit", "stoln", "stoma", "stond", "stong", "stonk", "stonn", "stook", "stoor", "stope", "stops", "stopt", "stoss", "stots", "stott", "stoun", "stoup", "stour", "stown", "stowp", "stows", "strad", "strae", "strag", "strak", "strep", "strew", "stria", "strig", "strim", "strop", "strow", "stroy", "strum", "stubs", "stude", "studs", "stull", "stulm", "stumm", "stums", "stuns", "stupa", "stupe", "sture", "sturt", "styed", "styes", "styli", "stylo", "styme", "stymy", "styre", "styte", "subah", "subas", "subby", "suber", "subha", "succi", "sucks", "sucky", "sucre", "sudds", "sudor", "sudsy", "suede", "suent", "suers", "suete", "suets", "suety", "sugan", "sughs", "sugos", "suhur", "suids", "suint", "suits", "sujee", "sukhs", "sukuk", "sulci", "sulfa", "sulfo", "sulks", "sulph", "sulus", "sumis", "summa", "sumos", "sumph", "sumps", "sunis", "sunks", "sunna", "sunns", "sunup", "supes", "supra", "surah", "sural", "suras", "surat", "surds", "sured", "sures", "surfs", "surfy", "surgy", "surra", "sused", "suses", "susus", "sutor", "sutra", "sutta", "swabs", "swack", "swads", "swage", "swags", "swail", "swain", "swale", "swaly", "swamy", "swang", "swank", "swans", "swaps", "swapt", "sward", "sware", "swarf", "swart", "swats", "swayl", "sways", "sweal", "swede", "sweed", "sweel", "sweer", "swees", "sweir", "swelt", "swerf", "sweys", "swies", "swigs", "swile", "swims", "swink", "swipe", "swire", "swiss", "swith", "swits", "swive", "swizz", "swobs", "swole", "swoln", "swops", "swopt", "swots", "swoun", "sybbe", "sybil", "syboe", "sybow", "sycee", "syces", "sycon", "syens", "syker", "sykes", "sylis", "sylph", "sylva", "symar", "synch", "syncs", "synds", "syned", "synes", "synth", "syped", "sypes", "syphs", "syrah", "syren", "sysop", "sythe", "syver", "taals", "taata", "taber", "tabes", "tabid", "tabis", "tabla", "tabor", "tabun", "tabus", "tacan", "taces", "tacet", "tache", "tacho", "tachs", "tacks", "tacos", "tacts", "taels", "tafia", "taggy", "tagma", "tahas", "tahrs", "taiga", "taigs", "taiko", "tails", "tains", "taira", "taish", "taits", "tajes", "takas", "takes", "takhi", "takin", "takis", "takky", "talak", "talaq", "talar", "talas", "talcs", "talcy", "talea", "taler", "tales", "talks", "talky", "talls", "talma", "talpa", "taluk", "talus", "tamal", "tamed", "tames", "tamin", "tamis", "tammy", "tamps", "tanas", "tanga", "tangi", "tangs", "tanhs", "tanka", "tanks", "tanky", "tanna", "tansy", "tanti", "tanto", "tanty", "tapas", "taped", "tapen", "tapes", "tapet", "tapis", "tappa", "tapus", "taras", "tardo", "tared", "tares", "targa", "targe", "tarns", "taroc", "tarok", "taros", "tarps", "tarre", "tarry", "tarsi", "tarts", "tarty", "tasar", "tased", "taser", "tases", "tasks", "tassa", "tasse", "tasso", "tatar", "tater", "tates", "taths", "tatie", "tatou", "tatts", "tatus", "taube", "tauld", "tauon", "taupe", "tauts", "tavah", "tavas", "taver", "tawai", "tawas", "tawed", "tawer", "tawie", "tawse", "tawts", "taxed", "taxer", "taxes", "taxis", "taxol", "taxon", "taxor", "taxus", "tayra", "tazza", "tazze", "teade", "teads", "teaed", "teaks", "teals", "teams", "tears", "teats", "teaze", "techs", "techy", "tecta", "teels", "teems", "teend", "teene", "teens", "teeny", "teers", "teffs", "teggs", "tegua", "tegus", "tehrs", "teiid", "teils", "teind", "teins", "telae", "telco", "teles", "telex", "telia", "telic", "tells", "telly", "teloi", "telos", "temed", "temes", "tempi", "temps", "tempt", "temse", "tench", "tends", "tendu", "tenes", "tenge", "tenia", "tenne", "tenno", "tenny", "tenon", "tents", "tenty", "tenue", "tepal", "tepas", "tepoy", "terai", "teras", "terce", "terek", "teres", "terfe", "terfs", "terga", "terms", "terne", "terns", "terry", "terts", "tesla", "testa", "teste", "tests", "tetes", "teths", "tetra", "tetri", "teuch", "teugh", "tewed", "tewel", "tewit", "texas", "texes", "texts", "thack", "thagi", "thaim", "thale", "thali", "thana", "thane", "thang", "thans", "thanx", "tharm", "thars", "thaws", "thawy", "thebe", "theca", "theed", "theek", "thees", "thegn", "theic", "thein", "thelf", "thema", "thens", "theow", "therm", "thesp", "thete", "thews", "thewy", "thigs", "thilk", "thill", "thine", "thins", "thiol", "thirl", "thoft", "thole", "tholi", "thoro", "thorp", "thous", "thowl", "thrae", "thraw", "thrid", "thrip", "throe", "thuds", "thugs", "thuja", "thunk", "thurl", "thuya", "thymi", "thymy", "tians", "tiars", "tical", "ticca", "ticed", "tices", "tichy", "ticks", "ticky", "tiddy", "tided", "tides", "tiers", "tiffs", "tifos", "tifts", "tiges", "tigon", "tikas", "tikes", "tikis", "tikka", "tilak", "tiled", "tiler", "tiles", "tills", "tilly", "tilth", "tilts", "timbo", "timed", "times", "timon", "timps", "tinas", "tinct", "tinds", "tinea", "tined", "tines", "tinge", "tings", "tinks", "tinny", "tints", "tinty", "tipis", "tippy", "tired", "tires", "tirls", "tiros", "tirrs", "titch", "titer", "titis", "titre", "titty", "titup", "tiyin", "tiyns", "tizes", "tizzy", "toads", "toady", "toaze", "tocks", "tocky", "tocos", "todde", "toeas", "toffs", "toffy", "tofts", "tofus", "togae", "togas", "toged", "toges", "togue", "tohos", "toile", "toils", "toing", "toise", "toits", "tokay", "toked", "toker", "tokes", "tokos", "tolan", "tolar", "tolas", "toled", "toles", "tolls", "tolly", "tolts", "tolus", "tolyl", "toman", "tombs", "tomes", "tomia", "tommy", "tomos", "tondi", "tondo", "toned", "toner", "tones", "toney", "tongs", "tonka", "tonks", "tonne", "tonus", "tools", "tooms", "toons", "toots", "toped", "topee", "topek", "toper", "topes", "tophe", "tophi", "tophs", "topis", "topoi", "topos", "toppy", "toque", "torah", "toran", "toras", "torcs", "tores", "toric", "torii", "toros", "torot", "torrs", "torse", "torsi", "torsk", "torta", "torte", "torts", "tosas", "tosed", "toses", "toshy", "tossy", "toted", "toter", "totes", "totty", "touks", "touns", "tours", "touse", "tousy", "touts", "touze", "touzy", "towed", "towie", "towns", "towny", "towse", "towsy", "towts", "towze", "towzy", "toyed", "toyer", "toyon", "toyos", "tozed", "tozes", "tozie", "trabs", "trads", "tragi", "traik", "trams", "trank", "tranq", "trans", "trant", "trape", "traps", "trapt", "trass", "trats", "tratt", "trave", "trayf", "trays", "treck", "treed", "treen", "trees", "trefa", "treif", "treks", "trema", "trems", "tress", "trest", "trets", "trews", "treyf", "treys", "triac", "tride", "trier", "tries", "triff", "trigo", "trigs", "trike", "trild", "trill", "trims", "trine", "trins", "triol", "trior", "trios", "trips", "tripy", "trist", "troad", "troak", "troat", "trock", "trode", "trods", "trogs", "trois", "troke", "tromp", "trona", "tronc", "trone", "tronk", "trons", "trooz", "troth", "trots", "trows", "troys", "trued", "trues", "trugo", "trugs", "trull", "tryer", "tryke", "tryma", "tryps", "tsade", "tsadi", "tsars", "tsked", "tsuba", "tsubo", "tuans", "tuart", "tuath", "tubae", "tubar", "tubas", "tubby", "tubed", "tubes", "tucks", "tufas", "tuffe", "tuffs", "tufts", "tufty", "tugra", "tuile", "tuina", "tuism", "tuktu", "tules", "tulpa", "tulsi", "tumid", "tummy", "tumps", "tumpy", "tunas", "tunds", "tuned", "tuner", "tunes", "tungs", "tunny", "tupek", "tupik", "tuple", "tuque", "turds", "turfs", "turfy", "turks", "turme", "turms", "turns", "turnt", "turps", "turrs", "tushy", "tusks", "tusky", "tutee", "tutti", "tutty", "tutus", "tuxes", "tuyer", "twaes", "twain", "twals", "twank", "twats", "tways", "tweel", "tween", "tweep", "tweer", "twerk", "twerp", "twier", "twigs", "twill", "twilt", "twink", "twins", "twiny", "twire", "twirp", "twite", "twits", "twoer", "twyer", "tyees", "tyers", "tyiyn", "tykes", "tyler", "tymps", "tynde", "tyned", "tynes", "typal", "typed", "types", "typey", "typic", "typos", "typps", "typto", "tyran", "tyred", "tyres", "tyros", "tythe", "tzars", "udals", "udons", "ugali", "ugged", "uhlan", "uhuru", "ukase", "ulama", "ulans", "ulema", "ulmin", "ulnad", "ulnae", "ulnar", "ulnas", "ulpan", "ulvas", "ulyie", "ulzie", "umami", "umbel", "umber", "umble", "umbos", "umbre", "umiac", "umiak", "umiaq", "ummah", "ummas", "ummed", "umped", "umphs", "umpie", "umpty", "umrah", "umras", "unais", "unapt", "unarm", "unary", "unaus", "unbag", "unban", "unbar", "unbed", "unbid", "unbox", "uncap", "unces", "uncia", "uncos", "uncoy", "uncus", "undam", "undee", "undos", "undug", "uneth", "unfix", "ungag", "unget", "ungod", "ungot", "ungum", "unhat", "unhip", "unica", "units", "unjam", "unked", "unket", "unkid", "unlaw", "unlay", "unled", "unlet", "unlid", "unman", "unmew", "unmix", "unpay", "unpeg", "unpen", "unpin", "unred", "unrid", "unrig", "unrip", "unsaw", "unsay", "unsee", "unsew", "unsex", "unsod", "untax", "untin", "unwet", "unwit", "unwon", "upbow", "upbye", "updos", "updry", "upend", "upjet", "uplay", "upled", "uplit", "upped", "upran", "uprun", "upsee", "upsey", "uptak", "upter", "uptie", "uraei", "urali", "uraos", "urare", "urari", "urase", "urate", "urbex", "urbia", "urdee", "ureal", "ureas", "uredo", "ureic", "urena", "urent", "urged", "urger", "urges", "urial", "urite", "urman", "urnal", "urned", "urped", "ursae", "ursid", "urson", "urubu", "urvas", "users", "usnea", "usque", "usure", "usury", "uteri", "uveal", "uveas", "uvula", "vacua", "vaded", "vades", "vagal", "vagus", "vails", "vaire", "vairs", "vairy", "vakas", "vakil", "vales", "valis", "valse", "vamps", "vampy", "vanda", "vaned", "vanes", "vangs", "vants", "vaped", "vaper", "vapes", "varan", "varas", "vardy", "varec", "vares", "varia", "varix", "varna", "varus", "varve", "vasal", "vases", "vasts", "vasty", "vatic", "vatus", "vauch", "vaute", "vauts", "vawte", "vaxes", "veale", "veals", "vealy", "veena", "veeps", "veers", "veery", "vegas", "veges", "vegie", "vegos", "vehme", "veils", "veily", "veins", "veiny", "velar", "velds", "veldt", "veles", "vells", "velum", "venae", "venal", "vends", "vendu", "veney", "venge", "venin", "vents", "venus", "verbs", "verra", "verry", "verst", "verts", "vertu", "vespa", "vesta", "vests", "vetch", "vexed", "vexer", "vexes", "vexil", "vezir", "vials", "viand", "vibes", "vibex", "vibey", "viced", "vices", "vichy", "viers", "views", "viewy", "vifda", "viffs", "vigas", "vigia", "vilde", "viler", "villi", "vills", "vimen", "vinal", "vinas", "vinca", "vined", "viner", "vines", "vinew", "vinic", "vinos", "vints", "viold", "viols", "vired", "vireo", "vires", "virga", "virge", "virid", "virls", "virtu", "visas", "vised", "vises", "visie", "visne", "vison", "visto", "vitae", "vitas", "vitex", "vitro", "vitta", "vivas", "vivat", "vivda", "viver", "vives", "vizir", "vizor", "vleis", "vlies", "vlogs", "voars", "vocab", "voces", "voddy", "vodou", "vodun", "voema", "vogie", "voids", "voile", "voips", "volae", "volar", "voled", "voles", "volet", "volks", "volta", "volte", "volti", "volts", "volva", "volve", "vomer", "voted", "votes", "vouge", "voulu", "vowed", "vower", "voxel", "vozhd", "vraic", "vrils", "vroom", "vrous", "vrouw", "vrows", "vuggs", "vuggy", "vughs", "vughy", "vulgo", "vulns", "vulva", "vutty", "waacs", "wacke", "wacko", "wacks", "wadds", "waddy", "waded", "wader", "wades", "wadge", "wadis", "wadts", "waffs", "wafts", "waged", "wages", "wagga", "wagyu", "wahoo", "waide", "waifs", "waift", "wails", "wains", "wairs", "waite", "waits", "wakas", "waked", "waken", "waker", "wakes", "wakfs", "waldo", "walds", "waled", "waler", "wales", "walie", "walis", "walks", "walla", "walls", "wally", "walty", "wamed", "wames", "wamus", "wands", "waned", "wanes", "waney", "wangs", "wanks", "wanky", "wanle", "wanly", "wanna", "wants", "wanty", "wanze", "waqfs", "warbs", "warby", "wards", "wared", "wares", "warez", "warks", "warms", "warns", "warps", "warre", "warst", "warts", "wases", "washy", "wasms", "wasps", "waspy", "wasts", "watap", "watts", "wauff", "waugh", "wauks", "waulk", "wauls", "waurs", "waved", "waves", "wavey", "wawas", "wawes", "wawls", "waxed", "waxer", "waxes", "wayed", "wazir", "wazoo", "weald", "weals", "weamb", "weans", "wears", "webby", "weber", "wecht", "wedel", "wedgy", "weeds", "weeke", "weeks", "weels", "weems", "weens", "weeny", "weeps", "weepy", "weest", "weete", "weets", "wefte", "wefts", "weids", "weils", "weirs", "weise", "weize", "wekas", "welds", "welke", "welks", "welkt", "wells", "welly", "welts", "wembs", "wends", "wenge", "wenny", "wents", "weros", "wersh", "wests", "wetas", "wetly", "wexed", "wexes", "whamo", "whams", "whang", "whaps", "whare", "whata", "whats", "whaup", "whaur", "wheal", "whear", "wheen", "wheep", "wheft", "whelk", "whelm", "whens", "whets", "whews", "wheys", "whids", "whift", "whigs", "whilk", "whims", "whins", "whios", "whips", "whipt", "whirr", "whirs", "whish", "whiss", "whist", "whits", "whity", "whizz", "whomp", "whoof", "whoot", "whops", "whorl", "whort", "whoso", "whows", "whump", "whups", "whyda", "wicca", "wicks", "wicky", "widdy", "wides", "wiels", "wifed", "wifes", "wifey", "wifie", "wifty", "wigan", "wigga", "wiggy", "wikis", "wilco", "wilds", "wiled", "wiles", "wilga", "wilis", "wilja", "wills", "wilts", "wimps", "winds", "wined", "wines", "winey", "winge", "wings", "wingy", "winks", "winna", "winns", "winos", "winze", "wiped", "wiper", "wipes", "wired", "wirer", "wires", "wirra", "wised", "wises", "wisha", "wisht", "wisps", "wists", "witan", "wited", "wites", "withe", "withs", "withy", "wived", "wiver", "wives", "wizen", "wizes", "woads", "woald", "wocks", "wodge", "woful", "wojus", "woker", "wokka", "wolds", "wolfs", "wolly", "wolve", "wombs", "womby", "womyn", "wonga", "wongi", "wonks", "wonky", "wonts", "woods", "wooed", "woofs", "woofy", "woold", "wools", "woons", "woops", "woopy", "woose", "woosh", "wootz", "words", "works", "worms", "wormy", "worts", "wowed", "wowee", "woxen", "wrang", "wraps", "wrapt", "wrast", "wrate", "wrawl", "wrens", "wrick", "wried", "wrier", "wries", "writs", "wroke", "wroot", "wroth", "wryer", "wuddy", "wudus", "wulls", "wurst", "wuses", "wushu", "wussy", "wuxia", "wyled", "wyles", "wynds", "wynns", "wyted", "wytes", "xebec", "xenia", "xenic", "xenon", "xeric", "xerox", "xerus", "xoana", "xrays", "xylan", "xylem", "xylic", "xylol", "xylyl", "xysti", "xysts", "yaars", "yabas", "yabba", "yabby", "yacca", "yacka", "yacks", "yaffs", "yager", "yages", "yagis", "yahoo", "yaird", "yakka", "yakow", "yales", "yamen", "yampy", "yamun", "yangs", "yanks", "yapok", "yapon", "yapps", "yappy", "yarak", "yarco", "yards", "yarer", "yarfa", "yarks", "yarns", "yarrs", "yarta", "yarto", "yates", "yauds", "yauld", "yaups", "yawed", "yawey", "yawls", "yawns", "yawny", "yawps", "ybore", "yclad", "ycled", "ycond", "ydrad", "ydred", "yeads", "yeahs", "yealm", "yeans", "yeard", "years", "yecch", "yechs", "yechy", "yedes", "yeeds", "yeesh", "yeggs", "yelks", "yells", "yelms", "yelps", "yelts", "yenta", "yente", "yerba", "yerds", "yerks", "yeses", "yesks", "yests", "yesty", "yetis", "yetts", "yeuks", "yeuky", "yeven", "yeves", "yewen", "yexed", "yexes", "yfere", "yiked", "yikes", "yills", "yince", "yipes", "yippy", "yirds", "yirks", "yirrs", "yirth", "yites", "yitie", "ylems", "ylike", "ylkes", "ymolt", "ympes", "yobbo", "yobby", "yocks", "yodel", "yodhs", "yodle", "yogas", "yogee", "yoghs", "yogic", "yogin", "yogis", "yoick", "yojan", "yoked", "yokel", "yoker", "yokes", "yokul", "yolks", "yolky", "yomim", "yomps", "yonic", "yonis", "yonks", "yoofs", "yoops", "yores", "yorks", "yorps", "youks", "yourn", "yours", "yourt", "youse", "yowed", "yowes", "yowie", "yowls", "yowza", "yrapt", "yrent", "yrivd", "yrneh", "ysame", "ytost", "yuans", "yucas", "yucca", "yucch", "yucko", "yucks", "yucky", "yufts", "yugas", "yuked", "yukes", "yukky", "yukos", "yulan", "yules", "yummo", "yummy", "yumps", "yupon", "yuppy", "yurta", "yurts", "yuzus", "zabra", "zacks", "zaida", "zaidy", "zaire", "zakat", "zaman", "zambo", "zamia", "zanja", "zante", "zanza", "zanze", "zappy", "zarfs", "zaris", "zatis", "zaxes", "zayin", "zazen", "zeals", "zebec", "zebub", "zebus", "zedas", "zeins", "zendo", "zerda", "zerks", "zeros", "zests", "zetas", "zexes", "zezes", "zhomo", "zibet", "ziffs", "zigan", "zilas", "zilch", "zilla", "zills", "zimbi", "zimbs", "zinco", "zincs", "zincy", "zineb", "zines", "zings", "zingy", "zinke", "zinky", "zippo", "zippy", "ziram", "zitis", "zizel", "zizit", "zlote", "zloty", "zoaea", "zobos", "zobus", "zocco", "zoeae", "zoeal", "zoeas", "zoism", "zoist", "zombi", "zonae", "zonda", "zoned", "zoner", "zones", "zonks", "zooea", "zooey", "zooid", "zooks", "zooms", "zoons", "zooty", "zoppa", "zoppo", "zoril", "zoris", "zorro", "zouks", "zowee", "zowie", "zulus", "zupan", "zupas", "zuppa", "zurfs", "zuzim", "zygal", "zygon", "zymes", "zymic"]

# guessList = guessList.concat(wordList);

# var word = wordList[Math.floor(Math.random() * wordList.length)].toUpperCase();
# console.log(word);

# window.onload = function() {
#     intialize();
# }

# function intialize() {

#     // Create the game board
#     for (let r = 0; r < height; r++) {
#         for (let c = 0; c < width; c++) {
#             // <span id="0-0" class="tile">P</span>
#             let tile = document.createElement("span");
#             tile.id = r.toString() + "-" + c.toString();
#             tile.classList.add("tile");
#             tile.innerText = "";
#             document.getElementById("board").appendChild(tile);
#         }
#     }

#     // Create the key board
#     let keyboard = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"], ["A", "S", "D", "F", "G", "H", "J", "K", "L", " "], ["Enter", "Z", "X", "C", "V", "B", "N", "M", "⌫"]]

#     for (let i = 0; i < keyboard.length; i++) {
#         let currRow = keyboard[i];
#         let keyboardRow = document.createElement("div");
#         keyboardRow.classList.add("keyboard-row");

#         for (let j = 0; j < currRow.length; j++) {
#             let keyTile = document.createElement("div");

#             let key = currRow[j];
#             keyTile.innerText = key;
#             if (key == "Enter") {
#                 keyTile.id = "Enter";
#             } else if (key == "⌫") {
#                 keyTile.id = "Backspace";
#             } else if ("A" <= key && key <= "Z") {
#                 keyTile.id = "Key" + key;
#                 // "Key" + "A";
#             }

#             keyTile.addEventListener("click", processKey);

#             if (key == "Enter") {
#                 keyTile.classList.add("enter-key-tile");
#             } else {
#                 keyTile.classList.add("key-tile");
#             }
#             keyboardRow.appendChild(keyTile);
#         }
#         document.body.appendChild(keyboardRow);
#     }

#     // Listen for Key Press
#     document.addEventListener("keyup", (e)=>{
#         processInput(e);
#     }
#     )
# }

# function processKey() {
#     e = {
#         "code": this.id
#     };
#     processInput(e);
# }

# function processInput(e) {
#     if (gameOver)
#         return;

#     // alert(e.code);
#     if ("KeyA" <= e.code && e.code <= "KeyZ") {
#         if (col < width) {
#             let currTile = document.getElementById(row.toString() + '-' + col.toString());
#             if (currTile.innerText == "") {
#                 currTile.innerText = e.code[3];
#                 col += 1;
#             }
#         }
#     } else if (e.code == "Backspace") {
#         if (0 < col && col <= width) {
#             col -= 1;
#         }
#         let currTile = document.getElementById(row.toString() + '-' + col.toString());
#         currTile.innerText = "";
#     }
#     else if (e.code == "Enter") {
#         update();
#     }

#     if (!gameOver && row == height) {
#         gameOver = true;
#         document.getElementById("answer").innerText = word;
#     }
# }

# function update() {
#     let guess = "";
#     document.getElementById("answer").innerText = "";

#     //string up the guesses into the word
#     for (let c = 0; c < width; c++) {
#         let currTile = document.getElementById(row.toString() + '-' + c.toString());
#         let letter = currTile.innerText;
#         guess += letter;
#     }

#     guess = guess.toLowerCase();
#     //case sensitive
#     console.log(guess);

#     if (!guessList.includes(guess)) {
#         document.getElementById("answer").innerText = "Not in word list";
#         return;
#     }

#     //start processing guess
#     let correct = 0;

#     let letterCount = {};
#     //keep track of letter frequency, ex) KENNY -> {K:1, E:1, N:2, Y: 1}
#     for (let i = 0; i < word.length; i++) {
#         let letter = word[i];

#         if (letterCount[letter]) {
#             letterCount[letter] += 1;
#         } else {
#             letterCount[letter] = 1;
#         }
#     }

#     console.log(letterCount);

#     //first iteration, check all the correct ones first
#     for (let c = 0; c < width; c++) {
#         let currTile = document.getElementById(row.toString() + '-' + c.toString());
#         let letter = currTile.innerText;

#         //Is it in the correct position?
#         if (word[c] == letter) {
#             currTile.classList.add("correct");

#             let keyTile = document.getElementById("Key" + letter);
#             keyTile.classList.remove("present");
#             keyTile.classList.add("correct");

#             correct += 1;
#             letterCount[letter] -= 1;
#             //deduct the letter count
#         }

#         if (correct == width) {
#             gameOver = true;
#         }
#     }

#     console.log(letterCount);
#     //go again and mark which ones are present but in wrong position
#     for (let c = 0; c < width; c++) {
#         let currTile = document.getElementById(row.toString() + '-' + c.toString());
#         let letter = currTile.innerText;

#         // skip the letter if it has been marked correct
#         if (!currTile.classList.contains("correct")) {
#             //Is it in the word?         //make sure we don't double count
#             if (word.includes(letter) && letterCount[letter] > 0) {
#                 currTile.classList.add("present");

#                 let keyTile = document.getElementById("Key" + letter);
#                 if (!keyTile.classList.contains("correct")) {
#                     keyTile.classList.add("present");
#                 }
#                 letterCount[letter] -= 1;
#             }// Not in the word or (was in word but letters all used up to avoid overcount)
#             else {
#                 currTile.classList.add("absent");
#                 let keyTile = document.getElementById("Key" + letter);
#                 keyTile.classList.add("absent")
#             }
#         }
#     }

#     row += 1;
#     //start new row
#     col = 0;
#     //start at 0 for new row
# }




# body {
#     font-family: Arial, Helvetica, sans-serif;
#     text-align: center;
# }

# hr {
#     width: 500px;
# }

# #title {
#     font-size: 36px;
#     font-weight: bold;
#     letter-spacing: 2px;
# }

# #board {
#     width: 350px;
#     height: 420px;
#     margin: 0 auto;
#     margin-top: 3px;
#     display: flex;
#     flex-wrap: wrap;
# }

# .tile {
#     /* Box */
#     border: 2px solid lightgray;
#     width: 60px;
#     height: 60px;
#     margin: 2.5px;

#     /* Text */
#     color: black;
#     font-size: 36px;
#     font-weight: bold;
#     display: flex;
#     justify-content: center;
#     align-items: center;
# }

# .correct {
#     background-color: #6AAA64;
#     color: white;
#     border-color: white;
# }

# .present {
#     background-color: #C9B458;
#     color: white;
#     border-color: white;
# }

# .absent {
#     background-color: #787C7E;
#     color: white;
#     border-color:white;
# }


# .keyboard-row {
#     width: 400px;

#     margin: 0 auto;
#     display: flex;
#     flex-wrap: wrap;
# }

# .key-tile {
#     width: 36px;
#     height: 40px;
#     margin: 1px;
#     border: 1px solid lightgray;

#     /* Text */
#     font-size: 20px;
#     font-weight: bold;
#     display: flex;
#     justify-content: center;
#     align-items: center;
# }

# .enter-key-tile {
#     width: 76px;
#     height: 40px;
#     margin: 1px;
#     border: 1px solid lightgray;

#     /* Text */
#     font-size: 20px;
#     font-weight: bold;
#     display: flex;
#     justify-content: center;
#     align-items: center;
# }

            
            else :
                print('wrong game selected')
                speak('wrong game selected')







        else:    
             print ('i dont have specific functions for it,so i am just going to search the web for it ')
             
             speak ('i dont have specific functions for it, so i am just going to search the web for it ')
             print (search_wikipedia(query)) 
             
             
             speak (search_wikipedia(query))
             
             
             if 'No page found' in (search_wikipedia(query)):
                 speak('Soory it looks like I wont be able to help you with that but you can submit your feedback and we will fix it as soon as possible')
                 print('Soory it looks like I wont be able to help you with that but you can submit your feedback and we will fix it as soon as possible')

            



       





print('thansk for using me,Good bye')
speak('thanks for using me, Good bye')








        







                                                #End
#End
#End
#End
#End
#End
#End
#End
#End
#End
#End
            #End


     

