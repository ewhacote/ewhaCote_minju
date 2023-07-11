from heapq import heappop, heappush

def solution(book_time):
    bookings = sorted([(time_to_minutes(b[0]), time_to_minutes(b[1])) for b in book_time])  
    rooms = []
    for check_in, check_out in bookings:
        if rooms and rooms[0] <= check_in:
            heappop(rooms) 
        heappush(rooms, check_out + 10)  
    return len(rooms)

def time_to_minutes(time):
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes
