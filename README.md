# ACWaypoints
## Assetto Corsa Waypoint Logger
This is a mod for Assetto Corsa that allows you to collect and save waypoints during a driving session.
The goal is to use the recorded data later for tasks such as developing an autonomous driving system using PID controllers.

### Features
- In-game Python app integrated into Assetto Corsa
- Logs car position as waypoints
- Saves data to a .csv file for later use

### Installation
Clone this repository into the Assetto Corsa Python apps folder:
```
C:\Program Files (x86)\Steam\steamapps\common\assettocorsa\apps\python
```

### Usage
1. Starting the App:
    - Launch Assetto Corsa and enter a driving session (Practice, Hotlap, etc.)
    - Press the "Apps" button in the right sidebar or press Home key
    - Find and click on "Waypoint Recorder" in the apps list
2. Interface Overview:
    - The app displays your current position coordinates (X, Z)
    - Shows the last recorded waypoint
    - Displays a counter for the total number of saved waypoints
3. Recording Waypoints:
    - Drive your car to the position you want to record
    - Click the "ADD Waypoint" button to save the current car position
    - The "Last waypoint" field will update to show the coordinates just recorded
    - The waypoint counter will increase
4. Saving Your Data:
    - After recording all desired waypoints, click the "Save Waypoints" button
    - The waypoints will be saved to a CSV file in the "waypoints" folder:
    &nbsp;&nbsp;&nbsp;&nbsp;*[ACWaypoints folder]/waypoints/waypoints_[track_name]_[timestamp].csv*
    - The app will confirm the save operation
5. Using the Recorded Data:
    - The saved CSV file contains X and Z coordinates in Assetto Corsa's world space
    - Each row represents one waypoint in the order they were recorded