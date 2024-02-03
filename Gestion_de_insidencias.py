# MODULO
from art import *
from colorama import *
import os , msvcrt , progressbar ,time ,stdiomask ,getpass , pyfiglet , colorama
# VARIABLES GLOBALES
administrador_lista = ["C1","1755779061","Mateo","Ortiz","18","A","mateo@gmail.com","mateo12r"]
supervisor_lista = ["C2","2133422123","Isacc","Floril","20","A","isacc@gmail.com","isacc12r"]
usuario_lista = ["C3","5321344763","Gabriel","Guerra","19","A","gabriel@gmail.com","gabriel12r","C4","1265348924","Josue","Chicaiza","18","A","josue@gmail.com","josue12r"]
Incidencias_lista = []
admi = False
sup = False
usu = False
op = 0
corr1 = 0
nombre = ""
pasw = ""
intentos = 0
session = 0
codigo = 4
ticket = 0
repite = True
repite1 = True
repite2 = True
repite3 = True
x = 0
# FUNCIONES
def logo():
    print(Fore.LIGHTRED_EX + """
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣶⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⢚⢫⣽⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡶⠛⠳⣎⢥⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠁⠀⠀⠀⣹⢾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣆⣆⣶⣶⣶⡶⣶⢶⣀⣀⣀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⢛⡏⠀⠀⠀⣠⡖⢏⠺⣿⣿⣷⣦⣤⣤⣤⠶⠖⠊⠀⠀⣀⣤⣤⡴⣖⡾⠟⠛⠉⠉⠉⠙⣏⡞⣼⣼⣷⣿⡿⠿⠛⠉⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⣉⠖⡩⢝⡦⠴⣞⠱⡸⢌⣣⣽⣿⣿⠿⠛⠉⣀⣠⣤⣶⡾⠟⠛⠋⠉⠙⣾⣇⠀⠀⠀⢀⣀⣤⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⢀⣴⢋⠖⡱⢊⡕⢪⢔⠫⡔⢫⣱⣾⠿⠛⢉⣠⡴⣶⠿⠟⠋⠁⠀⠀⠀⠀⠀⢀⣠⡿⣹⢳⣻⠻⡽⣹⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⣰⠟⣤⢋⡎⢵⡩⢜⢣⢎⣣⣽⠟⢋⣡⡴⣞⣯⠟⠋⠁⠀⠀⠀⠀⣀⣤⢶⢶⣛⢯⣓⢧⣓⡏⣶⢫⣽⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠼⢯⣞⡤⢳⡸⢅⡞⣩⣖⠷⠋⠳⢶⣏⢧⣽⠋⠀⠀⠀⢀⣠⡴⣞⡻⡝⣮⢝⡲⣭⢞⡼⣣⢧⣛⢶⣫⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠈⠻⣵⢊⠷⡸⢥⣧⠀⠀⠀⠀⠉⠳⣾⣦⣠⣤⡞⣯⠳⣝⡲⣭⢳⣣⢏⡷⢳⣎⢷⡹⢮⡝⣮⢳⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⣸⣏⣞⣱⡧⠾⢷⣄⡀⠀⠀⠀⠈⠳⣏⡶⣹⢖⡻⣜⡳⣭⢳⡭⣞⡽⣳⢎⡷⣹⢧⣻⠼⣏⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣩⣥⣶⣿⣭⣶⣿⠿⠛⠛⠀⠀⠙⣷⡹⣎⠷⣭⢳⣭⢳⡝⣮⢳⣝⢾⡹⢧⣟⢮⣟⣭⢿⣮⣝⠻⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⣠⡴⣞⡟⣻⣛⢿⡻⣿⣿⣦⣤⣄⡀⠀⠀⠀⢹⡷⣭⣻⢼⡳⣞⡽⣺⡭⣟⢮⣯⢽⣻⡼⣏⡾⣞⡽⣞⡿⣿⣦⣈⠉⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⣰⠿⣭⣷⣭⡞⣵⡹⣎⠷⣭⣛⣿⣿⣭⣉⠀⠀⠀⠀⢿⣧⣛⣮⢷⣫⣞⠷⣽⢞⣯⠾⣽⢶⣻⣭⢷⡯⣟⣳⣟⡿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⢀⣹⡿⣯⣴⢿⡹⢶⡹⣎⡟⣶⡹⣖⢿⣿⡿⠛⠦⠀⠀⢸⡷⣏⣾⡳⣽⡺⣟⡽⣾⣭⢿⡽⣞⣷⣫⣟⡾⣽⣳⣯⣿⣿⡿⠿⠛⠛⠲⠀⠀⠀⠀
                                                                           ⣾⣤⡶⣿⡹⣞⡵⣫⣞⣽⣣⣟⣵⣻⠷⣟⡾⣭⢿⣿⣦⡀⠀⠀⢸⡿⣽⢶⣻⣳⢿⣹⡽⣶⢯⣟⡾⣿⡷⣟⣾⣽⣳⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠻⣷⣝⡶⠟⣳⡿⠋⠉⠀⠈⠉⠛⡿⣸⢻⣽⡞⣯⣿⡿⣷⠀⠀⣿⢿⡽⣞⡷⣯⣟⣷⣻⣽⣻⢾⣽⣻⢿⣜⢿⣾⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠘⠻⣤⣾⡟⠀⠀⠀⠀⠀⠀⣀⣴⣿⢸⣿⣽⡳⣿⣷⡌⠁⣰⣿⢯⡿⣽⣻⣵⣻⣞⡷⣯⣟⡿⣾⣽⣻⢿⣦⠙⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠉⠉⠀⠀⠀⢀⣰⣾⣿⣿⢇⣿⡿⣶⢿⡿⠉⢷⢀⣿⣏⣿⣹⢷⡿⣾⢷⣏⣿⢿⣾⣿⣷⣿⣿⣿⣿⣷⠾⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⡿⣣⣿⢿⡽⣯⢿⡇⠀⣠⣿⣟⣾⣳⣯⢿⣽⢯⣟⣯⣿⡟⣿⣿⣿⣿⠿⠿⠿⣿⣷⣅⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⡿⣫⣾⢿⡽⣯⢿⡽⣿⣠⣼⣿⣻⢾⣳⣯⣿⣟⣾⣟⣯⣿⣽⣷⢻⡿⠋⠀⠀⠀⠀⠀⠉⠙⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⣰⣿⣿⣿⣿⡿⣫⣾⡿⣯⢿⡽⣯⢿⣽⣿⣿⣻⢷⣻⣟⣯⣿⢻⣿⣷⣻⣟⣾⣿⣿⠸⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⢰⣿⣿⣿⣿⢏⣾⣿⢯⣿⡽⣯⣿⣻⣟⣾⣽⣾⣻⣟⣯⣿⣽⡟⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⢸⣿⣿⣿⣏⣾⣿⡽⣟⣾⢿⣽⡾⣷⡿⣻⣿⣿⣿⣿⣿⣿⡟⠁⣿⠟⠋⠉⠉⠙⠻⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠈⠘⣿⣿⣿⢸⣿⣯⢿⡿⣽⡿⣯⣿⢿⣇⠉⠀⠀⠀⠀⠉⠿⠁⠀⠃⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠹⣿⣿⢼⣿⣟⣿⣟⣿⣽⣿⣽⣿⣿⣿⣶⣶⣴⣤⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠘⢿⣏⣿⣿⣻⣾⣟⣿⣾⢿⣾⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠙⠪⠿⣿⣯⣿⣟⣿⣿⣟⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⠿⠯⠿⠿⠿⠿⠿⠷⠿⠿⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣿⣿⣷⣶⣶⡄⠘⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⡿⢀⣿⣿⣿⣿⡿⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⡿⠁⣼⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣷⣶⣤⣤⣤⣶⣿⣿⣿⣿⣿⠟⠁⠸⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠈⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠿⠿⠿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⡄⢹⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀"""+Fore.RESET )
    

