import time
import roslibpy

client = roslibpy.Ros(host='localhost', port=9090)
client.run()

topic_move = roslibpy.Topic(client, '/move', 'std_msgs/String')
topic_rotate = roslibpy.Topic(client, "/rotate", 'std_msgs/String')
topic_room = roslibpy.Topic(client, "/room", 'std_msgs/String')

while client.is_connected:
    message = input("Message: ")
    message = str(message)

    print('Sending message...')

    if message.startswith("rotate"):
        topic_rotate.publish(roslibpy.Message({'data': message}))
    elif message.startswith("move"):
        topic_move.publish(roslibpy.Message({'data': message}))
    elif message.startswith("room"):
        topic_room.publish(roslibpy.Message({'data': message}))

    time.sleep(1)

topic_move.unadvertise()
topic_rotate.unadvertise()
topic_room.unadvertise()
client.terminate()
