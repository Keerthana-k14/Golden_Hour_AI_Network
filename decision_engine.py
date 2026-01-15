def select_best_hospital(hospitals):
    available = [h for h in hospitals if h.capacity > 0]
    return available[0] if available else None
