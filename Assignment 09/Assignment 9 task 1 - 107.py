# ============================================================
# NORMAL CLASS (Without AI Comments)
# ============================================================

class sru_student:
    # Initializes name, roll number, and hostel details
    def __init__(self, name, roll_no, hostel_status):
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee = 0  # Default fee

    # Updates the fee for the student
    def fee_update(self, new_fee):
        self.fee = new_fee

    # Prints all student details
    def display_details(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Hostel Status:", self.hostel_status)
        print("Fee:", self.fee)
        print()


# ============================================================
# AI COMMENTED CLASS
# ============================================================

class sru_student_AI:
    # Initializes the class with name, roll number, and hostel details
    def __init__(self, name, roll_no, hostel_status):
        self.name = name          # Assigns the name argument
        self.roll_no = roll_no    # Saves the roll number
        self.hostel_status = hostel_status  # Stores hostel status
        self.fee = 0              # Sets default fee to zero

    # Updates the fee for the student
    def fee_update(self, new_fee):
        self.fee = new_fee        # Updates the fee

    # Prints all student details
    def display_details(self):
        print("Student Details:")      # Title
        print("Name:", self.name)      # Student's name
        print("Roll No:", self.roll_no)  # Roll number
        print("Hostel Status:", self.hostel_status)  # Hostel status
        print("Fee:", self.fee)        # Fee paid
        print()


# ============================================================
# OBJECT CREATION AND FUNCTION CALLS
# ============================================================

student1 = sru_student("Kampally Saipriya", 2107, "Yes")  # Create student object
student1.fee_update(45000)                      # Update fee
student1.display_details()                      # Display details

print("\n---- AI Commented Class Output ----\n")

student2 = sru_student_AI("Pavan", 1110, "No")  # Create another object
student2.fee_update(50000)                      # Update fee
student2.display_details()                      # Display details