def logo_pequeño():
    print(Fore.LIGHTRED_EX+"""
                                                                                         ⢀⣠⣤⣶⣶⡞⡀⣤⣬⣴⠀⠀⢳⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀
                                                                                  ⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡇⠀⢸⣿⠿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀
                                                                                  ⠀⠀⢠⡾⣫⣿⣻⣿⣽⣿⡇⠀⠈⢿⣧⡝⠟⠀⠀⢸⣿⣿⣿⣿⣿⣟⢷⣄⠀⠀
                                                                                  ⠀⢠⣯⡾⢿⣿⣿⡿⣿⣿⣿⣆⣠⣶⣿⣿⣷⣄⣰⣿⣿⣿⣿⣿⣿⣿⢷⣽⣄⠀
                                                                                  ⢠⣿⢋⠴⠋⣽⠋⡸⢱⣯⡿⣿⠏⣡⣿⣽⡏⠹⣿⣿⣿⡎⢣⠙⢿⡙⠳⡙⢿⠄
                                                                                  ⣰⢣⣃⠀⠊⠀⠀⠁⠘⠏⠁⠁⠸⣶⣿⡿⢿⡄⠈⠀⠁⠃⠈⠂⠀⠑⠠⣈⡈⣧
                                                                                  ⡏⡘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡥⢄⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⢸
                                                                                  ⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⣸⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢨
                                                                                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
                                                                                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡳⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          """+Fore.RESET)


def lista_de_tecnicos():
    print("lista de tecnicos")


def barra_carga():
    def progress_bar(part, total, tamano= 20):
        frac= part/ total
        completed= int(frac * tamano)
        missing= tamano - completed
        bar= f"                  [{f'{Fore.LIGHTGREEN_EX}🔥{Fore.RESET}'* completed}{'-'* missing}]{frac:.2%}"
        return bar
    n=30
    for i in range (n+1):
        time.sleep(0.05)
        print(progress_bar(i,n,35),  end="\r")
    os.system("cls")


def Mostrar_incidencias():
    print(f"{Fore.LIGHTGREEN_EX}                         Lista De Incidencias   {Fore.RESET}")
    for x in range (0,len(Incidencias_lista())):
        if x % 8 ==0:
            print("                 ╔════════════════════════════════╗")
            print("                 ║  Codigo: " + usuario_lista[x] +" "*((33-11)-len(usuario_lista[x])) +"║")
            print("                 ║  Cedula: " + usuario_lista[x+1] +" "*((33-11)-len(usuario_lista[x+1])) +"║")
            print("                 ║  Nombre: " + usuario_lista[x+2] +" "*((33-11)-len(usuario_lista[x+2])) +"║")
            print("                 ║  Apellido: " + usuario_lista[x+3] +" "*((31-11)-len(usuario_lista[x+3])) +"║")
            print("                 ║  Edad: " + usuario_lista[x+4] +" "*((32-8)-len(usuario_lista[x+4])) +"║")
            print("                 ║  Estado: " + usuario_lista[x+5] +" "*((33-11)-len(usuario_lista[x+5])) +"║")
            print("                 ║  Usuario: " + usuario_lista[x+6] +" "*((33-12)-len(usuario_lista[x+6])) +"║")
            print("                 ║  Contraseña: " + usuario_lista[x+7] +" "*((33-15)-len(usuario_lista[x+7])) +"║")
            print("                 ╚════════════════════════════════╝")


