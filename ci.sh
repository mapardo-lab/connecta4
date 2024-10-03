echo "==== black ===="
black .
echo "==== isort ===="
isort .
echo "==== pylint ===="
pylint prueba
echo "==== mypy ===="
mypy prueba
echo "==== pytest ===="
pytest --cov prueba tests
