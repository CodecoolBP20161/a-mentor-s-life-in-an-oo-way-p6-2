#Education

## Description
This class represent events what a mentor call.

## Parent class
Event

## Attributes

* ```mentor```
  * data type: object
  * description: the mentor obj from csv file
* ```students```
  * data type: object
  * description: the student obj from csv file


## Instance methods

### ```check_schedule```

Check if the mentor is calling the method in the right time

#### Arguments
mentor, event.time

#### Return value

boolean value

## methods

### ```coffee_break```

The mentor 'call' a coffee-break

#### Arguments

time, check_schedule, event.change-level, mentor, student, score

#### Return value
mentor&student energy level, mentor's score

### ```lunch_break```

The mentor 'call' a lunch-break

#### Arguments

time, check_schedule, event.change-level, mentor, student, score

#### Return value
mentor&student energy level, mentor's score

### ```day_begin```

The mentor starts the class in the morning with checking the attendance

#### Arguments

time, check_schedule, mentor, student, score

#### Return value
list of the attendance, mentor's score

### ```day_ending```

The mentor closing the day.

#### Arguments

time, check_schedule, mentor, student

#### Return value
mentor's score
