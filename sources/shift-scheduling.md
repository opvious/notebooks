# Shift scheduling

## Overview

This formulation derives optimal schedules for achieving a given coverage level
per shift at minimum cost. It is a simplified version of [a similar scheduling problem](https://medium.com/walmartglobaltech/automating-shift-scheduling-with-linear-programming-fe1720f13620)
encountered at Walmart.

## Description

 The formulation allows a flexible number of `shifts`, each with its own
 `coverage` (i.e. number of required contractors). We assume access to a pool of
 `contractors` with their own pay `rate` per shift who may also have
 `unavailable` days, during which they cannot be scheduled.

 This formulation produces a schedule for the next `horizon` days which
 minimizes the total cost of contractors while satisfying the following
 constraints:

+ `enoughCoverage`: each shift must be covered by enough contractors.
+ `allAvailable`: all contractors on a shift must be available that day.
+ `atMostOneShiftPerDay`: contractors can be scheduled for at most one shift per
  day.
+ `atMostFiveShiftsPerWeek`: contractors are guaranteed to have at least two
  days off per rolling seven days.

## Specification

### Inputs

+ Planning horizon, $\S^p_{horizon}: h \in \mathbb{N}$
+ Required coverage per shift, $\S^p_{coverage}: c \in \mathbb{N}^{S}$ where
  $\S^d_{shifts}: S$ is the set of shifts
+ Rate per contractor and shift, $\S^p_{rate}: r \in \mathbb{R}_+^{A \times S}$
  where $\S^d_{contractors}: A$ is the set of contractors
+ Contractor unavailability schedule, $\S^p_{unavailable[days]}: v \in \{0,1\}^{D \times A}$
  where $\S^a: D \doteq \{1 \ldots h\}$ is a convenience alias for the set of
  planned days.

### Output

+ Contractor schedule,
  $\S^v_{schedule[days]}: \alpha \in \{0,1\}^{D \times A \times S}$

### Constraints & Objective

We minimize total cost
$\S^o_{totalCost}: \min \sum_{a \in A, d \in D, s \in S} \alpha_{d,a,s} r_{a,s}$ such that:

+ Each shift has enough contractors:

  $$
  \S^c_{enoughCoverage[days]}:
  \forall d \in D, s \in S,
    \sum_{a \in A} \alpha_{d,a,s} \geq c_s
  $$

+ Each contractor is available when scheduled:

  $$
  \S^c_{allAvailable[days]}:
  \forall d \in D, a \in A, s \in S \mid v_{d,a} > 0,
    \alpha_{d,a,s} = 0
  $$

+ Each contractor works at most one shift per day:

  $$
  \S^c_{atMostOneShiftPerDay[days]}:
  \forall d \in D, a \in A,
    \sum_{s \in S} \alpha_{d,a,s} \leq 1
  $$

+ Each constract works at most five shifts per rolling 7 days:

  $$
  \S^c_{atMostFiveShiftsPerWeek[days]}:
  \forall d \in D, a \in A  \mid d < h-5,
    \sum_{d^c \in \{d \ldots d+6\}} \lambda_{d^c,a} \geq 2
  $$

  where $\S^a: \forall a \in A, d \in D, \lambda_{d,a} \doteq 1 - \sum_{s \in S} \alpha_{d,a,s}$.
