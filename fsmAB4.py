import time
from fsm import State, StateMachine, Event, EventHandler, test_state_machine

timeoutA = 1
timeoutB = 2

# Define states as functions that take a State class as an argument
def state_a(StateClass):
    return StateClass()

def state_b(StateClass):
    return StateClass()

# Define events as functions that take an Event class as an argument
def event_init_ab(EventClass):
    print("Initializing State Machine...")
    return EventClass()

def event_timeout_a(EventClass):
    time.sleep(timeoutA)
    return EventClass()

def event_timeout_b(EventClass):
    time.sleep(timeoutB)
    return EventClass()

# Define handlers as functions that take an EventHandler class as an argument
def init_handler_ab(HandlerClass):
    print("State Machine Init...")
    return HandlerClass()

def a_to_b_handler(HandlerClass):
    return HandlerClass()

def b_to_a_handler(HandlerClass):
    print("Transitioning from B to A")
    return HandlerClass()

class StateMachineAB(StateMachine):
    def __init__(self, fsm_config):
        self.fsm_config = fsm_config
        super().__init__()

    def run(self):
        events = [
            event_init_ab,
            event_timeout_a,
            event_timeout_b
        ]
        handlers = {
            event_init_ab: init_handler_ab,
            event_timeout_a: a_to_b_handler,
            event_timeout_b: b_to_a_handler  
        }
        initial_state = state_a(State)  # Instantiate the initial state
        self.set_initial_state(initial_state)  # Set initial state
        
        while True:
            for event_func in events:
                time.sleep(1)  # Simulate delay between events
                next_state_func = handlers[event_func]
                next_state = next_state_func(EventHandler)
                if isinstance(next_state, State):
                    self.current_state = next_state
                else:
                    print("Handler returned an invalid state")

if __name__ == "__main__":
    # Define the state machine configuration
    fsmMachineAB = [
        {'fsmState': state_a, 'fsmEvent': event_init_ab, 'fsmHandler': init_handler_ab},
        {'fsmState': state_a, 'fsmEvent': event_timeout_a, 'fsmHandler': a_to_b_handler},
        {'fsmState': state_b, 'fsmEvent': event_timeout_b, 'fsmHandler': b_to_a_handler}
    ]

    # Test the state machine
    test_state_machine(StateMachineAB, fsmMachineAB)