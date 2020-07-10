import coffeehouse_languagedetection.cld

en_text = "Hello World! This is an example of a large text paragraph. There is nothing interesting about this " \
          "content. It will be used used to accurately predict the language input. "

es_text = "Hola Mundo! Este es un ejemplo de un parrafo de texto grande. No hay nada interesante sobre este " \
          "contenido. Se utilizara para predecir con precision la entrada del idioma. "

print(en_text)
print(coffeehouse_languagedetection.cld.identify_language(en_text))
print(coffeehouse_languagedetection.cld.predict_probabilities(en_text))
print("\n\n")

print(es_text)
print(coffeehouse_languagedetection.cld.identify_language(es_text))
print(coffeehouse_languagedetection.cld.predict_probabilities(es_text))