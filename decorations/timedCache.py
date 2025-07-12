from datetime import datetime

class TimedCache:
    def __init__(self, expiration_time):
        self.cache = {}
        self.expiration_time = expiration_time

    def get(self, func, *args, **kwargs):
        key = (func.__name__, args, tuple(kwargs.items()))
        if key in self.cache:
            now = datetime.now()
            if now - self.cache[key]["timestamp"] < self.expiration_time:
                return self.cache[key]["value"]

        # Cache miss: execute the function and store the result
        result = func(*args, **kwargs)
        self.cache[key] = {"value": result, "timestamp": datetime.now()}
        return result