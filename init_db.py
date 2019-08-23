#!/usr/bin/env python3

from jhdag2019 import db, Party

db.drop_all()

db.create_all()

party_1 = Party(name="Zeus WPI", score=10)
party_2 = Party(name="WiNA", score=1)

db.session.add(party_1)
db.session.add(party_2)
db.session.commit()
