# assistente de voz
import pyttsx3
import speech_recognition as sr

# criando a função take_commands() podemos capiturar
# audios, reconhecer e retornar se não tiver erros
def take_commands():
    # inicializa o speech_recognition
    r = sr.Recognizer()
    # abre o microfone do computador
    with sr.Microphone() as source:
        print('Estou pronto! Vamos conversar?...')
        r.pause_threshold = 0.7
        # armazena o som para variável de audio
        audio = r.listen(source)
        try:
            print("Reconhecendo...")
            # reconhece audio usando api do google
            Query = r.recognize_google(audio, language="pt-BR")
            print("Imprimindo consulta='", Query, "'")
        except Exception as e:
            print(e)
            print("Desculpe, não entendi. Fale novamente...")
            # retorna "None" se não tem erros
            return "None"
    # retorna audio como texto
    return Query

# criando função Speak() para dar poder de fala ao jarvinho
def Speak(audio):
    # inicializa o pyttsx3
    engine = pyttsx3.init()
    # o que for passado dentro de engine.say(),
    # será falado pelo jarvinho
    engine.say(audio)
    engine.runAndWait()

# driver
if __name__ == '__main__':
    # usando o while para comunicar infinitamente
    while True:
        command = take_commands()
        if "sair" in command:
            Speak("Até mais!")
            break
        if "Oi" in command:
            Speak("Oi! Meu nome é Jarvinho!")
        if "melhor Vingador" in command:
            Speak("Essa é fácil... É o Homem de ferro!")