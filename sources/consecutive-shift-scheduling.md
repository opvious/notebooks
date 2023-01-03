# Consecutive shift scheduling

## Overview

This formulation derives an optimal schedule for assigning staff to shifts while
respecting various constraints. It solves a problem originally used by Walmart,
described [here](https://medium.com/walmartglobaltech/automating-shift-scheduling-with-linear-programming-fe1720f13620).

## Definitions

### Inputs

+ $\S^d_{employee}: E$, set of employees

+ $\S^p_{level}: l \in \mathbb{N}^{E}$, level of each employee

+ $\S^p_{resource}: r \in \mathbb{N}^{S}$, required number of employees per
  shift $\S^d_{shift}: S$

+ $\S^p_{horizon}: h \in \mathbb{N}$, number of days to include in the schedule
  + $\S^a: D \doteq \lbrace 1 \ldots h \rbrace$, convenience alias for the set
    of days until the horizon

### Output

The staffing schedule is the only output:  $\S^v_{schedule[day]}: \alpha \in \lbrace 0,1 \rbrace^{D \times E \times S}$

### Objective

We maximize the total level of scheduled employees: $\S^o: \max \sum_{d \in D, e \in E, s \in S} l_e \alpha_{d,e,s}$

### Constraints

Each employee works at most one shift per day.

$$
  \S^c_{atMostOneShift[day]}:
  \forall d \in D, e \in E,
    \sum_{s \in S} \alpha_{d,e,s} \leq 1
$$

We have enough employees for each shift.

$$
  \S^c_{enoughResource[day]}:
  \forall d \in D, s \in S,
    \sum_{e \in E} \alpha_{d,e,s} \geq r_s
$$

Employees keep the same shift on consecutive work days.

$$
  \S^c_{sameConsecutiveShift[day]}:
  \forall d \in D, e \in E, s \in S \mid d < h,
    \alpha_{d,e,s} + \sum_{s^n \in S \mid s^n \neq s} \alpha_{d+1,e,s^n} \leq 1
$$

Employees rotate shifts at least once every two weeks.

$$
  \S^c_{rotatingShift[day]}:
  \forall d \in D, e \in E, s \in S \mid d < h-13,
    \alpha_{d,e,s} + \alpha_{d+7,e,s} + \alpha_{d+14,e,s} \leq 2
$$

Each employee works at most 5 days per week.

$$
  \S^c_{atMostFiveShiftsPerWeek[day]}:
  \forall d \in D, e \in E \mid d < h-5,
    \sum_{d^c \in \{d \ldots d+6\}} \lambda_{d^c,e} \geq 2
$$

Employees have at least two days off at a time ($\S^a: \forall d \in D, e \in E, \lambda_{d,e} \doteq 1 - \sum_{s \in S} \alpha_{d,e,s}$
is the indicator of an employee being off on a given day).

$$
  \S^c_{consecutiveTimeOff[day]}:
  \forall d \in D, e \in E \mid d < h-1,
    \lambda_{d,e} - \lambda_{d+1,e} + \lambda_{d+2,e} \geq 0
$$
