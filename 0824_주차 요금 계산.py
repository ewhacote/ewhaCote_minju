import math

def convertToMinutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def calculateParkingFees(fees, records):
    fee_list = []
    base_time, base_fee, unit_time, unit_fee = fees
    parking_records = {}

    for record in records:
        timestamp, car_number, action = record.split()
        car_number = int(car_number)
        
        if car_number in parking_records:
            parking_records[car_number].append([convertToMinutes(timestamp), action])
        else:
            parking_records[car_number] = [[convertToMinutes(timestamp), action]]

    sorted_parking_records = sorted(parking_records.items())

    for car_number, logs in sorted_parking_records:
        total_minutes = 0
        
        for time, status in logs:
            if status == "IN":
                total_minutes -= time
            else:
                total_minutes += time

        if logs[-1][1] == "IN":
            total_minutes += convertToMinutes("23:59")

        if total_minutes <= base_time:
            fee_list.append(base_fee)
        else:
            fee_list.append(base_fee + math.ceil((total_minutes - base_time) / unit_time) * unit_fee)

    return fee_list
