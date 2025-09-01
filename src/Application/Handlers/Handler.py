from abc import ABC, abstractmethod
from Application.Events.Broker import Broker
from pydantic import BaseModel, ValidationError
from typing import Dict, Any, Optional, TypeVar, Generic

Schema = TypeVar("Schema", bound=BaseModel)

class Handler(Generic[Schema], ABC):
  def __init__(self, broker: Broker, schema: Schema):
    self.broker: Broker = broker
    self.schema: Schema = schema

  def validate(self, data: Dict[str, Any]) -> Optional[Schema]:
    try:
      return self.schema(**data)
    except ValidationError:
      return None

  def handle(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return
    self.process(validated)

  @abstractmethod
  def process(self, validated: Schema) -> None:
    pass
