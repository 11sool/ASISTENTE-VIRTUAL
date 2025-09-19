import pyttsx3
# import speech_recognition as sr  # ← COMENTAMOS ESTA LÍNEA
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import time

# Opciones de voz / idioma (CORREGIDO)
id1 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
id2 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id3 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"


# 🆕 NUEVA FUNCIÓN: Para escribir comandos en lugar de hablarlos
def obtener_texto_usuario():
    """
    En lugar de escuchar el micrófono, el usuario escribirá los comandos
    """
    try:
        # El usuario escribe el comando
        pedido = input("¿Qué necesitas? (escribe tu comando): ")
        print(f"Escribiste: {pedido}")
        return pedido
    except:
        print("Error al leer el texto")
        return "Sigo esperando"


# Función para que el asistente pueda ser escuchado (IGUAL QUE ANTES)
def hablar(mensaje):
    try:
        engine = pyttsx3.init()
        engine.setProperty("voice", id3)
        engine.say(mensaje)
        engine.runAndWait()
        print(f"🔊 Asistente dice: {mensaje}")  # También lo mostramos en pantalla
    except:
        # Si no funciona la voz, al menos mostramos el texto
        print(f"🔊 Asistente dice: {mensaje}")


# ========================================
# 🆕 FUNCIÓN: EJERCICIO DE RESPIRACIÓN
# ========================================

def ejercicio_respiracion():
    """
    Esta función guía al usuario en un ejercicio de respiración relajante.
    Usa la técnica 4-4-4: inhalar 4 segundos, mantener 4 segundos, exhalar 4 segundos
    """

    # 1️⃣ SALUDO INICIAL
    hablar("Perfecto, vamos a hacer un ejercicio de respiración juntos para relajarnos.")

    # 2️⃣ INSTRUCCIONES
    hablar("Ponte cómodo, puedes sentarte o estar de pie. Si quieres, cierra los ojos.")

    # 3️⃣ PAUSA
    print("⏰ Preparándote... (3 segundos)")
    time.sleep(3)

    # 4️⃣ COMENZAMOS
    hablar("Comenzamos. Haremos 3 respiraciones profundas.")

    # 5️⃣ BUCLE PARA 3 RESPIRACIONES
    for numero_respiracion in range(1, 4):

        hablar(f"Respiración número {numero_respiracion}")
        time.sleep(1)

        # INHALAR
        hablar("Inhala profundamente por la nariz")
        print("💨 Inhalando... (4 segundos)")
        time.sleep(4)

        # MANTENER
        hablar("Mantén el aire en tus pulmones")
        print("⏸️ Manteniendo... (4 segundos)")
        time.sleep(4)

        # EXHALAR
        hablar("Ahora exhala lentamente por la boca")
        print("💨 Exhalando... (4 segundos)")
        time.sleep(4)

        # PAUSA ENTRE RESPIRACIONES
        if numero_respiracion < 3:
            print("⏰ Pausa... (2 segundos)")
            time.sleep(2)

    # 6️⃣ MENSAJE FINAL
    hablar("Excelente. Has completado el ejercicio de respiración. Espero que te sientas más relajado.")


# ========================================
# FUNCIONES ORIGINALES (SIN CAMBIOS)
# ========================================

def pedir_dia():
    dia = datetime.datetime.today()
    dia_semana = dia.weekday()
    calendario = {0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves",
                  4: "Viernes", 5: "Sábado", 6: "Domingo"}
    hablar(f"Hoy es {calendario[dia_semana]}")


def pedir_hora():
    hora = datetime.datetime.now()
    hora_texto = f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    hablar(hora_texto)


def saludo_inicial():
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buen día"
    else:
        momento = "Buenas tardes"

    hablar(f"{momento} Juan, en qué te puedo ayudar? Ahora también puedo guiarte en ejercicios de respiración.")
    print("\n📝 COMANDOS DISPONIBLES:")
    print("- 'respiración' o 'respirar' o 'relajar' → Ejercicio de respiración")
    print("- 'abrir youtube' → Abre YouTube")
    print("- 'abrir navegador' → Abre Google")
    print("- 'qué día es hoy' → Te dice el día")
    print("- 'qué hora es' → Te dice la hora")
    print("- 'chiste' → Te cuenta un chiste")
    print("- 'adiós' → Termina el programa")
    print("=" * 50)


# ========================================
# FUNCIÓN CENTRAL MODIFICADA
# ========================================

def centro_pedido():
    saludo_inicial()
    comenzar = True

    while comenzar:
        # 🔄 CAMBIO: Usamos input() en lugar del micrófono
        pedido = obtener_texto_usuario().lower()
        print(f"Comando recibido: {pedido}")

        # COMANDOS ORIGINALES
        if "abrir youtube" in pedido:
            hablar("Estoy abriendo YouTube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "abrir navegador" in pedido or "abrir el navegador" in pedido:
            hablar("Estoy abriendo el navegador")
            webbrowser.open("https://www.google.com.ar")
            continue
        elif "que día es hoy" in pedido or "qué día es hoy" in pedido or "qué día es" in pedido:
            pedir_dia()
            continue
        elif "qué hora es" in pedido or "que hora es" in pedido or "qué hora" in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("buscando en wikipedia")
            pedido = pedido.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            try:
                resultado = wikipedia.summary(pedido, sentences=1)
                hablar("Encontré esta información en wikipedia")
                hablar(resultado)
            except:
                hablar("No pude encontrar información sobre ese tema")
            continue
        elif "busca en internet" in pedido:
            hablar("Buscando información")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif "reproducir" in pedido:
            hablar("Reproduciendo")
            pedido = pedido.replace("reproducir", "").strip()
            pywhatkit.playonyt(pedido)
            continue
        elif "chiste" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue
        elif "precio de la acción" in pedido:
            accion = pedido.split("de")[-1].strip().lower()
            cartera = {"apple": "AAPL", "amazon": "AMZN", "google": "GOOGL", "tesla": "TSLA"}
            try:
                accion_buscada = cartera[accion]
                ticker = yf.Ticker(accion_buscada)
                precio_actual = ticker.info['regularMarketPrice']
                hablar(f"La encontré, el precio de {accion} es {precio_actual} dólares.")
            except KeyError:
                hablar(f"No tengo información sobre la acción de {accion}.")
            except Exception as e:
                hablar("Perdón, pero no pude encontrar la información de la acción.")
            continue

        # 🆕 NUEVO COMANDO: EJERCICIO DE RESPIRACIÓN
        elif "respiración" in pedido or "respirar" in pedido or "relajar" in pedido:
            ejercicio_respiracion()
            continue

        elif "adiós" in pedido:
            hablar("Nos vemos, avísame si necesitas otra cosa Juan")
            break
        elif "sigo esperando" not in pedido:
            hablar(
                "No entendí ese comando. Puedes escribir 'respiración' para el ejercicio de respiración, o 'adiós' para salir.")
            continue


# Ejecutar el programa
if __name__ == "__main__":
    print("=== ASISTENTE VIRTUAL DE BIENESTAR MENTAL ===")
    print("MODO: Solo texto (sin micrófono)")
    print("Escribe tus comandos en lugar de hablarlos")
    print("=" * 45)
    centro_pedido()