#!/usr/bin/env python3
from flask import Flask
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Hero, Power, hero_power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

@app.route('/')
def home():
    return '<h1>Welcome home</h1>'

class Index (Resource):
    def get(self):
        response_dict={
            'Status':'success'
        }
        response = make_response(
            jsonify(response_dict
                    ),
                    200,
            
        )
        return response
api.add_resource(Index,'/')

#GET(heroes)

class Heroes(Resource):
    def get(self):
        #heros= [hero.to_dict() for hero in Hero.query.all()]
        heroes = []
        for hero in Hero.query.all():
            hero_data = {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name,
                "created_at": hero.created_at
            }
            heroes.append(hero_data)
        return make_response(jsonify(heroes), 200)
api.add_resource(Heroes, '/heroes')

#GET (/heroes/:id)

class HeroesById(Resource):
    def get(self,id):
        hero = Hero.query.filter_by(id=id).first()
        if hero:
             hero_data = {
                    "id": hero.id,
                    "name": hero.name,
                    "super_name": hero.super_name,
                    "powers": [
                        {
                            "id": power.id,
                            "name": power.name,
                            "description": power.description
                        }
                        for power in hero.powers
                    ]
                }
             return make_response(jsonify(hero_data), 200)
        else:
            response_dict = {
                "error": "Hero not found"
            }
            response = make_response(jsonify(response_dict), 404)
            return response
          
api.add_resource(HeroesById, '/heroes:<int:id>')

                
            
if __name__ == '__main__':
    app.run(port=5555)
