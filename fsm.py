from abc import ABC, abstractmethod
import time

class Event(ABC):
    @abstractmethod
    def trigger(self):
        pass

class EventHandler(ABC):
    @abstractmethod
    def handle_event(self):
        pass

class State(ABC):
    @abstractmethod
    def handle_event(self):
        pass

class StateMachine(ABC):
    def __init__(self):
        self.current_state = None

    def set_initial_state(self, state):
        self.current_state = state

    @abstractmethod
    def run(self):
        pass

class StateA(State):
    def handle_event(self):
        print("STATE_A")

class StateB(State):
    def handle_event(self):
        print("STATE_B")

class EventInitAB(Event):
    def trigger(self):
        print("Initializing State Machine...")
        return StateA()

class EventTimeoutA(Event):
    def trigger(self):
        print("Timeout A")
        return StateB()

class EventTimeoutB(Event):
    def trigger(self):
        print("Timeout B")
        return StateA()

class InitHandlerAB(EventHandler):
    def handle_event(self):
        print("State Machine Init...")
        return StateA()

class AtoBHandler(EventHandler):
    def handle_event(self):
        print("Transitioning from A to B")
        return StateB()

class BtoAHandler(EventHandler):
    def handle_event(self):
        print("Transitioning from B to A")
        return StateA()

class StateMachineAB(StateMachine):
    def run(self):
        events = [
            EventInitAB(),
            EventTimeoutA(),
            EventTimeoutB()
        ]
        handlers = {
            EventInitAB: InitHandlerAB(),
            EventTimeoutA: AtoBHandler(),
            EventTimeoutB: BtoAHandler()
        }
        self.set_initial_state(handlers[EventInitAB].handle_event())
        while True:
            for event in events:
                time.sleep(1)  # Simulate delay between events
                next_state = handlers[type(event)].handle_event()
                self.current_state = next_state

def test_state_machine():
    state_machine = StateMachineAB()
    state_machine.run()

if __name__ == "__main__":
    test_state_machine()