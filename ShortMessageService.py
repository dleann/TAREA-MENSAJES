#-*- coding: utf -8 -*-
#Programa: ShortMessageService.py
#Objetivo: Clase que simula el comportamiento de una bandeja de mensajes Orientado a Objetos
#Autor: Dina Guerrero
#Fecha: 26/02/2020
import sys
import os
import platform
import time

class ShortMessageService:
    """
    Se encarga de las funcionalidades de la bandeja de entrada y de salida de mensajes.
    Inserta, cuenta y elimina los mensajes
    """
    has_been_viewed = []
    from_number = []
    time_arrived = []
    text_of_sms = []
    #message = [] = has_been_viewed
    
    my_imbox = [from_number,time_arrived,text_of_sms]

    def __init__(self):
        """Inicializa la bandeja de entrada"""
        self.options = {"1": self.add_new_arrival,
                        "2": self.message_count,
                        "3": self.get_unread_indexes,
                        "4": self.get_message,
                        "5": self.delete_message,
                        "6": self.clear,
                        "7": self.close} 
        

    def menu(self):
        """Despliga el menu principar"""
        self.clear_screen
        print("""-------------------MENU---------------------------
               
            1. Añadir nuevo mensaje     
            2. Cantidad de mensajes en bandeja
            3. Mensajes sin leer
            4. Mostrar Mensaje       
            5. Borrar mensaje
            6. Borrar todos los mensajes                   
            """)

    def add_new_arrival(self):
        """Añade mensajes nuevos a la bandeja"""
        print("\n=== Agregar nuevos mensajes a la bandeja de entrada ====")
        print(" ---- Los mensajes deben seguir el siguiente formato:---- ")
        print(" ----          numero de tel + mensaje                --- ")
        print("----------------------------------------------------------")
        a = True
        x = 0
        while (a == True):
            a = int(input("¿Desea añadir un mensaje nuevo? SI(1) - NO(0): "))
            if a == 1:
                a = True
                self.my_imbox.append(input("Ingrese el mensaje: "))
            elif a == 0:
                print("Saliendo...")
                a == False
                self.press_enter()
            else:
                print("¡Comando inválido!")
                self.press_enter()

         #self.from_number.append(input("Ingrese su número "))
        #self.time_arrived.append(input("Ingrese hora ")) #time.ctime()
        #self.text_of_sms.append(input("Ingrese el mensaje "))


    def message_count(self):
        """Cuenta y muestra la cantidad de mensajes que hay en la bandeja"""
        print("Tiene {0} mensajes".format(len(self.my_imbox)))
        self.press_enter()

    def get_unread_indexes(self):
        """Retorna la cantidad de mensajes sin leer"""


    def delete_message(self):
        """"""
    
    def get_message(self,search_position="", delete=False):
        """ Retorna el mensaje en una pocision en espesifico """
        message = 0
        message_position = 0
        if search_position == "":
            print(self.my_imbox)
            print(len(self.my_imbox))
            search_position = int(
                    input("Ingresa la posición del mensaje: "))
        
        for x in range (len(self.my_imbox)):
            if self.my_imbox[x] != message:
                message = self.my_imbox[x]
                message_position = x + 1
                if message_position == search_position:
                    print("El mensaje {0} es: ".format(search_position))
                    print(self.my_imbox[x])
                    self.press_enter() if not delete else True
                
                    return True
        
        print("El mensaje no existe")                                    
        self.press_enter()
        
        return False

    def delete_message(self):
        """Elimina el mensaje en la posicion que envie"""
        search_position = int(input("Ingrese la posicion del mensaje:"))
        if self.get_message(search_position,True):
            try:
                self.my_imbox.remove(self.my_imbox[search_position-1])
                print("¡El mensaje {0} ha sido eliminado satisfactoriamente!"
                      .format(search_position))
                self.press_enter()
            except ValueError:
                print("¡El mensaje no esta en la bandeja!")
                self.press_enter()


    def clear(self):
        """Elimina todos los mensajes"""
        condition = int(input("¿Desea Eliminar todos los mensajes? SI(1) - NO(0)"))
        if condition == 1:
            self.my_imbox[:] = []
            print("Mensajes Eliminados Satisfactoriamente")
            self.press_enter()
        elif condition == 0:
            print("¡Mensajes no han sido eliminados!")
            self.press_enter()
        else:
            print("¡Comando invalido!")
            self.press_enter()



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

    def run(self):
        """ Despliega el menú principal y procesa las opciones. """ 
        while True:
            self.menu()
            choice = input("Ingrese una opción: ")
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("¡{0} no es una opción vålida!".format(choice))
                self.press_enter()    

if __name__ == "__main__":
    miimbox = ShortMessageService()
    miimbox.run()

    


    