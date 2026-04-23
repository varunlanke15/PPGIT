import math

class Order:
    def __init__(self, oid, x, y, demand):
        self.oid = oid
        self.x = x
        self.y = y
        self.demand = demand


class Vehicle:
    def __init__(self, vid, capacity):
        self.vid = vid
        self.capacity = capacity
        self.remaining = capacity
        self.route = []
        self.x = 0
        self.y = 0


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def optimize_routes(orders, vehicles):
    unassigned = orders[:]

    while unassigned:
        progress = False

        for v in vehicles:
            nearest = None
            min_dist = float('inf')

            for o in unassigned:
                if o.demand <= v.remaining:
                    d = distance(v.x, v.y, o.x, o.y)
                    if d < min_dist:
                        min_dist = d
                        nearest = o

            if nearest:
                v.route.append(nearest)
                v.remaining -= nearest.demand
                v.x = nearest.x
                v.y = nearest.y
                unassigned.remove(nearest)
                progress = True

        if not progress:
            print("\nSome orders could not be assigned due to capacity constraints.")
            break

    return vehicles


def display_orders(orders):
    if not orders:
        print("\nNo orders available.")
        return

    print("\nOrders List:")
    for o in orders:
        print(f"ID: {o.oid}, Location: ({o.x},{o.y}), Demand: {o.demand}")


def display_vehicles(vehicles):
    if not vehicles:
        print("\nNo vehicles available.")
        return

    print("\nVehicles List:")
    for v in vehicles:
        print(f"ID: {v.vid}, Capacity: {v.capacity}")


def display_routes(vehicles):
    for v in vehicles:
        print(f"\nVehicle {v.vid} Route:")
        print("Depot -> ", end="")
        for o in v.route:
            print(o.oid, "->", end=" ")
        print("Depot")


def calculate_distance(vehicle):
    total = 0
    x, y = 0, 0

    for o in vehicle.route:
        total += distance(x, y, o.x, o.y)
        x, y = o.x, o.y

    # Return to depot
    total += distance(x, y, 0, 0)

    return total


def main():
    orders = []
    vehicles = []

    while True:
        print("\n----- LOGISTICS SYSTEM -----")
        print("1. Add Order")
        print("2. Add Vehicle")
        print("3. View Orders")
        print("4. View Vehicles")
        print("5. Optimize Routes")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choice == 1:
            oid = input("Enter Order ID: ")
            x = float(input("Enter X location: "))
            y = float(input("Enter Y location: "))
            demand = float(input("Enter demand: "))
            orders.append(Order(oid, x, y, demand))

        elif choice == 2:
            vid = input("Enter Vehicle ID: ")
            capacity = float(input("Enter capacity: "))
            vehicles.append(Vehicle(vid, capacity))

        elif choice == 3:
            display_orders(orders)

        elif choice == 4:
            display_vehicles(vehicles)

        elif choice == 5:
            optimize_routes(orders, vehicles)
            display_routes(vehicles)

            print("\n--- Distance Details ---")
            for v in vehicles:
                print(f"Vehicle {v.vid} Distance: {calculate_distance(v):.2f}")

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()