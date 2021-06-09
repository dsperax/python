import pyttsx3
import os
engine = pyttsx3.init()
pyttsx3.speak("Digite o numero referente a aplicação e aperte enter para abri-la")
while True:
    print("Digite o numero referente a aplicação e aperte enter para abri-la")
    print("\n 1. MS WORD \n 2. MS POWERPOINT \n 3. MS EXCEL \n 4. CHROME \n 0. EXIT")

    p = input()
    p = p.upper()
    pyttsx3.speak(f"você digitou o numero {p}")

    if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p) or ("NÃO" in p) or ("NO" in p) or ("N" in p):
        pyttsx3.speak("tente novamente")
        print(".")
        print(".")
        continue

    elif ("1" in p):
        pyttsx3.speak("abrindo o microsoft word")
        os.system("start winword")

    elif ("2" in p):
        pyttsx3.speak("abrindo o microsoft powerpoint")
        os.system("start powerpoint")

    elif ("3" in p):
        pyttsx3.speak("abrindo o microsoft excel")
        os.system("start excel")

    elif ("4" in p):
        pyttsx3.speak("abrindo o google chrome")
        os.system("start chrome")

    elif ("0" in p):
        pyttsx3.speak("até a próxima")
        break
    
    else:
        pyttsx3.speak(p)
        print("Inválido, tente novamente")
        pyttsx3.speak("Inválido, tente novamente")