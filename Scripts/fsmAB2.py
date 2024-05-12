from abc import ABC, abstractmethod
import time

class State(ABC):
    @abstractmethod
    def handle_event(self):
        pass

class StateA(State):
    def handle_event(self):
        print("STATE_A")

class StateB(State):
    def handle_event(self):
        print("STATE_B")

class StateMachine(ABC):
    @abstractmethod
    def run(self):
        pass

class StateMachine_AB(StateMachine):
    def __init__(self):
        self.current_state = None

    def set_initial_state(self, state):
        self.current_state = state

    def run(self):
        while True:
            if self.current_state:
                self.current_state.handle_event()
            else:
                print("Initial state not set.")

# Define event types
class Event:
    INIT_AB = 'evInit_AB'
    TIMEOUT_A = 'evTimeout_A'
    TIMEOUT_B = 'evTimeout_B'

# Define handler functions
def InitHandler_AB():
    print("State Machine Init...")
    return StateA()

def AtoBHandler():
    print("Transitioning from A to B")
    return StateB()

def BtoAHandler():
    print("Transitioning from B to A")
    return StateA()

# Define state machine configuration
fsmMachineAB = [
    {'fsmState': StateA(), 'fsmEvent': Event.INIT_AB, 'fsmHandler': InitHandler_AB},
    {'fsmState': StateA(), 'fsmEvent': Event.TIMEOUT_A, 'fsmHandler': AtoBHandler},
    {'fsmState': StateB(), 'fsmEvent': Event.TIMEOUT_B, 'fsmHandler': BtoAHandler}
]

# Test the state machine
def test_state_machine():
    state_machine = StateMachine_AB()
    state_machine.set_initial_state(StateA())
    while(True):
        time.sleep(1)
        for entry in fsmMachineAB:
            state = entry['fsmState']
            event = entry['fsmEvent']
            handler = entry['fsmHandler']
            print(f"Triggering event: {event}")
            next_state = handler()
            state_machine.current_state = next_state

if __name__ == "__main__":
    test_state_machine()
