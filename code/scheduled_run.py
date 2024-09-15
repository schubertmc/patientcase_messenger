#engine.py
import os
import random 
import ankiaccess
import message_generation
import messaging
import time 
from datetime import datetime

print("Startingg.")
print(datetime.now())

collection_path = "..../Anki2/User 1/collection.anki2"
search_string = '"deck:1 M2" rated:5:1 prop:d>0.5'

## Get Anki cards
### #Run 
print("Getting cards...")
target_cards = ankiaccess.getCards(collection_path=collection_path, 
                        search_string=search_string)

random_keys = random.sample(list(target_cards.keys()),3)

bound_text = ""
for key in random_keys:
    cardtext = ankiaccess.getCardString(target_cards[key])
    #print(cardtext,key)
    bound_text += "------\n\n" + cardtext

bound_text
print("Creating vignette...")
start_time = datetime.now()
generated_messages = message_generation.generateVignette(bound_text)
time_end = datetime.now()
print(time_end-start_time)
q1 = generated_messages["vignette"]
a2 = generated_messages["explanation"]
org = generated_messages["flash_card"]

print(a2)

print("Sending...")

starter_sentences_de = [
    "**🚨 Alarm:** 🆕 Neuer Patientenankunft steht bevor!",
    "**👨‍⚕️ Eingehender Patient:** 🚪 Bereiten Sie den Untersuchungsraum sofort vor!",
    "**🚑 Neue Aufnahme:** Patient ist auf dem Weg in die Notaufnahme. Machen Sie sich bereit!",
    "**⚠️ Dringend:** Sofortige Aufnahme des Patienten erforderlich. Handeln Sie schnell!",
    "**🔔 Hinweis:** Neuer Patient erwartet in Kürze. Bleiben Sie wachsam!",
    "**📢 Achtung:** Eingehender Patient. Bitte sofort reagieren!",
    "**🆘 Notfall:** Kritischer Patient unterwegs. Priorität auf schnelle Reaktion!",
    "**🏥 Priorität:** Neuer Patientenankunft unmittelbar bevorstehend. Alle Mann an Deck!",
    "**🚨 Alarm:** Bereiten Sie sich auf die Beurteilung eines neuen Patienten vor. Zeit zu glänzen!",
    "**🔥 Erforderliche Aktion:** Neuer Patient kommt herein. Bereiten Sie alle Dienste vor. Auf geht's!"
]
alert = random.sample(starter_sentences, 1)[0]
messaging.send(alert)
time.sleep(5)


time_s = 100


try: 
    messaging.send(q1)
    time.sleep(time_s)
except Exception as e:
    messaging.send(str(e))

try: 
    empty_space = "-----\n-----\n-----\n-----\n-----\n-----\n-----"
    messaging.send(empty_space + a2)
    time.sleep(time_s/2)
except Exception as e:
    messaging.send(str(e))

try:
    empty_space = "-----\n-----\n-----\n-----\n-----\n-----\n-----"
    messaging.send(empty_space + org)
except Exception as e:
    messaging.send(str(e))

a2
