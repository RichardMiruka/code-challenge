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
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)

# add any models you may need. 