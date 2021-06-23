## Coolest projects

- [Estimate Pi](https://github.com/dsperax/python/tree/main/estimate_pi(n))
- [Find your password](https://github.com/dsperax/python/tree/main/PDF%20unlock)
- [AudioBook generator](https://github.com/dsperax/python/tree/main/AudioBook)

<hr>

### Python -> .exe

1- Vá no terminal do windows e digite 

```
python -m pip install pyinstaller
```
2- Você precisa ir até o diretório que o arquivos está contido pelo cmd, para isso execute o comando:

cd [endereço do diretorio] ex: cd c:\projeto\

3- Execute o comando: 

```
pyinstalller --onefile --windowed --ico = [endereço do icone] [nome do arquivo.py]

Ex:

pyinstalller --onefile --windowed --ico = c:\desktop\teste.ico exemplo.py
```

--onefile: cria o arquivo .exe em um único arquivo
--windowed: faz o terminal sumir quando o programa ser iniciado (opcional)
--ico =: Escolher o icone que será utilizado no seu programa (opcional)
