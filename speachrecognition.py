import speech_recognition as sr
import pyttsx3
 
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speechpip
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    print(str(command))
    engine.say(command)
    engine.runAndWait()

def get_text(text):
    info = []
    words = text.split() 
    for i in words:
        for i, item in enumerate(words):
            if item == "me":
                try:
                    for y in range(3):
                        info.append(words[i+2+y])
                        new_string = " ".join(words[i + 2:i + 5])
                        print(new_string)
                        return(new_string)
                except:
                    print("error but:  " + info)
                    return(info)
     
     
# Loop infinitely for user to
# speak
def passive_listen():
    while(1):   
        
        # Exception handling to handle
        # exceptions at the runtime
        try:
            
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                recieved_text = r.recognize_google(audio2)
                recieved_text = recieved_text.lower()
    
                print("Did you say ",recieved_text)

                if "hey robot" in recieved_text:
                    SpeakText("Who can I help you riz?")
                    audio_information = r.listen(source2)
                    info_text = r.recognize_google(audio_information)

                    if "help me" in info_text:
                        name_info = get_text(info_text)
                        return (name_info)
                    else:
                        print("Error Try Again")

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")

passive_listen()