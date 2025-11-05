PYTHON ?= $(shell command -v python3.11 || command -v python3 || command -v python)
PYTEST ?= $(PYTHON) -m pytest

.PHONY: help install test validate-docs validate-delta check

help:
	@echo "Доступные цели:"
	@echo "  install         Установка зависимостей из requirements.txt"
	@echo "  test            Запуск pytest"
	@echo "  validate-docs   Проверка синхронизации документации"
	@echo "  validate-delta  Валидация примеров ∆DΩΛ"
	@echo "  check           Полный цикл проверок (test + validate-docs + validate-delta)"

install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTEST) -q

validate-docs:
	$(PYTHON) tools/check_docs_sync.py

validate-delta:
	$(PYTHON) tools/validate_delta.py --examples

check: test validate-docs validate-delta
