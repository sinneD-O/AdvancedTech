from __future__ import print_function
import roslibpy

client = roslibpy.Ros(host='localhost', port=9090)
client.run()

topic_move = roslibpy.Topic(client, '/move', 'std_msgs/String')
topic_move.subscribe(lambda message: print('Move: ' + message['data']))
topic_rotate = roslibpy.Topic(client, '/rotate', 'std_msgs/String')
topic_rotate.subscribe(lambda message: print('Rotate: '+ message['data']))
topic_map = roslibpy.Topic(client, '/room', 'std_msgs/String')
topic_map.subscribe(lambda message: print('Room: ' + message['data']))

try:
    while True:
        pass
except KeyboardInterrupt:
    client.terminate()
