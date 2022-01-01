class Agent:
    def __init__(self, id: int, value: float, src: int, dest: int, speed: float, pos: str) -> None:
        self.id = id
        self.value = value
        self.src = src
        self.dest = dest
        self.speed = speed
        x, y, _ = pos.split(",")
        self._pos = (float(x), float(y), 0.0)
        self.path = []