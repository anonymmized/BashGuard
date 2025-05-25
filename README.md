# BashGuard – Terminal Command History Analyzer 🔍

A lightweight command-line tool that analyzes your Bash or Zsh history for suspicious patterns and potential security threats. Perfect for forensic analysis, penetration testing, or personal system monitoring.

[![License](https://img.shields.io/github/license/anonymmized/BashGuard)](https://github.com/anonymmized/Bashuard)

---

## 🧰 Features

- Scans `.bash_history` and `.zsh_history` files
- Detects suspicious commands (e.g., `wget`, `chmod +x`, `history -c`)
- Assigns risk scores to detected commands
- Outputs results with color-coded warnings
- Exports findings into a JSON or MARKDOWN file
- Supports filtering by risk score
- Includes bash scripts for setup and history logging
- Works across macOS, Linux, and Raspberry Pi

---
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

## 🔑 make support

### 1. Install 

For installation, go to the root catalog and execute the command:

```bash
make install
```

### 2. Dependencies

Next, the installation of dependencies:

```bash
make additions
```

### 3. Remove temp files

To remove temporary files and caches:

```bash
make clean
```

### 4. Save history

To save current shell history:

```bash
make log_history
```

### 5. Run CLI

To run the CLI tool without any options:

```bash
make run
```

### 6. Run CLI with options

Analyze shell history with risk filter:

```bash
make analyze
```

## 🐳 Docker Support

BashGuard is now optimized for running inside Docker containers . You can easily use it in an isolated environment without worrying about dependencies or system modifications.

## 📦 Build the Docker Image

```bash
docker build -t bashguard .
```

## 🚀 Run Analysis Inside a Container

To scan your terminal history using Docker:

```bash
docker run -it --rm \
    -v "$HOME/.bash_history:/root/.bash_history" \
    -v "$(pwd)/reports:/app/reports" \
    bashguard \
    bashguard analyze
```

This:

1. Mounts your .bash_history into the container,
2. Saves output to ./reports/report.json,
3. Uses isolated environment (no impact on host system).

## 🧪 Run Manually Inside the Container

You can also enter the container manually and run commands interactively:

```bash
docker run -it --rm bashguard bash
```

Then execute:

```bash
bashguard analyze
```

---
---

## 🚀 Usage

### Analyze terminal history:

```bash
bashguard analyze -fs 5 --report-format -o reports
```

### Available Options:

1) -f or --file  ->  Use a custom history file instead of default .bash_history or .zsh_history
2) -fs or --filter-score  ->  Show only commands with a risk score equal or higher than this value
3) --report-format (json/markdown)  ->  Save output as JSON or MARKDOWN 
4) -o:--output  ->  Specify output directory for report file

Example: 

```bash
bashguard analyze --filter-score 7 --report-format -o ./reports
```

This will:

- scan your shell history,
- filter out anything below score 7,
- save the report in ./reports/report.json.

---

## 📁 Core Modules

### core/history_parser.py

##### Parses .bash_history or .zsh_history files, strips timestamps (in Zsh), and returns clean list of commands.

### core/risk_analyzer.py

##### Analyzes each command against a set of suspicious patterns (like wget, sudo su, rm ~/.bash_history, etc.) and assigns a risk score.

### core/reporter.py

##### Outputs results to the terminal with color-coded severity levels and saves them in JSON/MARKDOWN format.

## 🖥️ Scripts

### scripts/install.sh

##### Installs Python dependencies (colorama) on your system.

Usage:

```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

### scripts/log_history.sh

##### Exports your current shell history into a separate file for backup or analysis.

Usage:

```bash
chmod +x scripts/log_history.sh
./scripts/log_history.sh
```

## 🛠 Troubleshooting

### `bashguard: command not found`

If you see the error:

```bash
zsh: command not found: bashguard
```

or 

```bash
bash: command not found: bashguard
```

##### It means that the `~/.local/bin` directory — where Python installs executable scripts — is not in your shell's `PATH`.

##### To fix this, we recommend running our **automated setup script**, which detects your shell (Bash or Zsh) and adds `~/.local/bin` to your `PATH` permanently.

##### It is also possible to solve this problem through:

```bash
make trouble
```

### 🔧 Run the Setup Script

```bash
./scripts/setup_path.sh
```

After running the script, verify it worked:

```bash
which bashguard
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