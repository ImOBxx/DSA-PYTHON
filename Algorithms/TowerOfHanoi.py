def tower_of_hanoi(n, source, auxiliary, target):
    if n > 0:
        # Move n-1 disks from source to auxiliary, so they are out of the way
        tower_of_hanoi(n-1, source, target, auxiliary)

        # Move the nth disk from source to target
        print(f"Move disk {n} from {source} to {target}")

        # Move the n-1 disks that we left on auxiliary to target
        tower_of_hanoi(n-1, auxiliary, source, target)

# Number of disks
n = 3

# Names of rods
source = 'A'
auxiliary = 'B'
target = 'C'

# Running the function
tower_of_hanoi(n, source, auxiliary, target)
