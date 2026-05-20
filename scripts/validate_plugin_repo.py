#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def validate_marketplace() -> list[Path]:
    marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"
    require(marketplace_path.exists(), f"missing {marketplace_path.relative_to(ROOT)}")
    marketplace = load_json(marketplace_path)
    require(isinstance(marketplace.get("plugins"), list), "marketplace plugins must be a list")

    plugin_paths: list[Path] = []
    for entry in marketplace["plugins"]:
        name = entry.get("name")
        source = entry.get("source", {})
        policy = entry.get("policy", {})
        require(name, "marketplace plugin entry is missing name")
        require(source.get("source") == "local", f"{name}: source.source must be local")
        require(source.get("path"), f"{name}: source.path is required")
        require(policy.get("installation"), f"{name}: policy.installation is required")
        require(policy.get("authentication"), f"{name}: policy.authentication is required")
        require(entry.get("category"), f"{name}: category is required")
        plugin_paths.append((ROOT / source["path"]).resolve())
    return plugin_paths


def validate_plugin(plugin_path: Path) -> None:
    manifest_path = plugin_path / ".codex-plugin" / "plugin.json"
    require(manifest_path.exists(), f"missing {manifest_path.relative_to(ROOT)}")
    manifest = load_json(manifest_path)
    require(manifest.get("name") == plugin_path.name, f"{plugin_path.name}: manifest name must match folder name")
    skills_dir = plugin_path / manifest.get("skills", "./skills/")
    require(skills_dir.exists(), f"{plugin_path.name}: skills directory is missing")

    skill_files = sorted(skills_dir.glob("*/SKILL.md"))
    require(skill_files, f"{plugin_path.name}: at least one skill is required")
    for skill_file in skill_files:
        text = skill_file.read_text(encoding="utf-8")
        require(text.startswith("---"), f"{skill_file.relative_to(ROOT)}: missing front matter")
        require("name:" in text.split("---", 2)[1], f"{skill_file.relative_to(ROOT)}: missing name")
        require("description:" in text.split("---", 2)[1], f"{skill_file.relative_to(ROOT)}: missing description")


def main() -> None:
    for plugin_path in validate_marketplace():
        validate_plugin(plugin_path)
    print("plugin-repo-ok")


if __name__ == "__main__":
    main()
