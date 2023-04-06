from django.db import models

# Create your models here.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.data == data:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

# player mode

from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)

class Puzzle(models.Model):
    image = models.ImageField(upload_to='puzzles')
    rows = models.IntegerField(default=4)
    cols = models.IntegerField(default=4)
    status = models.CharField(max_length=100, default='unsolved')
    correct = models.IntegerField(default=0)

# kullanıcının yüklediği görseli puzzle formatına çevirmek için Python Pillow kütüphanesi

from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Score(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.player.name} - {self.score}"
