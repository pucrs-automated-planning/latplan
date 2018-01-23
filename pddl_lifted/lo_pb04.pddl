(define (problem pb4)
  (:domain lights)
  (:objects
    c01 c02 c03 c04
    c05 c06 c07 c08
    c09 c10 c11 c12
    c13 c14 c15 c16
  )
  (:init
    (on c01)                   (on c04)
             (on c06) (on c07) (on c08)
    (on c09) (on c10) (on c11) (on c12)
                      (on c15) (on c16)
    (corner c01) (border c02) (border c03) (corner c04)
    (border c05) (center c06) (center c07) (border c08)
    (border c09) (center c10) (center c11) (border c12)
    (corner c13) (border c14) (border c15) (corner c16)
    (adjacent c01 c02) (adjacent c01 c05)
    (adjacent c02 c01) (adjacent c02 c03) (adjacent c02 c06)
    (adjacent c03 c02) (adjacent c03 c04) (adjacent c03 c07)
    (adjacent c04 c03) (adjacent c04 c08)
    (adjacent c05 c01) (adjacent c05 c06) (adjacent c05 c09)
    (adjacent c06 c02) (adjacent c06 c05) (adjacent c06 c07) (adjacent c06 c10)
    (adjacent c07 c03) (adjacent c07 c06) (adjacent c07 c08) (adjacent c07 c11)
    (adjacent c08 c04) (adjacent c08 c07) (adjacent c08 c12)
    (adjacent c09 c05) (adjacent c09 c10) (adjacent c09 c13)
    (adjacent c10 c06) (adjacent c10 c09) (adjacent c10 c11) (adjacent c10 c14)
    (adjacent c11 c07) (adjacent c11 c10) (adjacent c11 c12) (adjacent c11 c15)
    (adjacent c12 c08) (adjacent c12 c11) (adjacent c12 c16)
    (adjacent c13 c09) (adjacent c13 c14)
    (adjacent c14 c10) (adjacent c14 c13) (adjacent c14 c15)
    (adjacent c15 c11) (adjacent c15 c14) (adjacent c15 c16)
    (adjacent c16 c12) (adjacent c16 c15)
  )
  (:goal (and
         (on c01)  (not (on c02))      (on c03)       (on c04)
    (not (on c05))      (on c06)  (not (on c07)) (not (on c08))
         (on c09)       (on c10)       (on c11)       (on c12)
    (not (on c13))      (on c14)  (not (on c15))      (on c16)
  ))
)