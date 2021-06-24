#Translate documents

#Descobrir as linguagens possíveis de se traduzir
#import googletrans
#print(googletrans.LANGUAGES)

from googletrans import Translator

#texto a ser traduzido
text ='''
En apprentissage supervisé, l’algorithme d’apprentissage automatique trouve son fonctionnement dans le fait que la machine
possède dès le lancement de son apprentissage des données en entrée et en sortie déjà définies. Ainsi, l’algorithme sera en capacité
d’étudier ces exemples, de les comprendre et d’ainsi élaborer un modèle de prédictions capable ensuite de traiter les nouvelles données.
'''

translator = Translator()

#detectando o idioma do texto:
textLanguage = translator.detect(text)
print(textLanguage)

translation = translator.translate(text, dest='pt')
print(translation.text)
