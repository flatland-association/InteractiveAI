import importlib

from apiflask import Schema
from apiflask.fields import DateTime, Dict, Integer, String, List, Nested
from apiflask.validators import Length, OneOf
from marshmallow import ValidationError, validates_schema

from .models import UseCaseModel


class MetadataSchema(Schema):
    pass

# workaround to expose schema in openapi.json: copy-paste from resources/Railway
class MetadataSchemaRailway(MetadataSchema):
    trains = List(Dict(), required=False)
    list_of_target = Dict(required=False)
    direction_agents = List(Integer(), required=False)
    position_agents = Dict(required=False)

class ContextIn(Schema):
    use_case = String(
        required=True, validate=OneOf(["PowerGrid", "Railway", "ATM"])
    )
    date = DateTime(format="iso")
    data = Nested(MetadataSchemaRailway)

    @validates_schema
    def validate_metadata(self, data, **kwargs):
        use_case = data.get("use_case")

        usecase_db_data = UseCaseModel.query.filter(
            UseCaseModel.name == use_case
        ).first()
        if usecase_db_data is None:
            raise ValidationError("Invalid use case")

        metadata = data.get("data")

        # Dynamically import the metadata schema class
        metadata_schema_module = importlib.import_module(
            f"resources.{usecase_db_data.name}.schemas"
        )
        metadata_schema_class = getattr(
            metadata_schema_module, f"{usecase_db_data.metadata_schema_class}"
        )
        metadata_schema_class().load(metadata)


class ContextOut(Schema):
    id_context = String()
    use_case = String()
    date = DateTime(format="iso")
    data = Nested(MetadataSchemaRailway)


class UseCaseIn(Schema):
    name = String(required=True, validate=Length(1, 255))
    context_manager_class = String(validate=Length(1, 255))
    metadata_schema_class = String(validate=Length(1, 255))


class UseCaseOut(Schema):
    id = Integer()
    name = String(required=True, validate=Length(1, 255))
    context_manager_class = String(validate=Length(1, 255))
    metadata_schema_class = String(validate=Length(1, 255))
