def solution(record):
    user_info = {}
    result = []
    
    for entry in record:
        tokens = entry.split()
        action, user_id = tokens[0], tokens[1]
        
        if action == "Enter" or action == "Change":
            nickname = tokens[2]
            user_info[user_id] = nickname
            
    for entry in record:
        tokens = entry.split()
        action, user_id = tokens[0], tokens[1]
        
        if action == "Enter":
            result.append(f"{user_info[user_id]}님이 들어왔습니다.")
        elif action == "Leave":
            result.append(f"{user_info[user_id]}님이 나갔습니다.")
    
    return result
