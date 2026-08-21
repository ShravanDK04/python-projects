import json


# =========================
# ROOM CLASSES
# =========================

class Room:
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price
        self._is_available = True

    def calculate_price(self, nights):
        return self.price * nights

    def book(self):
        if not self._is_available:
            return False

        self._is_available = False
        return True

    def release(self):
        self._is_available = True

    def is_available(self):
        return self._is_available

    def display(self):
        status = "Available" if self._is_available else "Occupied"
        print(
            f"Room {self.room_number} | "
            f"{self.__class__.__name__} | "
            f"₹{self.price:.2f}/night | {status}"
        )


class StandardRoom(Room):
    def calculate_price(self, nights):
        return self.price * nights


class DeluxeRoom(Room):
    def calculate_price(self, nights):
        return (self.price * nights) + 500


class SuiteRoom(Room):
    def calculate_price(self, nights):
        return (self.price * nights) + 1500


# =========================
# GUEST
# =========================

class Guest:
    def __init__(self, guest_id, name, phone):
        self.guest_id = guest_id
        self.name = name
        self.phone = phone

    def display(self):
        print(
            f"Guest ID: {self.guest_id} | "
            f"Name: {self.name} | "
            f"Phone: {self.phone}"
        )


# =========================
# BOOKING
# =========================

class Booking:
    def __init__(self, booking_id, guest, room, nights):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.nights = nights

    def calculate_bill(self):
        return self.room.calculate_price(self.nights)

    def display(self):
        print(
            f"Booking ID: {self.booking_id} | "
            f"Guest: {self.guest.name} | "
            f"Room: {self.room.room_number} | "
            f"Nights: {self.nights} | "
            f"Bill: ₹{self.calculate_bill():.2f}"
        )


# =========================
# HOTEL
# =========================

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = []
        self.bookings = []

    # ---------- ROOM ----------

    def add_room(self):
        try:
            room_number = int(input("Enter room number: "))
            price = float(input("Enter price per night: "))

            print("\n1. Standard")
            print("2. Deluxe")
            print("3. Suite")

            choice = input("Choose room type: ")

            if choice == "1":
                room = StandardRoom(room_number, price)

            elif choice == "2":
                room = DeluxeRoom(room_number, price)

            elif choice == "3":
                room = SuiteRoom(room_number, price)

            else:
                print("Invalid room type.")
                return

            self.rooms.append(room)

            print("Room added successfully.")

        except ValueError:
            print("Please enter valid values.")

    def show_rooms(self):
        if not self.rooms:
            print("No rooms available.")
            return

        print("\n========== ROOMS ==========")

        for room in self.rooms:
            room.display()

    def show_available_rooms(self):
        available_rooms = [
            room for room in self.rooms
            if room.is_available()
        ]

        if not available_rooms:
            print("No rooms available.")
            return

        print("\n====== AVAILABLE ROOMS ======")

        for room in available_rooms:
            room.display()

    # ---------- GUEST ----------

    def add_guest(self):
        guest_id = len(self.guests) + 1

        name = input("Enter guest name: ").strip()
        phone = input("Enter phone number: ").strip()

        if not name or not phone:
            print("Name and phone cannot be empty.")
            return

        guest = Guest(guest_id, name, phone)

        self.guests.append(guest)

        print(f"Guest added successfully. Guest ID: {guest_id}")

    def show_guests(self):
        if not self.guests:
            print("No guests found.")
            return

        print("\n========== GUESTS ==========")

        for guest in self.guests:
            guest.display()

    # ---------- BOOKING ----------

    def book_room(self):
        if not self.rooms:
            print("No rooms available.")
            return

        if not self.guests:
            print("Please add a guest first.")
            return

        self.show_available_rooms()

        try:
            room_number = int(input("Enter room number: "))
        except ValueError:
            print("Invalid room number.")
            return

        room = None

        for r in self.rooms:
            if r.room_number == room_number:
                room = r
                break

        if room is None:
            print("Room not found.")
            return

        if not room.is_available():
            print("Room is already occupied.")
            return

        self.show_guests()

        try:
            guest_id = int(input("Enter guest ID: "))
        except ValueError:
            print("Invalid guest ID.")
            return

        guest = None

        for g in self.guests:
            if g.guest_id == guest_id:
                guest = g
                break

        if guest is None:
            print("Guest not found.")
            return

        try:
            nights = int(input("Enter number of nights: "))

            if nights <= 0:
                print("Nights must be greater than 0.")
                return

        except ValueError:
            print("Invalid number of nights.")
            return

        if room.book():

            booking_id = len(self.bookings) + 1

            booking = Booking(
                booking_id,
                guest,
                room,
                nights
            )

            self.bookings.append(booking)

            print("\nRoom booked successfully.")
            print(f"Booking ID: {booking_id}")
            print(f"Guest: {guest.name}")
            print(f"Room: {room.room_number}")
            print(f"Total Bill: ₹{booking.calculate_bill():.2f}")

    def show_bookings(self):
        if not self.bookings:
            print("No bookings found.")
            return

        print("\n========== BOOKINGS ==========")

        for booking in self.bookings:
            booking.display()

    # ---------- CHECK OUT ----------

    def check_out(self):
        if not self.bookings:
            print("No active bookings.")
            return

        self.show_bookings()

        try:
            booking_id = int(
                input("Enter booking ID to check out: ")
            )
        except ValueError:
            print("Invalid booking ID.")
            return

        booking = None

        for b in self.bookings:
            if b.booking_id == booking_id:
                booking = b
                break

        if booking is None:
            print("Booking not found.")
            return

        total_bill = booking.calculate_bill()

        booking.room.release()

        self.bookings.remove(booking)

        print("\n========== CHECK OUT ==========")
        print(f"Guest: {booking.guest.name}")
        print(f"Room: {booking.room.room_number}")
        print(f"Total Bill: ₹{total_bill:.2f}")
        print("Check-out completed successfully.")


# =========================
# MAIN PROGRAM
# =========================

def main():

    hotel = Hotel("Grand Python Hotel")

    # Sample rooms
    hotel.rooms.append(StandardRoom(101, 1500))
    hotel.rooms.append(StandardRoom(102, 1500))
    hotel.rooms.append(DeluxeRoom(201, 2500))
    hotel.rooms.append(SuiteRoom(301, 5000))

    while True:

        print("\n")
        print("================================")
        print("      GRAND PYTHON HOTEL")
        print("================================")
        print("1. Add Room")
        print("2. Show All Rooms")
        print("3. Show Available Rooms")
        print("4. Add Guest")
        print("5. Show Guests")
        print("6. Book Room")
        print("7. Show Bookings")
        print("8. Check Out")
        print("9. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                hotel.add_room()

            case "2":
                hotel.show_rooms()

            case "3":
                hotel.show_available_rooms()

            case "4":
                hotel.add_guest()

            case "5":
                hotel.show_guests()

            case "6":
                hotel.book_room()

            case "7":
                hotel.show_bookings()

            case "8":
                hotel.check_out()

            case "9":
                print("Thank you for using Grand Python Hotel.")
                break

            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
