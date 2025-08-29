from typing import Dict, Any
from Events.Broker import Broker
from Models.Person import Person
from Handlers.Handler import Handler
from datetime import datetime, timedelta

from Handlers.Queries.RecentBirths.RecentBirthsEvent import RecentBirthsEvent
from Handlers.Queries.RecentBirths.RecentBirthsSchema import RecentBirthsSchema

class RecentBirthsHandler(Handler[RecentBirthsSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, RecentBirthsSchema)

  def execute(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return

    ten_years_ago = datetime.now().date() - timedelta(days=10*365)
    recent_births = Person.select().where(Person.birthdate >= ten_years_ago)

    births_list = [
      {
        "id": person.id,
        "name": person.name,
        "cedula": person.cedula,
        "birthdate": person.birthdate.strftime("%Y-%m-%d"),
      } for person in recent_births
    ]

    self.broker.publish(RecentBirthsEvent({
      "births": births_list,
      "total_count": len(births_list)
    }))
