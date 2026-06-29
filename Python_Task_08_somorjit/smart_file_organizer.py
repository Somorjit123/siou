"""
====================================================================
 SMART FILE ORGANIZER
 A real-world file automation & data management system built in Python.

 Modules implemented:
   1. Directory Selection
   2. File Scanning
   3. Automatic File Organization
   4. File Statistics
   5. Search Functionality
   6. Duplicate File Detection
   7. Report Generation
   8. Exception Handling (throughout)
====================================================================
"""

import os
import shutil
from datetime import datetime
from collections import defaultdict


class SmartFileOrganizer:
    """
    Main class that manages scanning, organizing, searching,
    duplicate detection and reporting for a chosen directory.
    """

    # Extension -> Category mapping
    CATEGORY_MAP = {
        # Images
        ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images",
        ".bmp": "Images", ".svg": "Images", ".webp": "Images", ".tiff": "Images",
        # Documents
        ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
        ".txt": "Documents", ".xls": "Documents", ".xlsx": "Documents",
        ".ppt": "Documents", ".pptx": "Documents", ".csv": "Documents",
        # Videos
        ".mp4": "Videos", ".mkv": "Videos", ".avi": "Videos", ".mov": "Videos",
        ".wmv": "Videos", ".flv": "Videos",
        # Audio
        ".mp3": "Audio", ".wav": "Audio", ".aac": "Audio", ".flac": "Audio",
        ".m4a": "Audio",
        # Archives
        ".zip": "Archives", ".rar": "Archives", ".7z": "Archives",
        ".tar": "Archives", ".gz": "Archives",
        # Programs
        ".exe": "Programs", ".msi": "Programs", ".bat": "Programs",
        ".sh": "Programs", ".apk": "Programs",
    }

    CATEGORIES = ["Images", "Documents", "Videos", "Audio", "Archives", "Programs", "Others"]

    def __init__(self):
        self.directory = None          # Selected folder path
        self.files_info = []           # List of dicts: {name, ext, path}
        self.stats = {}                # category -> count
        self.duplicates = {}           # filename -> count (for names appearing > 1 time)

    # ----------------------------------------------------------------
    # MODULE 1: DIRECTORY SELECTION
    # ----------------------------------------------------------------
    def select_directory(self):
        """Ask the user for a folder path and validate it."""
        path = input("\nEnter Folder Path: ").strip().strip('"')

        try:
            if not path:
                print("[ERROR] Path cannot be empty.")
                return False

            if not os.path.exists(path):
                print(f"[ERROR] The path '{path}' does not exist.")
                return False

            if not os.path.isdir(path):
                print(f"[ERROR] '{path}' is not a directory.")
                return False

            # Check read permission
            if not os.access(path, os.R_OK):
                print(f"[ERROR] Permission Denied: Cannot read '{path}'.")
                return False

            self.directory = path
            print(f"[OK] Directory selected: {self.directory}")
            return True

        except PermissionError:
            print("[ERROR] Permission Denied while accessing the folder.")
            return False
        except Exception as e:
            print(f"[ERROR] Unexpected error while selecting directory: {e}")
            return False

    # ----------------------------------------------------------------
    # MODULE 2: FILE SCANNING
    # ----------------------------------------------------------------
    def scan_files(self):
        """Scan all files in the directory (top-level only) and store info."""
        if not self.directory:
            print("[ERROR] No directory selected yet. Please select a folder first.")
            return

        self.files_info = []

        try:
            entries = os.listdir(self.directory)
        except FileNotFoundError:
            print("[ERROR] Missing Folder: The directory no longer exists.")
            return
        except PermissionError:
            print("[ERROR] Permission Denied while scanning the folder.")
            return
        except Exception as e:
            print(f"[ERROR] Unexpected error while scanning: {e}")
            return

        for entry in entries:
            full_path = os.path.join(self.directory, entry)
            try:
                if os.path.isfile(full_path):
                    name, ext = os.path.splitext(entry)
                    ext = ext.lower() if ext else "(no extension)"
                    self.files_info.append({
                        "name": entry,
                        "ext": ext,
                        "path": full_path
                    })
            except OSError as e:
                print(f"[WARNING] Could not access '{entry}': {e}")
                continue

        print(f"\nFound {len(self.files_info)} Files\n")
        if not self.files_info:
            print("No files found in this directory.")
            return

        print(f"{'File Name':35} {'Extension':15}")
        print("-" * 50)
        for f in self.files_info:
            print(f"{f['name']:35} {f['ext']:15}")

    # ----------------------------------------------------------------
    # MODULE 3: AUTOMATIC FILE ORGANIZATION
    # ----------------------------------------------------------------
    def get_category(self, ext):
        """Return the category name for a given extension."""
        return self.CATEGORY_MAP.get(ext, "Others")

    def organize_files(self):
        """Create category folders and move files into them."""
        if not self.directory:
            print("[ERROR] No directory selected yet. Please select a folder first.")
            return

        if not self.files_info:
            print("[INFO] No scanned files found. Scanning now...")
            self.scan_files()
            if not self.files_info:
                return

        # Create category folders
        for category in self.CATEGORIES:
            folder_path = os.path.join(self.directory, category)
            try:
                os.makedirs(folder_path, exist_ok=True)
            except PermissionError:
                print(f"[ERROR] Permission Denied: Cannot create folder '{category}'.")
                return
            except Exception as e:
                print(f"[ERROR] Could not create folder '{category}': {e}")
                return

        moved_count = 0
        skipped_count = 0

        for f in self.files_info:
            try:
                # Skip files that are already inside a category folder
                # (in case the user re-runs organization)
                parent_folder = os.path.basename(os.path.dirname(f["path"]))
                if parent_folder in self.CATEGORIES:
                    continue

                category = self.get_category(f["ext"])
                dest_folder = os.path.join(self.directory, category)
                dest_path = os.path.join(dest_folder, f["name"])

                # Handle "File Already Exists" gracefully
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(f["name"])
                    counter = 1
                    new_dest_path = dest_path
                    while os.path.exists(new_dest_path):
                        new_name = f"{base}_copy{counter}{ext}"
                        new_dest_path = os.path.join(dest_folder, new_name)
                        counter += 1
                    dest_path = new_dest_path
                    print(f"[INFO] '{f['name']}' already exists in {category}/. "
                          f"Renaming to '{os.path.basename(dest_path)}'.")

                shutil.move(f["path"], dest_path)
                print(f"{f['name']} -> {category}/")
                moved_count += 1

            except FileNotFoundError:
                print(f"[ERROR] File '{f['name']}' not found (it may have been moved already).")
                skipped_count += 1
            except PermissionError:
                print(f"[ERROR] Permission Denied while moving '{f['name']}'.")
                skipped_count += 1
            except shutil.Error as e:
                print(f"[ERROR] Could not move '{f['name']}': {e}")
                skipped_count += 1
            except Exception as e:
                print(f"[ERROR] Unexpected error moving '{f['name']}': {e}")
                skipped_count += 1

        print(f"\nOrganization complete. Moved: {moved_count}, Skipped: {skipped_count}")
        # Refresh scan since files have moved
        self.scan_files()

    # ----------------------------------------------------------------
    # MODULE 4: FILE STATISTICS
    # ----------------------------------------------------------------
    def generate_statistics(self):
        """Generate and display category-wise file statistics."""
        if not self.directory:
            print("[ERROR] No directory selected yet. Please select a folder first.")
            return

        self.stats = defaultdict(int)

        try:
            # Count files inside each category folder (post-organization)
            for category in self.CATEGORIES:
                folder_path = os.path.join(self.directory, category)
                if os.path.isdir(folder_path):
                    count = sum(
                        1 for item in os.listdir(folder_path)
                        if os.path.isfile(os.path.join(folder_path, item))
                    )
                    self.stats[category] = count
                else:
                    self.stats[category] = 0

            total_files = sum(self.stats.values())

            print("\n" + "=" * 40)
            print(f"{'FILE STATISTICS':^40}")
            print("=" * 40)
            print(f"{'Category':<20}{'Count':>10}")
            print("-" * 40)
            for category in self.CATEGORIES:
                print(f"{category:<20}{self.stats[category]:>10}")
            print("-" * 40)
            print(f"{'Total Files':<20}{total_files:>10}")
            print("=" * 40)

        except PermissionError:
            print("[ERROR] Permission Denied while generating statistics.")
        except Exception as e:
            print(f"[ERROR] Unexpected error while generating statistics: {e}")

    # ----------------------------------------------------------------
    # MODULE 5: SEARCH FUNCTIONALITY
    # ----------------------------------------------------------------
    def search_files(self):
        """Search for files by name or extension across the directory tree."""
        if not self.directory:
            print("[ERROR] No directory selected yet. Please select a folder first.")
            return

        print("\nSearch Options:")
        print("1. Search by File Name")
        print("2. Search by Extension")
        choice = input("Enter choice (1/2): ").strip()

        try:
            results = []

            if choice == "1":
                keyword = input("Enter file name (or part of it): ").strip().lower()
                for root, _, files in os.walk(self.directory):
                    for name in files:
                        if keyword in name.lower():
                            results.append(os.path.join(root, name))

            elif choice == "2":
                ext = input("Enter extension (e.g. .pdf): ").strip().lower()
                if not ext.startswith("."):
                    ext = "." + ext
                for root, _, files in os.walk(self.directory):
                    for name in files:
                        if name.lower().endswith(ext):
                            results.append(os.path.join(root, name))
            else:
                print("[ERROR] Invalid choice.")
                return

            print(f"\nFound {len(results)} matching file(s):")
            if results:
                for r in results:
                    print(f" - {r}")
            else:
                print("No matching files found.")

        except PermissionError:
            print("[ERROR] Permission Denied while searching files.")
        except Exception as e:
            print(f"[ERROR] Unexpected error during search: {e}")

    # ----------------------------------------------------------------
    # MODULE 6: DUPLICATE FILE DETECTION
    # ----------------------------------------------------------------
    def detect_duplicates(self):
        """Detect duplicate file names across the directory (including subfolders)."""
        if not self.directory:
            print("[ERROR] No directory selected yet. Please select a folder first.")
            return

        name_counts = defaultdict(int)
        name_locations = defaultdict(list)

        try:
            for root, _, files in os.walk(self.directory):
                for name in files:
                    name_counts[name] += 1
                    name_locations[name].append(root)

            self.duplicates = {name: count for name, count in name_counts.items() if count > 1}

            print("\n" + "=" * 40)
            print(f"{'DUPLICATE FILE DETECTION':^40}")
            print("=" * 40)

            if self.duplicates:
                print("Duplicate Files Found:\n")
                for name, count in self.duplicates.items():
                    print(f" - {name}  (found {count} times)")
                    for loc in name_locations[name]:
                        print(f"     in: {loc}")
            else:
                print("No Duplicate Files Found")
            print("=" * 40)

        except PermissionError:
            print("[ERROR] Permission Denied while checking for duplicates.")
        except Exception as e:
            print(f"[ERROR] Unexpected error during duplicate detection: {e}")

    # ----------------------------------------------------------------
    # MODULE 7: GENERATE REPORT
    # ----------------------------------------------------------------
    def generate_report(self):
        """Generate file_report.txt summarizing the organization session."""
        if not self.directory:
            print("[ERROR] No directory selected yet. Please select a folder first.")
            return

        # Make sure stats and duplicates are up to date
        self.generate_statistics()
        self.detect_duplicates()

        report_path = os.path.join(self.directory, "file_report.txt")

        try:
            with open(report_path, "w", encoding="utf-8") as f:
                f.write("=" * 50 + "\n")
                f.write("SMART FILE ORGANIZER - REPORT\n")
                f.write("=" * 50 + "\n\n")

                f.write(f"Date           : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Folder Name    : {self.directory}\n\n")

                total_files = sum(self.stats.values()) if self.stats else 0
                f.write(f"Total Files    : {total_files}\n\n")

                f.write("Category-wise Count:\n")
                f.write("-" * 30 + "\n")
                for category in self.CATEGORIES:
                    count = self.stats.get(category, 0) if self.stats else 0
                    f.write(f"  {category:<15}: {count}\n")
                f.write("\n")

                f.write("Duplicate Files:\n")
                f.write("-" * 30 + "\n")
                if self.duplicates:
                    for name, count in self.duplicates.items():
                        f.write(f"  {name}  (x{count})\n")
                else:
                    f.write("  No Duplicate Files Found\n")
                f.write("\n")

                f.write("Organized Folder Structure:\n")
                f.write("-" * 30 + "\n")
                for category in self.CATEGORIES:
                    folder_path = os.path.join(self.directory, category)
                    f.write(f"  {category}/\n")
                    if os.path.isdir(folder_path):
                        try:
                            items = sorted(os.listdir(folder_path))
                            if items:
                                for item in items:
                                    f.write(f"      - {item}\n")
                            else:
                                f.write("      (empty)\n")
                        except PermissionError:
                            f.write("      [Permission Denied]\n")
                    else:
                        f.write("      (folder not created)\n")

                f.write("\n" + "=" * 50 + "\n")
                f.write("END OF REPORT\n")
                f.write("=" * 50 + "\n")

            print(f"\n[OK] Report generated successfully: {report_path}")

        except PermissionError:
            print("[ERROR] Permission Denied: Cannot write report file.")
        except Exception as e:
            print(f"[ERROR] Unexpected error while generating report: {e}")


