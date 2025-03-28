.PHONY: help install dev migrate makemigrations run lint check format test pre-commit hooks req

# help — Показывает список команд
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

# Установка зависимостей через uv (продакшн)
install: ## Установить зависимости через uv
	uv pip install -r requirements.txt

# Установка всех зависимостей: и прод, и dev
dev: ## Установка всех зависимостей (включая dev)
	uv pip install -r requirements.txt
	uv pip install -r requirements-dev.txt || true  # если есть отдельный dev файл

# Миграции
makemigrations: ## Создать миграции
	cd itg && python manage.py makemigrations

migrate: ## Применить миграции
	cd itg && python manage.py migrate

# Запуск сервера
run: ## Запустить локальный dev-сервер
	cd itg && python manage.py runserver

req:
	uv pip compile pyproject.toml --output requirements.txt

# Линтинг через ruff
lint: ## Проверка кода линтером
	uv pip install ruff || true
	ruff check .

# Авто-исправление
format: ## Форматирование кода
	ruff format .
	ruff check . --fix

# Тесты
test: ## Запуск тестов
	cd itg && pytest

# Pre-commit хуки
pre-commit: ## Установка и запуск pre-commit
	uv pip install pre-commit || true
	pre-commit install
	pre-commit run --all-files

# Установка хуков отдельно
hooks: ## Установка git-хуков
	pre-commit install