# Fun

## Description
This class represents the fun activities at CodeCool.

## Parent class
None

## Attributes

* ```list of participants```
  * data type: list
  * description: stores the participant objects

## Class methods

### None



#### Arguments
None

#### Return value


## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```select_teams()```

Reads the students csv and selects teams of 2.
Teams are only accepted if it is in the sol list.

#### Arguments
* ```None```

#### Return value
Returns a list of lists aka teams!

### ```decide()```

decides between two teams and plays the games between them until the score 6!

#### Arguments
* ```team1```
  * data type: list
  * description: stores team 1 players
* ```team2```
  * data type: list
  * description: stores team 2 players
* ```xsco```
  * data type: integer
  * description: team 1 score
* ```ysco```
  * data type: integer
  * description: team 2 score

#### Return value
Returns a 3 element tuple, (winner team, xsco, ysco)

### ```game()```

the main method of the fun class

#### Arguments
* ```team```
 * data type: list of lists
 * description: stores the teams in list of lists that it got from the select_teams method

#### Return value
None
