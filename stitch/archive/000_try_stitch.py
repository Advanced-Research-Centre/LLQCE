programs = [
    "(lam (+ 3 (* (+ 2 4) 2)))",
    "(lam (map (lam (+ 3 (* 4 (+ 3 $0)))) $0))",
    "(lam (* 2 (+ 3 (* $0 (+ 2 1)))))"
]

from stitch_core import compress

res = compress(programs, iterations=1, max_arity=2)
print(res.abstractions[0])

print(res.rewritten)

from stitch_core import rewrite
print(rewrite(["(lam (+ 3 (* (+ 1 1) 1)))", "(lam (- 5 (+ 3 (* $0 (+ 2 1)))))"], res.abstractions).rewritten)


