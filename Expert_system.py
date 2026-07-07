def expert_system():
    print("--- AI Medical Diagnostic Expert System ---")
    print("Please answer with 'yes' or 'no' to the following symptoms:\n")
    
    # User se symptoms poochne ke liye sawaal
    fever = input("Do you have a fever? ").lower()
    cough = input("Do you have a cough? ").lower()
    rash = input("Do you have a skin rash? ").lower()
    headache = input("Do you have a severe headache? ").lower()
    
    print("\n--- Diagnosis Result ---")
    
    # Decision Logic (Expert Rules)
    if fever == "yes" and cough == "yes" and rash == "no" and headache == "no":
        print("AI Expert Advice: You might have a common cold or flu. Rest well and stay hydrated.")
    elif fever == "yes" and cough == "yes" and headache == "yes":
        print("AI Expert Advice: These symptoms match Covid-19 or Influenza. Please consult a doctor and isolate.")
    elif fever == "yes" and rash == "yes":
        print("AI Expert Advice: Fever with a rash could indicate a viral infection like Measles or Chickenpox. Please visit a clinic.")
    elif headache == "yes" and fever == "no":
        print("AI Expert Advice: It could be a tension headache or migraine. Rest in a quiet, dark room.")
    else:
        print("AI Expert Advice: Symptoms are inconclusive. Maintain general health precautions and consult a professional if you feel unwell.")

if __name__ == "__main__":
    expert_system()

