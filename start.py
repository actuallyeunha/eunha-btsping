from subprocess import Popen
import sys
from console import console

if __name__ == '__main__': 
	console.print("[info][NovaLoop - BTSPing][text]: Iniciando...\n")
	p = Popen("python bapp.py", shell=True) # Primeira inicializacao do script.
	p.wait()

	while True: #Caso algo de errado, o loop comeca realmente.
		console.print("[info][NovaLoop - BTSPing][text]: Oh no, alguma coisa deu errado! Reiniciando...\n")
		p = Popen("python bapp.py", shell=True)
		p.wait()