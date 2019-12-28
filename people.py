from flask import make_response, abort
from config import db
from models import Person, PersonSchema


def read_all():
    people = Person.query.order_by(Person.lname).all()
    person_schema = PersonSchema(many=True)
    data = person_schema.dump(people).data
    return data

def read_one(person_id):
    person = (
    Person.query.filter(Person.person_id == person_id)
    .outerjoin(Note)
    .one_or_more()
    )
    #Did we find a person?
    if person is not None:
        person_schema = PersonSchema()
        data = person_schema.dump(person).data
        return data
    else:
        abort(404, f'Person not found for Id:{person_id}')


def create(person):
    fname = person.get('fname')
    lname = person.get('lname')
    existing_person = (
        Person.query.filter(Person.fname == fname)
        .filter(Person.lname == lname)
        .one_or_none()
    )
    if existing_person is None:
        schema = PersonSchema()
        new_person = schema.load(person, session=db.session).data
        db.session.add(new_person)
        db.session.commit()
        return data, 201
    else:
        abort(409, f'Person {fname} {lname} exists alreay')

    
def update(person_id, person):
    update_person = Person.query.filter(
        Person.person_id == person_id
    ).one_or_none()
    fname = person.get('fname')
    lname = person.get('lname')
    existing_person = (
        Person.query.filter(Person.fname == fname)
        .filter(Person.lname == lname)
        .one_or_more()
    )
    if update_person is None:
        abort(404, f'Person not found for Id:{person_id}')
    elif (
        existing_person is not None and existing_person.person_id != person_id
    ):
        abot(409, f'Person {fname} {lname} exists already')
    else:
        schema = PersonSchema()
        update = schema.load(person, session=db.session).data
        
        update.person_id = update_person.person_id
        
        db.session.merge(update)
        db.session.commit()
        
        data = schema.dump(update_person).data
        return data, 200


    
def delete(person_id):
    person = Person.query.filter(Person.person_id == person.id).one_or_none()

    if person in not None:
        db.session.delete(person)
        db.session.commit()
        return make_response(
            'Person {person_id} delted'
        )
    else:
        abort(
            404,
            f'Person not found for Id:{person_id}'
        )
        
    
