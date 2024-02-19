# importamos librerias
import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, -14, 32, 46, 59, 72, 100], dtype=float)

# usamos keras pq nos ayuda a hacer redes neuronales mas facilmente
capa = tf.keras.layers.Dense(units = 1, input_shape = [1])   # capa de tipo densa (todas las neuronas de una capa con todas las neuronas de la otra capa) units - capa_salida / input_shape - capa_entrada
modelo = tf.keras.Sequential([capa]) # modelo sequecial (modelo simple)

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),   # optimizador (tasa de aprendizaje - ajusta los sesgos y pesos en acorde para mejorar la precision) menos es mas lento, mas es mas rapido pero menos preciso
    loss = 'mean_squarred_error' # funcion de perdida - error cuadratico medio. considera q una poca cantidad de errores grandes es peor q una gran cantidad de errores pequeños
)

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs = 1000, verbose = False)  # fit(entrada, salida, vueltas/intentos) cada vuelta revisa todos los datos una sola vez
print("Modelo entrenado!")