
; Take a long string and break it into 13bp fragments
; Take 13bp fragments, add GCC and CAG onto the ends
; Take first three letters, search list if those 3 letters exist in string. If they do not, remove first 2 letters from string and do the procedure again. 

(require-extension s)

(define (sapi-buildable DNA previous-bases)
  (cond
    ((> 2 (string-length DNA)) (cons #t previous-bases))
    ((member (s-left 3 DNA) previous-bases) (list #f (s-left 3 DNA)))
    ((atom? #t) (sapi-buildable (s-chop-prefix (s-left 2 DNA) DNA) (append previous-bases (list (s-left 3 DNA))))))
  )

(define (DNA-chomp DNA sapi-list)
  (if (> 12 (string-length DNA))
    (append sapi-list (list DNA))
    (DNA-chomp (s-chop-prefix (s-left 13 DNA) DNA) (append sapi-list (list (s-left 13 DNA))))
    )
  )

(define (sapi-search DNA)
   (for-each (lambda (DNA-fragments) (print (sapi-buildable DNA-fragments '()))) (DNA-chomp DNA '())))

(require-extension srfi-13)
(define (reverse-complement DNA_sequence) (s-reverse (string-map (lambda (x) (list-ref (assq x '((#\A #\T) (#\T #\A) (#\G #\C) (#\C #\G))) 1)) DNA_sequence)))


(define (primer-order DNA previous-fragments)
  (cond
    ((> 5 (string-length DNA)) previous-fragments)
    ((atom? #t) (primer-order (s-chop-prefix (s-left 2 DNA) DNA) 
                              (append previous-fragments 
                                      ((lambda (x) (list x (reverse-complement x))) (s-prepend "AGATGGCTCTTCT" (s-prepend (s-left 5 DNA) "TGAAGAGCCACGG")
                                                                                                             
                                                                                                             ))))))
  )
