import re

def solution(files):
    def sort_key(file):
        match = re.match(r'([^\d]+)(\d+)', file)
        head, number = match.groups()
        return [head.lower(), int(number)] 

    return sorted(files, key=sort_key)