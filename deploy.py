import requests
import sys
import os  

STAGING_HEALTH_URL = "http://localhost:8001/health"
SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key")
print("=== INICIANDO PIPELINE DE DESPLIEGUE CONTINUO (CD)===")
print(f"=== VERIFICANDO CREDEANCIALES INYECTADAS... TOKEN: {SECRET_KEY} ===")
print(f"=== EJECUTANDO SMOKE TEST EN STAGING: {STAGING_HEALTH_URL} ===")

try:
    res = requests.get(STAGING_HEALTH_URL, timeout=3)
    if res.status_code == 200:
        print("=== SMOKE TEST EXITOSO: STAGING HEALTHY ===")
        print("=== DESPLIEGUE A PRODUCCIÓN AUTORIZADO ===")
        sys.exit(0)
    else:
        print(f"=== SMOKE TEST FALLIDO: STAGING UNHEALTHY (HTTP {res.status_code}) ===")
        print("=== ACTIVANDO ROLLBACK AUTOMÁTICO:   cancelando despliegue y mantenimiento ===")
        sys.exit(1)

except Exception as e:
        print(f"error de conexion: {e}")
        print("=== ACTIVANDO ROLLBACK AUTOMÁTICO: restaurando version previa ===")
        sys.exit(1)