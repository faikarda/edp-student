from student import Student
from embassy import Embassy
from embassy_appointment_request_event import EmbassyAppointmentRequestEvent
from appointment_confirmation_event import AppointmentConfirmationEvent




class BaseAgent:
    """Base class for all agents."""
    def __init__(self, name):
        self.name = name

    def handle_request(self, request):
        raise NotImplementedError("This method should be implemented by subclasses.")


class AdvisorAgent(BaseAgent):
    """Agent providing personalized advice on courses or programs."""
    def handle_request(self, request):
        return f"AdvisorAgent: Based on your interest in {request}, I recommend Course XYZ."


class EventCoordinatorAgent(BaseAgent):
    """Agent suggesting upcoming events and activities."""
    def handle_request(self, request):
        return f"EventCoordinatorAgent: Here are some events related to {request}: Hackathon 2025, Workshop on AI."


class MentorAgent(BaseAgent):
    """Agent matching students with mentors."""
    def handle_request(self, request):
        return f"MentorAgent: Based on your interest in {request}, I have matched you with Dr. Smith."


class ResourceLocatorAgent(BaseAgent):
    """Agent helping students find relevant academic or career resources."""
    def handle_request(self, request):
        return f"ResourceLocatorAgent: Here are some resources on {request}: Online Library, Research Papers."


class AgentManager:
    """Manages multiple agents and delegates requests to the appropriate one."""
    def __init__(self):
        self.agents = {
            "advisor": AdvisorAgent("Advisor"),
            "event_coordinator": EventCoordinatorAgent("EventCoordinator"),
            "mentor": MentorAgent("Mentor"),
            "resource_locator": ResourceLocatorAgent("ResourceLocator"),
        }

    def handle_request(self, agent_type, request):
        agent = self.agents.get(agent_type)
        if not agent:
            return f"No agent found for type: {agent_type}"
        return agent.handle_request(request)


# Example usage
if __name__ == "__main__":
    manager = AgentManager()

    # Example requests
    print(manager.handle_request("advisor", "machine learning"))
    print(manager.handle_request("event_coordinator", "technology"))
    print(manager.handle_request("mentor", "data science"))
    print(manager.handle_request("resource_locator", "career development")) 





event_queue = []

# Example Usage
student1 = Student("Piotr1", "Brudny", '1.02.1984', 'Ankara', '5435345345', 'ED4234323', event_queue)
polish_embassy = Embassy('Polish Embassy', 'Ankara, Harika 10', '343242344', 'polishembassy@gov.tr', event_queue)


student1.ask_for_embassy_appointment('10.12.2024')


while event_queue: # it runs as long as there is an event in the list
    event = event_queue.pop(0) # takes the event from the top

    # matches events with the handler
    if isinstance(event, EmbassyAppointmentRequestEvent):
        polish_embassy.handle_appointment_request(event) 
    elif isinstance(event, AppointmentConfirmationEvent):
        student1.handle_appointment_confirmation(event)

    