def registros_incidencias():
    global repite3, ticket
    repite3 = True
    while repite3:
        try:
            ticket += 1
            codu = str(ticket)
            print("      Ingrese los datos  de la incidencia a registrar: ")
            print("")
            Incidencias_lista.append("T" + codu)
            Incidencias_lista.append(input("      Nombre del Usuario: "))
            Incidencias_lista.append(input("      Cedula: "))
            Incidencias_lista.append(input("      Fecha: "))
            Incidencias_lista.append(input("      Detalle de la Incidencia: "))
            Incidencias_lista.append(input("      Estado de la Incidencia: "))
            print("Prioridades  -> [Alta , Baja , Urgente]")
            Incidencias_lista.append(input("      Prioridad: "))
            print("")
            print("Presione cualquier tecla para continuar")
            msvcrt.getch()
            os.system("cls")
            print("")
            print(f"{Fore.LIGHTGREEN_EX}                      *Incidencia Registrada con Exito*{Fore.RESET}")
            repite2 = False
        except:
            print(f"{Fore.LIGHTRED_EX}     ..Error: 'Ingrese una opcion que desea registar'.. {Fore.RESET}")
            msvcrt.getch()
    msvcrt.getch()


def editar_usuario():
    global repite3 , op
    op = 0
    repite3 = True
    while True:
        try:
            print("Ingrese el codigo del cliente que quiere editar..")
            Codigo = int(input())
            while Codigo < 1:
                print("El codigo ingresado es incorrecto..")
                print("Ingrese el codigo del cliente que quiere buscar..")
                Codigo = int(input())
            Codigo = str(Codigo)
            cod = "C" + Codigo
            if cod in usuario_lista:
                while repite3:    
                    codpsi = usuario_lista.index(cod)
                    print(f"""{Fore.LIGHTCYAN_EX}
                                        █▄██▄█                                                    █▄██▄█
                                        ▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▐█┼██▌
                                        ▐████▌║                 EDITOR DE USUARIOS               ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌ 
                                        ▐████▌║                    1.-CEDULA                     ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    2. NOMBRE                     ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    3. APELLIDO                   ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    4. EDAD                       ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    5. ESTADO                     ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    6. CORREO                     ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    7. CONTRASEÑA                 ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    S. Atras                      ║▐████▌
                               ,     ,        ╙──────────────────────────────────────────────────╜{Fore.RESET} {Fore.LIGHTRED_EX}
                              (\____/)
                               (_oo_)
                                 (O)
                               __||__          El dragón te guiará por las opciones.
                      []/_______\ [] /
                      / \______/ \/
                    {Fore.RESET}
                    """)
                    op = input("Ingrese la opcion del dato que quiere editar [1-7] o [S]: ")
                    op = op.upper()
                    match op:
                        case '1':
                            usuario_lista[codpsi+1] = input("              Cedula: ")
                        case '2':
                            usuario_lista[codpsi+2] = input("              Nombre: ")
                        case '3':
                            usuario_lista[codpsi+3] = input("              Apellido: ")
                        case '4':
                            usuario_lista[codpsi+4] = input("              Edad: ")
                        case '5':
                            usuario_lista[codpsi+5] = input("              Estado: ")
                        case '6':
                            usuario_lista[codpsi+6] = input("              Correo: ")
                        case '7':
                            usuario_lista[codpsi+7] = input("              Contraseña: ")
                        case 'S':
                            print("")
                            print(f"                                             {Fore.LIGHTCYAN_EX} .....Volviendo.....{Fore.RESET}")
                            print("")
                            print("")
                            barra_carga()
                            break
                        case _:
                            print(f"     {Fore.LIGHTRED_EX} ..Error: 'Opción ingresada invalida'.. {Fore.RESET}")
                            msvcrt.getch()
            elif cod in supervisor_lista:
                while repite3:    
                    codpsi = supervisor_lista.index(cod)
                    print(f"""{Fore.LIGHTCYAN_EX}
                                        █▄██▄█                                                    █▄██▄█
                                        ▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▐█┼██▌
                                        ▐████▌║                 EDITOR DE USUARIOS               ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌ 
                                        ▐████▌║                    1.-CEDULA                     ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    2. NOMBRE                     ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    3. APELLIDO                   ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    4. EDAD                       ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    5. ESTADO                     ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    6. CORREO                     ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    7. CONTRASEÑA                 ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    S. Atras                      ║▐████▌
                               ,     ,        ╙──────────────────────────────────────────────────╜{Fore.RESET} {Fore.LIGHTRED_EX}
                              (\____/)
                               (_oo_)
                                 (O)
                               __||__          El dragón te guiará por las opciones.
                      []/_______\ [] /
                      / \______/ \/
                    {Fore.RESET}
                    """)
                    op = input("Ingrese la opcion del dato que quiere editar [1-7] o [S]: ")
                    op = op.upper()
                    match op:
                        case '1':
                            supervisor_lista[codpsi+1] = input("              Cedula: ")
                        case '2':
                            supervisor_lista[codpsi+2] = input("              Nombre: ")
                        case '3':
                            supervisor_lista[codpsi+3] = input("              Apellido: ")
                        case '4':
                            supervisor_lista[codpsi+4] = input("              Edad: ")
                        case '5':
                            supervisor_lista[codpsi+5] = input("              Estado: ")
                        case '6':
                            supervisor_lista[codpsi+6] = input("              Correo: ")
                        case '7':
                            supervisor_lista[codpsi+7] = input("              Contraseña: ")
                        case 'S':
                            print("")
                            print(f"                                             {Fore.LIGHTCYAN_EX} .....Volviendo.....{Fore.RESET}")
                            print("")
                            print("")
                            barra_carga()
                            break
                        case _:
                            print(f"     {Fore.LIGHTRED_EX} ..Error: 'Opción ingresada invalida'.. {Fore.RESET}")
                            msvcrt.getch()
            elif cod in administrador_lista:
                while repite3:    
                    codpsi = administrador_lista.index(cod)
                    print(f"""{Fore.LIGHTCYAN_EX}
                                        █▄██▄█                                                    █▄██▄█
                                        ▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▐█┼██▌
                                        ▐████▌║                 EDITOR DE USUARIOS               ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌ 
                                        ▐████▌║                    1.-CEDULA                     ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    2. NOMBRE                     ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    3. APELLIDO                   ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    4. EDAD                       ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    5. ESTADO                     ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    6. CORREO                     ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    7. CONTRASEÑA                 ║▐████▌
                                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                                        ▐████▌║                    S. Atras                      ║▐████▌
                               ,     ,        ╙──────────────────────────────────────────────────╜{Fore.RESET} {Fore.LIGHTRED_EX}
                              (\____/)
                               (_oo_)
                                 (O)
                               __||__          El dragón te guiará por las opciones.
                      []/_______\ [] /
                      / \______/ \/
                    {Fore.RESET}
                    """)
                    op = input("Ingrese la opcion del dato que quiere editar [1-7] o [S]: ")
                    op = op.upper()
                    match op:
                        case '1':
                            administrador_lista[codpsi+1] = input("              Cedula: ")
                        case '2':
                            administrador_lista[codpsi+2] = input("              Nombre: ")
                        case '3':
                            administrador_lista[codpsi+3] = input("              Apellido: ")
                        case '4':
                            administrador_lista[codpsi+4] = input("              Edad: ")
                        case '5':
                            administrador_lista[codpsi+5] = input("              Estado: ")
                        case '6':
                            administrador_lista[codpsi+6] = input("              Correo: ")
                        case '7':
                            administrador_lista[codpsi+7] = input("              Contraseña: ")
                        case 'S':
                            print("")
                            print(f"                                             {Fore.LIGHTCYAN_EX} .....Volviendo.....{Fore.RESET}")
                            print("")
                            print("")
                            barra_carga()
                            break
                        case _:
                            print(f"     {Fore.LIGHTRED_EX} ..Error: 'Opción ingresada invalida'.. {Fore.RESET}")
                            msvcrt.getch()
            else:
                print("El cliente que quiere buscar no existe..")
                break
            break
        except:
            print(f"     {Fore.LIGHTRED_EX} ..Error: 'El codigo debe ser el numero entero positivo'.. {Fore.RESET}")
            msvcrt.getch()


