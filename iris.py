
import tkinter as tk
from mlforkidsnumbers import MLforKidsNumbers

project = MLforKidsNumbers(
    modelurl="https://mlforkids-newnumbers.j8ayd8ayn23.eu-de.codeengine.appdomain.cloud/saved-models/auth0|6a52566cf097b0cf74d56e90-4/status"
)

screen = tk.Tk()
screen.title("Iris Classifier")
screen.geometry("450x550")
screen.configure(bg="#101827")

fields = ["SepalLCm", "SepalWidthCm", "PetalLCm", "PetalWidthCm"]
entries = []

def result():
    try:
        data = {x: float(e.get()) for x, e in zip(fields, entries)}
        r = project.predict(data)[0]
        names = {"setosa": "Iris Setosa 🌸", "versicolor": "Iris Versicolor 🌺", "virginica": "Iris Virginica 🌷"}
        show(names.get(r["class_name"], r["class_name"]), r["confidence"])
    except:
        tk.messagebox.showerror("Error", "Please enter valid numbers.")

def show(name, confidence):
    for w in screen.winfo_children(): w.destroy()

    tk.Label(screen, text="Prediction", font=("Arial", 28, "bold"),
             bg="#101827", fg="white").pack(pady=70)

    tk.Label(screen, text=name, font=("Arial", 25, "bold"),
             bg="#101827", fg="#22c55e").pack(pady=10)

    tk.Label(screen, text=f"Confidence: {confidence}%",
             font=("Arial", 16), bg="#101827", fg="#94a3b8").pack(pady=10)

    tk.Button(screen, text="← Back", command=main,
              font=("Arial", 12), bg="#334155", fg="white",
              relief="flat", padx=30, pady=10).pack(pady=40)

def main():
    for w in screen.winfo_children(): w.destroy()
    entries.clear()

    tk.Label(screen, text="🌸 Iris Classifier", font=("Arial", 25, "bold"),
             bg="#101827", fg="white").pack(pady=35)

    for x in fields:
        tk.Label(screen, text=x, bg="#101827", fg="white",
                 font=("Arial", 11)).pack(pady=(8, 2))
        e = tk.Entry(screen, bg="#334155", fg="white",
                     insertbackground="white", relief="flat")
        e.pack(ipady=7, padx=70, fill="x")
        entries.append(e)

    tk.Button(screen, text="Predict 🔍", command=result,
              font=("Arial", 13, "bold"), bg="#38bdf8",
              fg="#0f172a", relief="flat", padx=30, pady=10).pack(pady=30)

main()
screen.mainloop()

