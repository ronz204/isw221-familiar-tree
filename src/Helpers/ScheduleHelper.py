from typing import Dict
from threading import Timer
from Handlers.Handler import Handler

class ScheduleHelper:
  def __init__(self):
    self.timers: Dict[str, Timer] = {}

  def start(self, handler: Handler, seconds: int, name: str):
    if name in self.timers:
      self.timers[name].cancel()

    def run():
      try:
        handler.execute()
      except Exception as e:
        print(f"Error executing handler {name}: {e}")
      finally:
        if name in self.timers:
          self.start(handler, seconds, name)
    
    self.timers[name] = Timer(seconds, run)
    self.timers[name].start()
  
  def stop(self, name: str):
    if name in self.timers:
      self.timers[name].cancel()
      del self.timers[name]
  
  def stop_all(self):
    for timer in self.timers.values():
      timer.cancel()
    self.timers.clear()
