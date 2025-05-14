PROJECT_NAME = bashguard
VENV = venv
CLI_MODULE = bashguard.cli
INSTALL_SCRIPT = scripts/install.sh
LOG_HISTORY_SCRIPT = scripts/log_history.sh
TROUBLESHOOTING_SCRIPT = scripts/setup_path.sh

.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "💡 BashGuard Makefile"
	@echo "======================="
	@echo "Available commands:"
	@echo ""
	@echo " install        : Install project dependencies"
	@echo " run            : Run the CLI tool"
	@echo " analyze        : Analyze shell history with risk filter"
	@echo " additions      : Install additional programs and files"
	@echo " log-history    : Save current shell history"
	@echo " trouble        : Run troubleshooting script"
	@echo " additions      : Run installation additions"
	@echo " clean          : Remove temporary files and caches"
	@echo " test           : Run tests (if any)"
	@echo ""

install:
	@pip install -e .

run:
	@bashguard analyze

analyze:
	@bashguard analyze --filter-score 5 --json-dump -o ./reports

additions:
	@chmod +x $(INSTALL_SCRIPT)
	@./$(INSTALL_SCRIPT)

trouble:
	@chmod +x $(TROUBLESHOOTING_SCRIPT)
	@./$(TROUBLESHOOTING_SCRIPT)

log-history:
	@chmod +x $(LOG_HISTORY_SCRIPT)
	@./$(LOG_HISTORY_SCRIPT)

clean:
	@rm -rf __pycache__ *.pyc reports/
	@echo "✅ Clean completed."

test:
	@echo "🧪 No tests implemented yet."
