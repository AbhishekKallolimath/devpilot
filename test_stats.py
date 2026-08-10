from app.services.project_stats_service import (
    count_python_files,
    count_markdown_files,
    count_json_files,
    count_total_files,
)

print("Python Files :", count_python_files())
print("Markdown Files :", count_markdown_files())
print("JSON Files :", count_json_files())
print("Total Files :", count_total_files())