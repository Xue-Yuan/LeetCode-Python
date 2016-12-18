class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.snake = collections.deque([[0, 0]])
        self.width = width
        self.height = height
        self.food = food[::-1]
        self.score = 0
        self.directions = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        d, head = self.directions[direction], self.snake[0]
        new_head = [head[0]+d[0], head[1]+d[1]]
        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width):
            return -1
        if self.food and new_head == self.food[-1]:
            self.score += 1
            self.food.pop()
        else:
            self.snake.pop()
        if new_head in self.snake:
            return -1
        self.snake.appendleft(new_head)
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)