import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#Parametros variables
st.sidebar.title("Trayectoria balistica de una pelota")
# La velocidad inicial maxima es de casi 40 m/seg
V = st.sidebar.slider('Varie la velocidad inicial (m/s): ',10, 40)
ang = st.sidebar.slider('Varie el angulo de salida (grados): ',10, 40)
opcion = st.sidebar.radio('Varie la gravedad: ',['Tierra','Marte'])
if(opcion == 'Marte'):
    g = 3.7 
else:
    g = 9.8

# Parametros fijos
M = 2  # Masa en kg
Cd = 0.25  # Coeficiente de resistencia del aire 
dt = 0.05  # Intervalo de tiempo en segundos

# Crear listas vacias
t = [0]
x = [0]
y = [0]
# Inicializar la velocidad en x e y para t = 0
vx = [V * np.cos(ang / 180 * np.pi)]
vy = [V * np.sin(ang / 180 * np.pi)]

# Resistencia del aire
drag = Cd * V ** 2

# Aceleracion en x e y
ax = [-(drag * np.cos(ang / 180 * np.pi)) / M]
ay = [-g - (drag * np.sin(ang / 180 * np.pi) / M)]

# Aproximacion numerica por Euler
counter = 0
while (y[counter] >= 0) :  
    t.append(t[counter] + dt) 

    # Actualizar velocidad
    vx.append(vx[counter] + dt * ax[counter])
    vy.append(vy[counter] + dt * ay[counter])

    # Actualizar posicion
    x.append(x[counter] + dt * vx[counter])
    y.append(y[counter] + dt * vy[counter])

    #  Recalcular la resistencia y la aceleracion
    vel = np.sqrt(vx[counter + 1] ** 2 + vy[counter + 1] ** 2)  
    drag = Cd * vel ** 2  # drag force
    ax.append(-(drag * np.cos(ang / 180 * np.pi)) / M)
    ay.append(-g - (drag * np.sin(ang / 180 * np.pi) / M))

    counter = counter + 1

# Graficar la trayectoria
#ylabel=plt.ylabel("Altura (m)")
#xlabel=plt.xlabel("Distancia (m)")
fig, ax = plt.subplots()
ax.plot(x,y)
st.pyplot(fig)
