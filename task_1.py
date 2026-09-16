times = '1h 45m,360s,25m,30m 120s,2h 60s'
times.split(',')
parts = times.split(',')
total_minutes = 0
for part in parts:
    units = part.split()
    for unit in units:
        if unit.endswith('h'):
            num_str = unit.replace('h', '')
            value = int(num_str)
            minutes = value * 60
            total_minutes += minutes
            
        elif unit.endswith('m'):
            num_str = unit.replace('m', '')
            value = int(num_str) 
            minutes = value  
            total_minutes += minutes 
            

        elif unit.endswith('s'):
            num_str = unit.replace('s', '')
            value = int(num_str)
            minutes = value / 60 
            total_minutes += minutes
             

print(f"Общее количество минут: {total_minutes}") 