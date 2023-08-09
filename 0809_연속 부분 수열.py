def solution(elements):
    unique_sums = set() 
    length = len(elements)
    
    for element in elements:
        unique_sums.add(element)
        
    unique_sums.add(sum(elements))
    
    partial_sums = [[0 for _ in range(length)] for _ in range(length+1)]
    partial_sums[1] = elements
    
    for seq_length in range(2, length):
        for start_index in range(length):
            partial_sums[seq_length][start_index] = partial_sums[seq_length-1][start_index] + partial_sums[seq_length-1][(start_index+1)%length] - partial_sums[seq_length-2][(start_index+1)%length]
            unique_sums.add(partial_sums[seq_length][start_index])
    return len(unique_sums)
