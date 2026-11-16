# Courier Tracking System

A menu-driven, terminal-based courier management and parcel tracking application built in Python.

This project was built to simulate how logistics and courier hubs manage parcel life cycles — from initial booking to final doorstep delivery — using core Python data structures without relying on third-party libraries.

---

## What It Does

The program handles four primary workflows through an interactive console menu:

1. **Book a Parcel**: Accepts sender, receiver, and destination details, automatically assigns a unique tracking ID (`CT1001`, `CT1002`, ...), and sets the status to `Booked`.
2. **Update Status**: Progresses a package forward along a fixed, one-way lifecycle. Once marked `Delivered`, the system locks further status updates.
3. **Track a Parcel**: Displays complete parcel information, the current status, and a full breadcrumb trail of where the parcel has been (`Booked -> Picked Up -> In Transit...`).
4. **Search by Receiver**: Uses a linear search to find all shipments assigned to a specific receiver (case-insensitive).

---

## Parcel Lifecycle & State Flow

Parcels follow a strict sequential state progression defined in code:

```text
[ Booked ] ──> [ Picked Up ] ──> [ In Transit ] ──> [ Out for Delivery ] ──> [ Delivered ]
                                                                                   │
                                                                           (Locked / Final)
```

- Status transitions are strictly forward-only; packages cannot jump stages or move backwards.
- When an update is triggered, the system resolves the current index in the lifecycle list, picks `index + 1`, and appends the new state to the parcel's chronological history.

---

## Technical Details & Data Structures

| Concept | Implementation in Code | Why It Was Used |
| :--- | :--- | :--- |
| **Dictionary** | `parcels = { tracking_id: { ... } }` | Gives $O(1)$ fast lookups when tracking or updating via tracking ID. |
| **Ordered List** | `STATUS_LIST = [...]` | Preserves the strict forward order of stages and allows index-based progression. |
| **Nested List** | `parcel["history"] = [...]` | Maintains an audit log of every stage the parcel transitioned through. |
| **Linear Search** | `search_by_receiver()` | Iterates through dictionary values (`parcels.items()`) to find matching receiver names. |
| **Modular Functions** | `book_parcel()`, `update_status()`, etc. | Keeps operations isolated, readable, and easy to debug. |

---

## Validations & Boundary Checks

- **Mandatory Fields**: Booking rejects empty strings for sender, receiver, or destination.
- **Case Normalization**: Tracking IDs (`ct1001` or `CT1001`) and receiver names are normalized so searches aren't broken by casing.
- **Unknown ID Handling**: Shows clear feedback if an entered tracking ID doesn't exist.
- **Delivered Boundary**: Prevents advancing status once a parcel has reached `Delivered`.

---

## Getting Started

### Prerequisites

- Python 3.7 or higher installed on your system.
- No external packages (`pip`) required — uses standard Python libraries only.

### Running the Program

1. Clone or download this repository.
2. Open your terminal or command prompt inside the project folder:
   ```bash
   cd courier_tracking_system
   ```
3. Run the script:
   ```bash
   python courier_tracking.py
   ```

---

## Example Walkthrough

```text
===============================
    COURIER TRACKING SYSTEM    
===============================
1. Book parcel
2. Update status
3. Track parcel
4. Search by receiver
5. Exit
Enter choice (1-5): 1

--- Book Parcel ---
Sender: Neha Sharma
Receiver: Karan Patel
Destination: Nagpur
Parcel booked. Tracking ID: CT1001 | Status: Booked

Enter choice (1-5): 2

--- Update status ---
Tracking ID: CT1001
Status updated: Booked -> Picked Up

Enter choice (1-5): 3

--- Track parcel ---
Tracking ID: CT1001
Tracking ID: CT1001 | Receiver: Karan Patel | Destination: Nagpur
History: Booked -> Picked Up
Current status: Picked Up
```

---

## Project Structure

```text
courier_tracking_system/
├── courier_tracking.py       # Main executable containing logic, state, and CLI
├── PROJECT_REPORT_AND_VIVA.md# Academic report, problem statement & viva Q&A
└── README.md                 # Project overview and usage guide
```

---

## Potential Future Improvements

- [ ] Add persistent storage (save/load data with JSON or SQLite so data survives program restarts).
- [ ] Add timestamps to the history audit trail.
- [ ] Add delivery cost estimation based on distance or weight.
- [ ] Build a simple Tkinter or web GUI.
