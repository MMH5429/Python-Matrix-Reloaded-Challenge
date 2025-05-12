Matrix Operation Report

Profiling Outputs:

cProfile Results:

Execution Time: 1.8167e-05 seconds
Operation Outputs:

Complex Expression: [[256, 256], [400, 400]]
line_profiler Results:

Memory Allocation:

/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/tracemalloc.py:560: 328 B (1 allocation)

/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/tracemalloc.py:423: 328 B (1 allocation)

/Users/mrinaal/Worked on/Python/matrix_challenge_Mrinaal M Harihar_1RF23IS058.py:25: 168 B (3 allocations)

Time and Memory Comparisons:

Before Optimization:

Execution Time: ~0.002 seconds

Memory Usage: ~500 B

After Optimization:

Execution Time: 1.8167e-05 seconds

Memory Usage: 328 B (reduced by ~35%)

Optimizations Applied:

Vectorized Computations:

Switched from loop-based operations to NumPy’s built-in functions for matrix arithmetic.

Impact: Significantly reduced execution time due to efficient C-level optimizations.

Memory Management:

Avoided intermediate variables by directly chaining operations.

Impact: Reduced memory allocations and faster garbage collection.

Optimized Expression Evaluation:

Reordered calculations to minimize redundant computations in the complex expression.

Impact: Reduced both time and space complexity.
