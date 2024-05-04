import time

class State:
    def handle_event(self, event):
        pass

class StateA(State):
    def __init__(self):
        self.name = "StateA"

    def handle_event(self, event):
        if event == 'timer_1':
            print(f"{self.name} at {time.time()}")
            return StateB()

class StateB(State):
    def __init__(self):
        self.name = "StateB"

    def handle_event(self, event):
        if event == 'timer_2':
            print(f"{self.name} at {time.time()}")
            return StateA()

class StateMachine:
    def __init__(self):
        self.current_state = None

    def set_initial_state(self, state):
        self.current_state = state

    def trigger_event(self, event):
        if self.current_state:
            self.current_state = self.current_state.handle_event(event)
        else:
            print("Initial state not set.")

    def run(self):
        while True:
            self.trigger_event('timer_1')
            time.sleep(2)  # Wait for timer_1 event
            self.trigger_event('timer_2')
            time.sleep(3)  # Wait for timer_2 event

# Create instances of states and state machine
state_machine = StateMachine()
stateA = StateA()
stateB = StateB()

# Set initial state
state_machine.set_initial_state(stateA)

# Run the state machine indefinitely
state_machine.run()