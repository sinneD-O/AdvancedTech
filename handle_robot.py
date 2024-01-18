import rospy
import subprocess
from geometry_msgs.msg import PoseStamped, Pose
from std_msgs.msg import String



def startup():
    rospy.init_node('robot_control_node', anonymous=True)

    launch_command = "rosrun auto_nav init_pose.py ~/home/init_pose_flur.yaml"
    process = subprocess.Popen(launch_command.split(), stdout=subprocess.PIPE)

    robot_status_publisher = rospy.Publisher('/robot_status', String, queue_size=10)
    rospy.sleep(1)
    message = {
        'status': 'idle',
        'enum': 0
    }
    robot_status_publisher.publish(message)


def move_to_goal(room):
    pose = room['Pose']
    position = pose['position']
    orientation = pose['orientation']
    x = position['x']
    y = position['y']
    z = orientation['z']
    w = orientation['w']

    launch_command = "rosrun auto_nav goal_pose.py " + x + " " + y + " " + z + " " + w
    process = subprocess.Popen(launch_command.split(), stdout=subprocess.PIPE)

    output, error = process.communicate()
    if error:
        print(error)

    message = {
        'status': 'delivering',
        'enum': 1
    }
    # Send status update
    robot_status_publisher = rospy.Publisher('/robot_status', String, queue_size=10)
    rospy.sleep(1)
    robot_status_publisher.publish(message)


def goal_reached():
    robot_status_publisher = rospy.Publisher('/robot_status', String, queue_size=10)
    rospy.sleep(1)
    message = {
        'status': 'goal reached',
        'enum': 2
    }
    robot_status_publisher.publish(message)


if __name__ == '__main__':
    startup()

