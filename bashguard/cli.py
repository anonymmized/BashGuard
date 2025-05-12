#!/usr/bin/env python3

import argparse
import os
import time
from colorama import Fore, init

from .core.history_parser import history_parser
from .core.risk_analyzer import check_command_for_risk
from .core.reporter import report_json, colorama_set

init(autoreset=True)

def parse_args():
    parser = argparse.ArgumentParser(description='Analysis of the history of teams')
    subparsers = parser.add_subparsers(dest='command', required=True)

    analyze_parser = subparsers.add_parser('analyze', help='Analyze the history of the teams')
    analyze_parser.add_argument('-f', '--file', help='Specify a file with a story')
    analyze_parser.add_argument('-fs', '--filter-score', type=int, help='Filter at risk')
    analyze_parser.add_argument('--json-dump', action='store_true', help='Save results in json')
    analyze_parser.add_argument('-o', '--output', default='reports', help='Way to save report')

    args = parser.parse_args()

    if args.filter_score and args.filter_score < 0:
        parser.error(Fore.RED + "🔴 The filter should be positive")

    return args
    
    return args

def main():
    args = parse_args()

    print(Fore.MAGENTA + "=" * 60)
    print(Fore.MAGENTA + " BashGuard - Analysis of the history of teams ")
    print(Fore.MAGENTA + "=" * 60 + '\n')
    time.sleep(2)

    if args.file:
        try:
            commands = history_parser(args.file)
        except Exception as e:
            print(f"A file reading error has occurred {args.file}: {e}")
    else:
        zsh_file = os.path.expanduser('~/.zsh_history')
        bash_file = os.path.expanduser('~/.bash_history')
        if os.path.isfile(zsh_file):
            commands = history_parser(zsh_file)
        
        elif os.path.isfile(bash_file):
            commands = history_parser(bash_file)
        
    if commands:
        print(Fore.MAGENTA + f"| Found: {len(commands)} commands")
        time.sleep(1)

    if not commands:
        print(Fore.RED + "🔴 Not loaded a single team")
        exit(1)
    
    print(Fore.MAGENTA + '| Started creating a report...\n')
    time.sleep(1)

    result = check_command_for_risk(commands)

    if args.filter_score and args.filter_score <= 0:
        parser.error()

    if args.filter_score:
        filtered_result = [e for e in result if e['score'] >= args.filter_score]
        for event in filtered_result:
            colorama_set(event)
            time.sleep(0.005)
    else:
        for event in result:
            colorama_set(event)
            time.sleep(0.005)

    if args.json_dump:
        if args.output:
            filepath = os.path.join(args.output, 'report.json')
            report_json(filepath, result)
        else:
            filepath = os.path.join('../reports', 'report.json')
            report_json(filepath, result)

if __name__ == '__main__':
    main()