class Booking:
    def book(self,seat,booked_seats):
        if seat not in booked_seats:
            booked_seats.append(seat)
            print(f"Seat {seat} booked successfully")
        else:
            print("Already booked")

    def cancel(self, seat, booked_seats):
        if seat in booked_seats:
            booked_seats.remove(seat)
            print(f"Seat {seat} cancelled successfully")
        else:
            print("Invalid cancellation")


obj = Booking()
total_seats = int(input("Enter total no. of seats: "))
seats = list(range(1, total_seats+1))
booked_seats = [2, 5, 7]
book_seat = int(input("Enter a seat to book: "))
obj.book(book_seat, booked_seats)
available_seats = [seat for seat in seats if seat not in booked_seats]
cancel_seat = int(input("Enter a seat to cancel: "))
obj.cancel(cancel_seat, booked_seats)
print(f"Available seats: {available_seats}")
