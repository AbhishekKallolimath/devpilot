from pathlib import Path

from app.services.scan_service import scan_project


def test_scan_detects_env_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    (tmp_path / ".env").write_text(
        "DATABASE_URL=test\n",
        encoding="utf-8",
    )

    result = scan_project()

    assert result["status"] == "Completed"
    assert result["secrets_found"] == 1
    assert result["files_with_findings"] == 1


def test_scan_detects_api_key(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    (tmp_path / "config.py").write_text(
        'API_KEY = "123456789abcdef"\n',
        encoding="utf-8",
    )

    result = scan_project()

    assert result["secrets_found"] == 1
    assert result["secret_matches"][0]["type"] == "API_KEY"


def test_scan_detects_password(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    (tmp_path / "config.py").write_text(
        'PASSWORD = "password123"\n',
        encoding="utf-8",
    )

    result = scan_project()

    assert result["secrets_found"] == 1
    assert result["secret_matches"][0]["type"] == "PASSWORD"


def test_scan_ignores_venv(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    venv_dir = tmp_path / ".venv"
    venv_dir.mkdir()

    (venv_dir / "config.py").write_text(
        'API_KEY = "123456789abcdef"\n',
        encoding="utf-8",
    )

    result = scan_project()

    assert result["secrets_found"] == 0