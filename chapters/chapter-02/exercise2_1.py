# Exercise 2.1: Student Management System
# Apply collections and classes to build a practical system

import json
from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from typing import Dict, List, Optional, Set, Tuple


class Grade(Enum):
    """Grade enumeration."""
    A_PLUS = "A+"
    A = "A"
    A_MINUS = "A-"
    B_PLUS = "B+"
    B = "B"
    B_MINUS = "B-"
    C_PLUS = "C+"
    C = "C"
    C_MINUS = "C-"
    D = "D"
    F = "F"

    @property
    def gpa_value(self) -> float:
        """Get GPA value for the grade."""
        grade_points = {
            Grade.A_PLUS: 4.0,
            Grade.A: 4.0,
            Grade.A_MINUS: 3.7,
            Grade.B_PLUS: 3.3,
            Grade.B: 3.0,
            Grade.B_MINUS: 2.7,
            Grade.C_PLUS: 2.3,
            Grade.C: 2.0,
            Grade.C_MINUS: 1.7,
            Grade.D: 1.0,
            Grade.F: 0.0,
        }
        return grade_points[self]


@dataclass
class Assignment:
    """Represents a single assignment."""
    name: str
    subject: str
    grade: Optional[Grade] = None
    points_earned: float = 0.0
    points_possible: float = 100.0
    due_date: Optional[date] = None
    submitted: bool = False

    @property
    def percentage(self) -> float:
        """Calculate percentage score."""
        if self.points_possible == 0:
            return 0.0
        return (self.points_earned / self.points_possible) * 100

    @property
    def letter_grade(self) -> Grade:
        """Calculate letter grade based on percentage."""
        percentage = self.percentage
        if percentage >= 97:
            return Grade.A_PLUS
        elif percentage >= 93:
            return Grade.A
        elif percentage >= 90:
            return Grade.A_MINUS
        elif percentage >= 87:
            return Grade.B_PLUS
        elif percentage >= 83:
            return Grade.B
        elif percentage >= 80:
            return Grade.B_MINUS
        elif percentage >= 77:
            return Grade.C_PLUS
        elif percentage >= 73:
            return Grade.C
        elif percentage >= 70:
            return Grade.C_MINUS
        elif percentage >= 60:
            return Grade.D
        else:
            return Grade.F

    def submit(self, points_earned: float) -> None:
        """Submit assignment with earned points."""
        self.points_earned = points_earned
        self.submitted = True
        self.grade = self.letter_grade


