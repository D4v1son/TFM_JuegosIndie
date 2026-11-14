import requests, time, json
from pathlib import Path

OUT = Path("data/raw/steamspy_all")
OUT.mkdir(parents=True, exist_ok=True)
URL = "https://steamspy.com/api.php"

def descargar_pagina(page, intentos=5):
    f = OUT / f"page_{page:03d}.json"
    if f.exists():
        return False                      # ya descargada
    for i in range(intentos):
        try:
            r = requests.get(URL, params={"request": "all", "page": page},
                             timeout=(10, 180))   # 10 s para conectar, 180 s para recibir
            print(f"página {page}, intento {i+1}: HTTP {r.status_code}, {len(r.content)} bytes")
            if r.status_code == 200:
                data = r.json()
                if not data:
                    return None            # página vacía: no quedan juegos
                f.write_text(json.dumps(data), encoding="utf-8")
                return True
        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"   error: {type(e).__name__}: {e}")
        time.sleep(30 * (i + 1))           # espera creciente: 30, 60, 90 s...
    raise RuntimeError(f"Página {page}: sin respuesta tras {intentos} intentos")

for page in range(200):
    estado = descargar_pagina(page)
    if estado is None:
        print("Fin del catálogo")
        break
    if estado:
        time.sleep(65)                     # límite de SteamSpy: 1 petición/min en "all"