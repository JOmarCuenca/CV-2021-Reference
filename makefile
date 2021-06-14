clean:
	@echo "Cleaning all the notebook ipynb_checkpoints"
	rm -rf **/.ipynb_checkpoints/
	@echo "Cleaning all the python cache"
	rm -rf **/__pycache__/