import threading
from typing import Optional


class SafeInt:
    def __init__(self, value: int):
        self._value = value
        self._lock = threading.Lock()

    @property
    def value(self) -> int:
        with self._lock:
            return self._value

    def increment(self, maximum: Optional[int] = None):
        with self._lock:
            if maximum is None:
                self._value += 1
            else:
                self._value = min(maximum, self._value + 1)

    def decrement(self, minimum: Optional[int] = None):
        with self._lock:
            if minimum is None:
                self._value -= 1
            else:
                self._value = max(minimum, self._value - 1)

    def __iadd__(self, right_value: int) -> "SafeInt":
        with self._lock:
            self._value += right_value
            return self

    def __isub__(self, right_value: int) -> "SafeInt":
        return self.__iadd__(-right_value)

    def __imul__(self, right_value: int) -> "SafeInt":
        with self._lock:
            self._value *= right_value
            return self

    def __itruediv__(self, right_value: int) -> float:
        with self._lock:
            return self._value / right_value

    def __ifloordiv__(self, right_value: int) -> "SafeInt":
        with self._lock:
            self._value //= right_value
            return self

    def __imod__(self, right_value: int) -> "SafeInt":
        with self._lock:
            self._value %= right_value
            return self

    def __ipow__(self, exponent: int, modulo: Optional[int] = None) -> "SafeInt":
        with self._lock:
            self._value = pow(self._value, exponent, modulo)
            return self

    def __add__(self, right_value: int) -> "SafeInt":
        self += right_value
        return self

    def __sub__(self, right_value: int) -> "SafeInt":
        self -= right_value
        return self

    def __mul__(self, right_value: int) -> "SafeInt":
        self *= right_value
        return self

    def __truediv__(self, right_value: int) -> float:
        self /= right_value
        return self

    def __floordiv__(self, right_value: int) -> "SafeInt":
        self //= right_value
        return self

    def __mod__(self, right_value: int) -> "SafeInt":
        self %= right_value
        return self

    def __pow__(self, exponent: int, modulo: Optional[int] = None) -> "SafeInt":
        self **= exponent % modulo
        return self

    def __lt__(self, right_value: int) -> bool:
        with self._lock:
            return self._value < right_value

    def __le__(self, right_value: int) -> bool:
        with self._lock:
            return self._value <= right_value

    def __eq__(self, right_value: int) -> bool:
        with self._lock:
            return self._value == right_value

    def __ne__(self, right_value: int) -> bool:
        with self._lock:
            return self._value != right_value

    def __gt__(self, right_value: int) -> bool:
        with self._lock:
            return self._value > right_value

    def __ge__(self, right_value: int) -> bool:
        with self._lock:
            return self._value >= right_value

    def __hash__(self) -> int:
        return hash(self._value)

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return repr(self._value)
