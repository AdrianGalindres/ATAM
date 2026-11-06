import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_latency_chart():
    csv_path = "evaluation/metrics/raw_results.csv"
    
    if not os.path.exists(csv_path):
        print(f"[!] No se encontró el archivo de datos en {csv_path}. Ejecuta primero el test de rendimiento.")
        return

    print("[*] Leyendo datos de rendimiento para generar la gráfica arquitectónica...")
    df = pd.read_csv(csv_path)

    # Filtrar solo las peticiones válidas con duración mayor a 0
    valid_data = df[df['duration'] > 0]

    # Configurar la gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(valid_data.index, valid_data['duration'], marker='o', linestyle='-', color='b', label='Latencia por Petición (ms)')
    
    # Línea de umbral definida en el Árbol de Utilidad (500ms)
    plt.axhline(y=500, color='r', linestyle='--', label='Umbral ATAM Máximo (500ms)')

    plt.title('Evaluación ATAM: Comportamiento de Latencia bajo Concurrencia')
    plt.xlabel('Número de Petición')
    plt.ylabel('Tiempo de Respuesta (ms)')
    plt.legend()
    plt.grid(True)

    # Guardar la gráfica como imagen
    output_image = "evaluation/metrics/atam_latency_chart.png"
    plt.savefig(output_image)
    print(f"[+] Gráfica de arquitectura generada y guardada exitosamente en: {output_image}")
    
    # Mostrar la ventana de la gráfica (opcional si estás en entorno con interfaz)
    plt.show()

if __name__ == "__main__":
    generate_latency_chart()
