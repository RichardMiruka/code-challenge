#!/usr/bin/env python3

from random import choice as rc, randint 

import random
from faker import Faker

from app import app
from models import db, Hero , Power, hero_power

fake = Faker()

def make_hero():

    Hero.query.delete()
    
    heroes = []
    for i in range(50):
        h= Hero(name=fake.name(), super_name = fake.name())
        heroes.append(h)

    db.session.add_all(heroes)
    db.session.commit()

def make_power():
    Power.query.delete()
    power = []
    for i in range(50):
        name = fake.name()
        description = fake.text(max_nb_chars=20)  # Generate a text with at least 20 characters
        while len(description) < 20:
            description = fake.text(max_nb_chars=20)
        p = Power(name=name, description=description)
        power.append(p)

    db.session.add_all(power)
    db.session.commit()


# def make_powers():
#     Hero_p.query.delete()
#     strengths = ["Strong","Weak","Average"]
#     hero_power = []   
#     for i in range(50):
#         h_p= Hero_p(strength = random.choice(strengths),hero_id = randint(1,20),power_id = randint(1,20))
#         hero_power.append(h_p)

#     db.session.add_all(hero_power)
    
    
#     db.session.commit()

def make_hero_power():
    combination = set()
    strengths = ["Strong","Weak","Average"]
    for _ in range(30):
        hero_id = randint(1,20)
        power_id = randint(1,20)
        strength = rc(strengths)

        if (hero_id,power_id,strength) in combination:
            continue
        combination.add((hero_id,power_id,strength))
        hero_power_data = {
            "hero_id": hero_id,
            "power_id": power_id,
            "strength": strength

        }

        statement = db.insert(hero_power).values(hero_power_data)

        db.session.execute(statement)
        db.session.commit()





if __name__ == '__main__':
    with app.app_context():
        make_hero()
        make_power()
        # make_powers()
        make_hero_power()