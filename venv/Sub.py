import rclpy
from rclpy.node import Node

from std_msg.msg import String

class Subscriber(Node):

    def __init__(self):
        super.__init__('minima_subscriber')
        self.subscription = self.create_subscribtion(String, 'topic', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = Subscriber()

    rclpy.spin(minimal_subscriber)

if __name__ == '__main__':
    main()