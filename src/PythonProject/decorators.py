import functools
import traceback


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
            except Exception as e:
                log_message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}\n"
                )
                traceback.print_exc()

            if filename:
                with open(filename, "a") as log_file:
                    log_file.write(log_message)
            else:
                print(log_message, end="")

            return result if "result" in locals() else None

        return wrapper

    return decorator
