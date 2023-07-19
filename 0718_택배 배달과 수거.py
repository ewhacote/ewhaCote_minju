def solution(capacity, num_of_stops, deliveries, pickups):
    total_time = 0
    while True:
        while len(deliveries) > 0 and deliveries[-1] == 0: 
            deliveries.pop()
        while len(pickups) > 0 and pickups[-1] == 0: 
            pickups.pop()
        
        if len(deliveries) == 0 and len(pickups) == 0: 
            break
        
        total_time += max(len(deliveries), len(pickups))*2
        remaining_capacity = capacity

        while len(deliveries) > 0 and remaining_capacity > 0:
            if deliveries[-1] > remaining_capacity:
                deliveries[-1] -= remaining_capacity
                break
            remaining_capacity -= deliveries.pop()

        remaining_capacity = capacity

        while len(pickups) > 0 and remaining_capacity > 0:
            if pickups[-1] > remaining_capacity:
                pickups[-1] -= remaining_capacity
                break
            remaining_capacity -= pickups.pop()            
    return total_time
