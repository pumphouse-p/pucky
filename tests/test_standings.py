import unittest
from pucky import standings

class TestStandings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = standings.LeagueStandings()
        cls.num_league_teams = 32
        cls.num_conference_teams = 16
        cls.num_division_teams = 8

    @classmethod
    def tearDownClass(cls):
        pass

    def test_league_standings(self):
        league_standings = self.client.league()
        self.assertEqual(len(league_standings), self.num_league_teams)

    def test_conference_standings(self):
        conference_standings = self.client.conference('Western')
        self.assertEqual(len(conference_standings), self.num_conference_teams)

    def test_division_standings(self):
        division_standings = self.client.division('Atlantic')
        self.assertEqual(len(division_standings), self.num_division_teams)