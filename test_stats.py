from app.services.project_stats_service import (
    count_python_files,
    count_markdown_files,
    count_json_files,
    count_total_files,
)


def test_project_statistics():
    assert count_python_files() >= 1
    assert count_markdown_files() >= 1
    assert count_json_files() >= 0
    assert count_total_files() >= 1