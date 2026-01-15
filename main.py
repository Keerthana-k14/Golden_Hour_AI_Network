from controller import IncidentController

if __name__ == "__main__":
    controller = IncidentController()
    controller.handle_incident(
        incident_id="INC-1001",
        location="Bengaluru - Whitefield"
    )
