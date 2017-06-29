import numpy as np
from sklearn import preprocessing

# Exemplo de rótulos
labels = np.array([1,5,3,2,1,4,2,1,3])

# Crie o codificador
lb = preprocessing.LabelBinarizer()

# O codificador encontra as classes e cria os vetores codificados em binário
lb.fit(labels)

# Finalmente, os rótulos são transformados em vetores conectados em binário
lb.transform(labels)
