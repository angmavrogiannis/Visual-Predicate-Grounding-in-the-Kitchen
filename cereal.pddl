(define (problem cereal)
    (:domain kitchen)
    (:objects
        robot-arm - robot
        refrigerator - appliance
        milk cereal - ingredient
        spoon - utensil
        counter - receptacle
        bowl milk-carton - container
    )
    
    (:init
        (robot-free robot-arm)
        (at cereal-box cabinet)
        (at cereal cereal-box)
        (at bowl counter)
        (at milk-carton refrigerator)
        (at milk milk-carton)
        (at knife1 counter)
    )
    
    (:goal (and
        (at milk bowl) ;; Put milk in the bowl
        (at cereal bowl) ;; Put cereal in the bowl
        (at spoon bowl) ;; Put spoon in the bowl
        (not (empty bowl)) ;; bowl is full
    ))
)