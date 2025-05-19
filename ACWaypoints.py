import os
import ac
import acsys
import csv
import datetime

# Define paths for files
APP_DIR = os.path.dirname(os.path.realpath(__file__))
WAYPOINTS_DIR = os.path.join(APP_DIR, 'waypoints')
if not os.path.exists(WAYPOINTS_DIR):
    os.makedirs(WAYPOINTS_DIR)

waypoints = []  # List to store waypoints

def acMain(ac_version):
    global appWindow, addWaypointButton, saveWaypointsButton, waypointCountLabel, lastPositionLabel, currentPositionLabel

    appWindow = ac.newApp("WaypointRecorder")
    ac.setSize(appWindow, 500, 500)  # Increased height for the new label
    ac.setTitle(appWindow, "Waypoint Recorder")
    
    # Label to show current position
    currentPositionLabel = ac.addLabel(appWindow, "Current position: X=0.00, Z=0.00")
    ac.setPosition(currentPositionLabel, 10, 40)
    ac.setSize(currentPositionLabel, 280, 20)

    # Label to show the last added waypoint
    lastPositionLabel = ac.addLabel(appWindow, "Last waypoint: None")
    ac.setPosition(lastPositionLabel, 10, 70)
    ac.setSize(lastPositionLabel, 280, 20)
    
    # Label to count waypoints
    waypointCountLabel = ac.addLabel(appWindow, "Waypoints saved: 0")
    ac.setPosition(waypointCountLabel, 10, 100)

    # Button to add a waypoint
    addWaypointButton = ac.addButton(appWindow, "ADD Waypoint")
    ac.setSize(addWaypointButton, 200, 40)
    ac.setPosition(addWaypointButton, 50, 130)
    ac.addOnClickedListener(addWaypointButton, add_waypoint)

    # Button to save all waypoints
    saveWaypointsButton = ac.addButton(appWindow, "Save Waypoints")
    ac.setSize(saveWaypointsButton, 200, 40)
    ac.setPosition(saveWaypointsButton, 50, 180)
    ac.addOnClickedListener(saveWaypointsButton, save_waypoints)

    ac.log("Waypoint Recorder loaded.")
    ac.console("Waypoint Recorder loaded.")
    return "WaypointRecorder"

def add_waypoint(button_id, app_id):
    global waypoints, waypointCountLabel, lastPositionLabel
    
    # Get the current car position
    coordinates = ac.getCarState(0, acsys.CS.WorldPosition)
    x = coordinates[0]
    z = coordinates[2]
    
    # Add the waypoint to the list
    waypoints.append([x, z])
    
    # Update labels
    ac.setText(waypointCountLabel, "Waypoints saved: {}".format(len(waypoints)))
    ac.setText(lastPositionLabel, "Last waypoint: X={:.2f}, Z={:.2f}".format(x, z))
    
    ac.console("Waypoint added: X={:.2f}, Z={:.2f}".format(x, z))

def save_waypoints(button_id, app_id):
    global waypoints
    
    if not waypoints:
        ac.console("No waypoints to save.")
        return

    # Create a timestamp for the filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = "waypoints_{}_{}.csv".format(ac.getTrackName(0), timestamp)
    save_path = os.path.join(WAYPOINTS_DIR, filename)
    
    try:
        with open(save_path, "w") as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(["X", "Z"])  # Headers
            writer.writerows(waypoints)
        ac.console("Waypoints saved in {}".format(save_path))
        
        # Add a message to the interface
        global lastPositionLabel
        current_text = ac.getText(lastPositionLabel)
        ac.setText(lastPositionLabel, "Saved {} waypoints!".format(len(waypoints)))
        
    except Exception as e:
        ac.console("Error saving waypoints: {}".format(str(e)))
    
def acUpdate(deltaT):
    # Update the current car position
    coordinates = ac.getCarState(0, acsys.CS.WorldPosition)
    x = coordinates[0]
    z = coordinates[2]
    
    # Add a label for current coordinates if it doesn't exist already
    global currentPositionLabel
    if 'currentPositionLabel' not in globals():
        currentPositionLabel = ac.addLabel(appWindow, "Current position: X=0.00, Z=0.00")
        ac.setPosition(currentPositionLabel, 10, 10)
        ac.setSize(currentPositionLabel, 280, 20)
    
    # Update the label with current coordinates
    ac.setText(currentPositionLabel, "Current position: X={:.2f}, Z={:.2f}".format(x, z))

def acShutdown():
    # No operations needed when closing
    pass