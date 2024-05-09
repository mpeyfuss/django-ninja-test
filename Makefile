# Format code
fmt:
	poetry run ruff format .

# lint code
lint:
	poetry run ruff check --fix .

# Django
migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

superuser:
	poetry run python manage.py createsuperuser
	@echo "Don't forget to add a static token with 'poetry run python manage.py addstatictoken USERNAME -t 123456'"

# Run Server
run_sync:
	poetry run gunicorn ninja_test.wsgi:application --workers 4 --worker-class gevent --bind :8000 --reload

run_async:
	poetry run gunicorn ninja_test.asgi:application --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind :8000 --reload