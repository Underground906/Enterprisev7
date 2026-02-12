#!/usr/bin/env python3
"""
List all Figma files from a team and export to CSV.
"""

import os
import requests
import csv
import json
import time
from datetime import datetime

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN", "")
TEAM_ID = "1506914777897164782"
FIGMA_API = "https://api.figma.com/v1"

headers = {"X-Figma-Token": FIGMA_TOKEN}

def get_projects():
    """Get all projects in the team."""
    url = f"{FIGMA_API}/teams/{TEAM_ID}/projects"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("projects", [])
    return []

def get_files(project_id):
    """Get all files in a project."""
    url = f"{FIGMA_API}/projects/{project_id}/files"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("files", [])
    return []

def main():
    all_files = []

    print("Fetching projects...")
    projects = get_projects()
    print(f"Found {len(projects)} projects\n")

    for project in projects:
        project_id = project["id"]
        project_name = project["name"]
        print(f"  {project_name}...", end=" ")

        files = get_files(project_id)
        print(f"{len(files)} files")

        for f in files:
            all_files.append({
                "project_id": project_id,
                "project_name": project_name,
                "file_key": f.get("key"),
                "file_name": f.get("name"),
                "last_modified": f.get("last_modified"),
                "thumbnail_url": f.get("thumbnail_url"),
                "figma_url": f"https://www.figma.com/file/{f.get('key')}"
            })

        time.sleep(0.3)  # Rate limiting

    # Save to CSV
    csv_path = "figma_files.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "project_name", "file_name", "file_key", "figma_url",
            "last_modified", "thumbnail_url", "project_id"
        ])
        writer.writeheader()
        writer.writerows(all_files)

    # Save to JSON too
    json_path = "figma_files.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_files, f, indent=2, ensure_ascii=False)

    # Save just the file keys for the extractor
    keys_path = "figma_file_keys.txt"
    with open(keys_path, "w") as f:
        for file in all_files:
            f.write(file["file_key"] + "\n")

    print(f"\n{'='*50}")
    print(f"TOTAL FILES: {len(all_files)}")
    print(f"{'='*50}")
    print(f"\nSaved to:")
    print(f"  - {csv_path}")
    print(f"  - {json_path}")
    print(f"  - {keys_path} (for extractor)")

if __name__ == "__main__":
    main()
