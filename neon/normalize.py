import functools
import inspect

def normalize_fields(**norms):
    def wrapper(func):
        binder = inspect.signature(func).bind
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):
            args = binder(*args, **kwargs)
            args.apply_defaults()
            arguments = args.arguments
            for v, n in norms.items():
                if v in arguments:
                    arguments[v] = n(arguments[v])
            return func(*args.args, **args.kwargs)
        return inner_wrapper
    return wrapper

