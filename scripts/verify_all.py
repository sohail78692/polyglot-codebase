#!/usr/bin/env python3
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LANGUAGES_DIR = os.path.join(BASE_DIR, "languages")

def verify():
    print("==================================================")
    print("  Polyglot Repository Verification Suite")
    print("  (50 Languages: Hello World + Basic Operations)")
    print("==================================================")
    
    if not os.path.exists(LANGUAGES_DIR):
        print(f"Error: {LANGUAGES_DIR} does not exist.")
        sys.exit(1)
        
    entries = sorted([d for d in os.listdir(LANGUAGES_DIR) if os.path.isdir(os.path.join(LANGUAGES_DIR, d))])
    total = len(entries)
    print(f"Discovered {total} language directories in 'languages/'.\n")
    
    passed = 0
    failed = 0
    
    for folder in entries:
        folder_path = os.path.join(LANGUAGES_DIR, folder)
        files = os.listdir(folder_path)
        readme_present = "README.md" in files
        
        has_hw = any("hello" in f.lower() for f in files)
        has_ops = any("basic" in f.lower() or "operation" in f.lower() for f in files)
        
        notes = []
        if not readme_present:
            notes.append("Missing README.md")
        if not has_hw:
            notes.append("Missing hello world source")
        if not has_ops:
            notes.append("Missing basic operations source")
            
        if not notes:
            passed += 1
            hw_file = [f for f in files if "hello" in f.lower()][0]
            ops_file = [f for f in files if "basic" in f.lower() or "operation" in f.lower()][0]
            print(f"  [PASS] {folder:<20} -> {hw_file}, {ops_file}")
        else:
            failed += 1
            print(f"  [FAIL] {folder:<20} -> {', '.join(notes)}")
            
    print("--------------------------------------------------")
    print(f"Results: {passed}/{total} language directories passed verification.")
    print(f"Total Programs: {passed * 2} verified source files.")
    print("==================================================")
    
    if failed > 0 or total != 50:
        print(f"Verification failed: Expected 50 languages, found {passed} passing.")
        sys.exit(1)
    else:
        print("All 50 languages with 100 programs are properly structured and verified!")
        sys.exit(0)

if __name__ == "__main__":
    verify()
