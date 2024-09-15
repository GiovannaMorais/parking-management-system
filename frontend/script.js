const url = 'http://localhost:5000';

document.getElementById('create-vehicle-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const make = document.getElementById('make').value;
  const model = document.getElementById('model').value;
  const year = document.getElementById('year').value;
  const price = document.getElementById('price').value;

  const response = await fetch(`${url}/vehicles`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ make, model, year, price })
  });

  if (response.ok) {
    alert('Veículo criado com sucesso!');
    document.getElementById('create-vehicle-form').reset();
    loadVehicles();
  } else {
    alert('Erro ao criar veículo.');
  }
});

document.getElementById('get-vehicles').addEventListener('click', loadVehicles);

async function loadVehicles() {
  const response = await fetch(`${url}/vehicles`);
  const vehicles = await response.json();
  const vehiclesList = document.getElementById('vehicles-list');
  const noVehiclesMessage = document.getElementById('no-vehicles');
  vehiclesList.innerHTML = '';
  if (vehicles.length === 0) {
    noVehiclesMessage.classList.add('visible');
  } else {
    noVehiclesMessage.classList.remove('visible');
    vehicles.forEach(vehicle => {
      const li = document.createElement('li');
      li.innerHTML = `<span>${vehicle.make} ${vehicle.model} (${vehicle.year}) - $${vehicle.price}</span>`;
      const deleteButton = document.createElement('button');
      deleteButton.textContent = 'Deletar';
      deleteButton.addEventListener('click', async () => {
        const deleteResponse = await fetch(`${url}/vehicles/${vehicle.id}`, {
          method: 'DELETE'
        });
        if (deleteResponse.ok) {
          alert('Veículo deletado com sucesso!');
          loadVehicles();
        } else {
          alert('Erro ao deletar veículo.');
        }
      });
      li.appendChild(deleteButton);
      vehiclesList.appendChild(li);
    });
  }
}

document.getElementById('create-parking-spot-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const spotNumber = document.getElementById('spot-number').value;

  const response = await fetch(`${url}/parking_spots`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ spot_number: spotNumber })
  });

  if (response.ok) {
    alert('Vaga criada com sucesso!');
    document.getElementById('create-parking-spot-form').reset();
    loadParkingSpots();
  } else {
    alert('Erro ao criar vaga.');
  }
});

document.getElementById('get-parking-spots').addEventListener('click', loadParkingSpots);

async function loadParkingSpots() {
  const response = await fetch(`${url}/parking_spots`);
  const spots = await response.json();
  const spotsList = document.getElementById('parking-spots-list');
  const noParkingSpotsMessage = document.getElementById('no-parking-spots');
  spotsList.innerHTML = '';
  if (spots.length === 0) {
    noParkingSpotsMessage.classList.add('visible');
  } else {
    noParkingSpotsMessage.classList.remove('visible');
    spots.forEach(spot => {
      const li = document.createElement('li');
      li.innerHTML = `<span>Vaga ${spot.spot_number} - ${spot.is_occupied ? 'Ocupada' : 'Livre'}</span>`;
      const deleteButton = document.createElement('button');
      deleteButton.textContent = 'Deletar';
      deleteButton.addEventListener('click', async () => {
        const deleteResponse = await fetch(`${url}/parking_spots/${spot.id}`, {
          method: 'DELETE'
        });
        if (deleteResponse.ok) {
          alert('Vaga deletada com sucesso!');
          loadParkingSpots();
        } else {
          alert('Erro ao deletar vaga.');
        }
      });
      li.appendChild(deleteButton);
      spotsList.appendChild(li);
    });
  }
}