def eliminar_cliente():
    global codigo
    codigo=0
    os.system("cls")
    while True:
        try:
            codigo= int(input("Ingrese el codigo del cliente para eliminar.."))
            while codigo <= 0:
                print(f"{Fore.LIGHTRED_EX}El codigo es invalido{Fore.RESET}")
                codigo= int(input("Ingrese el codigo del cliente para eliminar.."))
            cod = str(codigo)
            cod = "C" + cod
            if cod in usuario_lista:
                codpsi = usuario_lista.index(cod)
                for n in range(0,8):
                    usuario_lista.pop(codpsi)
            elif cod in supervisor_lista:
                codpsi = supervisor_lista.index(cod)
                for n in range(0,8):
                    supervisor_lista.pop(codpsi)
            elif cod in administrador_lista:
                codpsi = administrador_lista.index(cod)
                for n in range(0,8):
                    administrador_lista.pop(codpsi)
            else:
                print("El cliente que quiere eliminar no existe..")
        except:
            print(f"     {Fore.LIGHTRED_EX} ..Error: 'El codigo debe ser el numero entero positivo'.. {Fore.RESET}")
            msvcrt.getch()


def buscar_cliente():
    while True:
        try:
            print("Ingrese el codigo del cliente que quiere buscar..")
            Codigo = int(input())
            while Codigo < 1:
                print("El codigo ingresado es incorrecto..")
                print("Ingrese el codigo del cliente que quiere buscar..")
                Codigo = int(input())
            Codigo = str(Codigo)
            cod = "C" + Codigo
            if cod in usuario_lista:
                codpsi = usuario_lista.index(cod)
                print(f"{Fore.LIGHTGREEN_EX}                          Usuario   {Fore.RESET}")
                print("                 ╔════════════════════════════════╗")
                print("                 ║  Codigo: " + usuario_lista[codpsi] +" "*((33-11)-len(usuario_lista[codpsi])) +"║")
                print("                 ║  Cedula: " + usuario_lista[codpsi+1] +" "*((33-11)-len(usuario_lista[codpsi+1])) +"║")
                print("                 ║  Nombre: " + usuario_lista[codpsi+2] +" "*((33-11)-len(usuario_lista[codpsi+2])) +"║")
                print("                 ║  Apellido: " + usuario_lista[codpsi+3] +" "*((31-11)-len(usuario_lista[codpsi+3])) +"║")
                print("                 ║  Edad: " + usuario_lista[codpsi+4] +" "*((32-8)-len(usuario_lista[codpsi+4])) +"║")
                print("                 ║  Estado: " + usuario_lista[codpsi+5] +" "*((33-11)-len(usuario_lista[codpsi+5])) +"║")
                print("                 ║  Usuario: " + usuario_lista[codpsi+6] +" "*((33-12)-len(usuario_lista[codpsi+6])) +"║")
                print("                 ║  Contraseña: " + usuario_lista[codpsi+7] +" "*((33-15)-len(usuario_lista[codpsi+7])) +"║")
                print("                 ╚════════════════════════════════╝")
            elif cod in supervisor_lista:
                codpsi = supervisor_lista.index(cod)
                print(f"{Fore.LIGHTGREEN_EX}                          Supervisor   {Fore.RESET}")
                print("                 ╔════════════════════════════════╗")
                print("                 ║  Codigo: " + supervisor_lista[codpsi] +" "*((33-11)-len(supervisor_lista[codpsi])) +"║")
                print("                 ║  Cedula: " + supervisor_lista[codpsi+1] +" "*((33-11)-len(supervisor_lista[codpsi+1])) +"║")
                print("                 ║  Nombre: " + supervisor_lista[codpsi+2] +" "*((33-11)-len(supervisor_lista[codpsi+2])) +"║")
                print("                 ║  Apellido: " + supervisor_lista[codpsi+3] +" "*((31-11)-len(supervisor_lista[codpsi+3])) +"║")
                print("                 ║  Edad: " + supervisor_lista[codpsi+4] +" "*((32-8)-len(supervisor_lista[codpsi+4])) +"║")
                print("                 ║  Estado: " + supervisor_lista[codpsi+5] +" "*((33-11)-len(supervisor_lista[codpsi+5])) +"║")
                print("                 ║  Usuario: " + supervisor_lista[codpsi+6] +" "*((33-12)-len(supervisor_lista[codpsi+6])) +"║")
                print("                 ║  Contraseña: " + supervisor_lista[codpsi+7] +" "*((33-15)-len(supervisor_lista[codpsi+7])) +"║")
                print("                 ╚════════════════════════════════╝")
            elif cod in administrador_lista:
                codpsi = administrador_lista.index(cod)
                print(f"{Fore.LIGHTGREEN_EX}                          Usuario   {Fore.RESET}")
                print("                 ╔════════════════════════════════╗")
                print("                 ║  Codigo: " + administrador_lista[codpsi] +" "*((33-11)-len(administrador_lista[codpsi])) +"║")
                print("                 ║  Cedula: " + administrador_lista[codpsi+1] +" "*((33-11)-len(administrador_lista[codpsi+1])) +"║")
                print("                 ║  Nombre: " + administrador_lista[codpsi+2] +" "*((33-11)-len(administrador_lista[codpsi+2])) +"║")
                print("                 ║  Apellido: " + administrador_lista[codpsi+3] +" "*((31-11)-len(administrador_lista[codpsi+3])) +"║")
                print("                 ║  Edad: " + administrador_lista[codpsi+4] +" "*((32-8)-len(administrador_lista[codpsi+4])) +"║")
                print("                 ║  Estado: " + administrador_lista[codpsi+5] +" "*((33-11)-len(administrador_lista[codpsi+5])) +"║")
                print("                 ║  Usuario: " + administrador_lista[codpsi+6] +" "*((33-12)-len(administrador_lista[codpsi+6])) +"║")
                print("                 ║  Contraseña: " + administrador_lista[codpsi+7] +" "*((33-15)-len(administrador_lista[codpsi+7])) +"║")
                print("                 ╚════════════════════════════════╝")
            else:
                print("El cliente que quiere buscar no existe..")
            msvcrt.getch()
            os.system("cls")
            break
        except:
            print(f"     {Fore.LIGHTRED_EX} ..Error: 'El codigo debe ser el numero entero positivo'.. {Fore.RESET}")
            msvcrt.getch()


