# InteractiveAI: Adding a New Usecase

## Setup Instructions

### 1. Adding Resources for InteractiveAI Services

Before starting InteractiveAI, it's recommended to set up the following services:

#### 1.1 Event Service

To set up the Event Service for your use case (PowerGrid), follow these steps:

#### 1. Create a Folder and Files

Start by creating a folder named `PowerGrid` under `backend/event-service/resources` with the following files:

##### `event_manager.py`

event_manager.py defines a custom event manager (PowerGridEventManager) tailored for the PowerGrid use case within InteractiveAI, allowing customization of event handling behaviors, such as ensuring uniqueness based on specified fields.


```python
# backend/event-service/resources/PowerGrid/event_manager.py

from api.event_manager.base_event_manager import BaseEventManager

class PowerGridEventManager(BaseEventManager):
    def __init__(self):
        super().__init__()
        self.use_case = "PowerGrid"
        self.use_case_process = "cabProcess"
    
    # Optional: Customize Event Uniqueness
    def get_unique_fields(self, data):
        """
        Override to specify unique fields for event uniqueness.
        
        This method specifies the fields on which InteractiveAI will ensure event uniqueness.
        """
        input_line = data["data"].get("line")
        return {"line": input_line}
```

##### `schemas.py`

schemas.py defines the metadata schema (MetadataSchemaPowerGrid) used by InteractiveAI to validate and structure incoming events specific to the PowerGrid use case, ensuring data consistency and compliance with predefined formats and rules.

```python
# backend/event-service/resources/PowerGrid/schemas.py

from apiflask.fields import Float, String, Dict
from apiflask.validators import OneOf
from api.schemas import MetadataSchema

class MetadataSchemaPowerGrid(MetadataSchema):
    event_type = String(
        required=True,
        validate=OneOf(["KPI", "anticipation", "agent", "consignation"]),
    )
    creation_date = String()
    zone = String(validate=OneOf(["Est", "Ouest", "Centre"]))
    line = String(required=True)
    flux = Float()
    kpis = Dict(required=True)
    event_context = String()
```

#### Optional: Customize Event Uniqueness

The `PowerGridEventManager` class can override the `get_unique_fields` method to specify unique fields for ensuring event uniqueness in InteractiveAI. Modify this method according to your specific requirements and the data structure of your events.

#### 2. Integration with InteractiveAI

Further integration steps with InteractiveAI will depend on your specific deployment and configuration needs.


#### 1.2 Context Service

#### Files for PowerGrid in Context Service

To integrate PowerGrid with the Context Service, create the following files under `backend/context-service/resources/PowerGrid`:

###### `context_manager.py`

`context_manager.py` defines a custom context manager (`PowerGridContextManager`) for the PowerGrid use case within the Context Service, inheriting from `BaseContextManager` to manage context-related operations.


```python
# backend/context-service/resources/PowerGrid/context_manager.py

from api.context_manager.base_context_manager import BaseContextManager

class PowerGridContextManager(BaseContextManager):
    def __init__(self):
        super().__init__()
        self.use_case = "PowerGrid"
```


###### `schemas.py`

`schemas.py` defines the metadata schema (`MetadataSchemaPowerGrid`) used by the Context Service to validate and structure data specific to the PowerGrid use case ensuring data integrity and adherence to predefined formats.


```python
# backend/context-service/resources/PowerGrid/schemas.py

from api.schemas import MetadataSchema
from apiflask.fields import Dict, String

class MetadataSchemaPowerGrid(MetadataSchema):
    topology = String(allow_none=False)
    observation = Dict(allow_none=False)
```


#### 1.3 Recommendation Service

No specific setup instructions provided.

##### File for PowerGrid in Recommendation Service

To integrate PowerGrid with the Recommendation Service, create the following file under `backend/recommendation-service/resources/PowerGrid`:

###### `manager.py`

`manager.py` defines a custom recommendation manager (`PowerGridManager`) for the PowerGrid use case within the Recommendation Service. It extends `BaseRecommendationManager` and overrides the `get_recommendation` method to generate PowerGrid-specific recommendations based on `request_data`.
This file enables PowerGrid-specific recommendation functionality within the Recommendation Service of InteractiveAI.

