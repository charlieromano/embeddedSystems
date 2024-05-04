import time
from fsm import StateMachine 
from fsm import State, Event, EventHandler
from fsm import test_state_machine

timeoutA = 1
timeoutB = 2

class StateA(State):
    pass

class StateB(State):
    pass

class EventInitAB(Event):
    def trigger(self):
        print("Initializing State Machine...")
        return StateA()

class EventTimeoutA(Event):
    def trigger(self):
        time.sleep(timeoutA)
        return StateB()

class EventTimeoutB(Event):
    def trigger(self):
        time.sleep(timeoutB)
        return StateA()

class InitHandlerAB(EventHandler):
    def handle_event(self) -> State:
        print("State Machine Init...")
        return StateA()

class AtoBHandler(EventHandler):
    def handle_event(self) -> State:
        return StateB()

class BtoAHandler(EventHandler):
    def handle_event(self) -> State:
        print("Transitioning from B to A")
        return StateA()

class StateMachineAB(StateMachine):
    def __init__(self, fsm_config):
        self.fsm_config = fsm_config
        super().__init__()

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
        self.set_initial_state(StateA())  # Set initial state
        
        while True:
            for event in events:
                time.sleep(1)  # Simulate delay between events
                next_state = handlers[type(event)].handle_event()
                if isinstance(next_state, State) and isinstance(next_state, (StateA, StateB)):
                    self.current_state = next_state
                else:
                    print("Handler returned an invalid state")

if __name__ == "__main__":
    # Define the state machine configuration
    fsmMachineAB = [
        {'fsmState': StateA(), 'fsmEvent': EventInitAB(), 'fsmHandler': InitHandlerAB()},
        {'fsmState': StateA(), 'fsmEvent': EventTimeoutA(), 'fsmHandler': AtoBHandler()},
        {'fsmState': StateB(), 'fsmEvent': EventTimeoutB(), 'fsmHandler': BtoAHandler()}
    ]

    # Test the state machine
    test_state_machine(StateMachineAB, fsmMachineAB)