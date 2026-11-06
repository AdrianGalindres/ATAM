import time
import requests
import concurrent.futures
import pandas as pd
import os

# URL de tu endpoint en NestJS
URL = "http://localhost:3000/auth/register"
TOTAL_REQUESTS = 50       # Número de pruebas simuladas
CONCURRENCY = 10          # Hilos concurrentes simultáneos
LATENCY_THRESHOLD_MS = 500 # Umbral definido en el Árbol de Utilidad

def test_single_registration(index):
    # Generar un correo único para evitar conflictos de duplicidad en Supabase
    unique_email = f"architect_student_{index}_{int(time.time())}@test.com"
    payload = {
        "email": unique_email,
        "pass": "StrongPassword123!"
    }
    
    start_time = time.time()
    try:
        response = requests.post(URL, json=payload, timeout=5)
        duration_ms = (time.time() - start_time) * 1000
        
        success = response.status_code == 201 and duration_ms < LATENCY_THRESHOLD_MS
        return {
            "index": index,
            "success": success,
            "duration": duration_ms,
            "status": response.status_code
        }
    except Exception as e:
        return {
            "index": index,
            "success": False,
            "duration": 0,
            "error": str(e)
        }

def run_atam_evaluation():
    print("=" * 60)
    print("EJECUTANDO EVALUACIÓN ATAM: ESCENARIO DE RENDIMIENTO")
    print("=" * 60)
    print(f"[*] Destino: {URL}")
    print(f"[*] Criterio: {TOTAL_REQUESTS} peticiones con concurrencia de {CONCURRENCY}")
    print(f"[*] Umbral de Aceptación: < {LATENCY_THRESHOLD_MS}ms\n")

    results = []
    start_global = time.time()

    # Ejecutar peticiones concurrentes usando Python ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        futures = [executor.submit(test_single_registration, i) for i in range(TOTAL_REQUESTS)]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    total_time = time.time() - start_global
    successful_requests = sum(1 for r in results if r['success'])
    valid_durations = [r['duration'] for r in results if r['duration'] > 0]
    avg_duration = sum(valid_durations) / len(valid_durations) if valid_durations else 0

    print("\n" + "=" * 60)
    print("RESULTADOS FINALES DE LA EVALUACIÓN")
    print("=" * 60)
    print(f"Peticiones Totales: {TOTAL_REQUESTS}")
    print(f"Peticiones Exitosas bajo el umbral: {successful_requests}/{TOTAL_REQUESTS}")
    print(f"Tasa de cumplimiento del Escenario: {(successful_requests / TOTAL_REQUESTS) * 100:.2f}%")
    print(f"Latencia Promedio: {avg_duration:.2f}ms")
    print(f"Tiempo Total de la Prueba: {total_time:.2f}s")

    # Veredicto de Arquitectura
    if (successful_requests / TOTAL_REQUESTS) >= 0.90:
        print("\n[+] VEREDICTO ATAM: La arquitectura PASA la evaluación de rendimiento.")
    else:
        print("\n[!] VEREDICTO ATAM: RIESGO ARQUITECTÓNICO DETECTADO. El sistema no cumple con el nivel de servicio esperado bajo carga.")

if __name__ == "__main__":
    run_atam_evaluation()

os.makedirs("evaluation/metrics", exist_ok=True)
df_results = pd.DataFrame(results)
df_results.to_csv("evaluation/metrics/raw_results.csv", index=False)
print("[+] Datos de rendimiento exportados exitosamente a 'evaluation/metrics/raw_results.csv'")
