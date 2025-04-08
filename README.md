## React-Vite-Flask-Boilerplate

This is a boilerplate to set up a full-stack application with:

- **Frontend**: React (with Vite and TailwindCSS for fast development)
- **Backend**: Flask (Python-based web framework)
- **Docker**: For containerization, local database creation and easy deployment
- **Vercel**: For frontend deployment
- **Supabase**: For PostgresSQL database hosting

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

## How to Use
- Reset the local database with init.sql
   ```bash
   docker compose down -v
- Check local database via MySQL Workbench:
   - Open MySQL Workbench
   - Create a connection to port 3307 with the login info `root` and `password`
- Create Vercel predeployment with `vercel` or production deployment with `vercel --prod`

# Project Structure
```markdown.
├── api/                    # Flask backend code
│   ├── app/                # Flask app files
│   └── Dockerfile.backend  # Dockerfile for backend
├── frontend/               # React frontend code
│   ├── src/                # React source files
│   ├── public/             # Public assets
│   └── Dockerfile.frontend # Dockerfile for frontend
├── database/               # MySQL database code
│   ├── database_connector  # Create Supabase connection
│   ├── init.sql            # SQL file to initialize local database
└── docker-compose.yml      # Docker Compose configuration
└── vercel.json             # Vercel configurations
