from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Yazzhek:Yazhek5288@localhost:3306/java_db'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class InstrumentModel(db.Model):
    __tablename__ = 'instruments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String(length=80))
    model = db.Column(db.String(length=80))
    year_of_release = db.Column(db.Integer)

    def __init__(self, brand="brand", model="model", year_of_release=2001):
        self.brand = brand
        self.model = model
        self.year_of_release = year_of_release

    def __str__(self):
        return str(self.__dict__)


class InstrumentSchema(ma.Schema):
    class Meta:
        fields = ('brand', 'model', 'year_of_release')


instrument_schema = InstrumentSchema()
instruments_schema = InstrumentSchema(many=True)
db.create_all()


@app.route("/chemistry_instruments/", methods=["POST"])
def add_instrument():
    brand = request.get_json()["brand"]
    model = request.get_json()["model"]
    year_of_release = request.get_json()["year_of_release"]
    new_instrument = InstrumentModel(brand, model, year_of_release)
    db.session.add(new_instrument)
    db.session.commit()
    return jsonify(request.json)


@app.route("/chemistry_instruments/", methods=["GET"])
def get_instruments():
    all_instruments = InstrumentModel.query.all()
    return_info = instruments_schema.dump(all_instruments)
    return jsonify(return_info.data)


@app.route("/chemistry_instruments/<id>", methods=["GET"])
def get_instrument_by_id(id):
    instrument = InstrumentModel.query.get(id)
    return instrument_schema.jsonify(instrument)


@app.route("/chemistry_instruments/<id>", methods=["PUT"])
def replace_instrument(id):
    instrument = InstrumentModel.query.get(id)
    instrument.brand = request.json["brand"]
    instrument.model = request.json["model"]
    instrument.year_of_release = request.json["year_of_release"]
    db.session.commit()
    return instrument_schema.jsonify(request.json)


@app.route("/chemistry_instruments/<id>", methods=["DELETE"])
def delete_instrument(id):
    instrument = InstrumentModel.query.get(id)
    db.session.delete(instrument)
    db.session.commit()
    return instrument_schema.jsonify(instrument)


if __name__ == '__main__':
    app.run()
