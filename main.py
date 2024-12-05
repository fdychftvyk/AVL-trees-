import math

class Node:
    def __init__(self, key):
        self.key = key  # Значение узла
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок
        self.height = 1  # Высота узла

class AVLTree:
    # Вставка узла в AVL-дерево
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Обновляем высоту узла
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        # Проверяем балансировку
        balance = self.get_balance(root)

        # Балансировка дерева
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Левый поворот
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # Правый поворот
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # Получить высоту узла
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    # Вычислить баланс узла
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    # Подсчитать количество узлов в дереве
    def count_nodes(self, root):
        if not root:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

 # Оценить высоту дерева (по теоретической формуле)
    def estimate_height(self, root):
        node_count = self.count_nodes(root)
        if node_count == 0:
            return 0
        log_value = math.log2(node_count + 2)
        estimated_height = 1.44 * log_value - 0.328
        return math.ceil(estimated_height)

    # Вычислить реальную высоту дерева
    def calculate_real_height(self, root):
        if not root:
            return 0
        return 1 + max(self.calculate_real_height(root.left), self.calculate_real_height(root.right))

# Пример использования AVL-дерева
avl_tree = AVLTree()
root = None

# Вставляем элементы в дерево
data = [10, 20, 30, 40, 50, 25]
for key in data:
    root = avl_tree.insert(root, key)

# Реальная высота дерева
real_height = avl_tree.calculate_real_height(root)
print(f"Реальная высота АВЛ дерева: {real_height}")

# Оценка высоты дерева
estimated_height = avl_tree.estimate_height(root)
print(f"Оценка высоты АВЛ дерева: {estimated_height}")
