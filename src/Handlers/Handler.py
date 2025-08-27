from Events.Broker import Broker
from pydantic import BaseModel, ValidationError
from typing import Dict, Any, Optional, TypeVar, Generic

Schema = TypeVar("Schema", bound=BaseModel)

class Handler(Generic[Schema]):
  def __init__(self, broker: Broker, schema: Schema):
    self.broker: Broker = broker
    self.schema: Schema = schema

  def validate(self, data: Dict[str, Any]) -> Optional[Schema]:
    try:
      return self.schema(**data)
    except ValidationError as e:
      print(f"Validation error: {e}")
      return None

  def execute(self, data: Dict[str, Any]) -> None:
    raise NotImplementedError("This method should be overridden by subclasses")
