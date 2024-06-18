class TodoList:
    def __init__(self, title):
        self._title = title 
        self._todos = []
        
    @property
    def title(self):
        return self._title
    
    @property
    def todos(self):
        return self._todos
    
    def is_empty(self):
        return len(self.todos) == 0
        
    def add(self, new_todo):
        if not isinstance(new_todo, Todo):
            raise ValueError
        
        self._todos.append(new_todo)
        
    def first(self):
        if not self.is_empty():
            return self.todos[0]
        
        raise IndexError
    
    def last(self):
        if not self.is_empty():
            return self.todos[-1]
        
        raise IndexError
    
    def mark_done_at(self, index):
        if index > len(self.todos):
            raise IndexError
        
        self.todos[index].done = True
        
    def mark_undone_at(self, index):
        if index > len(self.todos):
            raise IndexError
        self.todos[index].done = False
        
    def mark_all_done(self):
        for todo in self.todos:
            todo.done = True
    
    def mark_all_undone(self):
        for todo in self.todos:
            todo.done = False
            
    def all_done(self):
        return all([todo.done for todo in self.todos])
    
    def remove_at(self, index):
        if index > len(self.todos):
            raise IndexError

        self.todos.pop(index)
        
    def each(self, callback):
        for todo in self.todos:
            callback(todo)
            
    def select(self, callback):
        new_todo_list = TodoList("Selected List")
        for todo in self.todos:
            if callback(todo):
                new_todo_list.add(todo) 
        
        return new_todo_list
        
    def find_by_title(self, task):
        for todo in self.todos:
            if todo.task == task:
                return todo 
            
        raise IndexError("No matching Todos!")
    
    def done_todos(self):
        new_todo_list = TodoList("Completed List")
        
        
    
    def __str__(self):
        output = [f"----{self.title}----"]
        output += [str(todo) for todo in self.todos]
        return "\n".join(output)
            
    def __len__(self):
        return len(self.todos)
    
    def __iter__(self):
        return iter(self.todos)
    
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError
        elif index > len(self.todos):
            raise IndexError
        
        return self.todos[index]

class Todo:
    def __init__(self, task):
        self.task = task 
        self.done = False
        
    def is_done(self):
        return "X" if self.done else " "
    
    def __str__(self):
        return f"[{self.is_done()}] {self.task}"
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        
        return self.task == other.task and self.done == other.done
        

# Code omitted for brevity.

empty_todo_list = TodoList('Nothing Doing')

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list

# Code omitted

def step_2():
    print('--------------------------------- Step 2')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

step_2()

def step_3():
    print('--------------------------------- Step 3')
    todo_list = setup()

    print(len(todo_list))              # 3
    print(len(empty_todo_list))        # 0

step_3()

def step_4():
    print('--------------------------------- Step 4')
    todo_list = setup()

    print(todo_list.first())           # [ ] Buy milk
    print(todo_list.last())            # [ ] Go to gym

    try:
        empty_todo_list.first()
    except IndexError:
        print('Expected IndexError: Got it!')

    try:
        empty_todo_list.last()
    except IndexError:
        print('Expected IndexError: Got it!')

step_4()

def step_5():
    print('--------------------------------- Step 5')
    todo_list = setup()

    #print(empty_todo_list.to_list())    # []

    todos = list(todo_list)
    print(type(todos).__name__)         # list

    for todo in todos:
        print(todo)                     # [ ] Buy milk
                                        # [X] Clean room
                                        # [ ] Go to gym

step_5()

def step_6():
    print('--------------------------------- Step 6')
    todo_list = setup()

    print(todo_list[0])        # [ ] Buy milk
    print(todo_list[1])        # [X] Clean room
    print(todo_list[2])        # [ ] Go to gym
    
    try:
        todo_list[3]
    except IndexError:
        print('Expected IndexError: Got it!')


    # Ensure we have a reference
    print(todo_list[1] is todo_list[1])  # True

step_6()

def step_7():
    print('--------------------------------- Step 7')
    todo_list = setup()

    todo_list.mark_done_at(0)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room'
    # [ ] Go to gym

    todo_list.mark_done_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room'
    # [ ] Go to gym

    todo_list.mark_done_at(2)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room'
    # [X] Go to gym

    try:
        todo_list.mark_done_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

    todo_list.mark_undone_at(0)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room'
    # [X] Go to gym

    todo_list.mark_undone_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room'
    # [X] Go to gym

    todo_list.mark_undone_at(2)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room'
    # [ ] Go to gym

    try:
        todo_list.mark_undone_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

step_7()

def step_8():
    print('--------------------------------- Step 8')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room'
    # [ ] Go to gym

    todo_list.mark_all_done()
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room'
    # [X] Go to gym

    todo_list.mark_all_undone()
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room'
    # [ ] Go to gym

step_8()

def step_9():
    print('--------------------------------- Step 9')
    todo_list = setup()

    print(todo_list.all_done())         # False

    todo_list.mark_all_done()
    print(todo_list.all_done())         # True

    todo_list.mark_undone_at(1)
    print(todo_list.all_done())         # False

    print(empty_todo_list.all_done())   # True

step_9()

def step_10():
    print('--------------------------------- Step 10')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room'
    # [ ] Go to gym

    todo_list.remove_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Go to gym

    todo_list.remove_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk

    try:
        todo_list.remove_at(1)
    except IndexError:
        print('Expected IndexError: Got it!')

    todo_list.remove_at(0)
    print(todo_list)
    # ---- Today's Todos -----
    print(todo_list)

step_10()

def step_11():
    print('--------------------------------- Step 11')
    todo_list = setup()

    todo_list.mark_all_undone()
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [ ] Go to gym

    def done_if_y_in_title(todo):
        if 'y' in todo.task:
            todo.done = True


    todo_list.each(done_if_y_in_title)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [ ] Clean room
    # [X] Go to gym

    todo_list.each(lambda todo: print('>>>', todo))
    # ---- Today's Todos -----
    # >>> [X] Buy milk
    # >>> [ ] Clean room
    # >>> [X] Go to gym

step_11()

def step_12():
    print('--------------------------------- Step 12')
    todo_list = setup()

    def y_in_title(todo):
        return 'y' in todo.task

    print(todo_list.select(lambda todo: 'y' in todo.task))
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Go to gym

    print(todo_list.select(lambda todo: todo.done))
    # ---- Today's Todos -----
    # [X] Clean room

step_12()

def step_13():
    print('--------------------------------- Step 13')
    todo_list = setup()

    todo_list.add(Todo('Clean room'))
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym
    # [ ] Clean room

    found = todo_list.find_by_title('Go to gym')
    print(found)
    # [ ] Go to gym

    found = todo_list.find_by_title('Clean room')
    print(found)
    # [X] Clean room

    try:
        todo_list.find_by_title('Feed cat')
    except IndexError:
        print('Expected IndexError: Got it!')

step_13()

def step_14():
    print('--------------------------------- Step 14')
    todo_list = setup()

    done = todo_list.done_todos()
    print(done)
    # ----- Today's Todos -----
    # [X] Clean room

    undone = todo_list.undone_todos()
    print(undone)
    # ----- Today's Todos -----
    # [ ] Buy milk
    # [ ] Go to gym

    done = empty_todo_list.done_todos()
    print(done)
    # ----- Nothing Doing -----

    undone = empty_todo_list.undone_todos()
    print(undone)
    # ----- Nothing Doing -----

step_14()