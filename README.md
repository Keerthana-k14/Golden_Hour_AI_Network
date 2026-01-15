# Golden_Hour_AI_Network
Multi-agent emergency coordination system using trust-based AI agents
# Golden AI Network 🚑🤖

A prototype demonstrating **multi-agent collaboration** for emergency incident handling.

## 🔹 Problem
Emergency response systems require coordination between ambulances, hospitals, and traffic control.
Manual coordination causes delays and failures.

## 🔹 Solution
This project simulates a **multi-agent AI network** where:
- Ambulance agents respond to incidents
- Hospital agents manage capacity
- Traffic agent optimizes routing
- A central controller coordinates decisions
- Failures are handled with fallback logic

## 🔹 Architecture
- Agents: Ambulance, Hospital, Traffic
- Controller: IncidentController
- Decision Engine: Selects optimal response
- Event Logger: Tracks events
- Failure Handler: Handles system failures

## 🔹 Tech Stack
- Python
- Agent-based architecture
- Event-driven design

## 🔹 How to Run
```bash
python main.py
