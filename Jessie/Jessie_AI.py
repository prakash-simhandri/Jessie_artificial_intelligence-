import datetime,time 
import speech_recognition as sr # sudo pip3 install SpeechRecognition % sudo pip3 install SpeechRecognition OR sudo apt-get install python-pyaudio python3-pyaudio 
import wikipedia,random         # sudo pip3 install wikipedia
import webbrowser,os,wolframalpha # sudo pip3 install wolframalpha
from playsound import playsound # sudo pip3 install playsound
from gtts import gTTS

client = wolframalpha.Client('') # you Fill up the your wolfromAlpha Id .

def speech(Text):
    tts = gTTS(text=audio, lang='en')
    tts.save("jessie.mp3")
    playsound("jessie.mp3")

def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("jessie.mp3")
    playsound("jessie.mp3")

def greetMe(hour):  
    if hour >= 0 and hour <=12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak('Good Evneing Sir!')
    speak('I am,Jessie')
    time.sleep(1)

def user_command():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)# listen for 1 second to calibrate the energy threshold for ambient noise levels
        print('Speak Anytgibg :) ')
        audio = mic.listen(source)

        # recognize speech using Google Speech Recognition

        try:
            text = mic.recognize_google(audio,language="en-in")
            print("Ok Sir , please wait")
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize your voice")
            return "Nothing"
        return text

if __name__ == "__main__":
    greetMe(int(datetime.datetime.now().hour))
    user_name = "Sir"
    while True:
        speak('Please tell me! How can i help you')
        query = user_command().lower()


        # Work on what the user asked.
        if 'wikipedia' in query:
            try:
                speak("Searching Wikipedia....")
                query = query.replace("wikipedia","")
                W_details = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(W_details)
                speech(W_details)
                time.sleep(5)
            except Exception as err:
                print('error: '+str(err))
                speech('error '+str(err))
                time.sleep(3)

        elif 'open youtube' in query:
            speak("ok "+user_name)
            webbrowser.open('https://www.youtube.com/')
            speak('please wait')
            time.sleep(5)

        elif 'open zoho' in query:
            speak("ok "+user_name)
            webbrowser.open('https://cliq.zoho.com/index.do')
            speak('please wait')
            time.sleep(6)
            
        elif 'open toggl' in query:
            speak("ok "+user_name)
            webbrowser.open('https://toggl.com/')
            speak('please wait')
            time.sleep(5)

        elif 'open saral' in query:
            speak("ok "+user_name)
            webbrowser.open('http://saral.navgurukul.org/home')
            speak('please wait')
            time.sleep(5)

        elif 'open saavn' in query:
            speak("ok "+user_name)
            webbrowser.open('https://www.jiosaavn.com')
            speak('please wait')
            time.sleep(5)

        elif 'open google' in query:
            speak("ok "+user_name)
            webbrowser.open('https://www.google.com/')
            speak('please wait')
            time.sleep(5)

        elif 'open facebook' in query:
            speak('Ok '+user_name)
            webbrowser.open('https://www.facebook.com/')
            speak('please wait')
            time.sleep(5)
        
        elif 'play the music' in query or 'play the song' in query:
            try:
                music_data = '/home/pandu/Music/Englesh_songs'
                songs = os.listdir(music_data)
                one_song = random.choice(songs)
                speak('Ok %s! Enjoy the Music'%(user_name))
                print('The song is running.')
                playsound("/home/pandu/Music/Englesh_songs/"+one_song)
            except Exception as err:
                print('error: '+str(err))
                speech('error '+str(err))
                time.sleep(3)

        elif 'hindi music list' in query or 'hindi songs list' in query:
            speak('ok %s. Choose the number! of your song'%(user_name))
            All_songs = "/home/pandu/Music/hindi"
            songs_list = os.listdir(All_songs)
            conting = 1
            for M_list in songs_list:
                print(str(conting)+'} '+M_list,"\n")
                conting+=1
            time.sleep(2)
            speak('How much time will you choose the song')
            user_time_minten = user_command().lower()
            user_time_minten = user_time_minten.replace("in","")
            user_time_minten = user_time_minten.replace('mute',"")
            user_time_minten = user_time_minten.replace("minute","")
            timeing = user_time_minten.split()
            print(timeing)                       
            try:
                meinten=int(timeing[0])
                speak("Ok,{}! I am waiting {} minutes".format(user_name,meinten))
                time.sleep(60*meinten)
                speak('please tell me song number')
                user_music_choes = user_command().lower()

            except Exception as err:
                print('error: '+str(err))
                speech('error '+str(err))
                time.sleep(3)

            try:      
                one_song = songs_list[int(user_music_choes)-1]
                speak('Ok %s! Enjoy the Music'%(user_name))
                print('The song is running.')
                playsound('/home/pandu/Music/hindi/'+one_song)

            except Exception as err:
                print("error: "+str(err))
                speech("error "+str(err))
                time.sleep(3)
            
        
        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H! Hour %M! Minute %S! Seconds "+user_name)
            speak(Time)
            time.sleep(3)


        elif 'weather' in query:
            try:
                query = query.replace("tell me","")
                query = query.replace('weather','')
                speak('Ok,%s! please wait'%(user_name))
                user_Aask =  ('weather forecast in '+query+', india')
                res = client.query(user_Aask)
                output = next(res.results).text
                print(output)
                time.sleep(4)
            except Exception as err:
                print("error: "+str(err))
                speech("error "+str(err))
                time.sleep(3)

        elif "who made you" in query or "created you" in query:
            speak("I have been created by prakash simhandri.")


        elif 'what are you doing' in query:
            Jessie_answer=['Just! remembering you.','i am waiting for you. ',
            'i am doing,some work.','Nothing',
            'i am talking with you. ','I am thinking something new.',
            'i am,wondering with my,friend.','I am trying, to learn, something new.']
            speak(random.choice(Jessie_answer))
            time.sleep(3)


        elif 'i love you' in query:
            speak(random.choice(['I love you to!'+user_name+'.',"i am sorry! i have boyfriend."]))


        elif 'please wait some time' in query:
            speak('How many! take the,time %s.'%(user_name))
            time_minten = user_command().lower()
            time_minten = time_minten.replace("in","")
            time_minten = time_minten.replace('mute',"")
            time_minten = time_minten.replace("minute","")
            timeing = time_minten.split()
            print(timeing)  
            try:
                meinten=int(timeing[0])
                speak("Ok,{} I am waiting {} minutes".format(user_name,meinten))
                time.sleep(60*meinten)

            except Exception as err:
                print('error: '+str(err))
                speech('error '+str(err))
                time.sleep(3)

        elif 'hello madame' in query or 'hello' in query:
            speak('yes Sir')
            speak('How canI, hellp you')
        
        elif 'who are you' in query or 'what is your name' in query:
            speak('i am jessie what, is a your name')
            user_Name = user_command().lower()
            user_Name = user_Name.replace("my name is","")
            user_name = user_Name.replace('i am','')
            speak('OK,%s'%(user_name))


        else:
            if 'quit' in query:
                speak('nice to meet you %s!'%(user_name))
                time.sleep(1)
                speak('good bye and Thank you') 
                break

            elif 'nothing' in query:
                speak('Sorry %s! I could not hear your voice'%(user_name))
                time.sleep(2)

            else:
                speak(random.choice(['Sorry: These word, are not in my Data,base.','Sorry '+user_name+'! i am not understand, What are you saying.']))
                time.sleep(2)     

