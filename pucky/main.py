import click
from prettytable import PrettyTable

from .standings import LeagueStandings

@click.command()
@click.option(
    "-c",
    "--conference",
    required=False,
    type=click.Choice(['east', 'west']),
    help="Displays the standings of only the given conference.",
)
@click.option(
    "-d",
    "--division",
    required=False,
    type=click.Choice(['atl', 'met', 'cen', 'pac']),
    help="Displays the standings of only the given division.",
)
def main(conference, division):
    league = LeagueStandings()
    standings = league.league()

    if conference == 'east':
        standings = league.conference('Eastern')
    elif conference == 'west':
        standings = league.conference('Western')
    
    if division == 'atl':
        standings = league.division('Atlantic')
    elif division == 'met':
        standings = league.division('Metropolitan')
    elif division == 'cen':
        standings = league.division('Central')
    elif division == 'pac':
        standings = league.division('Pacific')

    _print_standings(standings)

def _print_standings(standings):
    tbl = PrettyTable()
    tbl.field_names = [
        'TEAM',
        'W',
        'L',
        'OTL',
        'PTS',
        'P%',
        'RW',
        'ROW',
        'GF',
        'GA',
        'DIFF'
    ]
    for team in standings:
        tbl.add_row([
            team.team_name,
            team.wins,
            team.losses,
            team.ot_losses,
            team.points,
            ('{:.3f}'.format(team.points_percent)),
            team.reg_wins,
            team.reg_ot_wins,
            team.goals_scored,
            team.goals_against,
            (team.goals_scored - team.goals_against)
        ])
    print(tbl)

if __name__ == '__main__':
    main()