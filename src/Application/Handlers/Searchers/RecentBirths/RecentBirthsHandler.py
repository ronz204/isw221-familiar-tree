from Domain.Models.Person import Person
from datetime import datetime, timedelta

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.RecentBirthsFoundEvent import RecentBirthsFoundEvent
from Application.Handlers.Searchers.RecentBirths.RecentBirthsSchema import RecentBirthsSchema

class RecentBirthsHandler(Handler[RecentBirthsSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, RecentBirthsSchema)

  def process(self, validated: RecentBirthsSchema):
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

    self.broker.publish(RecentBirthsFoundEvent({
      "births": births_list,
      "total_count": len(births_list)
    }))
