import pytest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from employee_class import TeamLead, Developer

team_lead = TeamLead('TestName', '3333', 'backend', 'python', 88)
class TestTeamLeadClassAttributes:
    def test_team_lead_attributes_are_correct(self):
        assert team_lead.name == 'TestName'
        assert team_lead.salary == '3333'
        assert team_lead.department == 'backend'
        assert team_lead.programming_language == 'python'
        assert team_lead.team_size == 88




