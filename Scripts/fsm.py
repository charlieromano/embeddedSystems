from abc import ABC, abstractmethod

class State(ABC):
    pass

class Event(ABC):
    @abstractmethod
    def trigger(self):
        pass

class EventHandler(ABC):
    @abstractmethod
    def handle_event(self) -> State:
        pass

class StateMachine(ABC):
    def __init__(self):
        self.current_state = None

    def set_initial_state(self, state: State):
        self.current_state = state

    @abstractmethod
    def run(self):
        pass

def test_state_machine(state_machine_cls, fsm_config):
    state_machine = state_machine_cls(fsm_config)

    # Count and print total number of defined states
    states_count = len({entry['fsmState'].__class__.__name__ for entry in fsm_config})
    print(f"Total number of defined states: {states_count}")

    # Count and print total number of defined events
    events_count = len({entry['fsmEvent'] for entry in fsm_config})
    print(f"Total number of defined events: {events_count}")

    # Print names of states and events if available
    print("\nNames of states and events:")
    for entry in fsm_config:
        state = entry['fsmState']
        event = entry['fsmEvent']
        handler = entry['fsmHandler']
        state_name = getattr(state, 'name', None) or type(state).__name__
        event_name = getattr(event, 'name', None) or event
        handler_name = getattr(handler, 'name', None) or type(handler).__name__
        print(f"State: {state_name}, Event: {event_name}, Handler: {handler_name}")

    # Run the state machine
    state_machine.run()