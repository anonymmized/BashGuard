import os
import time
import json
import argparse
import re
from colorama import init, Fore
from .risk_analyzer import check_command_for_risk
from .reporter import report_json
from datetime import datetime, timezone

init(autoreset=True)

def parse_args():
    parser = argparse.ArgumentParser(description='Collects all entered teams')

    parser.add_argument('--json-dump', action='store_true', help='Save results in a separate file (JSON format)')
    parser.add_argument('-o', '--output', help='Way to save json report')
    parser.add_argument('-fs', '--filter-score', type=int, help='Filter the degree of risk (recommended 5)')
    parser.add_argument('-f', '--file', help='Add your file')

    args = parser.parse_args()

    if args.filter_score and args.filter_score < 0:
        parser.error(Fore.RED + "🔴 The filter should be positive")
    
    return args
    

def history_parser(filepath):
    if os.path.isfile(filepath):
        try:
            with open(filepath, 'r', encoding='latin1') as f:
                commands = []
                for line in f:
                    cleaned = line.split(';', 1)[-1].strip()
                    if len(cleaned) >= 1:
                        commands.append(cleaned)
        except Exception as e:
            print(f"There was a file reading error: {e}")
    else:
        print(Fore.RED + f"🔴 File {filepath} was not found")
        return []
    
    return commands

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