# ----------------------------------------------------------------
# MAIN MENU / DRIVER PROGRAM
# ----------------------------------------------------------------
def print_menu():
    print("\n" + "=" * 45)
    print(f"{'SMART FILE ORGANIZER':^45}")
    print("=" * 45)
    print("1. Select / Change Folder")
    print("2. Scan Files")
    print("3. Organize Files Automatically")
    print("4. Show File Statistics")
    print("5. Search Files")
    print("6. Detect Duplicate Files")
    print("7. Generate Report (file_report.txt)")
    print("8. Exit")
    print("=" * 45)


def main():
    organizer = SmartFileOrganizer()

    # Require a valid directory before allowing other operations
    while organizer.directory is None:
        if not organizer.select_directory():
            retry = input("Try again? (y/n): ").strip().lower()
            if retry != "y":
                print("Exiting program. Goodbye!")
                return

    while True:
        try:
            print_menu()
            choice = input("Enter your choice (1-8): ").strip()

            if choice == "1":
                organizer.select_directory()
            elif choice == "2":
                organizer.scan_files()
            elif choice == "3":
                organizer.organize_files()
            elif choice == "4":
                organizer.generate_statistics()
            elif choice == "5":
                organizer.search_files()
            elif choice == "6":
                organizer.detect_duplicates()
            elif choice == "7":
                organizer.generate_report()
            elif choice == "8":
                print("Exiting Smart File Organizer. Goodbye!")
                break
            else:
                print("[ERROR] Invalid choice. Please enter a number between 1 and 8.")

        except KeyboardInterrupt:
            print("\n\n[INFO] Program interrupted by user. Exiting safely.")
            break
        except Exception as e:
            print(f"[ERROR] An unexpected error occurred: {e}")
            print("The application will continue running.")


if __name__ == "__main__":
    main()