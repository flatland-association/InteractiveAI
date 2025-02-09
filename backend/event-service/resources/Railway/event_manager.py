# backend/event-service/resources/Railway/event_manager.py

from api.event_manager.base_event_manager import BaseEventManager

class RailwayEventManager(BaseEventManager):
    def __init__(self):
        super().__init__()
        self.use_case = "Railway"
        self.use_case_process = "cabProcess"
    
    # Optional: Customize Event Uniqueness
    def get_unique_fields(self, data):
        """
        Override to specify unique fields for event uniqueness.
        
        This method specifies the fields on which InteractiveAI will ensure event uniqueness.
        """
        input_line = data["data"].get("line")
        return {"line": input_line}