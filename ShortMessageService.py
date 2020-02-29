#-*- coding: utf -8 -*-
#Programa: ShortMessageService.py
#Objetivo: Clase que simula el comportamiento de una bandeja de mensajes Orientado a Objetos
#Autor: Dina Guerrero
#Fecha: 26/02/2020
import sys
import os
import platform

class ShortMessageService:
    """
    Se encarga de las funcionalidades de la bandeja de entrada y de salida de mensajes.
    Inserta, cuenta y elimina los mensajes
    """
    def __init__(self):
        """Inicializa la bandeja de entrada"""
        self.my_imbox = list()

        self.options = { "1": add_new_arrival,
                         "2": message_count,
                         "3": get_unread_indexes,
                         "4": get_message,
                         "5": delete_message,
                         "6": clear
                         "7": exit}

    def menu(self):
        """Despliga el menu principar"""
        self.clear_screen
        print("""-------------------MENU---------------------------
               
                       1. Añadir nuevo mensaje     
                       2. Cantidad de mensajes en bandeja
                       3. Mensajes sin leer
                       4. Mostrar Mensaje       
                       5. Borrar mensaje
                       6. Borrar todos los mensajes                   """)

    def add_new_arrival(self):
        """Añade mensajes nuevos a la bandeja"""
        print("\n=== Agregar nuevos mensajes a la bandeja de entrada ====")
        print(" ---- Los mensajes deben seguir el siguiente formato:---- ")
        print(" ----          numero de tel + mensaje                --- ")
        print("----------------------------------------------------------")

    def clear_screen(self):
        """
        Verifica mediante la librería platform el sistema operativo
        del usuario y limpia la pantalla dependiendo del SO utilizado.
        """
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            os.system("clear")
        else:
            print("Plataforma no soportada")

    def close(self):
        """ Cierra el reproductor musical. """
        print("Gracias por utilizar nuestro reproductor musical.")
        sys.exit(0)

    def press_enter(self):
        """ Realiza una pausa y solicita presionar una tecla """
        input("\nPresiona Enter para continuar")



    


    