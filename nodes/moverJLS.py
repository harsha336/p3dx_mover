#!/usr/bin/env python
import getch
import roslib; roslib.load_manifest('p3dx_mover')
import rospy
import time

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy


#KEY_UP = 65
KEY_UP = 'w'
#KEY_DOWN = 66
KEY_DOWN = 's'
#KEY_RIGHT = 67
KEY_RIGHT = 'd'
#KEY_LEFT = 68
KEY_LEFT = 'a'
KEY_STOP = 'e'
#USER_QUIT = 100
USER_QUIT = 'q'

MAX_FORWARD = 0.9
MAX_LEFT = 1
MIN_FORWARD = -0.9
MIN_LEFT = -1

forward = 0.0
left = 0.0
keyPress = 0

#use of joystic
def callback(data):
        twist = Twist()
        twist.linear.x = 4*data.axes[1]
        twist.angular.z = 4*data.axes[0]
	print "joytics working..."
        pub.publish(twist)
print "\nThe Keyboard remote controlle is activated please use the following keys: \n"
print "w=forward, d=right, s=backwards, a=left, e=stop, q=quit \n"

while(keyPress != USER_QUIT):

	#keyPress = getch.getArrow()
	keyPress = getch.getch()

	if keyPress == KEY_UP or keyPress == KEY_DOWN or keyPress == KEY_LEFT or keyPress == KEY_RIGHT or keyPress == KEY_STOP :

		pub = rospy.Publisher('cmd_vel', Twist)
		rospy.init_node('p3dx_mover')

		twist = Twist()
	
	
		if((keyPress == KEY_UP) and (forward <= MAX_FORWARD)):
			forward += 0.1

		elif((keyPress == KEY_DOWN) and (forward >= MIN_FORWARD)):
			forward += -0.1
		
		elif((keyPress == KEY_LEFT) and (left <= MAX_LEFT)):
			left += 0.1

		elif((keyPress == KEY_RIGHT) and (left >= MIN_LEFT)):
			left -= 0.1

		elif keyPress == KEY_STOP :
			forward = 0			
			left = 0

		#make sure that we have perfect zero and the robot still
		if forward >-0.001 and forward<0.001:
			forward=0.0;
		if left >-0.001 and left<0.001:
			left=0.0;

		if forward >= MAX_FORWARD:
			forward=MAX_FORWARD
		elif  forward <= MIN_FORWARD:
			forward = MIN_FORWARD
		if left >= MAX_LEFT:
			left = MAX_LEFT
		elif left <= MIN_LEFT:
			left = MIN_LEFT

		twist.linear.x = forward
		twist.angular.z = left

		print forward,left
		
		pub.publish(twist)
		keyPress=KEY_STOP

	




 

pub = rospy.Publisher('cmd_vel', Twist)
 # subscribed to joystick inputs on topic "joy"
rospy.Subscriber("joy", Joy, callback)

rospy.init_node('p3dx_mover')
twist = Twist()
pub.publish(twist)
exit()
	
