def repeat_func(repetition):
    def procedure(func):
        def decorator():
            for _ in range(repetition):
                func()
        return decorator
    return procedure

@repeat_func(repetition=2)
def func():
    print("Hello")

func()

