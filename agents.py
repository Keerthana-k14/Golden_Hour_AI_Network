class AmbulanceAgent:
    def __init__(self, ambulance_id, location):
        self.ambulance_id = ambulance_id
        self.location = location
        self.available = True


class HospitalAgent:
    def __init__(self, hospital_id, location, capacity):
        self.hospital_id = hospital_id
        self.location = location
        self.capacity = capacity


class TrafficAgent:
    def get_best_route(self, source, destination):
        return f"Optimized route from {source} to {destination}"
