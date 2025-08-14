from setuptools import setup, find_packages

# Чтение зависимостей из requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="aiogram-botkit",
    version="0.1.0",
    description="fully-featured template for creating production-ready Telegram bots.",
    author="HellSAS",
    author_email="hellsas666@gmail.com",
    url="https://github.com/HellSAS/aiogram-botkit",
    packages=find_packages(),
    install_requires=requirements,
    license="Apache-2.0",
    python_requires=">=3.8",
)
