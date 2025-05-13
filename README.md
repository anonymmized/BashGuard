# BashGuard – Terminal Command History Analyzer 🔍

A lightweight command-line tool that analyzes your Bash or Zsh history for suspicious patterns and potential security threats. Perfect for forensic analysis, penetration testing, or personal system monitoring.

[![License](https://img.shields.io/github/license/anonymmized/BashGuard)](https://github.com/anonymmized/Bashuard)
[![Python Version](https://img.shields.io/pypi/pyversions/BashGuard)](https://pypi.org/project/BashGuard/)

---

## 🧰 Features

- Scans `.bash_history` and `.zsh_history` files
- Detects suspicious commands (e.g., `wget`, `chmod +x`, `history -c`)
- Assigns risk scores to detected commands
- Outputs results with color-coded warnings
- Exports findings into a JSON file
- Supports filtering by risk score
- Includes bash scripts for setup and history logging
- Works across macOS, Linux, and Raspberry Pi

---

## 🛠️ Installation

### 1. Install via pip (recommended)

You can install the package directly using pip after publishing to PyPI:

```bash
pip install bashguard
```

If you're developing locally or installing from source:

```bash
git clone https://github.com/YOUR_USERNAME/bashguard.git
cd bashguard
pip install -e .
```

## 🚀 Usage

### Analyze terminal history:
```bash
bashguard analyze -fs 5 --json-dump -o reports
```

### Available Options:

1) -f:--file            Use a custom history file instead of default .bash_history or .zsh_history
2) -fs:--filter-score   Show only commands with a risk score equal or higher than this value
3) --json-dump          Save output as JSON
4) -o:--output          Specify output directory for JSON report

Example: 
```bash
bashguard analyze --filter-score 7 --json-dump -o ./reports
```
This will:

⚪️ scan your shell history,
⚪️ filter out anything below score 7,
⚪️ save the report in ./reports/report.json.

## 📁 Core Modules

### core/history_parser.py

Parses .bash_history or .zsh_history files, strips timestamps (in Zsh), and returns clean list of commands.

### core/risk_analyzer.py

Analyzes each command against a set of suspicious patterns (like wget, sudo su, rm ~/.bash_history, etc.) and assigns a risk score.

### core/reporter.py

Outputs results to the terminal with color-coded severity levels and saves them in JSON format.

## 🖥️ Scripts

### scripts/install.sh

Installs Python dependencies (colorama) on your system.

Usage:
```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

### scripts/log_history.sh

Exports your current shell history into a separate file for backup or analysis.

Usage:
```bash
chmod +x scripts/log_history.sh
./scripts/log_history.sh
```

## 📦 File Structure

```
bashguard/
├── bashguard/
│   ├── cli.py
│   └── core/
│       ├── history_parser.py
│       ├── risk_analyzer.py
│       └── reporter.py
├── scripts/
│   ├── install.sh
│   └── log_history.sh
├── setup.py
├── README.md
└── LICENSE
```

## 📝 License

This project is licensed under the MIT License – see LICENSE for details.

## 🧪 Future Ideas

⚪️ Add GUI support (via tkinter or streamlit)
⚪️ Integrate with VirusTotal API for URL checking
⚪️ Monitor user behavior over time
⚪️ Real-time history watcher
⚪️ Export reports to Markdown or HTML
⚪️ Integration with SIEM systems (Splunk, ELK)


