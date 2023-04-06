def generate_puzzle(image):
    image = Image.open(image)
    resized_image = image.resize((400, 400), resample=Image.BICUBIC)
    cropped_images = []
    for row in range(4):
        for col in range(4):
            left = col * 100
            upper = row * 100
            right = left + 100
            lower = upper + 100
            cropped_image = resized_image.crop((left, upper, right, lower))
            cropped_images.append(cropped_image)
    random.shuffle(cropped_images)
    linked_list = LinkedList()
    for cropped_image in cropped_images:
        data = cropped_image.tobytes()
        linked_list.add(data)
    return linked_list

#board.py

def generate_coords_list(size):
    """
    Returns a list of coordinates for a given size of puzzle.
    """
    coords_list = []
    for row in range(size):
        for col in range(size):
            coords_list.append((row, col))
    return coords_list

#convert_to_puzzle

from PIL import Image

def convert_to_puzzle(image_path):
    """
    Converts the uploaded image to puzzle format.
    """
    try:
        image = Image.open(image_path)
    except IOError:
        return None
    width, height = image.size
    size = min(width, height)
    left = (width - size) / 2
    top = (height - size) / 2
    right = (width + size) / 2
    bottom = (height + size) / 2
    image = image.crop((left, top, right, bottom)).resize((400, 400), Image.ANTIALIAS)
    pixels = image.load()
    coords_list = generate_coords_list(4)
    puzzle = []
    for i in range(0, len(coords_list), 4):
        row = []
        for j in range(i, i + 4):
            row.append(pixels[coords_list[j][1] * 100, coords_list[j][0] * 100])
        puzzle.append(row)
    return puzzle

#

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def length(self):
        length = 0
        current_node = self.head

        while current_node:
            length += 1
            current_node = current_node.next

        return length

    def delete_at_index(self, index):
        if index >= self.length():
            return None

        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        current_index = 0
        while current_index < index-1:
            current_node = current_node.next
            current_index += 1

#

import random

class Puzzle:
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]
        self.solution = None
        self.moves = 0
    
    def shuffle(self):
        flat_board = [elem for row in self.board for elem in row]
        random.shuffle(flat_board)
        self.board = [[flat_board[row*self.size + col] for col in range(self.size)] for row in range(self.size)]
    
    def is_solved(self):
        return self.board == self.solution
    
    def get_empty_pos(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] is None:
                    return (row, col)
    
    def move(self, row, col):
        empty_row, empty_col = self.get_empty_pos()
        if row == empty_row and col == empty_col:
            return False  # No move was made
        
        # Check if the move is legal
        if row == empty_row:
            start, end = sorted([col, empty_col])
            if None in self.board[row][start+1:end]:
                return False  # Move is not legal
        elif col == empty_col:
            start, end = sorted([row, empty_row])
            if None in [self.board[i][col] for i in range(start+1, end)]:
                return False  # Move is not legal
        else:
            return False  # Move is not legal
        
        # Make the move
        self.board[empty_row][empty_col] = self.board[row][col]
        self.board[row][col] = None
        self.moves += 1
        return True
    
    def create_solution(self):
        num_list = list(range(1, self.size**2))
        num_list.append(None)
        random.shuffle(num_list)
        self.solution = [[num_list[row*self.size + col] for col in range(self.size)] for row in range(self.size)]
    
    def reset(self):
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.solution = None
        self.moves = 0
    
    def get_board(self):
        return self.board

#
