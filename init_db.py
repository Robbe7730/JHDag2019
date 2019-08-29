#!/usr/bin/env python3

from jhdag2019 import db, Party, Message

db.drop_all()

db.create_all()

party_1 = Party(name="Partij A", score=10)
party_2 = Party(name="Partij B", score=1)

message_1 = Message(title="Titel", content="Dit is een bericht met een boodschap en kan misschien wel iets belangrijk bevatten maar nu moet ik gewoon een lange text hebben die het scherm een beetje opvult dus typ ik hier maar wat bij aan...") 

db.session.add(party_1)
db.session.add(party_2)
db.session.add(message_1)
db.session.commit()
