# danielvo-plugin

Codex で使う自分用の開発支援プラグイン集です。

このリポジトリは、`koizumikento/stray-plugin` と同じく「リポジトリ直下に marketplace を置き、その下に複数のローカルプラグインを束ねる」形にしています。

## 参考にした構成

`stray-plugin` は次のような構成です。

```text
.agents/plugins/marketplace.json
plugins/
  stray-skillops/
    .codex-plugin/plugin.json
    skills/
  stray-research/
    .codex-plugin/plugin.json
    skills/
  stray-studio/
    .codex-plugin/plugin.json
    skills/
  stray-japan-govdocs/
    .codex-plugin/plugin.json
    references/
    skills/
```

ポイントは次の3つです。

- `.agents/plugins/marketplace.json` が、このリポジトリ内のプラグイン一覧です。
- 各プラグインは `plugins/<plugin-name>/.codex-plugin/plugin.json` を持ちます。
- 実際のふるまいは `plugins/<plugin-name>/skills/<skill-name>/SKILL.md` に書きます。

このリポジトリでは、まず `danielvo-dev` という開発支援プラグインから始めます。

## 現在のプラグイン

| Plugin | Path | Purpose |
| --- | --- | --- |
| Danielvo Dev | `plugins/danielvo-dev/` | 日々の開発、レビュー、プラグイン保守を補助する自分用ワークフロー |

## 現在のスキル

| Skill | Use for |
| --- | --- |
| `dev-workflow` | 実装タスクを始めるときの調査、計画、実装、検証、報告の流れを安定させる |
| `plugin-maintainer` | このプラグインリポジトリにスキルを追加・更新・整理するときの保守手順 |

## 使い方

1. Codex 側でこのリポジトリをプラグイン置き場として参照します。
2. `.agents/plugins/marketplace.json` の `plugins[]` に載っているプラグインを有効化します。
3. 作業時に自然文でスキル名や用途を指定します。

例:

```text
dev-workflow を使って、この機能追加の進め方を整理してから実装してください。
```

```text
plugin-maintainer を使って、新しいレビュー用スキルを追加してください。
```

## 更新方針

定期的に更新しやすいように、変更時は次の順番で進めます。

1. 既存スキルと重複しないか確認する。
2. `plugins/danielvo-dev/skills/<skill-name>/SKILL.md` を追加または更新する。
3. `plugins/danielvo-dev/.codex-plugin/plugin.json` の説明や `defaultPrompt` を必要に応じて更新する。
4. この README の「現在のスキル」を更新する。
5. JSON とスキル構造を検証する。

検証コマンド:

```bash
python3 scripts/validate_plugin_repo.py
```

## 定期メンテナンス

GitHub Actions の `validate.yml` は次のタイミングで検証を実行します。

- `main` への push
- pull request
- 毎週月曜 09:00 JST

定期更新時に見る観点:

- 使っていないスキルが残っていないか
- よく使う作業がスキル化されているか
- `SKILL.md` の trigger が広すぎないか
- README と `plugin.json` の説明が現状と一致しているか
- 検証スクリプトが通るか

## 追加するとよさそうなスキル候補

- `code-review-routine`: 自分のレビュー観点を固定化する
- `release-preflight`: リリース前の確認項目を標準化する
- `issue-to-plan`: issue やメモから実装計画を作る
- `docs-updater`: 実装後に README や運用ドキュメントを更新する
