import time
from roslibpy import Ros, Topic, Message

client = Ros(host='localhost', port=9090)
client.run()

topic_coordinates = Topic(client, '/coordinates', 'std_msgs/String')
topic_goal_reached = Topic(client, '/goal_reached', 'std_msgs/String')


# 1. Verbindung zu TurtleBot
# Mehrere Turtlebots kompatibel machen

# Sollen mehrere Turtlebots gleichzeitig fahren?
# Wenn ja, dann muss die Verbindung zu jedem Turtlebot einzeln aufgebaut werden
# Wenn nein, kann die Verbindungen zu den Turtlebots über eine Verbindung aufgebaut werden

# Feste IP-Adresse für Turtlebot erstellen
# Verbindung zu Turtlebot aufbauen, wenn ausgewählt


# 2. Roboter soll beladen werden und bei “Submit” zum gewählten Ziel fahren
def move_to_goal(target_room):
    # 1. aus target_room die Koordinaten des Ziels bestimmen
    x = 0
    y = 0
    if target_room == "Room 1":
        # Koordinaten von Room 1
        x = 1
        y = 1
    elif target_room == "Room 2":
        # Koordinaten von Room 2
        x = 2
        y = 2
    elif target_room == "Room 3":
        # Koordinaten von Room 3
        x = 3
        y = 3

    # Koordinaten in JSON umwandeln
    data = {"room": target_room, "coordinates": {"x": x, "y": y, "w": 1.0}}

    message = Message({'json_data': data})

    topic_coordinates.publish(message)



# 3. Feedback: Signal empfangen, dass der Turtlebot an Zielkoordinate angekommen ist