def mostrar_usuario():
    print(f"{Fore.LIGHTGREEN_EX}                         Lista De Usuarios   {Fore.RESET}")
    for x in range (0,len(usuario_lista)):
        if x % 8 ==0:
            print("                 ╔════════════════════════════════╗")
            print("                 ║  Codigo: " + usuario_lista[x] +" "*((33-11)-len(usuario_lista[x])) +"║")
            print("                 ║  Cedula: " + usuario_lista[x+1] +" "*((33-11)-len(usuario_lista[x+1])) +"║")
            print("                 ║  Nombre: " + usuario_lista[x+2] +" "*((33-11)-len(usuario_lista[x+2])) +"║")
            print("                 ║  Apellido: " + usuario_lista[x+3] +" "*((31-11)-len(usuario_lista[x+3])) +"║")
            print("                 ║  Edad: " + usuario_lista[x+4] +" "*((32-8)-len(usuario_lista[x+4])) +"║")
            print("                 ║  Estado: " + usuario_lista[x+5] +" "*((33-11)-len(usuario_lista[x+5])) +"║")
            print("                 ║  Usuario: " + usuario_lista[x+6] +" "*((33-12)-len(usuario_lista[x+6])) +"║")
            print("                 ║  Contraseña: " + usuario_lista[x+7] +" "*((33-15)-len(usuario_lista[x+7])) +"║")
            print("                 ╚════════════════════════════════╝")
    print(f"{Fore.LIGHTGREEN_EX}                         Lista De Supervisor   {Fore.RESET}")
    for y in range (0,len(supervisor_lista)):
        if y % 8 ==0:
            print("                 ╔════════════════════════════════╗")
            print("                 ║  Codigo: " + supervisor_lista[y] +" "*((33-11)-len(supervisor_lista[y])) +"║")
            print("                 ║  Cedula: " + supervisor_lista[y+1] +" "*((33-11)-len(supervisor_lista[y+1])) +"║")
            print("                 ║  Nombre: " + supervisor_lista[y+2] +" "*((33-11)-len(supervisor_lista[y+2])) +"║")
            print("                 ║  Apellido: " + supervisor_lista[y+3] +" "*((31-11)-len(supervisor_lista[y+3])) +"║")
            print("                 ║  Edad: " + supervisor_lista[y+4] +" "*((32-8)-len(supervisor_lista[y+4])) +"║")
            print("                 ║  Estado: " + supervisor_lista[y+5] +" "*((33-11)-len(supervisor_lista[y+5])) +"║")
            print("                 ║  Usuario: " + supervisor_lista[y+6] +" "*((33-12)-len(supervisor_lista[y+6])) +"║")
            print("                 ║  Contraseña: " + supervisor_lista[y+7] +" "*((33-15)-len(supervisor_lista[y+7])) +"║")
            print("                 ╚════════════════════════════════╝")
    print(f"{Fore.LIGHTGREEN_EX}                           Lista De Administrador   {Fore.RESET}")
    for z in range (0,len(administrador_lista)):
        if z % 8 ==0:
            print("                 ╔════════════════════════════════╗")
            print("                 ║  Codigo: " + administrador_lista[z] +" "*((33-11)-len(administrador_lista[z])) +"║")
            print("                 ║  Cedula: " + administrador_lista[z+1] +" "*((33-11)-len(administrador_lista[z+1])) +"║")
            print("                 ║  Nombre: " + administrador_lista[z+2] +" "*((33-11)-len(administrador_lista[z+2])) +"║")
            print("                 ║  Apellido: " + administrador_lista[z+3] +" "*((31-11)-len(administrador_lista[z+3])) +"║")
            print("                 ║  Edad: " + administrador_lista[z+4] +" "*((32-8)-len(administrador_lista[z+4])) +"║")
            print("                 ║  Estado: " + administrador_lista[z+5] +" "*((33-11)-len(administrador_lista[z+5])) +"║")
            print("                 ║  Usuario: " + administrador_lista[z+6] +" "*((33-12)-len(administrador_lista[z+6])) +"║")
            print("                 ║  Contraseña: " + administrador_lista[z+7] +" "*((33-15)-len(administrador_lista[z+7])) +"║")
            print("                 ╚════════════════════════════════╝")
    msvcrt.getch()
    os.system("cls")


