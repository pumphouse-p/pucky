import requests

from pucky import constants

class TeamRecord:
    def __init__(self,
        conference,
        division,
        team_name,
        wins,
        losses,
        ot_losses,
        reg_wins,
        goals_against,
        goals_scored,
        points,
        div_rank,
        div_rank_l10,
        div_road_rank,
        div_home_rank,
        div_rank_pp,
        conf_rank,
        conf_rank_l10,
        conf_road_rank,
        conf_home_rank,
        conf_rank_pp,
        league_rank,
        league_rank_l10,
        league_road_rank,
        league_home_rank,
        league_rank_pp,
        wildcard_rank,
        reg_ot_wins,
        games_played,
        streak,
        points_percent,
    ):
        self.conference = conference
        self.division = division
        self.team_name = team_name
        self.wins = int(wins)
        self.losses = int(losses)
        self.ot_losses = int(ot_losses)
        self.reg_wins = int(reg_wins)
        self.goals_against = goals_against
        self.goals_scored = goals_scored
        self.points = int(points)
        self.div_rank = div_rank,
        self.div_rank_l10 = div_rank_l10
        self.div_road_rank = div_road_rank
        self.div_home_rank = div_home_rank
        self.div_rank_pp = div_rank_pp
        self.conf_rank = conf_rank
        self.conf_rank_l10 = conf_rank_l10
        self.conf_road_rank = conf_road_rank
        self.conf_home_rank = conf_home_rank
        self.conf_rank_pp = conf_rank_pp
        self.league_rank = league_rank
        self.league_rank_l10 = league_rank_l10
        self.league_road_rank = league_road_rank
        self.league_home_rank = league_home_rank
        self.league_rank_pp = league_rank_pp
        self.wildcard_rank = wildcard_rank
        self.reg_ot_wins = reg_ot_wins
        self.games_played = games_played
        self.streak = streak
        self.points_percent = points_percent

    def __str__(self):
        return '{} | {} W | {} L | {} OTL | {} PTS'.format(
            self.team_name,
            self.wins,
            self.losses,
            self.ot_losses,
            self.points
        )

class LeagueStandings:
    def __init__(self):
        self.team_records = []
        raw = requests.get(
            constants.NHL_STATSAPI_BASE_URL + 'standings',
            timeout=60
        ).json()

        for d in raw['records']:
            conf_name = d['conference']['name']
            div_name = d['division']['name']
            
            for t in d['teamRecords']:
                rec = TeamRecord(
                    conf_name,
                    div_name,
                    t['team']['name'],
                    t['leagueRecord']['wins'],
                    t['leagueRecord']['losses'],
                    t['leagueRecord']['ot'],
                    t['regulationWins'],
                    t['goalsAgainst'],
                    t['goalsScored'],
                    t['points'],
                    t['divisionRank'],
                    t['divisionL10Rank'],
                    t['divisionRoadRank'],
                    t['divisionHomeRank'],
                    t['ppDivisionRank'],
                    t['conferenceRank'],
                    t['conferenceL10Rank'],
                    t['conferenceRoadRank'],
                    t['conferenceHomeRank'],
                    t['ppConferenceRank'],
                    t['leagueRank'],
                    t['leagueL10Rank'],
                    t['leagueRoadRank'],
                    t['leagueHomeRank'],
                    t['ppLeagueRank'],
                    t['wildCardRank'],
                    t['row'],
                    t['gamesPlayed'],
                    0,
                    t['pointsPercentage']
                )
                self.team_records.append(rec)

    def league(self):
        standings = sorted(self.team_records, key=lambda x: x.points, reverse=True)
        return standings

    def conference(self, conference_name):
        conf_teams = []
        for tr in self.team_records:
            if tr.conference == conference_name:
                conf_teams.append(tr)

        standings = sorted(conf_teams, key=lambda x: x.points, reverse=True)
        
        return standings

    def division(self, division_name):
        div_teams = []
        for tr in self.team_records:
            if tr.division == division_name:
                div_teams.append(tr)

        return div_teams