```python
# backend/recommendation-service/resources/PowerGrid/manager.py

from api.manager.base_manager import BaseRecommendationManager

class PowerGridManager(BaseRecommendationManager):
    def __init__(self):
        super().__init__()

    def get_recommendation(self, request_data):
        """
        Override to provide recommendations specific to the PowerGrid use case.
        
        This method generates and returns recommendations tailored for PowerGrid.
        """
        action_dict = {}

        output_json = {
            "title": "recommendation",
            "description": "description",
            "use_case": "PowerGrid",
            "agent_type": "agent_type",
            "actions": [action_dict],
        }

        return [output_json]
```

### 2. Users, Groups, and Entities Administration

InteractiveAI utilizes the user management system based on the OperatorFabric project. For detailed information, refer to the [OperatorFabric Documentation](https://opfab.github.io/documentation/current/deployment/#_users_groups_and_entities_administration).

## Users, Groups, and Entities Administration

After setting up InteractiveAI, follow these steps to manage users, groups, and entities:

### 1. Users

Retrieve a list of users:

```bash
curl -v http://localhost:2103/users -H "Authorization:Bearer $token" -H "Content-Type:application/type"
```

Example Response:
```json
[
    {"login": "admin", "entities": ["PowerGrid"], "groups": ["ADMIN"]},
    {"login": "PowerGrid_user", "entities": ["PowerGrid"], "groups": ["ReadOnly", "PowerGrid", "ADMIN", "Dispatcher"]}
]
```

### 2. Groups

Retrieve a list of groups:

```bash
curl http://localhost:2103/groups -H "Authorization:Bearer $token" -H "Content-Type:application/json"
```

Example Response:
```json
[
    {"id": "ADMIN", "name": "ADMINISTRATORS", "description": "The admin group", "realtime": false},
    {"id": "PowerGrid", "name": "RTE France", "description": "RTE TSO Group", "realtime": false},
    {"id": "Dispatcher", "name": "Dispatcher", "description": "Dispatcher Group", "perimeters": ["cabProcess"], "realtime": true},
    {"id": "Planner", "name": "Planner", "description": "Planner Group", "perimeters": ["cabProcess"], "realtime": true},
    {"id": "Supervisor", "name": "Supervisor", "description": "Supervisor Group", "perimeters": ["cabProcess"], "realtime": true},
    {"id": "Manager", "name": "Manager", "description": "Manager Group", "realtime": false},
    {"id": "ReadOnly", "name": "ReadOnly", "description": "ReadOnly Group", "realtime": false}
]
```

### 3. Entities

Retrieve a list of entities:

```bash
curl http://localhost:2103/entities -H "Authorization:Bearer $token" -H "Content-Type:application/json"
```

Example Response:
```json
[
    {"id": "PowerGrid", "name": "Electricity Transmission Network", "description": "Electricity Transmission Network", "entityAllowedToSendCard": true, "parents": ["IRT_MAIN"]},
    {"id": "IRT_MAIN", "name": "IRT Control Centers", "description": "IRT Control Centers", "entityAllowedToSendCard": false}
]
```

## Loading Event, Context, and Recommendation Resources

Follow these steps to load resources for event, context, and recommendation:

### 1. Event

Post a new event use case:

```bash
curl -X POST $url:3200/cab_event/api/v1/usecases -H "Content-type:application/json" -H "Authorization:Bearer $token" --data @$1.json -v
```

Example JSON (`PowerGridEvent.json`):
```json
{
    "name": "PowerGrid",
    "event_manager_class": "PowerGridEventManager",
    "metadata_schema_class": "MetadataSchemaPowerGrid"
}
```

### 2. Context

Post a new context use case:

```bash
curl -X POST $url:3200/cabcontext/api/v1/usecases -H "Content-type:application/json" -H "Authorization:Bearer $token" --data @$1.json -v
```

Example JSON (`PowerGridContext.json`):
```json
{
    "name": "PowerGrid",
    "context_manager_class": "PowerGridContextManager",
    "metadata_schema_class": "MetadataSchemaPowerGrid"
}
```

### 3. Recommendation

Post a new recommendation use case:

```bash
curl -X POST $url:3200/cab_recommendation/api/v1/usecases -H "Content-type:application/json" -H "Authorization:Bearer $token" --data @$1.json -v
```

Example JSON (`PowerGridRecommendationUC.json`):
```json
{
    "name": "PowerGrid",
    "manager_class": "PowerGridManager"
}
```
