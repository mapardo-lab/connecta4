echo "==== black ===="
black .
echo "==== isort ===="
isort .
echo "==== pylint ===="
pylint connecta
echo "==== mypy ===="
mypy connecta
echo "==== pytest ===="
pytest --cov connecta tests
