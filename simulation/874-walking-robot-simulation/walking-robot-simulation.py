# time: O(n + s), где n - кол-во команд, s - сумма положительных комманд
# memory: O(m), где m - кол-во препятствий
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        self.dx, self.dy = 0, 1
        self.position = 0, 0
        self.obstacles = set()
        self.max_distance = 0

        for obstacle in obstacles:
            self.obstacles.add((obstacle[0], obstacle[1]))

        for command in commands:
            if command == -2:
                self.turn(False)
            elif command == -1:
                self.turn(True)
            else:
                self.move(command)
                self.update_stat()

        return self.max_distance

    def turn(self, to_right):
        if to_right:
            self.dx *= -1
        else:
            self.dy *= -1
        
        self.dx, self.dy = self.dy, self.dx

    def get_next(self):
        return self.position[0] + self.dx, self.position[1] + self.dy

    def move(self, k):
        while k > 0 and self.get_next() not in self.obstacles:
            self.position = self.get_next()
            k -= 1
    
    def update_stat(self):
        self.max_distance = max(self.max_distance, self.position[0] ** 2 + self.position[1] ** 2)
