import os
import json 
from datetime import datetime
from colorama import Fore, init
from .risk_analyzer import check_command_for_risk

init(autoreset=True)

def get_risk_label(score):
    if score >= 7:
        return "High 🔴"
    elif score >= 4:
        return "Medium 🟡"
    else:
        return "Low 🟢"


def report_markdown(filepath, result):
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'w') as f:
            f.write("# BashGuard - Analysis of the history of teams\n\n")
            f.write("Date: {}\n\n".format(datetime.now().strftime("%Y-%m-%d %H:%M")))
            f.write("| Command | Risk level | Description |\n")
            f.write("|----------|----------------|-----------|\n")

            for entry in result:
                risk_label = get_risk_label(entry['score'])
                if "🟡" in risk_label or "🔴" in risk_label:
                    f.write(f"| `{entry['command']}` | {risk_label} | {entry.get('match', '—')} |\n")
        print(f"🟢 The report is saved in Markdown: {filepath}")

    
    except Exception as e:
        print(f"🔴 Failed to save markdown report: {e}")

def report_json(filepath, result):
    directory = os.path.dirname(filepath)
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        with open(filepath, 'w') as f:
            json.dump(result, f, indent=4)
        print(Fore.GREEN + f'🟢 The report is successfully preserved: {filepath}')
    except Exception as e:
        print(Fore.RED + f'🔴 Error when recording reports: {e}')

def colorama_set(event):
    score = event['score']
    command = event['command']
    matches = ', '.join(event['matches'])

    if score <= 4:
        print(Fore.GREEN + f"|🟢 [Low] {command} \n   Matches: {matches} \n   Risk: {score}\n")
    elif 4 < score < 7:
        print(Fore.YELLOW + f"|🟡 [Middle] {command} \n   Matches: {matches} \n   Risk: {score}\n")
    else:
        print(Fore.RED + f"|🔴 [High] {command} \n   Matches: {matches} \n   Risk: {score}\n")
