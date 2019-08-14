class Player:

    def __init__(self, row, col):
        self.current_index = (row, col)
        self.new_index = None

    def up(self):
        self.new_index = (self.current_index[0] - 1, self.current_index[1])

    def down(self):
        self.new_index = (self.current_index[0] + 1, self.current_index[1])

    def left(self):
        self.new_index = (self.current_index[0], self.current_index[1] - 1)

    def right(self):
        self.new_index = (self.current_index[0], self.current_index[1] + 1)

    def confirm_move(self):
        self.current_index = self.new_index
        self.new_index = None

    def reset_move(self):
        self.new_index = None
