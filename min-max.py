from typing import Any, List, Callable, Optional

from numpy import number, quantile, roots
from numpy.random import choice


class TreeNode:
  value: Any
  state: Optional [Any]
  score: Optional [int]
  children: List['TreeNode']
  choice: Optional[int]

  def __init__(self, value: Any, state: Optional [Any] = None, score: Optional [int] = 0) -> None:
    self.value = value
    self.state = state
    self.score = score
    self.children = []

    
    if (self.value == "Protagonista"):
      if (score < 21):
        self.add(TreeNode("Antagonista", 4, score + 4))
        self.add(TreeNode("Antagonista", 5, score + 5))
        self.add(TreeNode("Antagonista", 6, score + 6))

    if (self.value == "Antagonista"):
      if (score < 21):
        self.add(TreeNode("Protagonista", 4, score + 4))
        self.add(TreeNode("Protagonista", 5, score + 5))
        self.add(TreeNode("Protagonista", 6, score + 6))


  @property
  def is_leaf(self) -> bool:
    return len(self.children) == 0
  
  def add(self, child: 'TreeNode') -> None:
    self.children.append(child)
    
  def traverse_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
    for child in self.children:
      child.traverse_deep_first(visit)
    visit(self)

  def __str__(self) -> str:
      return '{}, {}, {}'.format(self.value, self.state, self.score)

      
      
class Tree:
    root: TreeNode

    def __init__(self, node: TreeNode) -> None:
      self.root = node
      
    def traverse_deep_first(self, visit: Callable[[TreeNode], None]) -> None:
      self.root.traverse_deep_first(visit)
      
    def min_max(self, node: TreeNode) -> None:
      # nalezy zmodyfikowac wyniki w kazdym wezle tego grafu
      if (node.is_leaf is True):
        return node.value
      if (node.value == "Protagonista"):
        node.choice = max(node.children[0].state, node.children[1].state, node.children[2].state)
      if (node.value == "Antagonista"):
        node.choice = min(node.children[0].state, node.children[1].state, node.children[2].state)
      
      


root = TreeNode('Protagonista', 0, 0)

drzewo = Tree(root)

drzewo.traverse_deep_first(drzewo.min_max)
print(root.choice)