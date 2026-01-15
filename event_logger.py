from datetime import datetime

def log_event(incident_id, event_type, details):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n📌 EVENT LOG")
    print(f"Time        : {timestamp}")
    print(f"Incident ID : {incident_id}")
    print(f"Event       : {event_type}")
    print(f"Details     : {details}")