@dataclass
class Student:
    """Represents a student with their assignments and grades."""

    student_id: str
    first_name: str
    last_name: str
    email: str
    assignments: List[Assignment] = field(default_factory=list[Assignment])
    subjects: Set[str] = field(default_factory=set[str])

    @property
    def full_name(self) -> str:
        """Get student's full name."""
        return f"{self.first_name} {self.last_name}"

    @property
    def display_name(self) -> str:
        """Get display name for reports."""
        return f"{self.last_name}, {self.first_name}"

    def add_assignment(self, assignment: Assignment) -> None:
        """Add an assignment to the student."""
        self.assignments.append(assignment)
        self.subjects.add(assignment.subject)

    def get_assignments_by_subject(self, subject: str) -> List[Assignment]:
        """Get all assignments for a specific subject."""
        return [
            assignment
            for assignment in self.assignments
            if assignment.subject == subject
        ]

    def get_subject_average(self, subject: str) -> float:
        """Calculate average percentage for a subject."""
        subject_assignments = self.get_assignments_by_subject(subject)
        submitted_assignments = [a for a in subject_assignments if a.submitted]

        if not submitted_assignments:
            return 0.0

        total_points = sum(a.points_earned for a in submitted_assignments)
        total_possible = sum(a.points_possible for a in submitted_assignments)

        if total_possible == 0:
            return 0.0

        return (total_points / total_possible) * 100

    def get_overall_gpa(self) -> float:
        """Calculate overall GPA across all subjects."""
        if not self.subjects:
            return 0.0

        total_gpa = 0.0
        for subject in self.subjects:
            avg_percentage = self.get_subject_average(subject)
            # Convert percentage to letter grade, then to GPA
            if avg_percentage >= 97:
                grade = Grade.A_PLUS
            elif avg_percentage >= 93:
                grade = Grade.A
            elif avg_percentage >= 90:
                grade = Grade.A_MINUS
            elif avg_percentage >= 87:
                grade = Grade.B_PLUS
            elif avg_percentage >= 83:
                grade = Grade.B
            elif avg_percentage >= 80:
                grade = Grade.B_MINUS
            elif avg_percentage >= 77:
                grade = Grade.C_PLUS
            elif avg_percentage >= 73:
                grade = Grade.C
            elif avg_percentage >= 70:
                grade = Grade.C_MINUS
            elif avg_percentage >= 60:
                grade = Grade.D
            else:
                grade = Grade.F

            total_gpa += grade.gpa_value

        return total_gpa / len(self.subjects)

    def get_pending_assignments(self) -> List[Assignment]:
        """Get all unsubmitted assignments."""
        return [a for a in self.assignments if not a.submitted]

    def to_dict(self) -> Dict[str, object]:
        """Convert student to dictionary for JSON serialization."""
        return {
            "student_id": self.student_id,
            "name": self.full_name,
            "email": self.email,
            "subjects": list(self.subjects),
            "overall_gpa": round(self.get_overall_gpa(), 2),
            "total_assignments": len(self.assignments),
            "pending_assignments": len(self.get_pending_assignments()),
        }


