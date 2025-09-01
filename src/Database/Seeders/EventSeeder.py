from typing import List
from Database.Core.Seeder import Seeder
from Application.Events.Event import Event
from Domain.Models.Event import Event as Model

from Application.Events.Person.PersonBornEvent import PersonBornEvent
from Application.Events.Person.NewChildrenEvent import NewChildrenEvent
from Application.Events.Person.CousinsFoundEvent import CousinsFoundEvent
from Application.Events.Person.MatchedPeopleEvent import MatchedPeopleEvent
from Application.Events.Person.RelatedPeopleEvent import RelatedPeopleEvent
from Application.Events.Person.DeathedPersonEvent import DeathedPersonEvent
from Application.Events.Person.WidowedPersonEvent import WidowedPersonEvent
from Application.Events.Person.RelativesFoundEvent import RelativesFoundEvent
from Application.Events.Person.RegisteredPersonEvent import RegisteredPersonEvent
from Application.Events.Person.DisplayedTimelineEvent import DisplayedTimelineEvent
from Application.Events.Person.RecentBirthsFoundEvent import RecentBirthsFoundEvent
from Application.Events.Person.DeathedPeopleFoundEvent import DeathedPeopleFoundEvent
from Application.Events.Person.ChildrenTogetherFoundEvent import ChildrenTogetherFoundEvent
from Application.Events.Person.DescendantsFoundAliveEvent import DescendantsFoundAliveEvent
from Application.Events.Person.MaternalAncestorsFoundEvent import MaternalAncestorsFoundEvent

class EventSeeder(Seeder):
  def seed(self) -> None:
    events: List[Event] = [
      PersonBornEvent,
      NewChildrenEvent,
      CousinsFoundEvent,
      RelatedPeopleEvent,
      MatchedPeopleEvent,
      DeathedPersonEvent,
      WidowedPersonEvent,
      RelativesFoundEvent,
      RegisteredPersonEvent,
      DisplayedTimelineEvent,
      RecentBirthsFoundEvent,
      DeathedPeopleFoundEvent,
      ChildrenTogetherFoundEvent,
      DescendantsFoundAliveEvent,
      MaternalAncestorsFoundEvent,
    ]

    for event in events:
      Model.create(name=event.name, label=event.label)
