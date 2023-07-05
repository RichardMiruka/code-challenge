from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

hero_power = db.Table(
    'hero_powers',
    db.Column('hero_id', db.Integer, db.ForeignKey('heroes.id'), primary_key=True),
    db.Column('power_id', db.Integer, db.ForeignKey('powers.id'), primary_key=True),
    db.Column("strength", db.String),
    db.Column("created_at", db.DateTime, server_default=db.func.now()),
    db.Column("updated_at", db.DateTime, onupdate=db.func.now())
)

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # hero_ps = db.relationship("Hero_p", backref="hero")
    powers = db.relationship(
        'Power',
        secondary=hero_power, 
        back_populates='heroes'
    )
    
class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # hero_ps = db.relationship("Hero_p", backref="power")
    heroes = db.relationship(
        'Hero',
        secondary=hero_power, 
        back_populates='powers'
    )
    
