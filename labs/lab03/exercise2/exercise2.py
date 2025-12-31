def find_station(stations, name):
    
   if name not in stations:
      return None
   
   count = 0
   for i in range (len(stations)):
      if stations[i] == name:
         return i
      


def count_stops(stations, start, stop):
   start_index = find_station(stations, start)
   end_index = find_station(stations, stop)

   if start_index == None or end_index == None:
      return -1
   
   return abs(end_index - start_index)
   
