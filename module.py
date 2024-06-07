from datetime import datetime

def obtenir_temps():
    return "il est " + datetime.now().strftime("%H:%M:%S")
