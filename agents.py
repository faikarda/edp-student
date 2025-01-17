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