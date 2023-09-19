def solution(input_str):
    parsed_str = input_str[2:-2].split("},{")
    set_list = []
    
    for elem in parsed_str:
        subset = elem.split(",")
        set_list.append(set(subset))
        
    set_list.sort(key=lambda x: len(x))
    
    result_set = set()
    final_result = []
    
    for current_set in set_list:
        diff = current_set - result_set
        final_result.append(list(diff)[0])
        result_set = result_set | diff
    
    final_result = [int(x) for x in final_result]
    
    return final_result
