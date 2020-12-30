#Enigma bot query script
#Process enigma encryptions/decryptions and send to core.
import pyenigma
#Build ENIGMA
from enigma.machine import EnigmaMachine #Stupid imports that don't really work. :/

machine = EnigmaMachine.from_key_sheet(
       rotors='IV V I',
       reflector='B',
       ring_settings='21 15 16',
       plugboard_settings='AC LS BQ WN MY UV FJ PZ TR OK')

def encrypt(body):
   #text
   machine.set_display('GKW')
   output = machine.process_text(body)
   return output
#Set the daily rotors
#machine.set_display('GKW')
#toEncrypt = input("Enter secret")#Text to encrypt
#encryptedMsg = machine.process_text(toEncrypt, replace_char='G')
#print(encryptedMsg)