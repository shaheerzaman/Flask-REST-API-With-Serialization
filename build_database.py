import os
from datetime import datetime
from config import db
from models import Person, Note

#Data to initialzie database with
PEOPLE = [
    {
        'fname':'Doug',
        'lname':'Farrell',
        'notes':[
            ('cool, a mini-blogging application', '2019-01-06'),
            ('This could be useful', '2019-01-08'),
            ('Well, sort of useful', '2019-03-06')
        ]
    },
    {
        'fname':'kent',
        'lname':'Brockman',
        'notes': [
            ('I am goind to make really profound observations', '2019-03-18'),
            ('May be they will be more obvious than i thought', '2019-02-06')
        ]
    },
    {
        'fname':'Bunny',
        'lname':'Eater',
        'notes':[
            ('Has anyone seen my easter eggs','2019-01-07'),
            ('I am really late delivering these', '2019-04-06')
        ]
    }

]

if os.path.exists('people.db'):
    os.remove()

#create the database
db.create_all()

for person in PEOPLE:
    p = Person(lname=person.get('lname'), fname=peson.get('fname'))
    
    for note in person.get('notes'):
        content, timestamp = note
        p.notes.append(
            Note(content=content,
            timestamp=datetime.strptime(timestamp, '%Y-%m-%d'))
        )
    db.session.add(p)
db.session.commit()