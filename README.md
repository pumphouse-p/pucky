# PuckY 🏒

An extremely poorly written Python CLI utility that will pull and display various
data points from the NHL API.

## Usage

Display usage information:

```
pucky --help
```

```
Usage: pucky [OPTIONS]

Options:
  -c, --conference [east|west]    Displays the standings of only the given
                                  conference.
  -d, --division [atl|met|cen|pac]
                                  Displays the standings of only the given
                                  division.
  --help                          Show this message and exit.
```

### Standings

Display league wide standings:

```
pucky
```

Display conference standings:

```
pucky --conference east
```

Display division standings:

```
pucky --division pac
```