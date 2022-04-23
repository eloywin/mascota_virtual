import time
import random
import speech_recognition as sr
from alive_progress import alive_bar
#Clase y funciones
class Mascota():
    Parado = True
    Higiene = False
    Tristeza = False
    Enojado = False
    Feliz = True
    Tranquilo = False
    def jugar(self):
        self.Tristeza = False
        self.Feliz = True
        self.Higiene = False
    def bañar(self):
        self.Higiene = True
    def golpear(self):
        self.Feliz = False
        self.Enojado = True
        self.Tranquilo = False
        self.Tristeza = True
    def acariciar(self):
        self.Enojado = False
        self.Tristeza = False
        self.Feliz = True
        self.Tranquilo = True
mascota=Mascota()

#Bienvenida y recopilacion de datos
print("[+]Hola! Bienvenido a nuestro centro de adopcion!")
time.sleep(1.5)
nombre_usuario = input("[+]Cual es tu nombre?\n>>>")
print(f"[+]Que nombre extraño... No importa {nombre_usuario}, He oido peores nombres...")
time.sleep(1.5)
print(f"[+]Bueno, {nombre_usuario}, Tengo varias mascotas que te pueden gustar...")
time.sleep(1.5)
mascota_elegida = None
mascotas = {1:"Jordy", 2:"Homero", 3:"Faker", 4:"Manuel"}
tiene_mascota = 0
try:
    while tiene_mascota == 0:
        ver_mascotas = input("[+]Quieres ver la lista? (Si/No)\n>>>")

        if ver_mascotas == "Si" or ver_mascotas == "si" or ver_mascotas == "SI":
            print("=====================")
            print("= Lista de mascotas =")
            print("=                   =")
            print("=  (1)+Jordy ENP    =")
            print("=  (2) +Homero      =")
            print("=  (3)  +Faker      =")
            print("=  (4) +Manuel      =")
            print("=                   =")
            print("=====================")
            mascota_elegida = input("[+]Ingrese el numero ID de la mascota que quiere.\n>>>")
            print("[+]Adquiriendo mascota...")
            with alive_bar(50, bar="bubbles", spinner="arrows") as bar:
                for i in range(50):
                    time.sleep(0.01)
                    bar()
            print(f"[+]Felicitaciones! Ya tienes tu mascota! Espero que cuides a {mascotas[int(mascota_elegida)]}")
            time.sleep(1.5)
            tiene_mascota = 1

        elif ver_mascotas == "No" or ver_mascotas == "no" or ver_mascotas == "NO":
            print("[+]Entonces te doy una al azar...")
            time.sleep(1.5)
            print(f"[+]Felicitaciones! Ahora tienes tu mascota! Espero que cuides a {mascotas[random.randrange(1, 4)]}")
            time.sleep(1.5)
            tiene_mascota = 1
            break

        else:
            print("[+]No entiendo tu respuesta.")
            pass
except:
    print("Que pasa no sabes leer papi?")
mascota_en_caja = 0
print("#=============================================#")
print("#=======Fase de seleccion finalizada==========#")
print("#=============================================#")
time.sleep(2)
print("[+]LLegaste a casa...")
time.sleep(1.5)
#Sacando mascota de la caja
while mascota_en_caja == 0:
    unboxing_mascota = input("[+]Quieres sacar a tu mascota de la caja (Si/No)\n>>>")
    if unboxing_mascota == "Si" or unboxing_mascota == "si" or unboxing_mascota == "SI":
        with alive_bar(150, bar="bubbles", spinner="arrows") as bar:
            for i in range(150):
                time.sleep(0.01)
                bar()
        print("[+]Unboxing de mascota exitosa.")
        time.sleep(1.5)
        print("[+]Esta es tu mascota!!!")
        print(" ( ͡° ᴥ ͡°)")
        print("    /█\  ")
        print("    / \  ")
        print("[+]Que fachero!")
        mascota_en_caja = 1
        break
    elif unboxing_mascota == "No" or unboxing_mascota == "no" or unboxing_mascota == "NO":
        with alive_bar(150, bar="bubbles", spinner="arrows") as bar:
            for i in range(150):
                time.sleep(0.01)
                bar()
        print("[+]La mascota logra salir por su cuenta (No maltrates a tu mascota.)")
        mascota.Tristeza = True
        time.sleep(2)
        print("[+]Esta es tu mascota!!!")
        print(" (ಥ_ಥ)")
        print("  /█\  ")
        print("  / \  ")
        print("[+]Esta triste.")
        
        break
    else:
        print("[+]No entiendo tu respuesta")
        pass

