# utils.py

import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print("\033[1;34m")
    print("██████╗ ██████╗     ██████╗  █████╗ ")
    print("██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗")
    print("██████╔╝██████╔╝    ██████╔╝███████║")
    print("██╔═══╝ ██╔═══╝     ██╔═══╝ ██╔══██║")
    print("██║     ██║         ██║     ██║  ██║")
    print("╚═╝     ╚═╝         ╚═╝     ╚═╝  ╚═╝")
    print("           \033[94mR.R\033[1;34m")
    print("\033[0;94m        Porn.Down.Operation\033[0m")