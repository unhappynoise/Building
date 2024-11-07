class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = (0, 23)
        self.minutes = (0, 59)
        self.seconds = (0, 59)
        self.current_hours = hours
        self.current_minutes = minutes
        self.current_seconds = seconds

    def __str__(self):
        return f"{self.current_hours:02d}:{self.current_minutes:02d}:{self.current_seconds:02d}"

    def next_second(self):
        self.current_seconds += 1
        if self.current_seconds > 59:
            self.current_seconds = 0
            self.current_minutes += 1
            if self.current_minutes > 59:
                self.current_minutes = 0
                self.current_hours += 1
                if self.current_hours > 23:
                    self.current_hours = 0

    def previous_second(self):
        self.current_seconds -= 1
        if self.current_seconds < 0:
            self.current_seconds = 59
            self.current_minutes -= 1
            if self.current_minutes < 0:
                self.current_minutes = 59
                self.current_hours -= 1
                if self.current_hours > 0:
                    self.current_hours = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.previous_second()
print(timer)