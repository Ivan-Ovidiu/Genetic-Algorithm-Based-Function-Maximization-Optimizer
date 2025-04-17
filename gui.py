import tkinter as tk
from tkinter import ttk
import main

window = tk.Tk()
window.title("Genetic Algorithm Optimizer")
window.configure(bg="#f0f0f0")
window.geometry("500x550")

main_frame = tk.Frame(window, bg="#f0f0f0", padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

header = tk.Label(
    main_frame,
    text="Genetic Algorithm Optimizer",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#333333",
    pady=10
)
header.pack(fill="x")

params_frame = tk.LabelFrame(
    main_frame,
    text="Algorithm Parameters",
    font=("Arial", 12),
    bg="#f0f0f0",
    fg="#333333",
    padx=15,
    pady=15
)
params_frame.pack(fill="both", expand=True)

label_style = {"bg": "#f0f0f0", "fg": "#333333", "font": ("Arial", 10), "pady": 5}
entry_style = {"width": 15, "font": ("Arial", 10), "bg": "white", "relief": "solid", "bd": 1}

entries = [
    ("Population Size:", ""),
    ("Domain Start:", ""),
    ("Domain End:", ""),
    ("Coefficient A:", ""),
    ("Coefficient B:", ""),
    ("Coefficient C:", ""),
    ("Precision:", ""),
    ("Crossover Probability:", ""),
    ("Mutation Probability:", ""),
    ("Number of Generations:", "")
]

entries_dict = {}

for i, (param_text, default_value) in enumerate(entries):
    label = tk.Label(params_frame, text=param_text, **label_style)
    label.grid(row=i, column=0, sticky="w", padx=10)

    entry = tk.Entry(params_frame, **entry_style)
    entry.grid(row=i, column=1, sticky="ew", padx=10)

    if default_value:
        entry.insert(0, default_value)

    entries_dict[param_text] = entry

# Status and result labels
status_label = tk.Label(
    main_frame,
    text="OK",
    font=("Arial", 10),
    bg="#f0f0f0",
    fg="#333333",
    pady=5
)
status_label.pack(fill="x")

result_label = tk.Label(
    main_frame,
    text="Results will appear here.",
    font=("Arial", 10),
    bg="#f0f0f0",
    fg="#000000",
    pady=10
)
result_label.pack(fill="x")


button_frame = tk.Frame(main_frame, bg="#f0f0f0", pady=15)
button_frame.pack(fill="x")

def runMainFunction():

    population_size = int(entries_dict["Population Size:"].get().strip())
    domain_start = float(entries_dict["Domain Start:"].get().strip())
    domain_end = float(entries_dict["Domain End:"].get().strip())
    a = float(entries_dict["Coefficient A:"].get().strip())
    b = float(entries_dict["Coefficient B:"].get().strip())
    c = float(entries_dict["Coefficient C:"].get().strip())
    precision = int(entries_dict["Precision:"].get().strip())
    crossover_prob = float(entries_dict["Crossover Probability:"].get().strip())
    mutation_prob = float(entries_dict["Mutation Probability:"].get().strip())
    generations = int(entries_dict["Number of Generations:"].get().strip())

    # Call the main function with the gathered values
    avg_fit, max_fit = main.functionMax(
        population_size,
        domain_start,
        domain_end,
        a, b, c,
        precision,
        crossover_prob,
        mutation_prob,
        generations
    )
    status_label.config(text="Successfully ran", fg="green")
    result_label.config(
        text=f"Average Fitness: {avg_fit:.4f}\nMaximum Fitness: {max_fit:.4f}",
        fg="blue"
    )




# Run button
run_button = tk.Button(
    button_frame,
    text="Run Optimization",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=8,
    relief="raised",
    bd=2,
    command=runMainFunction
)
run_button.pack()


window.mainloop()
