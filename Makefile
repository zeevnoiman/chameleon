install-requirements:
	@echo "Installing requirements..."
	@cd backend && pip3 install -r requirements.txt

update-requirements:
	@echo "Updating requirements..."
	@cd backend && pip3 freeze > requirements.txt
	
run-backend:
	@echo "Running backend..."
	@cd backend && flask --app src/app run

run-backend-debug:
	@echo "Running backend in debug mode..."
	@cd backend && flask --app src/app run --debug
 
