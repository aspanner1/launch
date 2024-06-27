import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todoList = TodoList("Today's Todos")
        self.todoList.add(self.todo1)
        self.todoList.add(self.todo2)
        self.todoList.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todoList))
        
    def test_to_list(self):
        self.assertEqual(self.todoList._todos, self.todoList.to_list())
        
    def test_first(self):
        self.assertEqual(self.todoList.first(), self.todoList._todos[0])
        
    def test_last(self):
        self.assertEqual(self.todoList.last(), self.todoList._todos[-1])
        
    def test_is_done(self):
        self.todoList.mark_all_done() 
        self.assertTrue(self.todoList.is_done())
        
    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todoList.add("Invalid string")
    
    def test_item_at(self):
        with self.assertRaises(IndexError):
            self.todoList.todo_at(len(self.todoList))
        
        for index, _ in enumerate(self.todoList.to_list()):
            self.assertEqual(self.todoList.todo_at(index), self.todoList._todos[index])
            
    def test_mark_done_at(self):
        with self.assertRaises(IndexError):
            self.todoList.mark_done_at(len(self.todoList))
            
        for index, _ in enumerate(self.todoList.to_list()):
            self.todoList.mark_done_at(index)
        
        self.assertTrue(self.todoList.is_done())
        
    def test_mark_undone_at(self):
        with self.assertRaises(IndexError):
            self.todoList.mark_undone_at(len(self.todoList))
            
        for index, _ in enumerate(self.todoList.to_list()):
            self.todoList.mark_undone_at(index)
        
        self.assertTrue(not self.todoList.is_done())
        
    def test_str(self):
        string = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym"
        )
        self.assertEqual(string, str(self.todoList))
        
    def test_str_done_todo(self):
        self.todoList.mark_done_at(-1)
        string = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[ ] Clean room\n"
            "[X] Go to the gym"
        )
        self.assertEqual(string, str(self.todoList))
    
    def test_select(self):
        self.todo1.done = True
        selected = self.todoList.select(lambda todo: todo.done)
        self.assertEqual("----- Today's Todos -----\n[X] Buy milk",
                     str(selected))
        
    

if __name__ == "__main__":
    unittest.main()