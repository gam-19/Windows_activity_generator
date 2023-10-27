import time
import random
import webbrowser

# Lista de países
countries = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Perú", "Surinam", "Uruguay", "Venezuela"]

def install_modules():
    # Instalar módulo pyautogui si no está instalado
    try:
        import pyautogui
    except ImportError:
        import subprocess
        import sys
        subprocess.call([sys.executable, "-m", "pip", "install", "pyautogui"])

def main():
    import pyautogui
    import subprocess

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

    while now < activity_duration:
        time.sleep(frequency)

        action = random.choice([
            "Mover mouse",
            "Escribir en notepad",
            "Busqueda en chrome"
        ])

        if action == "Mover mouse":
            pyautogui.moveRel(random.randint(-100, 100), random.randint(-100, 100))
        elif action == "Escribir en notepad":
            subprocess.Popen(["notepad.exe"])
            time.sleep(2)
            try:
                text = random.choice(["perruna", "lobezna", "me gusta el chori", "soy taca"])
                pyautogui.typewrite(text)
                time.sleep(2)
                pyautogui.hotkey('alt', 'f4')
                time.sleep(1)
                pyautogui.press("n")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif action == "Busqueda en chrome":
            #import pyautogui  # Importa pyautogui solo cuando se necesita
            webbrowser.open("https://www.google.com/search?q=capital+de+%s" % random.choice(countries))
            time.sleep(2)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press("n")

if __name__ == "__main__":
    install_modules()
    main()
