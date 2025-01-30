## React-Vite-Flask-Boilerplate

This is a boilerplate to set up a full-stack application with:

- **Frontend**: React (with Vite for fast development)
- **Backend**: Flask (Python-based web framework)
- **Docker**: For containerization and easy deployment

This boilerplate helps quickly create an application, with an easy setup process for quick use.

# Prerequisites
Install the following:
- [Docker](https://www.docker.com/get-started) (version 20.x or higher)
- [Docker Compose](https://docs.docker.com/compose/install/) (version 1.27.0 or higher)

# How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/keeryno4/react-vite-flask-boilerplate.git
   cd react-vite-flask-boilerplate
2. Open Docker Desktop
3. Run the Boilerplate
   ```bash
   docker-compose up --build

# Project Structure
```markdown.
├── backend/                # Flask backend code
│   ├── app/                # Flask app files
│   └── Dockerfile.backend  # Dockerfile for backend
├── frontend/               # React frontend code
│   ├── src/                # React source files
│   ├── public/             # Public assets
│   └── Dockerfile.frontend # Dockerfile for frontend
└── docker-compose.yml      # Docker Compose configuration
