from random import random
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self, msg=""):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'microk8s',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.msg = msg

    def listener_callback(self, msg):
        self.get_logger().info('%s: "%s"' % (self.msg, msg.data))


def main(msg = ""):
    rclpy.init(args=None)
    msg += ":"
    msg += str(int(random()*1000))

    minimal_subscriber = MinimalSubscriber(msg)

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    if len (sys.argv) == 2:
        main (sys.argv[1])
    else:
        main()