def primer_pantalla():
    global op,repite
    op = 0
    os.system("cls")
    logo()
    msvcrt.getch()
    os.system("cls")
    logo_pequeño()
    print(f"""{Fore.LIGHTBLACK_EX}
                                                                    █▄██▄█                                                    █▄██▄█
                                                                    ▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▐█┼██▌{Fore.RESET}
                                                                    ▐████▌║                 {Fore.LIGHTBLUE_EX}Menú de inicio {Fore.RESET}                  ║▐████▌
                                                                    ▐████▌║──────────────────────────────────────────────────║▐████▌ 
                                                                    ▐████▌║                {Fore.YELLOW}1. Inicio de sesión{Fore.RESET}               ║▐████▌
                                                                    ▐████▌║──────────────────────────────────────────────────║▐████▌
                                                                    ▐████▌║               {Fore.YELLOW} S. Salir del programa  {Fore.RESET}           ║▐████▌
                                                                    ▐████▌╙──────────────────────────────────────────────────╜▐████▌{Fore.RESET} 
    """)
    print("")
    op= input(f"{Fore.LIGHTBLACK_EX}         Ingresa La opcion que desea realizar [1-S]:  {Fore.RESET}")
    op = op.upper()
    match op:
        case '1':
            login_seguridad()
        case 'S':
            repite = False
        case _:
            print(f"     {Fore.LIGHTRED_EX} ..Error: 'Opción ingresada invalida'.. {Fore.RESET}")
    msvcrt.getch()


def menu_usuario():
    pass


def menu_supervisor():
    global repite1,op
    repite1=True
    op = 0
    while repite1:
        print(f"""{Fore.LIGHTCYAN_EX}
                        █▄██▄█                                                    █▄██▄█
                        ▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▐█┼██▌
                        ▐████▌║                 Menú de Tecnico                  ║▐████▌
                        ▐████▌║──────────────────────────────────────────────────║▐████▌ 
                        ▐████▌║                1. Registro de incidencias        ║▐████▌
                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                        ▐████▌║                2. Revison de Incidencias         ║▐████▌
                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                        ▐████▌║                3. Lista de tecnicos              ║▐████▌
                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                        ▐████▌║                S. Salir del programa             ║▐████▌
               ,     ,  ▐████▌╙──────────────────────────────────────────────────╜▐████▌{Fore.RESET} 
        """)
        op = input(f"     {Fore.CYAN}Ingrese la opcion que quiere [1-6] y [S]:  {Fore.RESET}")
        op= op.upper()
        match op:
            case '1':
                registros_incidencias()
            case '2':
                Mostrar_incidencias()
            case '3':
                lista_de_tecnicos()
            case 'S':
                print("")
                print(f"                                             {Fore.LIGHTCYAN_EX} .....Cerrando Sesión.....{Fore.RESET}")
                print("")
                print("")
                barra_carga()
                repite1 = False
            case _:
                print(f"     {Fore.LIGHTRED_EX} ..Error: 'Opción ingresada invalida'.. {Fore.RESET}")
                msvcrt.getch()
        os.system("cls")


def menu_administrador():
    global repite1,op
    repite1=True
    op = 0
    while repite1:
        print(f"""{Fore.LIGHTCYAN_EX}
                            █▄██▄█                                                    █▄██▄█
                            ▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▐█┼██▌
                            ▐████▌║                 Menú de Administrador            ║▐████▌
                            ▐████▌║──────────────────────────────────────────────────║▐████▌ 
                            ▐████▌║                1. Registro Personal              ║▐████▌
                            ▐████▌║──────────────────────────────────────────────────║▐████▌
                            ▐████▌║                2. Mostrar Usuarios               ║▐████▌
                            ▐████▌║──────────────────────────────────────────────────║▐████▌
                            ▐████▌║                3. Buscar Usuarios                ║▐████▌
                            ▐████▌║──────────────────────────────────────────────────║▐████▌
                            ▐████▌║                4. Editar Usuarios                ║▐████▌
                            ▐████▌║──────────────────────────────────────────────────║▐████▌
                            ▐████▌║                5. Eliminar Usuarios              ║▐████▌
                            ▐████▌║──────────────────────────────────────────────────║▐████▌
                            ▐████▌║                6. Ver registro de Incidencias    ║▐████▌
                            ▐████▌║──────────────────────────────────────────────────║▐████▌
                            ▐████▌║                S. Cerrar Sesión                  ║▐████▌
                   ,     ,        ╙──────────────────────────────────────────────────╜{Fore.RESET} {Fore.LIGHTRED_EX}
                  (\____/)
                   (_oo_)
                     (O)
                   __||__          El dragón te guiará por las opciones.
          []/_______\ [] /
          / \______/ \/
            {Fore.RESET}
        """)
        op = input(f"     {Fore.CYAN}Ingrese la opcion que quiere [1-6] y [S]:  {Fore.RESET}")
        op= op.upper()
        match op:
            case '1':
                registrar_personal()
            case '2':
                mostrar_usuario()
            case '3':
                buscar_cliente()
            case '4':
                editar_usuario()
            case '5':
                eliminar_cliente()
            case '6':
                registros_incidencias()
            case 'S':
                print("")
                print(f"                                             {Fore.LIGHTCYAN_EX} .....Cerrando Sesión.....{Fore.RESET}")
                print("")
                print("")
                barra_carga()
                repite1 = False
            case _:
                print(f"     {Fore.LIGHTRED_EX} ..Error: 'Opción ingresada invalida'.. {Fore.RESET}")
                msvcrt.getch()
        os.system("cls")


