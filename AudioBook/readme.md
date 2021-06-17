# How to use - PDF to AudioBook converter.

## Explicação do código
<hr>

Para preparar o ambiente, certifique-se de ter o python instalado e execute no prompt de comando o comando abaixo para instalar as bibliotecas utilizadas:

```
pip install pyttsx3 pdfplumber PyPDF2
```

## Explicação do código
<hr>

Importando bibliotecas:
```
import pyttsx3
import pdfplumber
import PyPDF2
```

Nome do pdf e localização. No caso abaixo, o arquivo está na pasta do audioBook.py:
```
file = 'ApostilaPOO.pdf'
```

Criando o objeto arquivo PDF:
```
pdfFileObj = open(file, 'rb')
```

Criando leitor do arquivo PDF:
```
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
```

Passando o numero de páginas:
```
pages = pdfReader.numPages
```

Criando objeto pdfplumber + loop do numero de paginas para o computador ler pagina por pagina: 
```
with pdfplumber.open(file) as pdf:
```
Loop das paginas:
```
for i in range(0, pages):
    page = pdf.pages[i]
    text = page.extract_text()
    print(text)
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()
```

## OBS:
<hr>

* Em ``` for i in range(0,pages) ``` o numero 0 representa a pagina que o leitor irá começar. No programa audioBook.py nesse repositório optei por putar o indice e comecei na página 2.

* A linha ``` print(text)``` é opcional: Caso queira ver o texto que será falado apenas.
