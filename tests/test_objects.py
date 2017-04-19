# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from smartship.objects import Agent


def test_repr():
    agent = Agent({"quickId": "1"})
    valid_reprs = (
        "Agent({u'quickId': u'1'})",  # Unicode literals
        "Agent({'quickId': '1'})",
    )
    assert repr(agent) in valid_reprs
    data = agent.get_json()
    new_agent = eval(repr(agent))
    assert data == new_agent.get_json()
