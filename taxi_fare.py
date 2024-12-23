def fare_cal(trips):
    base_fare = 50
    dist_fare = 10
    trip_fare = []
    for i in trips:
        trip_fare.append(base_fare+(dist_fare*i))
        print(f"Trip {trips.index(i)+1}:${base_fare+(dist_fare*i)}")
    print(f"Total fare:${sum(trip_fare)}")


trips_list = [5, 10, 3]
fare_cal(trips_list)
