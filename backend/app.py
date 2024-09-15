from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Vehicle, ParkingSpot
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)  # Adicione esta linha para habilitar CORS

@app.before_first_request
def create_tables():
    db.create_all()

# Create a new vehicle
@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    data = request.get_json()
    new_vehicle = Vehicle(
        make=data['make'],
        model=data['model'],
        year=data['year'],
        price=data['price']
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify({'id': new_vehicle.id}), 201

# Read all vehicles
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    output = []
    for vehicle in vehicles:
        vehicle_data = {
            'id': vehicle.id,
            'make': vehicle.make,
            'model': vehicle.model,
            'year': vehicle.year,
            'price': vehicle.price
        }
        output.append(vehicle_data)
    return jsonify(output)

# Update a vehicle
@app.route('/vehicles/<int:id>', methods=['PUT'])
def update_vehicle(id):
    data = request.get_json()
    vehicle = Vehicle.query.get(id)
    if not vehicle:
        return jsonify({'message': 'Vehicle not found'}), 404

    vehicle.make = data['make']
    vehicle.model = data['model']
    vehicle.year = data['year']
    vehicle.price = data['price']
    db.session.commit()
    return jsonify({'message': 'Vehicle updated'})

# Delete a vehicle
@app.route('/vehicles/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if not vehicle:
        return jsonify({'message': 'Vehicle not found'}), 404

    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({'message': 'Vehicle deleted'})

# Create a new parking spot
@app.route('/parking_spots', methods=['POST'])
def create_parking_spot():
    data = request.get_json()
    new_spot = ParkingSpot(
        spot_number=data['spot_number']
    )
    db.session.add(new_spot)
    db.session.commit()
    return jsonify({'id': new_spot.id}), 201

# Read all parking spots
@app.route('/parking_spots', methods=['GET'])
def get_parking_spots():
    spots = ParkingSpot.query.all()
    output = []
    for spot in spots:
        spot_data = {
            'id': spot.id,
            'spot_number': spot.spot_number,
            'is_occupied': spot.is_occupied
        }
        output.append(spot_data)
    return jsonify(output)

# Assign a vehicle to a parking spot
@app.route('/parking_spots/<int:spot_id>/assign', methods=['POST'])
def assign_vehicle_to_spot(spot_id):
    data = request.get_json()
    spot = ParkingSpot.query.get(spot_id)
    if not spot:
        return jsonify({'message': 'Parking spot not found'}), 404

    vehicle = Vehicle.query.get(data['vehicle_id'])
    if not vehicle:
        return jsonify({'message': 'Vehicle not found'}), 404

    if spot.is_occupied:
        return jsonify({'message': 'Parking spot is already occupied'}), 400

    spot.is_occupied = True
    vehicle.parking_spot = spot
    db.session.commit()
    return jsonify({'message': 'Vehicle assigned to parking spot'})

# Remove a vehicle from a parking spot
@app.route('/parking_spots/<int:spot_id>/remove', methods=['POST'])
def remove_vehicle_from_spot(spot_id):
    spot = ParkingSpot.query.get(spot_id)
    if not spot:
        return jsonify({'message': 'Parking spot not found'}), 404

    if not spot.is_occupied:
        return jsonify({'message': 'Parking spot is not occupied'}), 400

    vehicle = spot.vehicle
    spot.is_occupied = False
    vehicle.parking_spot = None
    db.session.commit()
    return jsonify({'message': 'Vehicle removed from parking spot'})

if __name__ == '__main__':
    app.run(debug=True)
