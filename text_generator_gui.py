import openai
import tkinter as tk
from tkinter import messagebox
import logging

# Setup OpenAI API key
openai.api_key = 'youapikey'

# Setup logging for error tracking
logging.basicConfig(filename='app.log', level=logging.ERROR)

# Function to generate text from OpenAI's API
def generate_text():
    prompt = input_box.get("1.0", tk.END).strip()
    
    if not prompt:
        messagebox.showwarning("Input Error", "Please enter a prompt.")
        return
    
    temperature = temperature_input.get()
    
    try:
        # Make the API call to generate text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can replace with any model you want to use
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=temperature,
        )
        
        generated_text = response['choices'][0]['message']['content']
        
        # Display the result in the output box
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, generated_text)
        
        # Save to file
        with open("generated_text.txt", "w") as file:
            file.write(generated_text)
        messagebox.showinfo("Success", "Text generated and saved to generated_text.txt")

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"❌ Error: {e}")
        messagebox.showerror("API Error", "An error occurred while generating text. Check the logs for details.")

# Creating the main window
root = tk.Tk()
root.title("AI Text Generator")
root.geometry("600x500")

# Add instructions
instructions = tk.Label(root, text="Enter your prompt below and click 'Generate Text'.", font=("Arial", 12))
instructions.pack(pady=10)

# Input box
input_box = tk.Text(root, height=5, width=40, font=("Arial", 12))
input_box.pack(pady=5)

# Temperature control (Dynamic parameter)
temperature_label = tk.Label(root, text="Select Temperature (0 to 1):", font=("Arial", 12))
temperature_label.pack(pady=5)

temperature_input = tk.Scale(root, from_=0, to=1, orient="horizontal", label="Temperature", font=("Arial", 12))
temperature_input.set(0.7)  # Default temperature
temperature_input.pack(pady=5)

# Button to generate text
generate_button = tk.Button(root, text="Generate Text", command=generate_text, bg="lightblue", font=("Arial", 12))
generate_button.pack(pady=20)

# Output box
output_box = tk.Text(root, height=10, width=40, font=("Arial", 12))
output_box.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
