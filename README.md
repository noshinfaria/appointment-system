# appointment-system

appointment-system/
│
├── app/
│   ├── main.py
│   ├── core/              # Config, auth, utils
│   ├── db/                # DB init, session, models
│   ├── api/               # Routers (auth, users, doctors, appointments)
│   ├── schemas/           # Pydantic models
│   ├── services/          # Business logic
│   ├── tasks/             # Celery tasks for reminders & reports
│   ├── static/            # For uploads (profile images)
│   └── templates/         # Optional if using server-side rendering
│
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── requirements.txt
├── alembic/               # For migrations
├── seed_data.py
└── README.md
