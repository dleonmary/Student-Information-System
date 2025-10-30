from src.services.student_service import StudentService
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

class StudentInformationSystem:
    def __init__(self):
        self.student_service = StudentService()
        self.logger = logging.getLogger(__name__)

    def display_menu(self):
        print("\n=== Student Information System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

    def add_student(self):
        print("\n--- Add New Student ---")
        name = input("Name: ")
        email = input("Email: ")
        course = input("Course: ")
        year_level = input("Year Level: ")
        student_id = input("Student ID: ")

        student_data = {
            "name": name,
            "email": email,
            "course": course,
            "year_level": year_level,
            "student_id": student_id
        }

        try:
            student = self.student_service.add_student(student_data)
            self.logger.info(f"Added student: {student['student_id']}")
            print(f"✅ Student added successfully! ID: {student['student_id']}")
        except Exception as e:
            self.logger.error(f"Error adding student: {e}")
            print("❌ Error adding student.")

    def view_all_students(self):
        print("\n--- All Students ---")
        students = self.student_service.get_all_students()
        if not students:
            print("No students found.")
            return
        for s in students:
            print(f"ID: {s['student_id']} | Name: {s['name']} | Email: {s['email']} | Course: {s['course']} | Year: {s['year_level']}")

    def view_student_by_id(self):
        student_id = input("\nEnter Student ID: ")
        student = self.student_service.get_student(student_id)
        if student:
            print("\n--- Student Details ---")
            for key, value in student.items():
                print(f"{key}: {value}")
        else:
            print("❌ Student not found.")

    def update_student(self):
        print("\n--- Update Student ---")
        student_id = input("Enter Student ID to update: ")
        student = self.student_service.get_student(student_id)

        if not student:
            print("❌ Student not found.")
            return

        print("\nLeave blank if you don't want to change a field.")
        name = input(f"New Name (current: {student['name']}): ") or student["name"]
        email = input(f"New Email (current: {student['email']}): ") or student["email"]
        course = input(f"New Course (current: {student['course']}): ") or student["course"]
        year_level = input(f"New Year Level (current: {student['year_level']}): ") or student["year_level"]

        update_data = {
            "name": name,
            "email": email,
            "course": course,
            "year_level": year_level
        }

        updated = self.student_service.update_student(student_id, update_data)
        if updated:
            self.logger.info(f"Updated student: {student_id}")
            print("✅ Student updated successfully!")
        else:
            print("❌ Failed to update student.")

    def delete_student(self):
        print("\n--- Delete Student ---")
        student_id = input("Enter Student ID to delete: ")
        confirm = input(f"Are you sure you want to delete student {student_id}? (y/n): ").lower()

        if confirm == 'y':
            deleted = self.student_service.delete_student(student_id)
            if deleted:
                self.logger.info(f"Deleted student: {student_id}")
                print("🗑️ Student deleted successfully.")
            else:
                print("❌ Student not found or already deleted.")
        else:
            print("Deletion cancelled.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-6): ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_all_students()
            elif choice == "3":
                self.view_student_by_id()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                print("👋 Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = StudentInformationSystem()
    app.run()
