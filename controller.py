from agents import AmbulanceAgent, HospitalAgent, TrafficAgent
from decision_engine import select_best_hospital
from trust import verify_agent
from event_logger import log_event
from failure_handler import handle_failure

class IncidentController:

    def handle_incident(self, incident_id, location):
        log_event(incident_id, "CALL_RECEIVED", f"Emergency at {location}")

        ambulance = AmbulanceAgent("AMB-01", "MG Road")
        hospital = HospitalAgent("HOSP-01", "Indiranagar", capacity=2)
        traffic = TrafficAgent()

        if not verify_agent("AmbulanceAgent"):
            handle_failure("Ambulance authentication failed")
            return

        best_hospital = select_best_hospital([hospital])

        if not best_hospital:
            handle_failure("No hospitals available")
            return

        route = traffic.get_best_route(ambulance.location, best_hospital.location)

        log_event(
            incident_id,
            "DISPATCH_SUCCESS",
            f"Ambulance routed to {best_hospital.hospital_id} via {route}"
        )
