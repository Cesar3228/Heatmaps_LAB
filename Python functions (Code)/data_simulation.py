import numpy as np
import pandas as pd

def simulate_mouse_data(duration=300, timestep=0.2, start_x=280, start_y=250):
    """
    Simula los datos del movimiento de un ratón en un laberinto en cruz.
    
    
    Argumentos:
        duration (float): Duración total de la simulación en segundos.
        timestep (float): Intervalo de tiempo entre cada medición en segundos.
        start_x (int): Posición inicial en el eje X.
        start_y (int): Posición inicial en el eje Y.
    
    Returns:
        pd.DataFrame: DataFrame con columnas "Time", "Centre position X", "Centre position Y".
    """
    
    # Generar el rango de tiempo, desde 0 hasta `duration` con intervalos de `timestep`
    times = np.arange(0, duration, timestep)
    
    # Inicializar listas para las posiciones de X e Y
    x_positions = [start_x]
    y_positions = [start_y]
    
    # Simulación del movimiento del ratón
    for _ in times[1:]:
        # Las variaciones en X e Y son pequeños movimientos aleatorios
        delta_x = np.random.randint(-3, 4)  # Movimiento aleatorio en X (-3 a 3)
        delta_y = np.random.randint(-3, 4)  # Movimiento aleatorio en Y (-3 a 3)
        
        # Agregar estas variaciones a la última posición registrada
        new_x = x_positions[-1] + delta_x
        new_y = y_positions[-1] + delta_y
        
        # Asegurarse de que las posiciones no caigan por debajo de ciertos límites si es necesario (e.g., límites del laberinto)
        new_x = max(0, new_x)  # Limitar X a no ser menor que 0
        new_y = max(0, new_y)  # Limitar Y a no ser menor que 0
        
        # Añadir las nuevas posiciones a las listas
        x_positions.append(new_x)
        y_positions.append(new_y)
    
    # Crear el DataFrame con los tiempos y posiciones
    data = {
        "Time": times,
        "Centre position X": x_positions,
        "Centre position Y": y_positions
    }
    
    df = pd.DataFrame(data)
    
    return df

# Ejecutar la simulación y mostrar los primeros resultados
df_simulation = simulate_mouse_data(duration=300, timestep=0.2)
print(df_simulation.head())

# Exportar a CSV si es necesario
df_simulation.to_csv("simulated_mouse_data.csv", index=False)