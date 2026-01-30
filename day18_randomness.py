import numpy as np

# Normal distribution
normal_data = np.random.normal(loc=50, scale=10, size=1000)

# Exponential distribution (failure time simulation)
failure_time = np.random.exponential(scale=5, size=1000)

print("Normal Distribution")
print("Mean:", np.mean(normal_data))
print("Standard Deviation:", np.std(normal_data))

print("\nExponential Distribution (Failure Time)")
print("Average Failure Time:", np.mean(failure_time))
