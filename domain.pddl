(define (domain kitchen)
(:requirements :typing :equality)
(:types 
	robot
	appliance counter container ingredient utensil - object
	appliance container counter ingredient - location
	appliance container - receptacle
	knife - utensil
)

(:predicates
	(at ?o - object ?l - location)
	(robot-free ?r robot)
	(empty ?r receptacle)
	(sliced ?i - ingredient)
	(stirred ?i - ingredient)
	(picked-up ?o - object)
	(opened ?a - appliance)
	(turned-on ?a - appliance)
)

(:action pick-up
	:parameters (?r - robot ?o - object ?l - location)
	:precondition (and
	 	(robot-free ?r)
		(not (picked-up ?o))
		(at ?o ?l)
	)
	:effect (and
		(not (robot-free ?r))
		(picked-up ?o)
		(not (at ?o ?l))
	)
)

(:action place
	:parameters (?r - robot ?o - object ?l - location)
	:precondition (and
		(not (robot-free ?r))
		(picked-up ?o)
		(not (at ?o ?l))
	)
	:effect (and
		(robot-free ?r)
		(not (picked-up ?o))
		(at ?o ?l)
	)
)

(:action put-in
	:parameters (?r - robot ?o - object ?a - appliance)
	:precondition (and
		(not (robot-free ?r))
		(picked-up ?o)
		(not (at ?o ?a))
		(empty ?a)
	)
	:effect (and
		(robot-free ?r)
		(not (picked-up ?o))
		(at ?o ?a)
		(not (empty ?a))
	)
)

(:action cut
	:parameters (?r - robot ?k - knife ?i - ingredient)
	:precondition (and
	 	(picked-up ?k)
		(not (sliced ?i))
	)
	:effect (sliced ?i)
)

(:action stir
	:parameters (?r - robot ?u - utensil ?i - ingredient ?c - container)
	:precondition (and
	 	(picked-up ?u)
	 	(at ?i ?c)
		(not (stirred ?i))
		(not (empty ?c))
	)
	:effect (stirred ?i)
)

(:action pour
	:parameters (?r - robot ?i1 - ingredient ?i2 - ingredient ?c - container)
	:precondition (and
		(at ?i1 ?c)
		(not (empty ?c))
	 	(picked-up ?c)
	)
	 :effect (and
		(at ?i1 ?i2)
		(empty ?c)
	)
)

(:action turn-on
	:parameters (?r - robot ?a - appliance)
	:precondition (and
	 	(robot-free ?r)
		(not (turned-on ?a))
	)
	:effect (turned-on ?a)
)

(:action turn-off
	:parameters (?r - robot ?a - appliance)
	:precondition (and
	 	(robot-free ?r)
		(turned-on ?a)
	)
	:effect (not (turned-on ?a))
)

(:action open
	:parameters (?r - robot ?a - appliance)
	:precondition (and
	 	(robot-free ?r)
		(not (opened ?a))
	)
	:effect (opened ?a)
)

(:action close
	:parameters (?r - robot ?a - appliance)
	:precondition (and  
	 	(robot-free ?r)
		(opened ?a)
	)
	:effect (not (opened ?a))
)

(:axiom
    :vars (?i1 - ingredient ?i2 - ingredient ?c - container)
    :context (and
        (at ?i1 ?i2)
        (at ?i2 ?c)
    )
    :implies (at ?i1 ?c)
)