def load_steps(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

# Load each file into its own list
steps_p1 = load_steps('data/p1_method.txt')
steps_p2 = load_steps('data/p2_method.txt')

print(f"File 1 has {len(steps_p1)} steps.")
print(f"File 2 has {len(steps_p2)} steps.")