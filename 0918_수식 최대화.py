from itertools import permutations

def solution(expression):
    ops = ["*", "+", "-"]
    max_results = []

    for order in permutations(ops, 3):
        first_op = order[0]
        second_op = order[1]
        
        first_split = []
        
        for sub_expr in expression.split(first_op):
            second_split = []
            
            for inner_sub_expr in sub_expr.split(second_op):
                second_split.append(f"({inner_sub_expr})")
            
            first_split.append(f"({second_op.join(second_split)})")
        
        combined_expr = first_op.join(first_split)
        evaluated_result = abs(eval(combined_expr))
        
        max_results.append(evaluated_result)
        
    return max(max_results)
 