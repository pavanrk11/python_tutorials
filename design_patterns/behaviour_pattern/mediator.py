class Aircraft:
    def __init__(self, call_sign, mediator):
        self.call_sign = call_sign
        self.mediator = mediator

    def request_landing(self):
        print(f"{self.call_sign} requests landing.")
        self.mediator.code = self.call_sign
        self.mediator.request_landing(self)

    def receive_message(self, message):
        print(f"{self.call_sign} receives message: {message}")


class ControlTowerMediator:

    code = None

    def __init__(self):
        self.aircrafts = []

    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def request_landing(self, requesting_aircraft):
        # Example logic: only allow landing if no other aircraft is landing
        for aircraft in self.aircrafts:
            if aircraft != requesting_aircraft:
                aircraft.receive_message(f"{requesting_aircraft.call_sign} is requesting to land.")

        # Simulate checking conditions and granting landing permission
        landing_granted = any(aircraft != requesting_aircraft for aircraft in self.aircrafts)
        # print(landing_granted)
        if landing_granted:
            requesting_aircraft.receive_message("Landing permission granted.")

        else:
            requesting_aircraft.receive_message("Landing permission denied. Wait for clearance.")




# Creating the mediator (control tower)
control_tower = ControlTowerMediator()

# Creating aircraft
aircraft1 = Aircraft("Flight-101", control_tower)
aircraft2 = Aircraft("Flight-102", control_tower)
aircraft3 = Aircraft("Flight-103", control_tower)


# Adding aircraft to the control tower mediator
control_tower.add_aircraft(aircraft1)
control_tower.add_aircraft(aircraft2)
control_tower.add_aircraft(aircraft3)


# Aircraft requesting landing
aircraft1.request_landing()
print()
print("Runway cleared..!")
aircraft2.request_landing()
print()
print("Runway cleared..!")
aircraft3.request_landing()

