# Django Template

This is a **Django and Docker Integration Template** using **UV python package manager**.

![Django](./django.jpg)

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Other:** Docker,Uv package manager, Shell

you can also use integrate with:

- **Frontend:** React, Next.js, TypeScript
- **Caching/Message Broker:** Redis
- **Web Server/Reverse Proxy:** Nginx

## Setup

To run project locally, in production or using Docker you need to setup environment variables first. Rename the `.env.example` to `.env` and fill the required values.

You can also use this command in linux for ease of use to have `.env` file in `/backend` directory as well:

```bash
ln -s ../.env backend/.env
```

### Backend Setup (Django)

1. Install dependencies:
First install [uv package manager](https://docs.astral.sh/uv/getting-started/installation/) (feel free to read [uv documents](https://docs.astral.sh/uv/getting-started/))

   ```bash
   pip install uv
   ```

2. install packages:

   ```bash
   cd backend
   uv sync
   ```

3. Run migrations:

   ```bash
   uv run manage.py makemigrations
   uv run manage.py migrate
   ```

4. Start the backend server:

   ```bash
   uv run manage.py runserver
   ```

### Running with Docker

- Just build and start all services **(recommended)**:
  
   ```bash
   docker compose up --build
   ```

## Project Structure

Brief overview of the main directories and their purposes.

```bash
Template
├── backend          # Django project
├── compose.yaml     # Docker Compose file
├── dockerfiles      # Docker files
├── frontend         # frontend codes
├── .env.example     ## .env.example file which must be
│                    ## modified like mentioned in 'Setup'
├── LICENSE
└── README.md
```

## Contributing

Contributions are always welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/).
