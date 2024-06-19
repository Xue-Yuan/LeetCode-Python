# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    '''Only turn right. Make sure the order of the directions matches the 
    turn direction, so that we will have consistent coordinates.
    -----------------> x
    |
    |
    |
    |
    |
    |
    v y
    
                 (-1, 0)
                    |
                    0
                    |
 (0, -1) ---3--- (0, 0) ---1--- (0, 1)
                    |
                    2
                    |
                 (1, 0)
    '''

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        def dfs(i, j, d):
            visited.add((i, j))
            robot.clean()
            for k in range(4):
                new_d = (d + k) % 4
                dx, dy = directions[new_d]
                x, y = i + dx, j + dy
                if (x, y) not in visited and robot.move():
                    dfs(x, y, new_d)
                    self.goBack(robot)
                # matches the order of directions
                robot.turnRight()

        dfs(0, 0, 0)

    def goBack(self, robot) -> None:
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
