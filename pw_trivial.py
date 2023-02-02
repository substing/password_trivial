#visual libraries
import pyfiglet
from termcolor import colored
from alive_progress import alive_bar


def header():
	t = pyfiglet.figlet_format("Password checker", font = "digital", justify = "center" )
	print()
	print(colored(t, attrs = ['bold']))
	print("""
		Tests if a password is trivially cracked by a common password list.
		v 1.0.
		written by Substing as a project for the OSSSSC.
""")
	print()

def main():
	
	header()
	#open file and get vulnerable passwords
	rockyou = open('rockyou.txt', 'r', encoding = "ISO-8859-1")

	upassword = input("\nEnter your password: ")
	vuln_passwds = []
	#this line takes a decent amount of time
	#vuln_passwds = [row.strip('\n') for row in rockyou]
	print(colored("Processing...", 'blue'))
	for row in rockyou:
		vuln_passwds.append(row.strip('\n'))



	if upassword in vuln_passwds:
		print(colored("\n[!] Password is trivially cracked!\n", 'red'))
		exit()
	print(colored("\n[+] Password is not trivially cracked.\n", 'green'))


main()