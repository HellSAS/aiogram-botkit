import toml

REQ_FILE = "requirements.txt"
PYPROJECT_FILE = "pyproject.toml"

# Чтение зависимостей из requirements.txt
with open(REQ_FILE) as req_file:
    requirements = [line.strip() for line in req_file if line.strip() and not line.startswith("#")]

# Чтение pyproject.toml
pyproject = toml.load(PYPROJECT_FILE)

# Обновление зависимостей
if "project" not in pyproject:
    pyproject["project"] = {}
pyproject["project"]["dependencies"] = requirements

# Сохранение изменений
with open(PYPROJECT_FILE, "w") as toml_file:
    toml.dump(pyproject, toml_file)

print("Requirements successfully synced to pyproject.toml!")
