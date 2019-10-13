### Cargando librerías

import glob
import numpy as np
import pandas as pd
from stop_words import get_stop_words
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


### Creando el Corpus

direccion = "*.txt"
corpus = []
textos = glob.glob(direccion)
for t in textos:
    f = open(t, 'r', encoding = 'UTF-8')
    corpus.append(f.read())


### Definir stop-words

stop_words_spanish = get_stop_words('spanish')


### Vectorizar y normalizar el Corpus

vectorizer = TfidfVectorizer(lowercase = True,
							 # stop_words = stop_words_spanish,
							 norm = 'l2',
							 use_idf = True,
							 smooth_idf = True,
							 encoding = 'UTF-8',
							 analyzer = 'word',
							 sublinear_tf = True,
							 binary = True,
							 ngram_range = (1, 3)
							 )
X_corpus = vectorizer.fit_transform(corpus)

print('La dimension del corpus es: ', X_corpus.shape)


### Calculando matriz de similitud

sim = cosine_similarity(X_corpus, None)


### Dejar en 0 la diagonal de la matriz 

n = sim.shape[0]
sim[range(n), range(n)] = 0


### Obtener valores máximos por cada fila

maximos = np.max(sim, axis = 1)
indices_maximos = np.argmax(sim, axis = 1)
textos_array = np.array(textos)
textos_array_maximos = textos_array[indices_maximos]


### Generar dataframe

estructura_df = {'archivo_1': textos_array, 'archivo_2': textos_array_maximos, 'similitud': maximos}
resultados = pd.DataFrame(data = estructura_df)


### Generar archivo similitud.txt
resultados_sin_similitud_txt = resultados[resultados['archivo_1'] != 'similitud.txt']
print(resultados_sin_similitud_txt)
resultados_finales = resultados_sin_similitud_txt.values
np.savetxt('similitud.txt', resultados_finales, delimiter="  ", fmt="%s")