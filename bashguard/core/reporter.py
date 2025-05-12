import os
import json 
from colorama import Fore, init
from .risk_analyzer import check_command_for_risk

init(autoreset=True)

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
