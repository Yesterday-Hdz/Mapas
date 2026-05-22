# 🗺️ Búsqueda A* - Rutas por Carretera

Una aplicación web que visualiza el algoritmo A* para encontrar rutas óptimas entre ciudades mexicanas.

## Características

- 🔍 **Búsqueda A***: Algoritmo de búsqueda informada que calcula la distancia geodésica
- 🗺️ **Mapa Interactivo**: Visualización de rutas en tiempo real usando Leaflet
- 🚗 **Red de Ciudades**: 10 ciudades mexicanas con conexiones por carretera
- 📊 **Información Detallada**: Costo total del viaje y ciudades intermedias

## Archivos Incluidos

- `app.py` - Aplicación Flask con el algoritmo A*
- `Carretera_A.py` - Script original con el algoritmo
- `arbol.py` - Estructura de datos de árbol/nodos
- `templates/index.html` - Interfaz web interactiva
- `requirements.txt` - Dependencias de Python
- `Procfile` - Configuración para Render

## Instalación Local

1. **Clona o descarga el repositorio**

2. **Instala las dependencias**:
```bash
pip install -r requirements.txt
```

3. **Ejecuta la aplicación**:
```bash
python app.py
```

4. **Abre en tu navegador**:
```
http://localhost:5000
```

## Despliegue en Render

### Paso 1: Prepara tu repositorio
Sube todos los archivos a GitHub en un repositorio público.

Estructura requerida:
```
├── app.py
├── arbol.py
├── Carretera_A.py
├── Procfile
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

### Paso 2: Crea una cuenta en Render
- Ve a [render.com](https://render.com)
- Regístrate o inicia sesión

### Paso 3: Nuevo Web Service
1. Haz clic en **"New +"** → **"Web Service"**
2. Conecta tu repositorio de GitHub
3. Selecciona el repositorio donde está tu código

### Paso 4: Configuración
- **Name**: Dale un nombre a tu aplicación (ej: `carretera-a-star`)
- **Environment**: Selecciona **Python**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python app.py`
- **Plan**: Selecciona **Free** (o pago si prefieres)

### Paso 5: Deploy
Haz clic en **"Create Web Service"** y espera a que se despliegue.

Tu aplicación estará disponible en: `https://tu-app-name.onrender.com`

## Uso de la Aplicación

1. **Selecciona la ciudad de inicio** en el primer desplegable
2. **Selecciona la ciudad de destino** en el segundo desplegable
3. Haz clic en **"Buscar Ruta"**
4. Visualiza:
   - La ruta en el mapa (línea azul)
   - Las ciudades intermedias
   - El costo total (distancia en km)

## Ciudades Disponibles

- 🏙️ Jiloyork
- 🏙️ CDMX
- 🏙️ QRO (Querétaro)
- 🏙️ MORELOS
- 🏙️ HGO (Hidalgo)
- 🏙️ AGS (Aguascalientes)
- 🏙️ SLP (San Luis Potosí)
- 🏙️ SONORA
- 🏙️ MEXICALI
- 🏙️ MTY (Monterrey)

## Algoritmo A*

El algoritmo utiliza:
- **g(n)**: Costo acumulado desde el inicio hasta el nodo actual
- **h(n)**: Estimación de la distancia geodésica al destino
- **f(n) = g(n) + h(n)**: Costo total estimado

La distancia se calcula usando la **fórmula de Haversine** con las coordenadas geográficas.

## Notas Importantes

- La aplicación está configurada para **no usar debug mode** en Render
- El servidor escucha en **0.0.0.0:5000** para compatibilidad con Render
- Si experimentas problemas, revisa los **logs** en el dashboard de Render

## Solución de Problemas

### "ModuleNotFoundError: No module named 'arbol'"
Asegúrate de que el archivo `arbol.py` esté en la raíz del proyecto.

### El mapa no aparece
Verifica que tengas conexión a internet (necesaria para cargar Leaflet y OpenStreetMap).

### La búsqueda devuelve error
- Verifica que ambas ciudades estén disponibles en la red
- Asegúrate de que no selecciones la misma ciudad como origen y destino

## Requisitos Mínimos para Render

- Python 3.7+
- 512 MB de RAM (suficiente para la aplicación)
- Conexión a Internet para cargar mapas

---

¡Tu aplicación está lista para desplegarse en Render! 🚀
