import tkinter as tk
from tkinter import messagebox

class CricketScorePredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket Score Prediction App")
        self.root.geometry("800x600")
        
        self.predictions = []  # List to store user predictions
        self.match_result = None  # Store the actual result of the match

        # Title Label
        self.title_label = tk.Label(self.root, text="Cricket Match Score Prediction", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=20)

        # Prediction Input Section
        self.match_name_label = tk.Label(self.root, text="Match (e.g., MI vs CSK):", font=("Arial", 14))
        self.match_name_label.pack(pady=5)
        self.match_name_entry = tk.Entry(self.root, font=("Arial", 14))
        self.match_name_entry.pack(pady=5)

        self.predicted_score_label = tk.Label(self.root, text="Predicted Total Score:", font=("Arial", 14))
        self.predicted_score_label.pack(pady=5)
        self.predicted_score_entry = tk.Entry(self.root, font=("Arial", 14))
        self.predicted_score_entry.pack(pady=5)

        self.top_scorer_label = tk.Label(self.root, text="Predicted Top Scorer:", font=("Arial", 14))
        self.top_scorer_label.pack(pady=5)
        self.top_scorer_entry = tk.Entry(self.root, font=("Arial", 14))
        self.top_scorer_entry.pack(pady=5)

        self.top_wicket_taker_label = tk.Label(self.root, text="Predicted Top Wicket-Taker:", font=("Arial", 14))
        self.top_wicket_taker_label.pack(pady=5)
        self.top_wicket_taker_entry = tk.Entry(self.root, font=("Arial", 14))
        self.top_wicket_taker_entry.pack(pady=5)

        # Submit Prediction Button
        self.submit_prediction_button = tk.Button(self.root, text="Submit Prediction", font=("Arial", 14, "bold"), command=self.submit_prediction, bg="#4CAF50", fg="white")
        self.submit_prediction_button.pack(pady=10)

        # Enter Actual Match Result Button
        self.enter_result_button = tk.Button(self.root, text="Enter Actual Match Result", font=("Arial", 14, "bold"), command=self.enter_actual_result, bg="#FF5722", fg="white")
        self.enter_result_button.pack(pady=10)

        # Display Predictions Button
        self.display_predictions_button = tk.Button(self.root, text="Display Predictions", font=("Arial", 14, "bold"), command=self.display_predictions, bg="#007BFF", fg="white")
        self.display_predictions_button.pack(pady=10)

        # Display Results Area
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), justify="left")
        self.result_label.pack(pady=20)

    def submit_prediction(self):
        """Submit user prediction for the match."""
        match_name = self.match_name_entry.get()
        predicted_score = self.predicted_score_entry.get()
        top_scorer = self.top_scorer_entry.get()
        top_wicket_taker = self.top_wicket_taker_entry.get()

        # Validation: Ensure fields are not empty and predicted score is numeric
        if not match_name or not predicted_score or not top_scorer or not top_wicket_taker:
            messagebox.showerror("Input Error", "All fields are required.")
            return

        try:
            predicted_score = int(predicted_score)
        except ValueError:
            messagebox.showerror("Input Error", "Predicted Total Score should be a number.")
            return

        # Save the prediction
        prediction = {
            "match_name": match_name,
            "predicted_score": predicted_score,
            "top_scorer": top_scorer,
            "top_wicket_taker": top_wicket_taker
        }
        self.predictions.append(prediction)

        # Clear input fields
        self.match_name_entry.delete(0, tk.END)
        self.predicted_score_entry.delete(0, tk.END)
        self.top_scorer_entry.delete(0, tk.END)
        self.top_wicket_taker_entry.delete(0, tk.END)

        messagebox.showinfo("Prediction Submitted", f"Your prediction for {match_name} has been submitted.")

    def enter_actual_result(self):
        """Enter the actual match result to compare predictions."""
        if not self.predictions:
            messagebox.showerror("No Predictions", "Please submit some predictions first.")
            return

        # Input fields for actual match result
        actual_score = tk.simpledialog.askinteger("Actual Score", "Enter the actual total score:")
        actual_top_scorer = tk.simpledialog.askstring("Actual Top Scorer", "Enter the actual top scorer:")
        actual_top_wicket_taker = tk.simpledialog.askstring("Actual Top Wicket-Taker", "Enter the actual top wicket-taker:")

        # Validation
        if not actual_score or not actual_top_scorer or not actual_top_wicket_taker:
            messagebox.showerror("Input Error", "All fields are required for the actual result.")
            return

        # Store actual result
        self.match_result = {
            "actual_score": actual_score,
            "actual_top_scorer": actual_top_scorer,
            "actual_top_wicket_taker": actual_top_wicket_taker
        }

        messagebox.showinfo("Result Entered", "The actual match result has been recorded.")

    def display_predictions(self):
        """Display all submitted predictions and compare with actual results."""
        if not self.predictions:
            messagebox.showerror("No Predictions", "No predictions have been submitted.")
            return

        # Generate predictions list
        predictions_text = "Match Name\tPredicted Score\tTop Scorer\tTop Wicket-Taker\n"
        predictions_text += "-"*60 + "\n"
        for prediction in self.predictions:
            predictions_text += f"{prediction['match_name']}\t{prediction['predicted_score']}\t{prediction['top_scorer']}\t{prediction['top_wicket_taker']}\n"

        # If actual result is entered, compare predictions
        if self.match_result:
            predictions_text += "\nActual Match Result:\n"
            predictions_text += f"Actual Score: {self.match_result['actual_score']}\n"
            predictions_text += f"Actual Top Scorer: {self.match_result['actual_top_scorer']}\n"
            predictions_text += f"Actual Top Wicket-Taker: {self.match_result['actual_top_wicket_taker']}\n"

            # Compare predictions with actual result
            predictions_text += "\nPrediction Accuracy:\n"
            for prediction in self.predictions:
                score_accuracy = "Correct" if prediction['predicted_score'] == self.match_result['actual_score'] else "Incorrect"
                top_scorer_accuracy = "Correct" if prediction['top_scorer'] == self.match_result['actual_top_scorer'] else "Incorrect"
                top_wicket_accuracy = "Correct" if prediction['top_wicket_taker'] == self.match_result['actual_top_wicket_taker'] else "Incorrect"

                predictions_text += f"{prediction['match_name']}:\n"
                predictions_text += f"  Score Prediction: {score_accuracy}\n"
                predictions_text += f"  Top Scorer Prediction: {top_scorer_accuracy}\n"
                predictions_text += f"  Top Wicket-Taker Prediction: {top_wicket_accuracy}\n"
        
        self.result_label.config(text=predictions_text)

# Running the Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    app = CricketScorePredictionApp(root)
    root.mainloop()
