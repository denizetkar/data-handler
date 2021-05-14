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
        return self.__iadd__(right_value)

    def __sub__(self, right_value: int) -> "SafeInt":
        return self.__isub__(right_value)

    def __mul__(self, right_value: int) -> "SafeInt":
        return self.__imul__(right_value)

    def __truediv__(self, right_value: int) -> float:
        return self.__itruediv__(right_value)

    def __floordiv__(self, right_value: int) -> "SafeInt":
        return self.__ifloordiv__(right_value)

    def __mod__(self, right_value: int) -> "SafeInt":
        return self.__imod__(right_value)

    def __pow__(self, exponent: int, modulo: Optional[int] = None) -> "SafeInt":
        return self.__ipow__(exponent, modulo)

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
        with self._lock:
            return hash(self._value)

    def __str__(self) -> str:
        with self._lock:
            return str(self._value)

    def __repr__(self) -> str:
        with self._lock:
            return repr(self._value)