time.sleep(3)
usuario_salir = False

#Actividades
while usuario_salir == False:
    
    print("[+]Que actividad deseas realizar con el?")
    print("==================")
    print("= 1)Jugar        =")
    print("= 2)Pegarle      =")
    print("= 3)Acariciar    =")
    print("= 4)Bañar        =")
    print("= 5)Dar ordenes  =")
    print("= 6)Ver estados  =")
    print("= 7)Dar veneno   =")
    print("==================")

    seleccion_menu = int(input(f"{nombre_usuario}, selecciona una opcion.\n>>>"))

    if seleccion_menu == 1:
        mascota.jugar()
        print("[+]Estas Jugando con tu mascota!")
        with alive_bar(200, bar="bubbles", spinner="arrows") as bar:
            for i in range(200):
                time.sleep(0.01)
                bar()
        print("[+]Actividad realizada con exito!")
        time.sleep(1.5)
    elif seleccion_menu == 2:
        mascota.golpear()
        print("[+]Estas Cagando a piñas a tu mascota...")
        with alive_bar(300, bar="bubbles", spinner="arrows") as bar:
            for i in range(300):
                time.sleep(0.01)
                bar()
        print("[+]Mascota golpeada exitosamente!")
        time.sleep(1.5)
    elif seleccion_menu == 3:
        mascota.acariciar()
        print("[+]Estas acariciando a tu mascota...")
        with alive_bar(100, bar="bubbles", spinner="arrows") as bar:
            for i in range(100):
                time.sleep(0.01)
                bar()
        print("[+]Mascota acariciada de manera exitosa!")
        time.sleep(1.5)
    elif seleccion_menu == 4:
        mascota.bañar()
        print("[+]Estas bañando a tu mascota!")
        with alive_bar(300, bar="bubbles", spinner="arrows") as bar:
            for i in range(300):
                time.sleep(0.01)
                bar()
        print("[+]Mascota bañada exitosamente!")
        time.sleep(1.5)
    elif seleccion_menu == 5:
        r=sr.Recognizer()
        print(sr.Microphone.list_microphone_names())
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=1)
            # r.energy_threshold()
            print("Dile algo a tu mascota!")
            audio= r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-MX")
            print(f"[+]Dijiste >>> {text} <<<")
        except:
            print("[+]Lo siento, no puedo entenderte.")
    elif seleccion_menu == 6:
        print("Revisando mascota...")
        with alive_bar(100, bar="bubbles", spinner="arrows") as bar:
            for i in range(100):
                time.sleep(0.01)
                bar()
        if mascota.Tristeza == True:
            print("*Tu mascota esta triste!*")
        if mascota.Enojado == True:
            print("*Tu mascota esta enojada!*")
        if mascota.Feliz == True:
            print("*Tu mascota esta feliz!*")
        if mascota.Tranquilo == True:
            print("*Tu mascota esta tranquila*")
        if mascota.Tranquilo == False:
            print("*Tu mascota esta inquieta*")
        if mascota.Parado == True:
            print("*Tu mascota esta de pie*")
        if mascota.Parado == False:
            print("*Tu mascota esta sentada*")
        if mascota.Higiene == True:
            print("*Tu mascota esta limpia*")
        if mascota.Higiene == False:
            print("*Tu mascota esta sucia*")
        time.sleep(6)
    elif seleccion_menu == 7:
        print("[+]OPCION NO DISPONIBLE EN ESTA VERSION.")