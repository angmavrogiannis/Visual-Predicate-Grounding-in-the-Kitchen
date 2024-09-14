(define (problem make-sandwich)
    (:domain kitchen)
    (:objects
        robot1 - robot
        bread-slice1 bread-slice2 tomato turkey cheese - ingredient
        knife1 - knife
        counter1 - counter
        plate - container
    )
    
    (:init
        (at bread-slice1 counter)
        (at bread-slice2 counter)
        (at tomato counter)
        (at turkey refrigerator)
        (at cheese refrigerator)
        (at knife1 counter)
        (empty plate)
        (robot-free robot-arm)
    )
    
    (:goal (and
        (at bread-slice1 plate) ;; Put bread slice on the plate
        (at cheese bread-slice1) ;; Put cheese on bread slice
        (at turkey cheese) ;; Put turkey on the cheese
        (at tomato turkey) ;; Put the tomato on the turkey
        (at bread-slice2 tomato) ;; Put the second bread slice on top of the tomato
        (sliced tomato) ;; Tomato needs to be sliced
        (sliced turkey) ;; Turkey needs to be sliced
        (sliced cheese) ;; Cheese needs to be sliced
    ))
)