build:
	docker compose -f develop.yaml up --build -d --remove-orphans

up:
	docker compose -f develop.yaml up -d

down:
	docker compose -f develop.yaml down

show-logs:
	docker compose -f develop.yaml logs

show-logs-api:
	docker compose -f develop.yaml logs api

migrations:
	docker compose -f develop.yaml run --rm api python manage.py makemigrations

migrate:
	docker compose -f develop.yaml run --rm api python manage.py migrate

collectstatic:
	docker compose -f develop.yaml run --rm api python manage.py collectstatic --no-input --clear

superuser:
	docker compose -f develop.yaml run --rm api python manage.py createsuperuser

down-v:
	docker compose -f develop.yaml down -v

volume:
	docker volume inspect src_local_postgres_data


blog-db:
	docker compose -f develop.yaml exec postgres psql --username=predro --dbname=blog-live

flake8:
	docker compose -f develop.yaml exec api flake8 .

black-check:
	docker compose -f develop.yaml exec api black --check --exclude=migrations .

black-diff:
	docker compose -f develop.yaml exec api black --diff --exclude=migrations .

black:
	docker compose -f develop.yaml exec api black --exclude=migrations .

isort-check:
	docker compose -f develop.yaml exec api isort . --check-only --skip venv --skip migrations

isort-diff:
	docker compose -f develop.yaml exec api isort . --diff --skip venv --skip migrations

isort:
	docker compose -f develop.yaml exec api isort . --skip venv --skip migrations