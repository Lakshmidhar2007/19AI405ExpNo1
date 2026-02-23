import random

class MedicinePrescribingAgent:
    def __init__(self):
        self.current_location = "Room A"
        self.performance = 0

    def check_room(self, rooms):
        temperature = rooms[self.current_location]

        print("\n--------------------------------")
        print(f"Agent Location : {self.current_location}")
        print(f"Patient Temp   : {temperature:.2f} °F")

        if temperature > 98.5:
            print("Status         : Unhealthy (Fever Detected)")
            print("Action         : Medicine Prescribed")
            self.performance += 1
        else:
            print("Status         : Healthy")
            print("Action         : No Treatment Required")

    def move(self):
        print("\nAgent moving to next room...")
        self.performance -= 1

        if self.current_location == "Room A":
            self.current_location = "Room B"
        else:
            self.current_location = "Room A"

    def show_performance(self):
        print("\n================================")
        print(f"Final Performance Score : {self.performance}")
        print("================================")


# MAIN PROGRAM
if __name__ == "__main__":

    rooms = {
        "Room A": random.uniform(97.0, 102.0),
        "Room B": random.uniform(97.0, 102.0)
    }

    print("====== HOSPITAL HEALTH MONITORING SYSTEM ======")
    print(f"Room A Initial Temp : {rooms['Room A']:.2f} °F")
    print(f"Room B Initial Temp : {rooms['Room B']:.2f} °F")

    agent = MedicinePrescribingAgent()

    # Check Room A
    agent.check_room(rooms)

    # Move to Room B
    agent.move()

    # Check Room B
    agent.check_room(rooms)

    # Show Performance
    agent.show_performance()