def registrar_personal():
    global repite2 , op
    repite2 = True
    op = 0
    os.system("cls")
    while repite2:
        try:
            print(f"""{Fore.LIGHTCYAN_EX}
                                █▄██▄█                                                    █▄██▄█
                                ▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▐█┼██▌
                                ▐████▌║                  Menú de Registro                ║▐████▌
                                ▐████▌║──────────────────────────────────────────────────║▐████▌ 
                                ▐████▌║                    1. Usuario                    ║▐████▌
                                ▐████▌║──────────────────────────────────────────────────║▐████▌
                                ▐████▌║                    2. Tecnico                    ║▐████▌
                                ▐████▌║──────────────────────────────────────────────────║▐████▌
                                ▐████▌║                    3. Administrador              ║▐████▌
                                ▐████▌║──────────────────────────────────────────────────║▐████▌
                                ▐████▌║                    A. Atras                      ║▐████▌
                       ,     ,        ╙──────────────────────────────────────────────────╜{Fore.RESET} {Fore.LIGHTRED_EX}
                      (\____/)
                       (_oo_)
                         (O)
                       __||__          El dragón te guiará por las opciones.
              []/_______\ [] /
              / \______/ \/
            {Fore.RESET}
            """)
            op = input(f"{Fore.LIGHTCYAN_EX}Ingrese la opción del usuario que desea registrar: {Fore.RESET}")
            op = op.upper()
            match op:
                case '1':
                    registrar_usuario()
                case '2':
                    registrar_supervisor()
                case '3':
                    registrar_administrador()
                case 'S':
                    print("")
                    print(f"                                             {Fore.LIGHTCYAN_EX} .....Volviendo.....{Fore.RESET}")
                    print("")
                    print("")
                    barra_carga()
                    repite2 = False
                case _:
                    print(f"     {Fore.LIGHTRED_EX} ..Error: 'Opción ingresada invalida'.. {Fore.RESET}")
                    msvcrt.getch()
        except:
            print(f"     {Fore.LIGHTRED_EX} ..Error: 'ingrese una opcion que desea registar'.. {Fore.RESET}")
            msvcrt.getch()
        os.system("cls")


def registrar_usuario():
    global repite2,codigo
    repite2 = True
    while repite2:
        try:
            codigo += 1
            codu = str(codigo)
            print("      Ingrese los datos a registrar: ")
            print("")
            usuario_lista.append("C" + codu)
            usuario_lista.append(input("      Cedula: "))
            usuario_lista.append(input("      Nombre: "))
            usuario_lista.append(input("      Apellido: "))
            usuario_lista.append(input("      Edad: "))
            usuario_lista.append(input("      Estado: "))
            print("")
            print("Presione cualquier tecla para continuar")
            msvcrt.getch()
            os.system("cls")
            usuario_lista.append(input("      Ingrese su correo para registrar: "))
            cont = input("      Ingrese una contraseña: ")
            cont1 = input("      Vuelva a ingresar la contraseña: ")
            while not (cont == cont1):
                print(f"{Fore.LIGHTRED_EX}La contraseña introducida no coincide..{Fore.RESET}")
                cont1 = input("      Vuelva a ingresar la contraseña: ")
                os.system("cls")
            usuario_lista.append(cont1)
            os.system("cls")
            print("")
            print(f"{Fore.LIGHTGREEN_EX}                      *EL USUARIO SE REGISTRO CON EXITO*{Fore.RESET}")
            repite2 = False
        except:
            print(f"{Fore.LIGHTRED_EX}     ..Error: 'Ingrese una opcion que desea registar'.. {Fore.RESET}")
            msvcrt.getch()


def registrar_supervisor():
    global repite2,codigo
    repite2 = True
    while repite2:
        try:
            codigo += 1
            codu = str(codigo)
            print("      Ingrese los datos a registrar: ")
            print("")
            supervisor_lista.append("C" + codu)
            supervisor_lista.append(input("      Cedula: "))
            supervisor_lista.append(input("      Nombre: "))
            supervisor_lista.append(input("      Apellido: "))
            supervisor_lista.append(input("      Edad: "))
            supervisor_lista.append(input("      Estado: "))
            print("")
            print("Presione cualquier tecla para continuar")
            msvcrt.getch()
            os.system("cls")
            supervisor_lista.append(input("      Ingrese su correo para registrar: "))
            cont = input("      Ingrese una contraseña: ")
            cont1 = input("      Vuelva a ingresar la contraseña: ")
            while not (cont == cont1):
                print(f"{Fore.LIGHTRED_EX}La contraseña introducida no coincide..{Fore.RESET}")
                cont1 = input("      Vuelva a ingresar la contraseña: ")
                os.system("cls")
            supervisor_lista.append(cont1)
            os.system("cls")
            print("")
            print(f"{Fore.LIGHTGREEN_EX}                      *EL USUARIO SE REGISTRO CON EXITO*{Fore.RESET}")
            repite2 = False
        except:
            print(f"{Fore.LIGHTRED_EX}     ..Error: 'Ingrese una opcion que desea registar'.. {Fore.RESET}")
            msvcrt.getch()


