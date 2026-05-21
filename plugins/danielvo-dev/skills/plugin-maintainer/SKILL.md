---
name: "plugin-maintainer"
description: "danielvo-plugin リポジトリ自体のメンテナンス(スキルの追加・更新・整理、メタデータの整合性確認、検証スクリプト実行)を行うときに使用。"
---

# Plugin Maintainer

`danielvo-plugin` 自身のメンテナンスに使うスキル。

## 使わない場面

- このプラグインリポジトリ外での通常のアプリ開発
- プラグインの振る舞いやドキュメントを変えない単発の質問対応
- このリポジトリを変更しないサードパーティプラグインのインストール

## ワークフロー

1. 現状を確認する
   - `.agents/plugins/marketplace.json` と `.claude-plugin/marketplace.json` を読む
   - 変更対象プラグインの `.codex-plugin/plugin.json` と `.claude-plugin/plugin.json` を読む
   - 新規スキルを追加する前に既存の `skills/*/SKILL.md` を一覧する

2. 追加・更新・分割・削除の判断
   - 明確なトリガーを持つ反復ワークフローのときだけスキルを追加する
   - 同じトリガーに属する新挙動なら既存スキルを更新する
   - 1ファイルに無関係なワークフローが混ざったら分割する
   - 大半のタスクで発火してしまう広すぎるスキルは避ける

3. メタデータの整合
   - プラグインの目的や `defaultPrompt` が変わったら `plugin.json` を更新する
   - スキルの追加・改名・削除があれば README のスキル表を更新する
   - 名前は kebab-case で安定させる

4. 検証
   - `python3 scripts/validate_plugin_repo.py` を実行する
   - JSON エラー、マニフェスト欠落、`SKILL.md` 欠落を修正してから終える

## 出力の方針

- 何のスキル / メタデータを変更したかを明示する
- 検証結果を含める
- 次の保守ステップは、明確に有用な場合のみ1つだけ提案する
