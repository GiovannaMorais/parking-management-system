# Gestão de Estacionamento

Este é um projeto de sistema de **Gestão de Estacionamento**, desenvolvido com **Flask (Python)** para o backend e **HTML, CSS e JavaScript** para o frontend. O sistema permite gerenciar veículos e vagas de estacionamento, fornecendo funcionalidades para criar, listar, atualizar e excluir veículos e vagas.

## Tecnologias Utilizadas

### Backend
- **[Flask](https://flask.palletsprojects.com/)**: Microframework para desenvolvimento web em Python.
- **[Flask-CORS](https://flask-cors.readthedocs.io/)**: Para habilitar Cross-Origin Resource Sharing (CORS).
- **[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)**: Integração com banco de dados usando SQLAlchemy.
- **[Flask-RESTful](https://flask-restful.readthedocs.io/)**: Extensão para criação de APIs RESTful.
- **[Flask-Migrate](https://flask-migrate.readthedocs.io/)**: Controle de migrações de banco de dados.

### Frontend
- **HTML5**: Estrutura das páginas web.
- **CSS3**: Estilização das páginas.
- **JavaScript**: Interatividade e integração com o backend via API.

### Banco de Dados
- **SQLite** (ou outro banco de dados à sua escolha): Banco de dados leve e rápido para o projeto.


## Estrutura do Projeto

```
parking_management/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── config.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
└──
```

# Instruções do projeto


## Instalação

### Backend

1. Clone o repositório:
   ```bash
   git clone https://github.com/GiovannaMorais/parking-management-system.git

   cd parking-management-system/backend

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt

3. Execute o servidor Flask:
   ```bash
    export FLASK_APP=app.py

    flask run

## Rotas da API

### Veículos

- `POST /vehicles` - Cria um novo veículo.

- `GET /vehicles` - Retorna todos os veículos.

- `PUT /vehicles/:id` - Atualiza um veículo existente.

- `DELETE /vehicles/:id` - Deleta um veículo existente.

### Vagas de Estacionamento

- `POST /parking_spots` - Cria uma nova vaga.

- `GET /parking_spots` - Retorna todas as vagas.

- `POST /parking_spots/:spot_id/assign` - Atribui um veículo a uma vaga.

- `POST /parking_spots/:spot_id/remove` - Remove um veículo de uma vaga.

## Contribuição

Contribuições são bem-vindas! Para contribuir com o projeto, siga os passos abaixo:

1. **Fork** o repositório.
2. Crie uma **branch** para sua funcionalidade ou correção de bug:
   ```bash
   git checkout -b minha-nova-funcionalidade
