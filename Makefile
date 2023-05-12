install-requirements:
	@echo "Installing requirements..."
	@cd backend && pip3 install -r requirements.txt

update-requirements:
	@echo "Updating requirements..."
	@cd backend && pip3 freeze > requirements.txt
	
run-backend:
	@echo "Running backend..."
	@cd backend && flask --app chameleon/app run

run-backend-debug:
	@echo "Running backend in debug mode..."
	@cd backend && flask --app chameleon/app run --debug
 
 run-test:
	@echo "Running tests"
	@cd backend && pytest

run-db:
	@echo "Running database..."
	@docker compose -f backend/docker_compose.yml up -d

stop-db:
	@echo "Stopping database..."
	@docker rm -f postgresDb