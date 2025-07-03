# PROTOTIPO DE UN MÉTODO DE ENSEÑANZA DE LENGUAJE DE SEÑAS BASADO EN INTERACCIONES VIRTUALES UTILIZANDO INTELIGENCIA ARTIFICIAL

Este proyecto implementa un sistema de reconocimiento de lenguaje de señas utilizando visión por computadora e inteligencia artificial. Se compone de varias fases que permiten capturar, procesar, entrenar y evaluar gestos realizados por el usuario.

---

## 📁 Estructura del Proyecto

El archivo `OrdenEjecucion.txt` detalla el flujo que debe seguirse para ejecutar correctamente la aplicación. A continuación se describe cada fase:

### 1. 📹 Captura de Samples

En esta fase el usuario debe grabar los gestos o señas que se desean entrenar. Cada gesto debe repetirse varias veces para generar suficientes muestras.

> ⚠️ **Recomendaciones para una correcta captura:**
>
> - Realizar la grabación en una habitación **bien iluminada**.
> - Asegurarse de estar **solo** en el área de captura, evitando interferencias visuales de otras personas.
> - Mantener una posición adecuada frente a la cámara, con el fondo lo más limpio posible.

### 2. 🎯 Extracción de Keypoints

Los videos obtenidos en la fase anterior se procesan para extraer **keypoints** (puntos clave del cuerpo y/o manos) mediante herramientas de visión por computadora como **MediaPipe**. Estos datos serán la base del entrenamiento.

### 3. 🧠 Entrenamiento del Modelo

Con los keypoints obtenidos, se entrena un modelo de aprendizaje profundo que aprenderá a reconocer los gestos capturados. Esta fase puede requerir tiempo dependiendo de la cantidad de datos y la complejidad del modelo.

### 4. ✅ Evaluación del Modelo

Una vez entrenado el modelo, se puede ejecutar en modo de evaluación. En esta fase:

- El usuario debe repetir los gestos entrenados.
- El sistema detectará el gesto en tiempo real.
- Se mostrará el nombre del gesto reconocido en pantalla.
- El gesto será **narrado en voz alta** mediante síntesis de voz (text-to-speech).

---

## 📎 Repositorio del Código

Puedes acceder al código fuente completo en el siguiente enlace:

🔗 [https://github.com/tu-usuario/tu-repositorio](https://github.com/Daniel-Chicas/LenseGua.git)  

---

## ▶️ Requisitos y Ejecución

- Python 3.10.4
- Librerías requeridas: `mediapipe`, `tensorflow`, `opencv-python`, `numpy`, `pyttsx3`, etc.
- Recomendable utilizar un entorno virtual (`venv` o `conda`)

### Instalación rápida

```bash
git clone https://github.com/Daniel-Chicas/LenseGua.git
cd "/LenseGua"
pip install -r requirements.txt
```

👨‍💻 # Autor
# Daniel Chicas
# Ingeniería en Ciencias y Sistemas – Universidad de San Carlos de Guatemala
