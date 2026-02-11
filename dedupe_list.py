import re

def extract_employee_id(line: str) -> str | None:
    """
    Extracts the employee ID number from a line.
    Assumes employee ID is a sequence of digits.
    """
    match = re.search(r"\d+", line)
    return match.group() if match else None


def normalize_to_username(value: str) -> str:
    """
    Converts a full name or username into:
    first initial + last name (lowercase)
    """
    value = value.strip()

    if " " not in value:
        return re.sub(r"[^a-z]", "", value.lower())

    parts = value.split()
    first_initial = parts[0][0].lower()
    last_name = parts[-1].lower()
    return re.sub(r"[^a-z]", "", f"{first_initial}{last_name}")


def normalize_full_name(value: str) -> str:
    """
    Cleans and formats a full name nicely.
    """
    parts = value.strip().split()
    return " ".join(p.capitalize() for p in parts)


def dedupe_by_employee_id(entries: list[str]) -> tuple[dict[str, dict[str, str]], int]:
    """
    Returns:
      - dictionary keyed by employee ID
      - count of valid employee ID entries processed
    """
    users: dict[str, dict[str, str]] = {}
    valid_entry_count = 0

    for entry in entries:
        if not entry.strip():
            continue

        emp_id = extract_employee_id(entry)
        if not emp_id:
            continue  # Skip lines with no employee ID

        valid_entry_count += 1

        # Initialize record if new
        if emp_id not in users:
            users[emp_id] = {
                "username": "(unknown)",
                "full_name": "(not provided)"
            }

        # Remove employee ID and separators before parsing name
        remainder = re.sub(r"\d+", "", entry)
        remainder = remainder.replace("-", " ").strip()

        if remainder:
            if " " in remainder:
                users[emp_id]["full_name"] = normalize_full_name(remainder)
                users[emp_id]["username"] = normalize_to_username(remainder)
            else:
                users[emp_id]["username"] = normalize_to_username(remainder)

    return dict(sorted(users.items())), valid_entry_count


if __name__ == "__main__":
    print("Paste employee entries (one per line). Press Enter on a blank line to finish:")

    entries: list[str] = []

    while True:
        line = input()
        if not line.strip():
            break
        entries.append(line)

    users, processed_count = dedupe_by_employee_id(entries)

    duplicate_count = processed_count - len(users)

    print("\nUsers scheduled for deletion:")
    print(f"{'Emp ID':<10} {'Username':<10} Full Name")
    print("-" * 40)

    for emp_id, data in users.items():
        print(f"{emp_id:<10} {data['username']:<10} {data['full_name']}")

    print("\nSummary:")
    print(f"Total entries processed: {processed_count}")
    print(f"Unique employee IDs:     {len(users)}")
    print(f"Duplicate entries removed: {duplicate_count}")