def registrar_administrador():
    global repite2,codigo
    repite2 = True
    while repite2:
        try:
            codigo += 1
            codu = str(codigo)
            print("      Ingrese los datos a registrar: ")
            print("")
            administrador_lista.append("C" + codu)
            administrador_lista.append(input("      Cedula: "))
            administrador_lista.append(input("      Nombre: "))
            administrador_lista.append(input("      Apellido: "))
            administrador_lista.append(input("      Edad: "))
            administrador_lista.append(input("      Estado: "))
            print("")
            print("Presione cualquier tecla para continuar")
            msvcrt.getch()
            os.system("cls")
            administrador_lista.append(input("      Ingrese su correo para registrar: "))
            cont = input("      Ingrese una contraseña: ")
            cont1 = input("      Vuelva a ingresar la contraseña: ")
            while not (cont == cont1):
                print(f"{Fore.LIGHTRED_EX}La contraseña introducida no coincide..{Fore.RESET}")
                cont1 = input("      Vuelva a ingresar la contraseña: ")
                os.system("cls")
            administrador_lista.append(cont1)
            os.system("cls")
            print("")
            print(f"{Fore.LIGHTGREEN_EX}                      *EL USUARIO SE REGISTRO CON EXITO*{Fore.RESET}")
            repite2 = False
            print(administrador_lista)
            msvcrt.getch()
        except:
            print(f"{Fore.LIGHTRED_EX}     ..Error: 'Ingrese una opcion que desea registar'.. {Fore.RESET}")
            msvcrt.getch()


def login_seguridad():
    global nombre,pasw,intentos,session,admi,sup,usu,corr1
    nombre = ""
    pasw = ""
    intentos = 0
    session = 0
    corr1 = 0
    admi = False
    sup = False
    usu = False
    while (intentos<=2 and session<=0):
        os.system("cls")
        logo_pequeño()
        print(f"""{Fore.LIGHTBLACK_EX}
                                   ╔════════════════════════════════════╗
                                   ║                                    ║
                                   ║    CORREO:__________________       ║
                                   ║    COTRASEÑA:_______________       ║
                                   ║                                    ║
                                   ╚════════════════════════════════════╝
         {Fore.RESET}""")  
        nombre=input("INGRESE SU CORREO DE USUARIO: ")
        os.system("cls")
        coarr = nombre.count("@")
        while not (coarr >=1):
            os.system("cls")
            logo_pequeño()
            print(f"""{Fore.LIGHTBLACK_EX}
                                       ╔════════════════════════════════════╗
                                       ║                                    ║
                                       ║    CORREO:__________________       ║
                                       ║    COTRASEÑA:_______________       ║
                                       ║                                    ║
                                       ╚════════════════════════════════════╝
             {Fore.RESET}""")  
            print(f"{Fore.LIGHTRED_EX}Correo invalido..{Fore.RESET}")
            nombre=input("INGRESE SU CORREO DE USUARIO: ")
            os.system("cls")
            coarr = nombre.count("@")
        logo_pequeño()
        print(f"""{Fore.LIGHTBLACK_EX}
                                   ╔════════════════════════════════════╗
                                   ║                                    ║
                                   ║    CORREO:{nombre}{" "*(25-len(nombre))}║
                                   ║    COTRASEÑA:_______________       ║
                                   ║                                    ║
                                   ╚════════════════════════════════════╝
         {Fore.RESET}""")  
        contraseña=stdiomask.getpass("INGRESE SU CONTRASEÑA: ")
        os.system("cls")
        logo_pequeño()
        print(f"""{Fore.LIGHTBLACK_EX}
                                   ╔════════════════════════════════════╗
                                   ║                                    ║
                                   ║    CORREO:{nombre}{" "*(25-len(nombre))}║
                                   ║    COTRASEÑA:{"*"*(len(contraseña))}{" "*(22-(len(contraseña)))}║
                                   ║                                    ║
                                   ╚════════════════════════════════════╝
            {Fore.RESET} """) 
        if (nombre in usuario_lista):
            corr1 = usuario_lista.index(nombre)
            usu = True
        elif (nombre in supervisor_lista):
            corr1 = supervisor_lista.index(nombre)
            sup = True
        elif (nombre in administrador_lista):
            corr1 = administrador_lista.index(nombre)
            admi = True
        if (nombre==(usuario_lista[corr1]) and contraseña==(usuario_lista[corr1 + 1])) or (nombre==(administrador_lista[corr1]) and contraseña==(administrador_lista[corr1 + 1])) or (nombre==(supervisor_lista[corr1]) and contraseña==(supervisor_lista[corr1 + 1])):
            session +=1
            barra_carga()
            os.system("cls")
            if (nombre in usuario_lista):
                menu_usuario()
            elif (nombre in supervisor_lista):
                menu_supervisor()
            elif (nombre in administrador_lista):
                menu_administrador()
        else:
            intentos += 1
            os.system("cls")
            print(Fore.LIGHTRED_EX+"\t\t\t\t\t\t╔═════════════════════════════════╗")
            print("\t\t\t\t\t\t║ USUARIO O CONTRASEÑA INCORRECTA ║")
            print("\t\t\t\t\t\t╚═════════════════════════════════╝")
            print()
            print()
            print("PRESIONE UNA TECLA PARA CONTINUAR")
            msvcrt.getch()
            os.system("cls")
    if (intentos==3):
        os.system("cls")
        print(" \t\t\t\t\t\t╔═════════════════════════════════════════════════════════╗")
        print(" \t\t\t\t\t\t║            SOBREPASO EL NUMERO DE INTENTOS              ║")
        print(" \t\t\t\t\t\t╚═════════════════════════════════════════════════════════╝"+ Fore.RESET)
        print(" ")
        print(" ")
        print("PRESIONE UNA TECLA PARA CONTINUAR")
        msvcrt.getch()
        os.system("cls")
# PROCESO
while repite:
    primer_pantalla()