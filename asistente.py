import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import time

# Opciones de voz
id1 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
id2 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id3 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"


def transformar_audio_en_texto():
    """Convierte el audio del micrófono en texto"""
    r = sr.Recognizer()

    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("Te escucho... habla ahora")

        try:
            r.adjust_for_ambient_noise(origen, duration=0.5)
            audio = r.listen(origen, timeout=5, phrase_time_limit=10)
            print("Procesando lo que dijiste...")

            pedido = r.recognize_google(audio, language="es-es")
            print(f"Entendi: {pedido}")
            return pedido.lower()

        except sr.WaitTimeoutError:
            print("No escuche nada en 5 segundos")
            return "sigo esperando"

        except sr.UnknownValueError:
            print("No pude entender lo que dijiste, intenta de nuevo")
            return "sigo esperando"

        except sr.RequestError as e:
            print(f"Error con el servicio de reconocimiento: {e}")
            return "sigo esperando"

        except Exception as e:
            print(f"Error inesperado: {e}")
            return "sigo esperando"


def obtener_comando_usuario():
    """Permite al usuario elegir entre voz o texto"""
    print("\nOpciones de entrada:")
    print("1. Presiona ENTER para usar tu voz")
    print("2. Escribe 'texto' para escribir tu comando")

    eleccion = input("Elige tu opcion: ").strip().lower()

    if eleccion == "texto":
        try:
            pedido = input("Escribe tu comando: ")
            print(f"Escribiste: {pedido}")
            return pedido.lower()
        except:
            print("Error al leer el texto")
            return "sigo esperando"
    else:
        return transformar_audio_en_texto()


def hablar(mensaje):
    """Hace que el asistente hable"""
    try:
        engine = pyttsx3.init()
        engine.setProperty("voice", id3)
        engine.say(mensaje)
        engine.runAndWait()
        print(f"Asistente dice: {mensaje}")
    except:
        print(f"Asistente dice: {mensaje}")


def ejercicio_respiracion():
    """Ejercicio de respiración 4-4-4"""
    hablar("Perfecto, vamos a hacer un ejercicio de respiración juntos para relajarnos.")
    hablar("Ponte cómodo, puedes sentarte o estar de pie. Si quieres, cierra los ojos.")

    print("Preparándote... (3 segundos)")
    time.sleep(3)

    hablar("Comenzamos. Haremos 3 respiraciones profundas.")

    for numero_respiracion in range(1, 4):
        hablar(f"Respiración número {numero_respiracion}")
        time.sleep(1)

        hablar("Inhala profundamente por la nariz")
        print("Inhalando... (4 segundos)")
        time.sleep(4)

        hablar("Mantén el aire en tus pulmones")
        print("Manteniendo... (4 segundos)")
        time.sleep(4)

        hablar("Ahora exhala lentamente por la boca")
        print("Exhalando... (4 segundos)")
        time.sleep(4)

        if numero_respiracion < 3:
            print("Pausa... (2 segundos)")
            time.sleep(2)

    hablar("Excelente. Has completado el ejercicio de respiración. Espero que te sientas más relajado.")


def ejercicio_mindfulness():
    """Guía de mindfulness de 2 minutos"""
    hablar("Vamos a hacer un ejercicio de mindfulness de 2 minutos.")
    hablar("Encuentra un lugar cómodo donde puedas sentarte tranquilo.")

    time.sleep(3)

    hablar("Cierra los ojos suavemente y enfócate en tu respiración natural.")
    time.sleep(5)

    hablar("Nota cómo entra y sale el aire de tu cuerpo.")
    time.sleep(10)

    hablar("Si tu mente se distrae, simplemente vuelve tu atención a la respiración.")
    time.sleep(10)

    hablar("Siente tu cuerpo. Nota dónde estás sentado.")
    time.sleep(8)

    hablar("Continuemos en silencio por un momento.")
    time.sleep(15)

    hablar("Ahora, lentamente, mueve los dedos de tus pies y manos.")
    time.sleep(3)

    hablar("Cuando estés listo, abre los ojos.")
    time.sleep(2)

    hablar("Has completado tu práctica de mindfulness. Bien hecho.")


def pedir_dia():
    """Dice que día es hoy"""
    dia = datetime.datetime.today()
    dia_semana = dia.weekday()
    calendario = {0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves",
                  4: "Viernes", 5: "Sábado", 6: "Domingo"}
    hablar(f"Hoy es {calendario[dia_semana]}")


def pedir_hora():
    """Dice la hora actual"""
    hora = datetime.datetime.now()
    hora_texto = f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    hablar(hora_texto)


def saludo_inicial():
    """Saludo inicial del asistente"""
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buen día"
    else:
        momento = "Buenas tardes"

    hablar(f"{momento} Juan, en qué te puedo ayudar? Soy tu asistente de bienestar mental.")
    print("\nCOMANDOS DE BIENESTAR DISPONIBLES:")
    print("- 'respiracion' o 'respirar' - Ejercicio de respiración")
    print("- 'mindfulness' o 'meditacion' - Ejercicio de atención plena")
    print("- 'relajar' - Técnicas de relajación")
    print("\nCOMANDOS GENERALES:")
    print("- 'abrir youtube' - Abre YouTube")
    print("- 'que dia es hoy' - Te dice el día")
    print("- 'que hora es' - Te dice la hora")
    print("- 'chiste' - Te cuenta un chiste")
    print("- 'adios' - Termina el programa")
    print("=" * 50)


def centro_pedido():
    """Función principal del asistente"""
    print("Verificando micrófono...")
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
        print("Micrófono funcionando correctamente")
    except Exception as e:
        print(f"Problema con el micrófono: {e}")
        print("Puedes usar el modo texto escribiendo 'texto'")

    saludo_inicial()
    comenzar = True

    while comenzar:
        pedido = obtener_comando_usuario()
        print(f"Comando recibido: {pedido}")

        # Comandos de bienestar mental
        if "respiración" in pedido or "respirar" in pedido:
            ejercicio_respiracion()
            continue
        elif "mindfulness" in pedido or "meditacion" in pedido or "meditación" in pedido:
            ejercicio_mindfulness()
            continue
        elif "relajar" in pedido:
            hablar("¿Prefieres un ejercicio de respiración o de mindfulness?")
            continue

        elif "abrir youtube" in pedido:
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
        elif "adiós" in pedido or "adios" in pedido or "hasta luego" in pedido:
            hablar("Nos vemos, avísame si necesitas otra cosa Juan. Cuida tu bienestar mental.")
            break
        elif "sigo esperando" not in pedido:
            hablar("No entendí ese comando. Puedes decir respiración, mindfulness, o adiós para salir.")
            continue


if __name__ == "__main__":
    print("=== ASISTENTE VIRTUAL DE BIENESTAR MENTAL ===")
    print("MODO: Reconocimiento de voz + texto opcional")
    print("Habla claro y cerca del micrófono")
    print("=" * 50)

    try:
        import speech_recognition as sr

        print("speech_recognition disponible")
    except ImportError:
        print("Instala speech_recognition con: pip install SpeechRecognition")
        exit()

    try:
        import pyaudio

        print("pyaudio disponible")
    except ImportError:
        print("Para mejor rendimiento instala: pip install pyaudio")

    centro_pedido()
