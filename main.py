import time
import random
import webbrowser

# Lista de países
countries = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Perú", "Surinam", "Uruguay", "Venezuela"]

def install_modules():
    #Instalar módulo pyautogui si no está instalado
    try:
        import pyautogui
    except ImportError:
        import subprocess
        import sys
        subprocess.call([sys.executable, "-m", "pip", "install", "pyautogui"])

def main():
    # Obtener hora actual
    now = int(time.time())

    # Preguntar la duración de la actividad
    try:
        activity_duration = int(input("Durante cuánto tiempo desea generar actividad (en minutos): "))
    except ValueError:
        print("La duración de la actividad debe ser un número.")
        return

    # Preguntar la frecuencia de la actividad
    try:
        frequency = input("Con qué frecuencia desea que se realice la actividad (en segundos): ")
        frequency = int(frequency)
    except ValueError:
        print("La frecuencia de la actividad debe ser un número.")
        return

    # Convertir la duración de actividad a segundos
    activity_duration = now + activity_duration * 60

    # Mientras el valor de hora actual sea menor al tiempo de duración de la actividad, realizar bucle de actividad
    while now < activity_duration:
        # Frecuencia de actividad
        time.sleep(frequency)

        # Escoger acción aleatoria
        action = random.choice([
            "Mover mouse",
            "Escribir en notepad",
            "Busqueda en chrome"
        ])

        # Realizar acción
        if action == "Mover mouse":
            pyautogui.moveRel(random.randint(-100, 100), random.randint(-100, 100))
        elif action == "Escribir en notepad":
            # Abrir la aplicación Notepad
            subprocess.Popen(["notepad.exe"])
            time.sleep(2)
            try:
                # Escribir texto aleatorio
                text = random.choice(["perruna", "lobezna", "me gusta el chori", "soy taca"])
                pyautogui.typewrite(text)
                time.sleep(2)

                # Cerrar la aplicación Notepad
                pyautogui.hotkey('alt', 'f4')

                # Esperar a que aparezca el cuadro de diálogo
                time.sleep(1)

                # Simular presionar la tecla "N" para no guardar los cambios
                pyautogui.press("n")

            except Exception as e:
                print(f"An error occurred: {e}")

        elif action == "Busqueda en chrome":
            # Abrir una búsqueda en Google
            webbrowser.open("https://www.google.com/search?q=capital+de+%s" % random.choice(countries))
            time.sleep(2)

            # Cerrar la aplicación Chrome
            pyautogui.hotkey('alt', 'f4')

            # Esperar a que aparezca el cuadro de diálogo de guardar
            time.sleep(1)

            # Simular presionar la tecla "N" para no guardar los cambios
            pyautogui.press("n")

    # Repetir proceso
    main()

if __name__ == "__main__":
    # Instalar módulos si no están instalados
    install_modules()
    main()