class StudentManagementSystem:
    """Main system for managing students and their data."""

    def __init__(self) -> None:
        self.students: Dict[str, Student] = {}
        self.subjects: Set[str] = set()

    def add_student(
        self, student_id: str, first_name: str, last_name: str, email: str
    ) -> Student:
        """Add a new student to the system."""
        if student_id in self.students:
            raise ValueError(f"Student with ID {student_id} already exists")

        student = Student(student_id, first_name, last_name, email)
        self.students[student_id] = student
        return student

    def get_student(self, student_id: str) -> Optional[Student]:
        """Get student by ID."""
        return self.students.get(student_id)

    def add_assignment_to_student(
        self, student_id: str, assignment: Assignment
    ) -> None:
        """Add assignment to a specific student."""
        student = self.get_student(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found")

        student.add_assignment(assignment)
        self.subjects.add(assignment.subject)

    def get_students_by_subject(self, subject: str) -> List[Student]:
        """Get all students taking a specific subject."""
        return [
            student for student in self.students.values() if subject in student.subjects
        ]

    def get_class_average(self, subject: str) -> float:
        """Calculate class average for a subject."""
        students_in_subject = self.get_students_by_subject(subject)
        if not students_in_subject:
            return 0.0

        total_average = sum(
            student.get_subject_average(subject) for student in students_in_subject
        )
        return total_average / len(students_in_subject)

    def get_top_students(self, limit: int = 5) -> List[Tuple[Student, float]]:
        """Get top students by GPA."""
        student_gpas = [
            (student, student.get_overall_gpa()) for student in self.students.values()
        ]

        # Sort by GPA in descending order
        student_gpas.sort(key=lambda x: x[1], reverse=True)

        return student_gpas[:limit]

    def generate_student_report(self, student_id: str) -> str:
        """Generate a detailed report for a student."""
        student = self.get_student(student_id)
        if not student:
            return f"Student with ID {student_id} not found"

        lines = [
            f"Student Report: {student.full_name} ({student.student_id})",
            f"Email: {student.email}",
            f"Overall GPA: {student.get_overall_gpa():.2f}",
            "-" * 50,
        ]

        for subject in sorted(student.subjects):
            avg = student.get_subject_average(subject)
            assignments = student.get_assignments_by_subject(subject)
            submitted = len([a for a in assignments if a.submitted])

            lines.append(f"Subject: {subject}")
            lines.append(f"  Average: {avg:.1f}%")
            lines.append(f"  Assignments: {submitted}/{len(assignments)} submitted")

        pending = student.get_pending_assignments()
        if pending:
            lines.append(f"\nPending Assignments ({len(pending)}):")
            for assignment in pending:
                due_info = (
                    f" (Due: {assignment.due_date})" if assignment.due_date else ""
                )
                lines.append(f"  - {assignment.name} ({assignment.subject}){due_info}")

        return "\n".join(lines)

    def generate_class_report(self, subject: str) -> str:
        """Generate a class report for a subject."""
        students = self.get_students_by_subject(subject)
        if not students:
            return f"No students found for subject: {subject}"

        class_avg = self.get_class_average(subject)

        lines = [
            f"Class Report: {subject}",
            f"Students Enrolled: {len(students)}",
            f"Class Average: {class_avg:.1f}%",
            "-" * 50,
        ]

        # Sort students by average in descending order
        student_averages = [
            (student, student.get_subject_average(subject)) for student in students
        ]
        student_averages.sort(key=lambda x: x[1], reverse=True)

        for student, avg in student_averages:
            lines.append(f"{student.display_name}: {avg:.1f}%")

        return "\n".join(lines)

    def export_to_json(self) -> str:
        """Export all data to JSON format."""
        data: dict[str, object] = {
            "subjects": list(self.subjects),
            "students": [student.to_dict() for student in self.students.values()],
            "generated_at": datetime.now().isoformat(),
        }
        return json.dumps(data, indent=2)


# TODO: Complete the following functions for the exercise


def create_sample_data(system: StudentManagementSystem) -> None:
    """
    Create sample data for testing the system.

    Requirements:
    1. Add at least 5 students
    2. Create assignments for at least 3 subjects
    3. Submit some assignments with grades
    4. Leave some assignments pending
    """
    # TODO: Implement this function
    # Add students
    system.add_student("S001", "Alice", "Johnson", "alice.j@school.edu")
    system.add_student("S002", "Bob", "Smith", "bob.s@school.edu")
    system.add_student("S003", "Charlie", "Brown", "charlie.b@school.edu")
    system.add_student("S004", "Diana", "Wilson", "diana.w@school.edu")
    system.add_student("S005", "Eve", "Davis", "eve.d@school.edu")

    # Create assignments for different subjects
    subjects = ["Mathematics", "English", "Science"]

    for subject in subjects:
        for i, student_id in enumerate(["S001", "S002", "S003", "S004", "S005"]):
            # Assignment 1 - submitted
            assignment1 = Assignment(
                name=f"{subject} Quiz 1",
                subject=subject,
                points_possible=100.0,
                due_date=date(2024, 8, 15),
            )
            assignment1.submit(85 + i * 3)  # Different scores for variety
            system.add_assignment_to_student(student_id, assignment1)

            # Assignment 2 - submitted
            assignment2 = Assignment(
                name=f"{subject} Homework 1",
                subject=subject,
                points_possible=50.0,
                due_date=date(2024, 8, 20),
            )
            assignment2.submit(40 + i * 2)
            system.add_assignment_to_student(student_id, assignment2)

            # Assignment 3 - pending
            assignment3 = Assignment(
                name=f"{subject} Project",
                subject=subject,
                points_possible=200.0,
                due_date=date(2024, 9, 1),
            )
            system.add_assignment_to_student(student_id, assignment3)


def find_students_needing_help(
    system: StudentManagementSystem, threshold: float = 70.0
) -> List[Tuple[Student, str]]:
    """
    Find students who need help (average below threshold in any subject).

    Args:
        system: The student management system
        threshold: Grade threshold below which students need help

    Returns:
        List of tuples containing (Student, subject) for students needing help
    """
    # TODO: Implement this function
    students_needing_help = []

    for student in system.students.values():
        for subject in student.subjects:
            avg = student.get_subject_average(subject)
            if avg < threshold and avg > 0:  # Only consider if they have submitted work
                students_needing_help.append((student, subject))

    return students_needing_help


def get_honor_roll_students(
    system: StudentManagementSystem, gpa_threshold: float = 3.5
) -> List[Student]:
    """
    Get students eligible for honor roll (GPA above threshold).

    Args:
        system: The student management system
        gpa_threshold: Minimum GPA for honor roll

    Returns:
        List of students sorted by GPA (highest first)
    """
    # TODO: Implement this function
    honor_students = [
        student
        for student in system.students.values()
        if student.get_overall_gpa() >= gpa_threshold
    ]

    # Sort by GPA in descending order
    honor_students.sort(key=lambda s: s.get_overall_gpa(), reverse=True)

    return honor_students


def generate_summary_statistics(system: StudentManagementSystem) -> Dict[str, any]:
    """
    Generate summary statistics for the entire system.

    Returns:
        Dictionary containing various statistics
    """
    # TODO: Implement this function
    total_students = len(system.students)
    total_subjects = len(system.subjects)

    # Calculate overall statistics
    all_gpas = [student.get_overall_gpa() for student in system.students.values()]
    avg_gpa = sum(all_gpas) / len(all_gpas) if all_gpas else 0.0

    # Count pending assignments
    total_pending = sum(
        len(student.get_pending_assignments()) for student in system.students.values()
    )

    # Subject statistics
    subject_stats = {}
    for subject in system.subjects:
        class_avg = system.get_class_average(subject)
        student_count = len(system.get_students_by_subject(subject))
        subject_stats[subject] = {
            "students": student_count,
            "class_average": round(class_avg, 1),
        }

    return {
        "total_students": total_students,
        "total_subjects": total_subjects,
        "overall_gpa_average": round(avg_gpa, 2),
        "total_pending_assignments": total_pending,
        "subject_statistics": subject_stats,
        "honor_roll_count": len(get_honor_roll_students(system)),
        "students_needing_help": len(find_students_needing_help(system)),
    }


# Test your implementation
if __name__ == "__main__":
    # Create the system and add sample data
    sms = StudentManagementSystem()
    create_sample_data(sms)

    print("=== Student Management System Demo ===\n")

    # Test individual student report
    print("Individual Student Report:")
    print(sms.generate_student_report("S001"))
    print()

    # Test class report
    print("Class Report for Mathematics:")
    print(sms.generate_class_report("Mathematics"))
    print()

    # Test top students
    print("Top 3 Students by GPA:")
    top_students = sms.get_top_students(3)
    for student, gpa in top_students:
        print(f"  {student.display_name}: {gpa:.2f}")
    print()

    # Test students needing help
    print("Students Needing Help (below 70%):")
    help_needed = find_students_needing_help(sms)
    for student, subject in help_needed:
        avg = student.get_subject_average(subject)
        print(f"  {student.display_name} in {subject}: {avg:.1f}%")
    print()

    # Test honor roll
    print("Honor Roll Students (GPA >= 3.5):")
    honor_students = get_honor_roll_students(sms)
    for student in honor_students:
        print(f"  {student.display_name}: {student.get_overall_gpa():.2f}")
    print()

    # Test summary statistics
    print("System Summary:")
    stats = generate_summary_statistics(sms)
    for key, value in stats.items():
        if key == "subject_statistics":
            print(f"  {key.replace('_', ' ').title()}:")
            for subject, subject_stats in value.items():
                print(
                    f"    {subject}: {subject_stats['students']} students, {subject_stats['class_average']}% average"
                )
        else:
            print(f"  {key.replace('_', ' ').title()}: {value}")

    # Export to JSON
    print(f"\nExporting data to JSON...")
    json_data = sms.export_to_json()
    print("Export completed (data available in json_data variable)")

# Expected output should show:
# - Individual student report with grades and pending assignments
# - Class report showing all students in Mathematics
# - Top students ranked by GPA
# - Students who need help in specific subjects
# - Honor roll students
# - System-wide statistics
# - JSON export confirmation
