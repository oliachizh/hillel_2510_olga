from logs.logger_setup import logger

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Executing Function {func.__name__} with arguments: {args} {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Function {func.__name__} executed with result: {result}")
        return result
    return wrapper

def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as exc:
            print(f"The following error occurred: {exc}")

    return wrapper
@log_decorator
def say_hello():
    return "Hello!"

@exception_decorator
@log_decorator
def say_hello2(name):
    return f"Hello! {name}"

