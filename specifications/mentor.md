# Mentor

## Description
This class represents a mentor in real life.

## Parent class
Person


## Attributes

* ```nickname```
  * data type: string
  * description: stores the nicknames the students gave the mentors
* ```charisma```
  * data type: integer
  * description: stores the level of the charisma the mentors have. It is dependent on the actions of the mentors. If a mentor makes a bad decision or loses a foosball game they lose charisma points.


## Class methods

### ```create_by_csv```
Returns a list of the mentors from a .csv file.

#### Arguments
A csv file path

## Instance methods

### ```__init__```
Calls the Person class' constructor, and also set's the nickname attribute (raises an error, if empty).

#### Arguments
All of the arguments of the class itself and the parent class.

#### Return value
None
