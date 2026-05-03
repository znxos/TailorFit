import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        # Double-checked locking pattern for thread safety
        if cls._instance is None:
            with cls._lock:
                # Check again while under lock
                if cls._instance is None:
                    cls._instance = super(DatabaseConnection, cls).__new__(cls)
                    cls._instance.is_connected = True
        return cls._instance