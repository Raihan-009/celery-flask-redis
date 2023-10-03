build-app:
	@ docker build -f Dockerfile.app -t poridhi/celery-app:v0.2 .

build-worker:
	@ docker build -f Dockerfile.celery -t poridhi/celery-worker:v0.2 .

run-celery:
	@ docker run --name celery-worker --network celerynetwork poridhi/celery-worker:v0.2

run-redis:
	@ docker run --name celery-redis --network celerynetwork -p 6379:6379 redis

run-app:
	@ docker run --name celery-app --network celerynetwork -p 5009:5009 poridhi/celery-app:v0.2

clean-celery:
	@ docker rm celery-worker

clean-redis:
	@ docker rm celery-redis

clean-app:
	@ docker rm celery-app
