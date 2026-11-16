# Project Title: Courier Tracking System (PS No: 67)
# Rungta International Skills University - First Semester CSE
# Concepts Used: Dictionaries, Lists, Functions, Search

# 1. DATA STORAGE
# Global dictionary to store all parcel records
# Structure: { tracking_id: { details... } }
parcels = {}

# Starting counter for auto-generating unique tracking IDs (CT1001, CT1002, ...)
id_counter = 1001

# Sequential list defining the one-way forward lifecycle of a parcel
STATUS_LIST = ["Booked", "Picked Up", "In Transit", "Out for Delivery", "Delivered"]


def generate_tracking_id():
    """Generates the next unique tracking ID automatically."""
    global id_counter
    new_id = f"CT{id_counter}"
    id_counter += 1
    return new_id


def book_parcel():
    """Books a new parcel and assigns initial status as Booked."""
    print("\n--- Book Parcel ---")
    sender = input("Sender: ").strip()
    receiver = input("Receiver: ").strip()
    destination = input("Destination: ").strip()

    if sender == "" or receiver == "" or destination == "":
        print("All fields are mandatory.")
        return

    tracking_id = generate_tracking_id()

    # Store parcel data inside dictionary
    parcels[tracking_id] = {
        "sender": sender,
        "receiver": receiver,
        "destination": destination,
        "current_status": "Booked",
        "history": ["Booked"]  # List to maintain chronological status history
    }

    print(f"Parcel booked. Tracking ID: {tracking_id} | Status: Booked")


def update_status():
    """Updates status forward by one step along the STATUS_LIST."""
    print("\n--- Update status ---")
    tracking_id = input("Tracking ID: ").strip().upper()

    # Search whether tracking ID exists in dictionary
    if tracking_id not in parcels:
        print(f"Tracking ID {tracking_id} not found.")
        return

    parcel = parcels[tracking_id]
    current = parcel["current_status"]

    # Boundary check: If parcel is already Delivered, no further update is allowed
    if current == "Delivered":
        print(f"Parcel {tracking_id} is already delivered. No further updates allowed.")
        return

    # Find the current stage index and move forward to the next stage
    current_index = STATUS_LIST.index(current)
    next_status = STATUS_LIST[current_index + 1]

    # Update current status and append new status to history list
    parcel["current_status"] = next_status
    parcel["history"].append(next_status)

    print(f"Status updated: {current} -> {next_status}")


def track_parcel():
    """Tracks parcel details, full history trail, and current status."""
    print("\n--- Track parcel ---")
    tracking_id = input("Tracking ID: ").strip().upper()

    # Search whether tracking ID exists
    if tracking_id not in parcels:
        print(f"Tracking ID {tracking_id} not found.")
        return

    parcel = parcels[tracking_id]
    
    # Join history list elements with arrows
    history_trail = " -> ".join(parcel["history"])

    print(f"Tracking ID: {tracking_id} | Receiver: {parcel['receiver']} | Destination: {parcel['destination']}")
    print(f"History: {history_trail}")
    print(f"Current status: {parcel['current_status']}")


def search_by_receiver():
    """Searches parcels by receiver name using linear search through the dictionary."""
    print("\n--- Search by receiver ---")
    target_receiver = input("Receiver Name: ").strip()

    found = False
    for tid, info in parcels.items():
        if info["receiver"].lower() == target_receiver.lower():
            found = True
            print(f"Tracking ID: {tid} | Sender: {info['sender']} | Destination: {info['destination']} | Status: {info['current_status']}")

    if not found:
        print(f"No parcels found for receiver '{target_receiver}'.")


def main():
    """Main menu loop for user interaction."""
    while True:
        print("\n===============================")
        print("    COURIER TRACKING SYSTEM    ")
        print("===============================")
        print("1. Book parcel")
        print("2. Update status")
        print("3. Track parcel")
        print("4. Search by receiver")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            book_parcel()
        elif choice == "2":
            update_status()
        elif choice == "3":
            track_parcel()
        elif choice == "4":
            search_by_receiver()
        elif choice == "5":
            print("Exiting Courier Tracking System. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
