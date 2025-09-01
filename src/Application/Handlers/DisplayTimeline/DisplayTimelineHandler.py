from Domain.Models.Event import Event
from Domain.Models.Person import Person
from Domain.Models.Relation import Relation
from Domain.Models.Timeline import Timeline

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.DisplayedTimelineEvent import DisplayedTimelineEvent
from Application.Handlers.DisplayTimeline.DisplayTimelineSchema import DisplayTimelineSchema

class DisplayTimelineHandler(Handler[DisplayTimelineSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, DisplayTimelineSchema)

  def process(self, validated: DisplayTimelineSchema):
    person = Person.get_by_id(validated.person_id)
    if not person: return

    partner = None
    if person.gender == "M":
      relation = Relation.select().where((Relation.man == person) & (Relation.status == "C")).first()
      if relation: partner = relation.woman
    else:
      relation = Relation.select().where((Relation.woman == person) & (Relation.status == "C")).first()
      if relation: partner = relation.man

    timeline_events = []
    timelines = (Timeline
                .select(Timeline, Event)
                .join(Event)
                .where(Timeline.person == person)
                .order_by(Timeline.timestamp))
    
    for timeline in timelines:
      timeline_events.append({
        "name": timeline.event.name,
        "label": timeline.event.label,
        "timestamp": timeline.timestamp
      })

    data = {
      "person": person,
      "father": person.father,
      "mother": person.mother,
      "guard": person.guard,
      "partner": partner,
      "timeline": timeline_events
    }

    print(data["timeline"])

    self.broker.publish(DisplayedTimelineEvent({
      "person_id": validated.person_id,
      "data": data
    }))
