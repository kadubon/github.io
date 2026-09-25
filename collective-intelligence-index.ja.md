# 集合知研究・OSS索引

K. Takahashi · 2026-09-26

https://kadubon.github.io/github.io/collective-intelligence-index.ja.html

## 集合知研究・OSS索引

AIエージェントの信頼性・記憶・検証・複数エージェントの協調を、困りごとからK. Takahashiの研究とOSSへたどる索引。根拠と限界を確認するための選定地図であり、世界全体の総説ではありません。

## 最初に読む

研究者は成長論文から、実装者は以下の問題から入り、導入前に固定版契約と否定例を確認できる。機械利用者はJSONレジストリ、スキーマ、完全なMarkdownを取得できる。経路はホスト方針に従う助言。

reader: [paper-growth](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-growth) → [paper-vet](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-vet) → [paper-alt](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-alt) → [paper-cait](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-cait)

implementer: [sw-ccr](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-ccr) → [sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-pic) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-vek) → [sw-alt](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-alt) → [sw-cait](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-cait) → [sw-cpcf](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-cpcf)

machine: [sw-skill](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-skill) → [sw-simulator](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-simulator)

## 症状・困りごとから探す

近い症状を選ぶと、最初に読む資料・必要な根拠・停止条件へ進めます。経路は行為の許可ではありません。

### 完了・信頼性

- [AIエージェントが完了と言うのに実際には終わっていない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-completion-and-outcome)
- [同じツール呼び出しを繰り返す](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-retry-recovery)
- [デモでは動くのに本番で失敗する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-production-reliability)
- [作業手順の変更を試し、戻せる根拠を確認したい](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-adaptation)

### ツール・API・再利用

- [MCPのツールを正しく選べない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-tool-routing)
- [API更新後にエージェントが壊れた](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-version-and-dependency-drift)
- [この組合せのツールは実際に連携できるか](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-interchange)
- [以前使えたスキルが別の課題では失敗する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-distribution-shift)
- [スキルを再利用するか一から解くか迷う](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-reuse)

### 記憶・文脈

- [削除した記憶をまた使ってしまう](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-memory-governance)
- [会話やツール出力が長くなり判断が悪化する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-context-management)
- [保存した手続きを今も使ってよいかわからない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-memory)

### 安全性・権限

- [エージェントが強すぎる権限で動いている](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-authority)
- [ツールやRAGの内容に誘導されてエージェントが誤動作する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-security-boundary)

### 費用・レビュー容量

- [エージェントのトークン消費やAPI費用が大きすぎる](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-cost-and-capacity)
- [検証待ちが増えて処理が追いつかない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-verification-backlog)
- [承認依頼が多すぎて作業が進まない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-human-oversight)
- [追加投入する前にどの観測を行うべきか](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-information)
- [検証費用と残るリスクを誰が負担するか](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-verification-funding)

### 評価・根拠

- [ベンチマークは改善したのに本番性能が悪化した](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-evaluation-integrity)
- [AIの引用が主張の根拠になっていない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-evidence-support)
- [生成した出力に未確認事項が残っている](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-obligations)
- [仮説検定を繰り返して根拠を過大評価していないか](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-adaptive-research)
- [この結果からASIの到来時期を予測できるか](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-forecast)

### 複数エージェントの協調

- [エージェントを増やすと重複作業や上書きが起きる](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-coordinate)
- [成果物のコピーで本当に能力が増えたのか](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-accounting)

### 停止・事故対応

- [誤動作したエージェントを停止・隔離・復旧したい](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-incident-response)

### 具体的な対応資料を確認できていない項目

- エージェント向けOAuthの実装方法 — この識別プロトコルまたはパッケージ名の防御機構について、ソース確認済みの実装はない。該当ホスト・提供者の資料を参照。
- MCPのトークンパススルー対策 — この識別プロトコルまたはパッケージ名の防御機構について、ソース確認済みの実装はない。該当ホスト・提供者の資料を参照。
- 存在しないパッケージ名をAIが提案した — この識別プロトコルまたはパッケージ名の防御機構について、ソース確認済みの実装はない。該当ホスト・提供者の資料を参照。
- 生成されたパッケージ名の先取り攻撃を検出したい — この識別プロトコルまたはパッケージ名の防御機構について、ソース確認済みの実装はない。該当ホスト・提供者の資料を参照。
- AIが間違ったパッケージをインストールした — この識別プロトコルまたはパッケージ名の防御機構について、ソース確認済みの実装はない。該当ホスト・提供者の資料を参照。

## 定義と非主張

集合知は、課題と比較プロトコルを宣言した上での相互作用の寄与を指す。集合的能力成長は、検査済みで再利用可能な課題・研究能力の純変化を指す。運用上の自己加速は、資源・品質・時間・外部投入を揃えた上で既存能力が将来の形成速度に寄与する、より強い主張。これらは別の命題。phaseは原則として提案されたプロトコル相対の状態であり、Gibbsモデル論文には別途限定的な数学的前提がある。

## 問題から探す



### AIエージェントが完了と言うのに実際には終わっていない (completion-and-outcome)

[sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-pic) → [sw-fost](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-fost) → [paper-operational-claims](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-operational-claims)

必要入力: 完了条件、完了の申告、受領証、独立した観測。

期待出力: 申告・検査・外界で観測した完了を分け、未解決義務を残す。

条件: 受領証や検査済み台帳だけでは未観測の外部成果を確定できない。

停止・引継ぎ: 完了条件を観測できなければ未知のまま保持し、完了を報告する前に引き継ぐ。

ほかの言い方:

- 完了の誤報告
- ツールの受領証と実際の成果の違い
- 実行後の完了条件を確認したい
- 完了していないのにAIが完了と言うのはなぜ

関連する追加資料: [sw-checkedflow](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-checkedflow)

関連する困りごと: [同じツール呼び出しを繰り返す](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-retry-recovery) · [生成した出力に未確認事項が残っている](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-obligations) · [AIの引用が主張の根拠になっていない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-evidence-support)

### 同じツール呼び出しを繰り返す (retry-recovery)

[sw-pfg](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-pfg) → [sw-ccr](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-ccr) → [sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-pic)

必要入力: 試行ID、リース・送信履歴、再試行予算、冪等性契約、外部受領証。

期待出力: 証拠の再生と行為の再実行を分け、未完了・不確かな作用を明示する。

条件: 普遍的な停止証明、再試行スケジューラ、一度限りの作用保証はない。待機制御と重複排除はホストの責任。

停止・引継ぎ: 作用不明または予算超過なら無条件の再試行を止め、実行先の管理者と照合する。

ほかの言い方:

- エージェントが再試行を続ける
- エージェントがループから抜けない
- エージェントがいつまでも終了しない
- 処理が途中だけ失敗した
- クラッシュ後に処理を復旧したい
- 外部への操作が二重に実行された
- 再試行の冪等性を確認したい
- 履歴の再生と処理の再実行は違うのか
- 外部で操作が成功したかわからない
- 外部の実行結果と台帳を照合したい
- 429制限でエージェントが再試行する
- 再試行が集中して負荷が増える
- 再試行が連鎖して費用が膨らむ
- 同じMCPツールの再試行が止まらない

関連する追加資料: [sw-checkedflow](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-checkedflow)

関連する困りごと: [AIエージェントが完了と言うのに実際には終わっていない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-completion-and-outcome) · [エージェントのトークン消費やAPI費用が大きすぎる](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-cost-and-capacity) · [誤動作したエージェントを停止・隔離・復旧したい](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-incident-response)

### デモでは動くのに本番で失敗する (production-reliability)

[sw-loscr](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-loscr) → [paper-loscr](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-loscr) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-vek)

必要入力: 反復実行課題、版付き環境、失敗記録、サービス窓、条件を揃えた資源上限。

期待出力: サービスの主張を、裏付けのある観測・劣化・未解決容量に限定する。

条件: リリース、1回の成功、合成容量はSLO・SLA保証ではない。pass^k推定器や429対応処理は提供しない。

停止・引継ぎ: 分母・独立性・変化の検査・エラー予算が不足すれば本番適性を確定せずサービス管理者へ引き継ぐ。

ほかの言い方:

- AIエージェントの信頼性を評価したい
- エージェントの成功率をどう測るか
- エージェントのSLOやSLAを設定したい
- 失敗を許容する予算を決めたい
- 繰り返し実行すると結果が安定しない
- 連続試行の成功指標pass^kを評価したい
- エージェントが時々失敗する
- エージェントの障害耐性を確認したい
- 障害時に機能を段階的に制限したい
- エージェントを本番投入してよいか

関連する困りごと: [ベンチマークは改善したのに本番性能が悪化した](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-evaluation-integrity) · [API更新後にエージェントが壊れた](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-version-and-dependency-drift) · [検証待ちが増えて処理が追いつかない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-verification-backlog)

### 保護すべき限界の下で局所方策をどう変更するか？ (adaptation)

[sw-oasg](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-oasg) → [paper-conversion](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-conversion)

こんなとき: 作業手順の変更を試し、戻せる根拠を確認したい

必要入力: 台帳接頭辞、方策候補、試行課題、復旧根拠。

期待出力: shadow・lease試行結果と条件付き昇格・棄却。

条件: ホスト方針に従う助言経路。保護対象の劣化、受領証不足、実行権限の欠如。

停止・引継ぎ: 保護対象の劣化、受領証不足、実行権限の欠如。

関連する困りごと: [デモでは動くのに本番で失敗する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-production-reliability) · [API更新後にエージェントが壊れた](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-version-and-dependency-drift) · [誤動作したエージェントを停止・隔離・復旧したい](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-incident-response)

### MCPのツールを正しく選べない (tool-routing)

[sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-pic) → [sw-pfg](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-pfg)

必要入力: 課題、候補ツールの説明、入力スキーマ、作用、根拠、必要権限。

期待出力: ホストがツールを選ぶ前に、入力義務と権限を限定的に確認する。

条件: 診断の入口のみ。MCP検索エンジン、順位付け手法、多数ツールでの性能根拠はない。発見できることは使用許可ではない。

停止・引継ぎ: 説明や引数が曖昧なら確認とホスト側スキーマ検査を行い、一致から権限を推測しない。

ほかの言い方:

- エージェントが間違ったツールを選ぶ
- エージェントが必要なツールを見つけられない
- MCPツールが多すぎる
- MCPツールの説明で文脈が埋まる
- ツールの検索と振り分けを見直したい
- 多数のツールでfunction callingを使いたい
- ツールは合っているが引数が間違う
- ツールの説明が曖昧で選べない

関連する困りごと: [エージェントが強すぎる権限で動いている](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-authority) · [API更新後にエージェントが壊れた](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-version-and-dependency-drift) · [この組合せのツールは実際に連携できるか](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-interchange)

### API更新後にエージェントが壊れた (version-and-dependency-drift)

[sw-oawm](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-oawm) → [sw-fost](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-fost) → [sw-loscr](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-loscr)

必要入力: 変更前後の版、スキーマ、依存ダイジェスト、保存手続き契約、再生根拠。

期待出力: 影響する仮定を失効させ、変わった環境での再検査を要求する。

条件: JSONの形状適合や構造移行は意味・後方互換性の証明ではない。汎用の依存脆弱性検査器ではない。

停止・引継ぎ: 版の結び付けや必要な再検証がなければ古い手続きを隔離する。

ほかの言い方:

- ツールのスキーマが変更された
- 関数呼出しのスキーマ変更で壊れた
- 更新後にMCPツールが動かなくなった
- 古いツール定義を使っている
- JSON Schemaの互換性を再確認したい
- 後方互換性の根拠を確認したい
- 同じ形式でも意味が変わった
- 保存した手続きが古いAPIを使う
- 依存やツールの更新後に再検証したい
- 依存関係の更新でエージェントが壊れた
- 間接依存の変更で挙動が変わった
- モデル更新後にエージェントが壊れた

関連する追加資料: [paper-cgt](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-cgt)

関連する困りごと: [保存した手続きを今も使ってよいかわからない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-memory) · [MCPのツールを正しく選べない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-tool-routing) · [デモでは動くのに本番で失敗する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-production-reliability)

### このバージョンの連携で何が実際に検査されたか？ (interchange)

[sw-alt](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-alt) → [sw-ccr](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-ccr) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-vek)

こんなとき: この組合せのツールは実際に連携できるか

必要入力: 生成元・受け手の厳密な版、スキーマハッシュ、範囲、ホスト受入規則。

期待出力: 版に限定した写像と、未実装の補助記録受入処理。

条件: ホスト方針に従う助言経路。ホスト受入未実装、新しい版、未対応ライフサイクル、推移的互換性の推測。

停止・引継ぎ: ホスト受入未実装、新しい版、未対応ライフサイクル、推移的互換性の推測。

関連する追加資料: [sw-cait](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-cait) · [sw-checkedflow](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-checkedflow)

関連する困りごと: [API更新後にエージェントが壊れた](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-version-and-dependency-drift) · [MCPのツールを正しく選べない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-tool-routing) · [エージェントが強すぎる権限で動いている](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-authority)

### 以前使えたスキルが別の課題では失敗する (distribution-shift)

[sw-alt](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-alt) → [paper-alt](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-alt) → [sw-oawm](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-oawm)

必要入力: 受け手・課題・文脈、依存版、移転検査、条件を揃えた都度解法。

期待出力: 拒否・未知の移転と保守費用を残した、受け手限定の再利用。

条件: 汎用の分布変化検出や外的妥当性保証ではない。以前の検証は転用の根拠ではない。

停止・引継ぎ: 受け手が合わなければ再適格化または都度解法へ戻り、コピーを新しい能力と扱わない。

ほかの言い方:

- 以前使えたスキルが新しい課題では失敗する
- 再利用した知識が逆効果になる
- 課題の分布が変わった
- 再利用と一から解く方法を比較したい
- スキルと受け手の条件が合わない
- ある文脈で有効な手続きが別の文脈では使えない
- 検証結果を別の環境へ適用してよいか

関連する困りごと: [スキルを再利用するか一から解くか迷う](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-reuse) · [保存した手続きを今も使ってよいかわからない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-memory) · [API更新後にエージェントが壊れた](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-version-and-dependency-drift)

### 再利用はいつ都度の解法より有利か？ (reuse)

[paper-alt](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-alt) → [sw-alt](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-alt) → [paper-pcs](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-pcs)

こんなとき: スキルを再利用するか一から解くか迷う

必要入力: 受け手・課題、条件を揃えた都度解法、全形成・移転・検査・保守費用。

期待出力: 適格な受け手選択肢、厳密な型付き費用、有限比較。

条件: ホスト方針に従う助言経路。受け手の不一致、費用欠落、期限切れ、未対応のライフサイクル写像。

停止・引継ぎ: 受け手の不一致、費用欠落、期限切れ、未対応のライフサイクル写像。

ほかの言い方:

- 条件を満たした再利用か確認したい
- 検証済みでも再利用できるとは限らない

関連する困りごと: [以前使えたスキルが別の課題では失敗する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-distribution-shift) · [成果物のコピーで本当に能力が増えたのか](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-accounting) · [保存した手続きを今も使ってよいかわからない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-memory)

### 削除した記憶をまた使ってしまう (memory-governance)

[sw-cmgl](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-cmgl) → [sw-memoryflow](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-memoryflow) → [sw-oawm](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-oawm)

必要入力: 記憶・更新ID、元情報の系譜、廃止履歴、期限、権限、読出し・使用記録。

期待出力: 現行の裏付けられた記憶を受け入れ、失効版を遮断して古い・削除済み記憶の使用を監査する。

条件: 検索用の廃止印は物理消去やモデル学習解除ではない。派生要約・キャッシュには系譜と個別の失効処理が必要で、未記録のストア変更は見えない。

停止・引継ぎ: 版の結び付けや削除系譜が欠ければ再利用を止め、バックエンドと照合する。

ほかの言い方:

- エージェントが古い記憶を使い続ける
- エージェントが消したデータを思い出す
- AIエージェントに情報を忘れさせたい
- エージェントの記憶を削除したい
- 記憶の廃止印を検索に反映したい
- 記憶の誤りを修正したい
- 置き換え済みの記憶が使われる
- 記憶の有効期限を管理したい
- 派生した要約に削除済み情報が残っている
- キャッシュから消した情報が復活する
- RAGからの削除とモデルの学習解除の違い

関連する困りごと: [保存した手続きを今も使ってよいかわからない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-memory) · [会話やツール出力が長くなり判断が悪化する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-context-management) · [API更新後にエージェントが壊れた](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-version-and-dependency-drift)

### 会話やツール出力が長くなり判断が悪化する (context-management)

[sw-cmgl](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-cmgl) → [paper-split-inference](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-split-inference) → [paper-sqot](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-sqot)

必要入力: 元根拠、文脈上限、圧縮系譜、復元可能性の検査、注意予算。

期待出力: 文脈や要約を縮める際にも元情報への参照と未解決義務を残す。

条件: 汎用文脈圧縮器や指示保持の保証ではない。要約は認証済み事実でなく、モデル上の文脈優位は観測性能ではない。

停止・引継ぎ: 根拠や指示の来歴を失ったら、要約を昇格させず原文を取得して再確認する。

ほかの言い方:

- 会話が長くなるとエージェントの判断が悪化する
- コンテキスト窓がいっぱいになる
- ツール出力が多すぎる
- 根拠を残して文脈を圧縮したい
- 要約すると根拠が失われる
- 前に伝えた指示をエージェントが忘れる
- 文脈が大きくなりすぎる
- 証拠を保持したまま圧縮したい

関連する困りごと: [削除した記憶をまた使ってしまう](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-memory-governance) · [エージェントのトークン消費やAPI費用が大きすぎる](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-cost-and-capacity) · [エージェントを増やすと重複作業や上書きが起きる](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-coordinate)

### 失敗や撤回後も手続きをどう管理するか？ (memory)

[sw-oawm](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-oawm) → [paper-workflow-library](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-workflow-library) → [paper-continuity](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-continuity)

こんなとき: 保存した手続きを今も使ってよいかわからない

必要入力: 観測事象、検査受領証、手続き契約、明示的昇格。

期待出力: 矛盾と廃止履歴を保持したバージョン付き許容性。

条件: ホスト方針に従う助言経路。昇格受領証の欠落、事実の真実性またはALT自動昇格の要求。

停止・引継ぎ: 昇格受領証の欠落、事実の真実性またはALT自動昇格の要求。

ほかの言い方:

- 依存の撤回で保存手続きが無効になった
- 手続き記憶を再検証したい

関連する困りごと: [削除した記憶をまた使ってしまう](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-memory-governance) · [API更新後にエージェントが壊れた](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-version-and-dependency-drift) · [以前使えたスキルが別の課題では失敗する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-distribution-shift)

### エージェントが強すぎる権限で動いている (authority)

[sw-pfg](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-pfg) → [sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-pic) → [sw-ccr](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-ccr)

必要入力: 実行主体、委任範囲、発行者、期限、行為対象、保護操作の目録。

期待出力: ホスト方針の下で能力・承認・権限・行為根拠を分ける。

条件: OAuth提供者、トークン交換、資格情報の自動継承は実装しない。局所ゲートの受理は外部権限・法的権限の付与ではない。

停止・引継ぎ: 主体・範囲・期限・委任を確認できなければ拒否または引継ぎ。探索は許可ではない。

ほかの言い方:

- ツールの発見と使用許可を区別したい
- エージェントが誤った権限で動く
- エージェントが管理者として動いている
- サービスアカウントの権限が強すぎる
- エージェントが利用者を代理して操作する
- 委任された権限の範囲を確認したい
- 代理実行で権限が混同される
- 子エージェントに資格情報を継承してよいか
- 実行できることと許可されることは違う
- 承認と権限の違いを確認したい
- 見つけたツールを使ってよいとは限らない

関連する追加資料: [sw-checkedflow](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-checkedflow)

関連する困りごと: [MCPのツールを正しく選べない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-tool-routing) · [ツールやRAGの内容に誘導されてエージェントが誤動作する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-security-boundary) · [誤動作したエージェントを停止・隔離・復旧したい](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-incident-response)

### ツールやRAGの内容に誘導されてエージェントが誤動作する (security-boundary)

[sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-pic) → [sw-atrb](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-atrb) → [sw-cmgl](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-cmgl)

必要入力: 未信頼入力、起源・依存記録、権限境界、評価器の信頼前提。

期待出力: 候補内容と権限を分離し、汚染・評価器に残るリスクを記録する。

条件: 注入攻撃への免疫、マルウェア検査、MCPサーバ認証、供給網認証は提供しない。合成事例は敵対的本番環境の検証ではない。

停止・引継ぎ: 信頼基盤が侵害された場合は関連根拠・記憶を隔離し、ホストのセキュリティ管理者へ引き継ぐ。

ほかの言い方:

- ツールやRAGやMCP経由のプロンプト注入
- 悪意あるMCPサーバからの入力を隔離したい
- MCPの供給網攻撃の信頼境界を確認したい
- ツールの説明に不正な指示が混入した
- 依存パッケージの来歴と信頼範囲を確認したい

関連する困りごと: [エージェントが強すぎる権限で動いている](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-authority) · [誤動作したエージェントを停止・隔離・復旧したい](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-incident-response) · [ベンチマークは改善したのに本番性能が悪化した](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-evaluation-integrity)

### エージェントのトークン消費やAPI費用が大きすぎる (cost-and-capacity)

[sw-cait](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-cait) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-vek) → [paper-bit](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-bit)

必要入力: 課題・エージェント・ツール別の事象費用、再試行、トークン、金額、レビュー時間、単位付き共有容量。

期待出力: 安いモデルや追加エージェントを比較する前に、型付き費用と資源の律速を分ける。

条件: 課金連携、トークンから金額への自動換算、節約保証はない。欠測は未知のままで、モデル容量は測定サービスではない。

停止・引継ぎ: 予算や検証容量を使い切ったら停止・再配分し、異なる単位を混ぜない。

ほかの言い方:

- AIエージェントの費用が高すぎる
- トークン使用量が多すぎる
- エージェントがトークンを浪費する
- 複数エージェントで費用が急増する
- 検証にかかる費用を測りたい
- LLMエージェントの予算を管理したい
- 課題やエージェントやツール別に費用を把握したい
- 安いモデルにしたのに作業全体の費用が増えた
- トークンと金額と人間のレビュー時間を分けたい
- なぜエージェントはこんなにトークンを使うのか

関連する困りごと: [同じツール呼び出しを繰り返す](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-retry-recovery) · [検証待ちが増えて処理が追いつかない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-verification-backlog) · [会話やツール出力が長くなり判断が悪化する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-context-management)

### 検証が律速となるとき何を変更すべきか？ (verification-backlog)

[paper-vet](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-vet) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-vek) → [paper-sqot](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-sqot)

こんなとき: 検証待ちが増えて処理が追いつかない

必要入力: 検査、整数スロット、登録サービス適格性、型付き予算。

期待出力: 有限日程、滞留、修復、未完了作業の報告。

条件: ホスト方針に従う助言経路。合成局所プロファイルに観測サービスを要求、未対応の中断、有限上限の超過。

停止・引継ぎ: 合成局所プロファイルに観測サービスを要求、未対応の中断、有限上限の超過。

ほかの言い方:

- 検証キューがたまっている
- 検証がボトルネックになっている

関連する追加資料: [paper-verification-limited](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-verification-limited)

関連する困りごと: [エージェントのトークン消費やAPI費用が大きすぎる](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-cost-and-capacity) · [承認依頼が多すぎて作業が進まない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-human-oversight) · [デモでは動くのに本番で失敗する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-production-reliability)

### 承認依頼が多すぎて作業が進まない (human-oversight)

[sw-oversight](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-oversight) → [paper-sqot](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-sqot) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-vek)

必要入力: レビュー容量、割込み費用、リスク範囲、引継ぎ規則、検出根拠。

期待出力: 作業全体のレビュー負荷を、主張の余裕と残る義務を明示して比較する。

条件: 高費用レビューのスクリプトは疲労・自動化バイアスの人間実験ではない。承認は真偽検証でなく、普遍的な引継ぎ閾値もない。

停止・引継ぎ: 影響の大きい未解決義務を引き継ぎ、担当者不在なら承認を捏造せず不確実性を保つ。

ほかの言い方:

- 承認依頼が多すぎる
- 人間の確認待ちがボトルネックになる
- 承認疲れで確認が雑になる
- 自動化された判断を信じすぎてしまう
- どの時点で人間へ引き継ぐべきか
- 必要な案件だけ人間がレビューしたい
- 人間のレビュー容量を見積もりたい
- 承認したことと検証したことを区別したい

関連する困りごと: [エージェントが強すぎる権限で動いている](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-authority) · [検証待ちが増えて処理が追いつかない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-verification-backlog) · [エージェントのトークン消費やAPI費用が大きすぎる](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-cost-and-capacity)

### どの観測が次の投資判断を変えるか？ (information)

[paper-growth](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-growth) → [sw-cpcf](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-cpcf) → [paper-consequence](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-consequence)

こんなとき: 追加投入する前にどの観測を行うべきか

必要入力: 有限の結合モデル、観測核、費用、継続資源。

期待出力: 観測に基づく方策と条件付き情報利用比較。

条件: ホスト方針に従う助言経路。不可能な観測、探索予算超過、実世界の加速主張。

停止・引継ぎ: 不可能な観測、探索予算超過、実世界の加速主張。

関連する困りごと: [エージェントのトークン消費やAPI費用が大きすぎる](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-cost-and-capacity) · [検証待ちが増えて処理が追いつかない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-verification-backlog) · [検証費用と残るリスクを誰が負担するか](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-verification-funding)

### 検証費用と残余リスクを誰が負担するか？ (verification-funding)

[paper-conversion](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-conversion) → [paper-bit](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-bit) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-vek)

こんなとき: 検証費用と残るリスクを誰が負担するか

必要入力: 費用負担者、権限、資源所有、責任分担の宣言。

期待出力: 制度的な費用負担の論点と型付き費用。市場を生成するものではない。

条件: ホスト方針に従う助言経路。制度的合意の欠如。パッケージは法的権限や責任を割り当てられない。

停止・引継ぎ: 制度的合意の欠如。パッケージは法的権限や責任を割り当てられない。

関連する困りごと: [承認依頼が多すぎて作業が進まない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-human-oversight) · [エージェントのトークン消費やAPI費用が大きすぎる](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-cost-and-capacity) · [エージェントが強すぎる権限で動いている](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-authority)

### ベンチマークは改善したのに本番性能が悪化した (evaluation-integrity)

[sw-loscr](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-loscr) → [sw-atrb](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-atrb) → [sw-audit](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-audit)

必要入力: 保留事例、評価器・版の来歴、適応履歴、失敗、運用比較プロトコル。

期待出力: 事例適合、観測したベンチマーク結果、外的妥当性を持つ主張を分ける。

条件: 汎用汚染検出、偏りのないLLM評価器、テストオラクル問題の解決ではない。事例と検査器の共同開発や反復参照は推論を制限する。

停止・引継ぎ: 評価器改変、試験漏洩、未宣言の選択があれば強い主張を隔離し、独立した根拠を得る。

ほかの言い方:

- 評価器や信頼基盤が侵害された
- 指標を最適化したら目的から外れた
- 報酬ハッキングを疑っている
- エージェントがテストをすり抜ける
- 評価器を改変してスコアを上げている
- LLM評価器の偏りを確認したい
- ベンチマークの汚染を疑っている
- 探索中に評価用情報が混入した
- 評価に過適合している
- テストの正解判定自体が信用できない
- 合成評価と実世界の根拠を区別したい

関連する困りごと: [仮説検定を繰り返して根拠を過大評価していないか](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-adaptive-research) · [デモでは動くのに本番で失敗する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-production-reliability) · [AIの引用が主張の根拠になっていない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-evidence-support)

### AIの引用が主張の根拠になっていない (evidence-support)

[sw-fost](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-fost) → [sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-pic) → [paper-operational-claims](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-operational-claims)

必要入力: 具体的主張、原典、範囲、時点、来歴、支持不足の記録。

期待出力: 不在の根拠と有限の最終性を明示した、主張と支持根拠の義務。

条件: 事実の真偽・含意を自動判定するオラクルではない。署名・ハッシュは記録を結び付けても真実を証明しない。生成・検証・再利用は別。

停止・引継ぎ: 原典の支持を確かめられなければ主張を限定・保留し未知を残す。タイムアウトは検査済み否定ではない。

ほかの言い方:

- 引用が捏造または根拠として弱い
- 主張と根拠の対応を確認したい
- 根拠の来歴をたどりたい
- 署名済み記録でも真実とは限らない

関連する困りごと: [生成した出力に未確認事項が残っている](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-obligations) · [AIエージェントが完了と言うのに実際には終わっていない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-completion-and-outcome) · [ベンチマークは改善したのに本番性能が悪化した](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-evaluation-integrity)

### 出力を再利用する前に何を検証する必要があるか？ (obligations)

[sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-pic) → [paper-ecpt](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-ecpt) → [paper-operational-claims](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-operational-claims)

こんなとき: 生成した出力に未確認事項が残っている

必要入力: 出力、宣言スキーマ、根拠、既知・未知の測定。

期待出力: 残余を保持したパケットと有限の次検査。

条件: ホスト方針に従う助言経路。元根拠の不足または権限外の実行要求。

停止・引継ぎ: 元根拠の不足または権限外の実行要求。

ほかの言い方:

- 生成されたことは検証済みを意味しない
- 不明なものを不明のまま残したい

関連する追加資料: [sw-checkedflow](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-checkedflow)

関連する困りごと: [AIエージェントが完了と言うのに実際には終わっていない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-completion-and-outcome) · [AIの引用が主張の根拠になっていない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-evidence-support) · [スキルを再利用するか一から解くか迷う](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-reuse)

### 適応的研究で有効な根拠をどう保持するか？ (adaptive-research)

[paper-audit-closed](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-audit-closed) → [sw-audit](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-audit) → [sw-loscr](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-loscr)

こんなとき: 仮説検定を繰り返して根拠を過大評価していないか

必要入力: 事前登録プロトコル、標本化・観測の仮定、乱数種、アルファ予算。

期待出力: 宣言したベンチマーク根拠と支持される主張水準。

条件: ホスト方針に従う助言経路。未宣言の適応、未モデル化の実験室、普遍的認証の要求。

停止・引継ぎ: 未宣言の適応、未モデル化の実験室、普遍的認証の要求。

ほかの言い方:

- 有利な時点で検定を打ち切ってよいか
- 都合のよい仮説を選び続けている
- 適応的AI研究の妥当性を確認したい

関連する困りごと: [ベンチマークは改善したのに本番性能が悪化した](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-evaluation-integrity) · [AIの引用が主張の根拠になっていない](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-evidence-support) · [追加投入する前にどの観測を行うべきか](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-information)

### この索引からASI到来日を予測できるか？ (forecast)

[sw-simulator](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-simulator) → [sw-skill](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-skill)

こんなとき: この結果からASIの到来時期を予測できるか

必要入力: シナリオ分析を行う場合の、明示的な条件付き設定。

期待出力: 到来予測は未対応。条件付き感度分析のみ。

条件: ホスト方針に従う助言経路。日付・確率の予測は停止。経験的なASI到来モデルは確立されていない。

停止・引継ぎ: 日付・確率の予測は停止。経験的なASI到来モデルは確立されていない。

関連する困りごと: [成果物のコピーで本当に能力が増えたのか](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-accounting) · [デモでは動くのに本番で失敗する](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-production-reliability) · [ベンチマークは改善したのに本番性能が悪化した](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-evaluation-integrity)

### 複数エージェントの作業分担と意見の相違をどう保持するか？ (coordinate)

[sw-ccr](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-ccr) → [paper-split-inference](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-split-inference) → [paper-collective-phase](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-collective-phase)

こんなとき: エージェントを増やすと重複作業や上書きが起きる

必要入力: 任務範囲、独立提案、リース、共通予算。

期待出力: 追跡可能な根拠を伴うリース作業と未解決の意見差。

条件: ホスト方針に従う助言経路。実行権限の欠如、独立検証の不足、リース期限切れ。

停止・引継ぎ: 実行権限の欠如、独立検証の不足、リース期限切れ。

ほかの言い方:

- 子エージェントが同じ作業をしている
- エージェントを増やすと遅くなる
- エージェント同士が変更を上書きする
- コーディングエージェント間でGitのマージが競合する
- 複数エージェントの作業が重複する
- エージェント同士が同じ間違いをする
- 根拠なしにエージェントが同意している
- エージェントの作業をリースで管理したい
- エージェントの意見の相違を消さずに保持したい

関連する追加資料: [sw-checkedflow](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-checkedflow)

関連する困りごと: [エージェントのトークン消費やAPI費用が大きすぎる](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-cost-and-capacity) · [エージェントが強すぎる権限で動いている](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-authority) · [ベンチマークは改善したのに本番性能が悪化した](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-evaluation-integrity)

### 能力を蓄積したのか、成果物をコピーしただけか？ (accounting)

[paper-cait](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-cait) → [sw-cait](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-cait) → [paper-growth](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#paper-growth)

こんなとき: 成果物のコピーで本当に能力が増えたのか

必要入力: 一意な元履歴、起源、ライフサイクル、型付き費用、蓄積・サービス単位。

期待出力: 一意な蓄積、サービス、外部投入、未解明の帰属を分離。

条件: ホスト方針に従う助言経路。元履歴、評価証拠、単位整合、因果設計が欠ける場合。

停止・引継ぎ: 元履歴、評価証拠、単位整合、因果設計が欠ける場合。

ほかの言い方:

- 成果物のコピーと新しい能力を区別したい
- エージェントの貢献を割り当てたい
- どのエージェントが貢献したのか

関連する追加資料: [sw-checkedflow](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-checkedflow)

関連する困りごと: [スキルを再利用するか一から解くか迷う](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-reuse) · [エージェントのトークン消費やAPI費用が大きすぎる](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-cost-and-capacity) · [エージェントを増やすと重複作業や上書きが起きる](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-coordinate)

### 誤動作したエージェントを停止・隔離・復旧したい (incident-response)

[sw-pfg](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-pfg) → [sw-ccr](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-ccr) → [sw-cmgl](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#sw-cmgl)

必要入力: 行為・子課題一覧、送信履歴、資格情報、影響した記憶、独立した復旧根拠。

期待出力: ホスト責任の封じ込め確認：新規送信停止、作用不明の保持、隔離、再開前の照合。

条件: 全体停止スイッチ、資格情報の自動失効、任意の外部行為の巻戻しは提供しない。補償は別の行為であり履歴消去ではない。

停止・引継ぎ: ホスト・実行先の管理者へ引き継ぎ、子作業・権限・未解決作用を照合するまで再開しない。

ほかの言い方:

- AIエージェントを停止したい
- エージェントの緊急停止を設計したい
- 暴走したエージェントを封じ込めたい
- 停止後もエージェントが操作を続ける
- エージェントの操作を巻き戻したい
- 危険な呼出しを遮断したい
- 危険なツールを無効にしたい
- エージェントの資格情報を失効させたい
- 子エージェントがまだ動いている
- 補償処理と巻戻しの違いを確認したい
- 副作用が起きたかわからない
- 事故後に実行状態を照合したい
- 汚染された記憶や手続きを隔離したい
- 事故後の再開条件を決めたい

関連する困りごと: [エージェントが強すぎる権限で動いている](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-authority) · [同じツール呼び出しを繰り返す](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-retry-recovery) · [削除した記憶をまた使ってしまう](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html#problem-memory-governance)

## 中核ソフトウェア



### collective-capability-runtime (sw-ccr)

リース付き課題、独立作業群、意見の相違、検証容量を考慮した成長計上を調整する。

編集上の主役割: collective-coordination

限界・未対応用途: 成長例は合成。根拠の受理は確定ではない。外部実行には別の承認が必要。

ソース確認日: 2026-09-21

ソース版・宣言バージョン: 3b4702454f732c7a0a9f30d87483384dc8a281eb / 1.8.0

Review state / レビュー状態: newer_source_not_editorially_reviewed

確認したGitHubリリース: v1.9.0 · 2026-09-21T15:26:31Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: https://kadubon.github.io/collective-capability-runtime/schemas/task.schema.json · Inspected schema identity only; runtime and semantic admission remain separate.

入力: 課題・根拠・任務範囲・資源包絡・承認の対応。

出力: 課題・リース状態、パケット、残余、成長候補報告。

前提: 実行環境: &gt;=3.10。範囲とホスト権限を明示。

作用と信頼境界: 確認コマンドは別記。導入は環境変更を伴う。実行時の書込み・外部送信は個別コマンドの確認が必要。

最初の確認: 固定版README・契約・ライセンスを読み、チェックアウトとリリースを比較し、導入前にスキーマと否定テストを確認。

導入案内: 固定版READMEと確認済みリリース資産に従う。このサイト作業では導入していない。

ソース確認した操作（未実行）: ccr agent explain --json — 公開インターフェースの確認用。索引の調査では実行していない。 Ref: 3b4702454f732c7a0a9f30d87483384dc8a281eb; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/collective-capability-runtime)
- [Pinned interface schema](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/schemas/task.schema.json)
- [Observed release](https://github.com/kadubon/collective-capability-runtime/releases/tag/v1.9.0)
- [ccr-1.9.0-artifact-verification.json](https://github.com/kadubon/collective-capability-runtime/releases/download/v1.9.0/ccr-1.9.0-artifact-verification.json)
- [ccr-1.9.0-attestation-verification.json](https://github.com/kadubon/collective-capability-runtime/releases/download/v1.9.0/ccr-1.9.0-attestation-verification.json)
- [ccr-1.9.0-completion-report.md](https://github.com/kadubon/collective-capability-runtime/releases/download/v1.9.0/ccr-1.9.0-completion-report.md)
- [ccr-1.9.0-public-offline-verification.json](https://github.com/kadubon/collective-capability-runtime/releases/download/v1.9.0/ccr-1.9.0-public-offline-verification.json)
- [ccr-1.9.0-public-sdist-offline-verification.json](https://github.com/kadubon/collective-capability-runtime/releases/download/v1.9.0/ccr-1.9.0-public-sdist-offline-verification.json)
- [ccr-public-offline.py](https://github.com/kadubon/collective-capability-runtime/releases/download/v1.9.0/ccr-public-offline.py)
- [collective_capability_runtime-1.9.0-py3-none-any.whl](https://github.com/kadubon/collective-capability-runtime/releases/download/v1.9.0/collective_capability_runtime-1.9.0-py3-none-any.whl)
- [collective_capability_runtime-1.9.0.tar.gz](https://github.com/kadubon/collective-capability-runtime/releases/download/v1.9.0/collective_capability_runtime-1.9.0.tar.gz)
- [SHA256SUMS](https://github.com/kadubon/collective-capability-runtime/releases/download/v1.9.0/SHA256SUMS)
- [Agent entry: agent-manifest.json](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/agent-manifest.json)
- [Agent entry: SKILL.md](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/.agents/skills/collective-capability-runtime/SKILL.md)
- [e-collective-capability-runtime-readme-md](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/README.md)
- [Pinned contract](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/docs/verified-growth.md)
- [Apache-2.0 license](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/LICENSE)
- [e-collective-capability-runtime-pyproject-toml](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/pyproject.toml)

### percolation-inversion-compiler (sw-pic)

有限のエージェント出力を検査付きパケットに変換し、不明な出力義務を保持する。

編集上の主役割: evidence-and-verification

限界・未対応用途: ヒントは非実行。有限証明の受理は実行・真実・物理的成功を意味しない。

ソース確認日: 2026-09-21

ソース版・宣言バージョン: 55cd5f219d02f02927e247317156e757b1d5d6da / 1.1.0

Review state / レビュー状態: reviewed_snapshot

確認したGitHubリリース: v1.1.0 · 2026-07-11T07:05:56Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: null — upstream schema has no $id · Inspected schema identity only; runtime and semantic admission remain separate.

入力: 有限JSON入力、宣言した枠組み、根拠、検証証拠。

出力: 型付き報告、残余台帳、検証課題、経路候補。

前提: 実行環境: &gt;=3.11。範囲とホスト権限を明示。

作用と信頼境界: 確認コマンドは別記。導入は環境変更を伴う。実行時の書込み・外部送信は個別コマンドの確認が必要。

最初の確認: 固定版README・契約・ライセンスを読み、チェックアウトとリリースを比較し、導入前にスキーマと否定テストを確認。

導入案内: 固定版READMEと確認済みリリース資産に従う。このサイト作業では導入していない。

ソース確認した操作（未実行）: pic agent check --compact — 公開インターフェースの確認用。索引の調査では実行していない。 Ref: 55cd5f219d02f02927e247317156e757b1d5d6da; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/percolation-inversion-compiler)
- [Pinned interface schema](https://github.com/kadubon/percolation-inversion-compiler/blob/55cd5f219d02f02927e247317156e757b1d5d6da/schemas/AbstractionToken.schema.json)
- [Observed release](https://github.com/kadubon/percolation-inversion-compiler/releases/tag/v1.1.0)
- [percolation-inversion-compiler-1.1.0.cyclonedx.json](https://github.com/kadubon/percolation-inversion-compiler/releases/download/v1.1.0/percolation-inversion-compiler-1.1.0.cyclonedx.json)
- [percolation-inversion-compiler-1.1.0.provenance.json](https://github.com/kadubon/percolation-inversion-compiler/releases/download/v1.1.0/percolation-inversion-compiler-1.1.0.provenance.json)
- [percolation-inversion-compiler-1.1.0.sbom.json](https://github.com/kadubon/percolation-inversion-compiler/releases/download/v1.1.0/percolation-inversion-compiler-1.1.0.sbom.json)
- [percolation-inversion-compiler-1.1.0.schemas.zip](https://github.com/kadubon/percolation-inversion-compiler/releases/download/v1.1.0/percolation-inversion-compiler-1.1.0.schemas.zip)
- [percolation_inversion_compiler-1.1.0-py3-none-any.whl](https://github.com/kadubon/percolation-inversion-compiler/releases/download/v1.1.0/percolation_inversion_compiler-1.1.0-py3-none-any.whl)
- [percolation_inversion_compiler-1.1.0.tar.gz](https://github.com/kadubon/percolation-inversion-compiler/releases/download/v1.1.0/percolation_inversion_compiler-1.1.0.tar.gz)
- [Agent entry: agent-manifest.json](https://github.com/kadubon/percolation-inversion-compiler/blob/55cd5f219d02f02927e247317156e757b1d5d6da/agent-manifest.json)
- [Agent entry: SKILL.md](https://github.com/kadubon/percolation-inversion-compiler/blob/55cd5f219d02f02927e247317156e757b1d5d6da/.agents/skills/percolation-inversion-compiler/SKILL.md)
- [e-percolation-inversion-compiler-readme-md](https://github.com/kadubon/percolation-inversion-compiler/blob/55cd5f219d02f02927e247317156e757b1d5d6da/README.md)
- [Pinned contract](https://github.com/kadubon/percolation-inversion-compiler/blob/55cd5f219d02f02927e247317156e757b1d5d6da/docs/resource-matched-measurement.md)
- [Apache-2.0 license](https://github.com/kadubon/percolation-inversion-compiler/blob/55cd5f219d02f02927e247317156e757b1d5d6da/LICENSE)
- [e-percolation-inversion-compiler-pyproject-toml](https://github.com/kadubon/percolation-inversion-compiler/blob/55cd5f219d02f02927e247317156e757b1d5d6da/pyproject.toml)

### verification-ecology-kit (sw-vek)

検証パケットを記録し、共有資源を明示して有限の検証作業を割り当てる。

編集上の主役割: verification-capacity

限界・未対応用途: 実験的な局所容量プロファイルは最大12作業・行動、16スロット。合成・モデル計上のみ。観測・保証サービスはnull。

ソース確認日: 2026-09-21

ソース版・宣言バージョン: 4008e311ceb16edd6e74d9f71341a90120c0d046 / 1.3.0

Review state / レビュー状態: reviewed_snapshot

確認したGitHubリリース: v1.3.0 · 2026-09-12T23:26:21Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: https://verification-ecology-kit.org/schemas/capacity-report.schema.json · Inspected schema identity only; runtime and semantic admission remain separate.

入力: 登録した検査、サービス適格性、整数スロット、型付き予算、残余。

出力: 日程、独立検査、容量報告、未完了作業の計上。

前提: 実行環境: &gt;=3.11。範囲とホスト権限を明示。

作用と信頼境界: 確認コマンドは別記。導入は環境変更を伴う。実行時の書込み・外部送信は個別コマンドの確認が必要。

最初の確認: 固定版README・契約・ライセンスを読み、チェックアウトとリリースを比較し、導入前にスキーマと否定テストを確認。

導入案内: 固定版READMEと確認済みリリース資産に従う。このサイト作業では導入していない。

ソース確認した操作（未実行）: vek schema list — 公開インターフェースの確認用。索引の調査では実行していない。 Ref: 4008e311ceb16edd6e74d9f71341a90120c0d046; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/verification-ecology-kit)
- [Pinned interface schema](https://github.com/kadubon/verification-ecology-kit/blob/4008e311ceb16edd6e74d9f71341a90120c0d046/src/verification_ecology_kit/schemas/capacity-report.schema.json)
- [Observed release](https://github.com/kadubon/verification-ecology-kit/releases/tag/v1.3.0)
- [SHA256SUMS](https://github.com/kadubon/verification-ecology-kit/releases/download/v1.3.0/SHA256SUMS)
- [verification_ecology_kit-1.3.0-py3-none-any.whl](https://github.com/kadubon/verification-ecology-kit/releases/download/v1.3.0/verification_ecology_kit-1.3.0-py3-none-any.whl)
- [verification_ecology_kit-1.3.0.tar.gz](https://github.com/kadubon/verification-ecology-kit/releases/download/v1.3.0/verification_ecology_kit-1.3.0.tar.gz)
- [Agent entry: SKILL.md](https://github.com/kadubon/verification-ecology-kit/blob/4008e311ceb16edd6e74d9f71341a90120c0d046/.agents/skills/verification-ecology-kit/SKILL.md)
- [e-verification-ecology-kit-readme-md](https://github.com/kadubon/verification-ecology-kit/blob/4008e311ceb16edd6e74d9f71341a90120c0d046/README.md)
- [Pinned contract](https://github.com/kadubon/verification-ecology-kit/blob/4008e311ceb16edd6e74d9f71341a90120c0d046/docs/capacity.md)
- [Apache-2.0 license](https://github.com/kadubon/verification-ecology-kit/blob/4008e311ceb16edd6e74d9f71341a90120c0d046/LICENSE)
- [e-verification-ecology-kit-pyproject-toml](https://github.com/kadubon/verification-ecology-kit/blob/4008e311ceb16edd6e74d9f71341a90120c0d046/pyproject.toml)

### alt-foundry-kernel (sw-alt)

受け手を指定して有限の再利用候補を適格化し、全費用を都度解法と比較する。

編集上の主役割: reusable-abstraction

限界・未対応用途: 集団再利用プロファイルはAlpha。適格化は確定・実行権限を与えない。配布はGitHub Release資産でPyPIを仮定しない。

ソース確認日: 2026-09-21

ソース版・宣言バージョン: e0296486bb568fdeeda449dada3bc67753ddfe7f / 0.5.0

Review state / レビュー状態: newer_source_not_editorially_reviewed

確認したGitHubリリース: v0.5.0 · 2026-09-20T04:42:20Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: urn:alt-foundry-kernel:schema:token:0.4.0 · Inspected schema identity only; runtime and semantic admission remain separate.

入力: 不変の履歴、受け手契約、形成・移転・検査費用、ライフサイクル事象。

出力: 再利用計画、適格化記録、費用計上、部分的な連携補助記録。

前提: 実行環境: &gt;=3.11。範囲とホスト権限を明示。

作用と信頼境界: 確認コマンドは別記。導入は環境変更を伴う。実行時の書込み・外部送信は個別コマンドの確認が必要。

最初の確認: 固定版README・契約・ライセンスを読み、チェックアウトとリリースを比較し、導入前にスキーマと否定テストを確認。

導入案内: 固定版READMEと確認済みリリース資産に従う。このサイト作業では導入していない。

ソース確認した操作（未実行）: altk --help — 公開インターフェースの確認用。索引の調査では実行していない。 Ref: e0296486bb568fdeeda449dada3bc67753ddfe7f; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/alt-foundry-kernel)
- [Pinned interface schema](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/schemas/token.schema.json)
- [Observed release](https://github.com/kadubon/alt-foundry-kernel/releases/tag/v0.5.0)
- [alt_foundry_kernel-0.5.0-py3-none-any.whl](https://github.com/kadubon/alt-foundry-kernel/releases/download/v0.5.0/alt_foundry_kernel-0.5.0-py3-none-any.whl)
- [alt_foundry_kernel-0.5.0.tar.gz](https://github.com/kadubon/alt-foundry-kernel/releases/download/v0.5.0/alt_foundry_kernel-0.5.0.tar.gz)
- [qualification-manifest.json](https://github.com/kadubon/alt-foundry-kernel/releases/download/v0.5.0/qualification-manifest.json)
- [SHA256SUMS](https://github.com/kadubon/alt-foundry-kernel/releases/download/v0.5.0/SHA256SUMS)
- [validation-manifest.json](https://github.com/kadubon/alt-foundry-kernel/releases/download/v0.5.0/validation-manifest.json)
- [Agent entry: SKILL.md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/.agents/skills/collective-reuse/SKILL.md)
- [e-alt-foundry-kernel-readme-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/README.md)
- [Pinned contract](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/collective-reuse.md)
- [Apache-2.0 license](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/LICENSE)
- [e-alt-foundry-kernel-pyproject-toml](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/pyproject.toml)

### cait-certificate-schema (sw-cait)

有限の計上履歴を再生し、一意な蓄積、サービス再利用、コピー、未解明の起源を分ける。

編集上の主役割: capability-accounting

限界・未対応用途: 実験的計上。コピーは新しい資産ではない。VEKの数値は提供値であり、欠けた元履歴から再構成していない。

ソース確認日: 2026-09-21

ソース版・宣言バージョン: 0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7 / 0.2.0

Review state / レビュー状態: newer_source_not_editorially_reviewed

確認したGitHubリリース: v0.2.0 · 2026-09-13T00:23:18Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: https://cait-schema.local/schemas/accounting/v1/report.schema.json · Inspected schema identity only; runtime and semantic admission remain separate.

入力: 元事象、型付き資源費用、範囲、来歴、条件付きモデル証拠。

出力: 厳密な期間収支、残余、独立検査済みの計上報告。

前提: 実行環境: &gt;=3.11。範囲とホスト権限を明示。

作用と信頼境界: 確認コマンドは別記。導入は環境変更を伴う。実行時の書込み・外部送信は個別コマンドの確認が必要。

最初の確認: 固定版README・契約・ライセンスを読み、チェックアウトとリリースを比較し、導入前にスキーマと否定テストを確認。

導入案内: 固定版READMEと確認済みリリース資産に従う。このサイト作業では導入していない。

ソース確認した操作（未実行）: cait-analyze --help — 公開インターフェースの確認用。索引の調査では実行していない。 Ref: 0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/cait-certificate-schema)
- [Pinned interface schema](https://github.com/kadubon/cait-certificate-schema/blob/0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7/schemas/accounting/report.schema.json)
- [Observed release](https://github.com/kadubon/cait-certificate-schema/releases/tag/v0.2.0)
- [cait_certificate_schema-0.2.0-py3-none-any.whl](https://github.com/kadubon/cait-certificate-schema/releases/download/v0.2.0/cait_certificate_schema-0.2.0-py3-none-any.whl)
- [cait_certificate_schema-0.2.0.tar.gz](https://github.com/kadubon/cait-certificate-schema/releases/download/v0.2.0/cait_certificate_schema-0.2.0.tar.gz)
- [SHA256SUMS](https://github.com/kadubon/cait-certificate-schema/releases/download/v0.2.0/SHA256SUMS)
- [e-cait-certificate-schema-readme-md](https://github.com/kadubon/cait-certificate-schema/blob/0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7/README.md)
- [Pinned contract](https://github.com/kadubon/cait-certificate-schema/blob/0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7/docs/accounting.md)
- [Apache-2.0 license](https://github.com/kadubon/cait-certificate-schema/blob/0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7/LICENSE)
- [e-cait-certificate-schema-pyproject-toml](https://github.com/kadubon/cait-certificate-schema/blob/0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7/pyproject.toml)

### collective-phase-control-fabric (sw-cpcf)

モデル間の結合した不確実性を保持しつつ、有限の情報収集と費用付き能力投資を選ぶ。

編集上の主役割: finite-control-and-information

限界・未対応用途: Beta研究実装。有限モデルの例のみ。署名付き観測は因果モデルを認証しない。経験的加速実験はない。

ソース確認日: 2026-09-21

ソース版・宣言バージョン: 340b4899d5b0892e06d7d2c1ab1f1d48df15e981 / 1.0.1

Review state / レビュー状態: reviewed_snapshot

確認したGitHubリリース: v1.0.1 · 2026-09-13T15:02:46Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: https://schemas.cpcf.dev/v0.6.0/phase-contract.schema.json · Inspected schema identity only; runtime and semantic admission remain separate.

入力: 有限モデル集合、観測核、型付き資源、義務、継続期間。

出力: 検査した有限計画、モデル支持集合、探索未完了状態、介入案。

前提: 実行環境: &gt;=3.12,&lt;3.15,!=3.14.0,!=3.14.1。範囲とホスト権限を明示。

作用と信頼境界: 確認コマンドは別記。導入は環境変更を伴う。実行時の書込み・外部送信は個別コマンドの確認が必要。

最初の確認: 固定版README・契約・ライセンスを読み、チェックアウトとリリースを比較し、導入前にスキーマと否定テストを確認。

導入案内: 固定版READMEと確認済みリリース資産に従う。このサイト作業では導入していない。

ソース確認した操作（未実行）: cpcf agent explain --json — 公開インターフェースの確認用。索引の調査では実行していない。 Ref: 340b4899d5b0892e06d7d2c1ab1f1d48df15e981; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/collective-phase-control-fabric)
- [Pinned interface schema](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/schemas/v0.6.0/phase-contract.schema.json)
- [Observed release](https://github.com/kadubon/collective-phase-control-fabric/releases/tag/v1.0.1)
- [collective_phase_control_fabric-1.0.1-py3-none-any.whl](https://github.com/kadubon/collective-phase-control-fabric/releases/download/v1.0.1/collective_phase_control_fabric-1.0.1-py3-none-any.whl)
- [collective_phase_control_fabric-1.0.1.tar.gz](https://github.com/kadubon/collective-phase-control-fabric/releases/download/v1.0.1/collective_phase_control_fabric-1.0.1.tar.gz)
- [cpcf-sbom.cdx.json](https://github.com/kadubon/collective-phase-control-fabric/releases/download/v1.0.1/cpcf-sbom.cdx.json)
- [SHA256SUMS](https://github.com/kadubon/collective-phase-control-fabric/releases/download/v1.0.1/SHA256SUMS)
- [slsa-provenance.jsonl](https://github.com/kadubon/collective-phase-control-fabric/releases/download/v1.0.1/slsa-provenance.jsonl)
- [Agent entry: agent-manifest.json](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/agent-manifest.json)
- [Agent entry: llms.txt](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/llms.txt)
- [Agent entry: SKILL.md](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/.agents/skills/collective-phase-control-fabric/SKILL.md)
- [e-collective-phase-control-fabric-readme-md](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/README.md)
- [Pinned contract](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/docs/epistemic-growth-control.md)
- [Apache-2.0 license](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/LICENSE)
- [e-collective-phase-control-fabric-pyproject-toml](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/pyproject.toml)

## 中核論文



### Observing and Accelerating Collective Capability Growth (paper-growth)

課題遂行・研究サービス、相互作用の除去比較、証拠費用と継続資源を扱う。

編集上の主役割: finite-control-and-information

限界・未対応用途: 有限期間、情報・資源を揃えた比較、校正とモデルの前提が必要。合成例は実運用の加速を実証しない。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.22604358

Publication / 著者・発表: K. Takahashi · 2026-09-07 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.22604358)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-09-07-observing-and-accelerating-collective-capability-growth-22604358/)
- [e-paper-growth](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Observing%20and%20Accelerating%20Collective%20Capability%20Growth.zip)

### Verifier Ecology Theory: Packetized Self-Verification Under Residual Accountability (paper-vet)

検証が律速になるとき、残余義務と改訂可能な境界を検証パケットに保持する。

編集上の主役割: verification-capacity

限界・未対応用途: 構造的主張は宣言した遷移モデル内。パケット受理は外界の真実の証明ではない。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.21147093

Publication / 著者・発表: K. Takahashi · 2026-07-03 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.21147093)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-07-03-verifier-ecology-theory-packetized-self-verification-under-residual-accountability-21147093/)
- [e-paper-vet](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Verifier%20Ecology%20Theory.zip)

### Executable Capability Percolation Theory (paper-ecpt)

実行可能なパケットのハイパーグラフから能力形成、待ち行列、型付き診断を整理する。

編集上の主役割: capability-formation

限界・未対応用途: 商・応答則・基準・証明には個別の証拠が必要。到達可能性だけでは不十分。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.20535654

Publication / 著者・発表: K. Takahashi · 2026-06-04 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.20535654)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-06-04-executable-capability-percolation-theory-20535654/)
- [e-paper-ecpt](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Executable%20Capability%20Percolation%20Theory.zip)

### Abstraction Liquidity Theory (paper-alt)

受け手ごとの探索費用削減を、形成・移転・検証・ライフサイクル費用と比較する。

編集上の主役割: reusable-abstraction

限界・未対応用途: 正の認証済み剰余には測定・移転・権限・確定の前提が必要。圧縮だけでは足りない。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.20476200

Publication / 著者・発表: K. Takahashi · 2026-05-31 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.20476200)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-05-31-abstraction-liquidity-theory-20476200/)
- [e-paper-alt](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Abstraction%20Liquidity%20Theory.zip)

### Certified Autocatalytic Intelligence Theory: Net-Growth Certificate Algebra for Verified Capability Capital (paper-cait)

型付き部分証明で内生的な検証済み能力の再生産をコピーや外部投入と区別する。

編集上の主役割: capability-accounting

限界・未対応用途: 合成には領域証拠が必要。スペクトル診断や到達形式の記録は実際のASIを検出しない。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.20061296

Publication / 著者・発表: K. Takahashi · 2026-05-07 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.20061296)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-05-07-certified-autocatalytic-intelligence-theory-net-growth-20061296/)
- [e-paper-cait](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Certified%20Autocatalytic%20Intelligence%20Theory.zip)

### Layered Online Service and Replay Control for Verified AI R and D Acceleration (paper-loscr)

オンライン台帳、サービス義務、再生ライブラリから研究開発の主張可能な範囲を決める。

編集上の主役割: evidence-and-verification

限界・未対応用途: 推定・評価・基準・保守の根拠は前提であり、検査器が生成して補えるものではない。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.19836225

Publication / 著者・発表: K. Takahashi · 2026-04-28 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.19836225)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-04-28-layered-online-service-and-replay-control-for-veri-19836225/)
- [e-paper-loscr](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Layered%20Online%20Service%20and%20Replay%20Control%20for%20Verified%20AI%20R%20and%20D%20Acceleration.zip)

### Collective Phase Transitions beyond Individual Saturation (paper-collective-phase)

Gibbsモデルで個体の飽和と集団の優位、局所的な評価可能性を分ける。

編集上の主役割: collective-coordination

限界・未対応用途: 統計力学モデル、混合性、スカラー代理量の仮定に依存する。AIの実際の相転移は導かれない。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.17853555

Publication / 著者・発表: K. Takahashi · 2025-12-08 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.17853555)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2025-12-08-collective-phase-transitions-beyond-individual-s-17853555/)
- [e-paper-collective-phase](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Collective_Phase_Transitions_beyond_Individual_Saturation.zip)

### Audit-Closed AI Scientist Protocol (paper-audit-closed)

透明性ログ、逐次e過程、アルファ予算で適応的研究判断を制約する。

編集上の主役割: research-validity

限界・未対応用途: 統計的保証には宣言した観測・標本化の仮定が必要。合成ベンチマークの範囲は有限。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.18728589

Publication / 著者・発表: K. Takahashi · 2026-02-22 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.18728589)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-02-22-audit-closed-ai-scientist-protocol-18728589/)
- [e-paper-audit-closed](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Audit-Closed%20AI%20Scientist%20Protocol.zip)

## 支援研究とツール



### Reusable Consequence States Under Partial Support and Model Uncertainty (paper-consequence)

後続の行動・観測を通じて、モデル間の結合した不確実性を保持する更新状態を扱う。

編集上の主役割: finite-control-and-information

限界・未対応用途: 有限の動力学・プログラムが基礎。局所的包絡は保守的になり得る。CPCFとの関係は概念的支援。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.22170023

Publication / 著者・発表: K. Takahashi · 2026-08-30 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.22170023)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-08-30-reusable-consequence-states-under-partial-support-and-model-uncertainty-22170023/)
- [e-paper-consequence](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Reusable%20Consequence%20States%20Under%20Partial%20Support%20and%20Model%20Uncertainty.zip)

### Evidence-Carrying Operational Claims in Open Systems: Physical Ledgers, Typed Interfaces, and One-Sided Deployment Guarantees (paper-operational-claims)

型付き根拠が物理・資源台帳、不確実性、有限期間の片側保証を結ぶ。

編集上の主役割: evidence-and-verification

限界・未対応用途: 来歴と有限記録の検査は根拠の真実性、因果識別、物理的安全性を確立しない。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.21531413

Publication / 著者・発表: K. Takahashi · 2026-07-24 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.21531413)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-07-24-evidence-carrying-operational-claims-in-open-systems-physical-ledgers-typed-interfaces-and-one-sided-deployment-guarantees-21531413/)
- [e-paper-operational-claims](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Evidence-Carrying%20Operational%20Claims%20in%20Open%20Systems.zip)

### Bottleneck Inversion Theory: Machine-Readable Witness Calculus for Unlockable Potential (paper-bit)

単位を付けた介入証拠から、解放できる対象価値と資源代替の下界を求める。

編集上の主役割: resource-viability

限界・未対応用途: 裏付けのない座標は報告しない。整合した台帳と資源を揃えた比較が必要。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.20545356

Publication / 著者・発表: K. Takahashi · 2026-06-04 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.20545356)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-06-04-bottleneck-inversion-theory-machine-readable-witness-calculus-20545356/)
- [e-paper-bit](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Bottleneck%20Inversion%20Theory.zip)

### Salience-Queue Occupation Theory (paper-sqot)

有限の注意、診断用の予備資源、検証待ち行列から機会費用と監査費用を明示する。

編集上の主役割: verification-capacity

限界・未対応用途: プロトコル相対の診断は棄権・隔離を許す。注意の優先順位は普遍的目的ではない。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.20526451

Publication / 著者・発表: K. Takahashi · 2026-06-03 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.20526451)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-06-03-salience-queue-occupation-theory-20526451/)
- [e-paper-sqot](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Salience-Queue%20Occupation%20Theory.zip)

### Constraint Generative Theory: Typed Constraint Effects and Scientific Availability (paper-cgt)

型付き制約効果により、同じ最終報告でも生成・検証条件が異なることを扱う。

編集上の主役割: interoperability-and-discovery

限界・未対応用途: このカタログ記録はこの論文のみを指す。シリーズ情報を共有する関連原稿を同一視しない。 概念・シリーズDOIのカタログ日付2026-05-15とDataCite発行日2026-05-28は異なり、TeXと版の厳密な対応は未解決。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.20199440

Publication / 著者・発表: K. Takahashi · 2026-05-15 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.20199440)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-05-15-constraint-generative-theory-typed-constraint-effects-and-scien-20199440/)
- [e-paper-cgt](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Constraint%20Generative%20Theory.zip)

### Certified Conversion Networks for AI Workflows (paper-conversion)

認証された価値の処理量に、検証・権限・待ち行列容量・保守の律速を含める。

編集上の主役割: resource-viability

限界・未対応用途: 一様保証または検証用分割、不確実性契約、厳格なゲートが必要。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.19994795

Publication / 著者・発表: K. Takahashi · 2026-05-03 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.19994795)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-05-03-certified-conversion-networks-for-ai-workflows-19994795/)
- [e-paper-conversion](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Certified%20Conversion%20Networks%20for%20AI%20Workflows.zip)

### Certified Service Is Not Enough for Long-Running AGI (paper-continuity)

復旧・権限・同一性・記憶の健全性は、課題サービスの認証後も独立した義務として残る。

編集上の主役割: workflow-memory

限界・未対応用途: 信頼基盤と違反履歴を消さない条件付き保証であり、AGIの確認ではない。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.19719004

Publication / 著者・発表: K. Takahashi · 2026-04-24 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.19719004)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-04-24-certified-service-is-not-enough-for-long-running-agi-19719004/)
- [e-paper-continuity](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Certified%20Service%20Is%20Not%20Enough%20for%20Long-Running%20AGI.zip)

### Controller Scale Is Not Enough for Long-Running AGI: A Workflow Theory with Reusable Certified Libraries (paper-workflow-library)

再生資源の上限下で、監査済みの再利用ライブラリを資源条件を揃えた直接制御と比較する。

編集上の主役割: workflow-memory

限界・未対応用途: 構成的結果は型付き有限課題群、信頼する検査器、保守包絡に制限される。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.19690749

Publication / 著者・発表: K. Takahashi · 2026-04-22 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.19690749)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-04-22-controller-scale-is-not-enough-for-long-running-agi-19690749/)
- [e-paper-workflow-library](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Controller%20Scale%20Is%20Not%20Enough%20for%20Long-Running%20AGI.zip)

### When Should Inference Be Split? A Fixed-Budget Theory of Predictable Multi-Agent Advantage under Local Context Ceilings (paper-split-inference)

固定予算下で、局所文脈の限界が複数エージェントの優位を許す条件を問う。

編集上の主役割: collective-coordination

限界・未対応用途: 通信・検証費用と強い単体エージェントの比較対象を保持する必要がある。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.18932509

Publication / 著者・発表: K. Takahashi · 2026-03-10 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.18932509)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-03-10-when-should-inference-be-split-a-fixed-budget-th-18932509/)
- [e-paper-split-inference](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/When%20Should%20Inference%20Be%20Split.zip)

### Stop Recomputing for AI/LLMs: Proof-Carrying Skills for Compute-Saving Inference Reuse (paper-pcs)

有限の観測述語と呼出しに結び付けた受領証で全再計算なしの再利用を支える。

編集上の主役割: reusable-abstraction

限界・未対応用途: 信頼は最小検査器と宣言した観測基点に限定。受領証は無制限の意味的真実ではない。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.18490939

Publication / 著者・発表: K. Takahashi · 2026-02-05 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.18490939)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-02-05-stop-recomputing-for-ai-llms-proof-carrying-skil-18490939/)
- [e-paper-pcs](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Stop%20Recomputing%20for%20AILLMs%20Proof-Carrying%20Skills%20for%20Compute-Saving%20Inference%20Reuse.zip)

### Verification-Limited Intelligence Acceleration: Observable-Only Laws, Bounded Derivation, and Diagnostics under No-Meta Constraints (paper-verification-limited)

厳格な観測可能進捗の計上で、根拠の欠落による進捗水増しを防ぐ。

編集上の主役割: verification-capacity

限界・未対応用途: 条件付き加速包絡には観測可能な前提と能力への意味的対応が必要。

ソース確認日: 2026-09-21

DOI: 10.5281/zenodo.18436828

Publication / 著者・発表: K. Takahashi · 2026-01-31 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.18436828)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-01-31-verification-limited-intelligence-acceleration-o-18436828/)
- [e-paper-verification-limited](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/verification_limited_intelligence_acceleration.zip)

### observable-agent-workflow-memory (sw-oawm)

根拠目録と明示的な昇格受領証を通じ、検証済み手続きを記憶に昇格する。

編集上の主役割: workflow-memory

限界・未対応用途: 手続きの許容性は事実の真実性ではない。GitHubリリースは未確認。ソースの宣言は0.1.0 beta。

ソース確認日: 2026-09-21

ソース版・宣言バージョン: 414299d4d15b5de434f5fb1ccbb4ba17df9155ff / 0.1.0b0

Review state / レビュー状態: newer_source_not_editorially_reviewed

確認したGitHubリリース: null — no published GitHub release observed

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

入力: 観測可能事象、手続き候補、根拠目録、検査結果。

出力: 受領証に結び付けた手続き契約、廃止・矛盾を残す記憶。

前提: 実行環境: &gt;=3.11。範囲とホスト権限を明示。

作用と信頼境界: 確認コマンドは別記。導入は環境変更を伴う。実行時の書込み・外部送信は個別コマンドの確認が必要。

最初の確認: 固定版README・契約・ライセンスを読み、チェックアウトとリリースを比較し、導入前にスキーマと否定テストを確認。

導入案内: 固定版READMEと確認済みリリース資産に従う。このサイト作業では導入していない。

ソース確認した操作（未実行）: oawm --help — 公開インターフェースの確認用。索引の調査では実行していない。 Ref: 414299d4d15b5de434f5fb1ccbb4ba17df9155ff; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/observable-agent-workflow-memory)
- [e-observable-agent-workflow-memory-readme-md](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/README.md)
- [Pinned contract](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/docs/theory_mapping.md)
- [Apache-2.0 license](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/LICENSE)
- [e-observable-agent-workflow-memory-pyproject-toml](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/pyproject.toml)

### oasg (sw-oasg)

有限の局所ワークフロー方策を試行し、受領証で裏付けた非劣化のみ昇格する。

編集上の主役割: workflow-adaptation

限界・未対応用途: 参照実装・本番利用はAlpha。変更対象はモデル重みではなく方策。試行はホスト方針の下で局所コマンドを実行し得る。

ソース確認日: 2026-09-21

ソース版・宣言バージョン: 7593f74b5d6a4701865dc97b079c3e725c4fd7ee / 1.1.0

Review state / レビュー状態: newer_source_not_editorially_reviewed

確認したGitHubリリース: v1.2.0 · 2026-09-21T22:02:04Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

入力: 観測JSONL台帳、方策変更、shadow・lease試行、ロールバック受領証。

出力: 生存可能性・負債報告、試行判断、昇格・隔離された方策状態。

前提: 実行環境: &gt;=3.12。範囲とホスト権限を明示。

作用と信頼境界: 確認コマンドは別記。導入は環境変更を伴う。実行時の書込み・外部送信は個別コマンドの確認が必要。

最初の確認: 固定版README・契約・ライセンスを読み、チェックアウトとリリースを比較し、導入前にスキーマと否定テストを確認。

導入案内: 固定版READMEと確認済みリリース資産に従う。このサイト作業では導入していない。

ソース確認した操作（未実行）: oasg --help — 公開インターフェースの確認用。索引の調査では実行していない。 Ref: 7593f74b5d6a4701865dc97b079c3e725c4fd7ee; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/oasg)
- [Observed release](https://github.com/kadubon/oasg/releases/tag/v1.2.0)
- [coverage-gates.json](https://github.com/kadubon/oasg/releases/download/v1.2.0/coverage-gates.json)
- [dependency-audit.json](https://github.com/kadubon/oasg/releases/download/v1.2.0/dependency-audit.json)
- [manifest.json](https://github.com/kadubon/oasg/releases/download/v1.2.0/manifest.json)
- [native-requirements.txt](https://github.com/kadubon/oasg/releases/download/v1.2.0/native-requirements.txt)
- [oasg-1.2.0-py3-none-any.whl](https://github.com/kadubon/oasg/releases/download/v1.2.0/oasg-1.2.0-py3-none-any.whl)
- [oasg-1.2.0.tar.gz](https://github.com/kadubon/oasg/releases/download/v1.2.0/oasg-1.2.0.tar.gz)
- [public-verification.json](https://github.com/kadubon/oasg/releases/download/v1.2.0/public-verification.json)
- [qualification.json](https://github.com/kadubon/oasg/releases/download/v1.2.0/qualification.json)
- [SHA256SUMS](https://github.com/kadubon/oasg/releases/download/v1.2.0/SHA256SUMS)
- [source-scan.json](https://github.com/kadubon/oasg/releases/download/v1.2.0/source-scan.json)
- [e-oasg-readme-md](https://github.com/kadubon/oasg/blob/7593f74b5d6a4701865dc97b079c3e725c4fd7ee/README.md)
- [Pinned contract](https://github.com/kadubon/oasg/blob/7593f74b5d6a4701865dc97b079c3e725c4fd7ee/docs/architecture.md)
- [Apache-2.0 license](https://github.com/kadubon/oasg/blob/7593f74b5d6a4701865dc97b079c3e725c4fd7ee/LICENSE)
- [e-oasg-pyproject-toml](https://github.com/kadubon/oasg/blob/7593f74b5d6a4701865dc97b079c3e725c4fd7ee/pyproject.toml)

### audit-closed-ai-scientist (sw-audit)

コミット済みログと逐次検定で適応的科学発見をベンチマークする。

編集上の主役割: research-validity

限界・未対応用途: ベンチマークは任意の実験室・エージェントを認証しない。実行は成果物を書き込む。ソフトはApache-2.0、同梱論文はCC BY 4.0。

ソース確認日: 2026-09-21

ソース版・宣言バージョン: 1e844d1bca18d7bb298aa198e1250bb07bd7ea44 / 0.2.0

Review state / レビュー状態: reviewed_snapshot

確認したGitHubリリース: v0.2.0 · 2026-08-26T02:05:53Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

入力: 宣言した合成設定、乱数種、試行アダプタ、アルファ予算。

出力: 偽発見・再現・逐次根拠・敵対的条件の報告。

前提: 実行環境: &gt;=3.10。範囲とホスト権限を明示。

作用と信頼境界: 確認コマンドは別記。導入は環境変更を伴う。実行時の書込み・外部送信は個別コマンドの確認が必要。

最初の確認: 固定版README・契約・ライセンスを読み、チェックアウトとリリースを比較し、導入前にスキーマと否定テストを確認。

導入案内: 固定版READMEと確認済みリリース資産に従う。このサイト作業では導入していない。

ソース確認した操作（未実行）: audit-closed-ai-scientist --help — 公開インターフェースの確認用。索引の調査では実行していない。 Ref: 1e844d1bca18d7bb298aa198e1250bb07bd7ea44; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/audit-closed-ai-scientist)
- [Observed release](https://github.com/kadubon/audit-closed-ai-scientist/releases/tag/v0.2.0)
- [Agent entry: SKILL.md](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/.agents/skills/audit-closed-ai-scientist/SKILL.md)
- [Pinned contract](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/README.md)
- [Apache-2.0 license](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/LICENSE)
- [e-audit-closed-ai-scientist-pyproject-toml](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/pyproject.toml)

### loscr (sw-loscr)

再生・サービス・評価・依存の根拠不足時に研究開発の強い主張を格下げ・隔離する。

編集上の主役割: evidence-and-verification

限界・未対応用途: 構造検査には外部の統計的前提が必要。doctorも局所状態を初期化し得る。

ソース確認日: 2026-09-21

ソース版・宣言バージョン: 334307b59a4870b90f6162705c793bb5615a555a / 0.1.0

Review state / レビュー状態: newer_source_not_editorially_reviewed

確認したGitHubリリース: v0.1.0 · 2026-04-29T05:30:28Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

入力: 追記型JSONL根拠と明示的な主張契約。

出力: 支持される主張レベル、失敗コード、再生・ライブラリ記録。

前提: 実行環境: &gt;=3.12。範囲とホスト権限を明示。

作用と信頼境界: 確認コマンドは別記。導入は環境変更を伴う。実行時の書込み・外部送信は個別コマンドの確認が必要。

最初の確認: 固定版README・契約・ライセンスを読み、チェックアウトとリリースを比較し、導入前にスキーマと否定テストを確認。

導入案内: 固定版READMEと確認済みリリース資産に従う。このサイト作業では導入していない。

ソース確認した操作（未実行）: loscr --help — 公開インターフェースの確認用。索引の調査では実行していない。 Ref: 334307b59a4870b90f6162705c793bb5615a555a; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/loscr)
- [Observed release](https://github.com/kadubon/loscr/releases/tag/v0.1.0)
- [e-loscr-readme-md](https://github.com/kadubon/loscr/blob/334307b59a4870b90f6162705c793bb5615a555a/README.md)
- [Pinned contract](https://github.com/kadubon/loscr/blob/334307b59a4870b90f6162705c793bb5615a555a/docs/theory-map.md)
- [Apache-2.0 license](https://github.com/kadubon/loscr/blob/334307b59a4870b90f6162705c793bb5615a555a/LICENSE)
- [e-loscr-pyproject-toml](https://github.com/kadubon/loscr/blob/334307b59a4870b90f6162705c793bb5615a555a/pyproject.toml)

### asi-proxy-phase-growth-simulator (sw-simulator)

条件付きシナリオで検証・資源・調整・記憶の変動を探索する。

編集上の主役割: scenario-analysis

限界・未対応用途: 世界予測・ASI到来日・確率は提供しない。合成パラメータは測定値ではない。

ソース確認日: 2026-09-21

ソース版・宣言バージョン: 24690a225c86fde2a24de4d9f93e2a282789b67d / 0.1.0

Review state / レビュー状態: reviewed_snapshot

確認したGitHubリリース: v0.1.0 · 2026-07-21T04:16:46Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

入力: 宣言したパラメータ、有限資源量、乱数種、解法。

出力: 条件付き軌道、感度、Monte Carlo報告。

前提: 実行環境: &gt;=3.12,&lt;3.14。範囲とホスト権限を明示。

作用と信頼境界: 確認コマンドは別記。導入は環境変更を伴う。実行時の書込み・外部送信は個別コマンドの確認が必要。

最初の確認: 固定版README・契約・ライセンスを読み、チェックアウトとリリースを比較し、導入前にスキーマと否定テストを確認。

導入案内: 固定版READMEと確認済みリリース資産に従う。このサイト作業では導入していない。

ソース確認した操作（未実行）: apxsim --help — 公開インターフェースの確認用。索引の調査では実行していない。 Ref: 24690a225c86fde2a24de4d9f93e2a282789b67d; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/asi-proxy-phase-growth-simulator)
- [Observed release](https://github.com/kadubon/asi-proxy-phase-growth-simulator/releases/tag/v0.1.0)
- [asi_proxy_phase_growth_simulator-0.1.0-py3-none-any.whl](https://github.com/kadubon/asi-proxy-phase-growth-simulator/releases/download/v0.1.0/asi_proxy_phase_growth_simulator-0.1.0-py3-none-any.whl)
- [asi_proxy_phase_growth_simulator-0.1.0.tar.gz](https://github.com/kadubon/asi-proxy-phase-growth-simulator/releases/download/v0.1.0/asi_proxy_phase_growth_simulator-0.1.0.tar.gz)
- [e-asi-proxy-phase-growth-simulator-readme-md](https://github.com/kadubon/asi-proxy-phase-growth-simulator/blob/24690a225c86fde2a24de4d9f93e2a282789b67d/README.md)
- [Pinned contract](https://github.com/kadubon/asi-proxy-phase-growth-simulator/blob/24690a225c86fde2a24de4d9f93e2a282789b67d/docs/model-reference.md)
- [Apache-2.0 license](https://github.com/kadubon/asi-proxy-phase-growth-simulator/blob/24690a225c86fde2a24de4d9f93e2a282789b67d/LICENSE)
- [e-asi-proxy-phase-growth-simulator-pyproject-toml](https://github.com/kadubon/asi-proxy-phase-growth-simulator/blob/24690a225c86fde2a24de4d9f93e2a282789b67d/pyproject.toml)

### asi-proxy-phase-skill (sw-skill)

インストール可能なスキルが、根拠を条件とした探索と有限介入の手引きを提供する。

編集上の主役割: interoperability-and-discovery

限界・未対応用途: 助言用スキルであり稼働サービスではない。同梱コーパスは古いスナップショット。導入・実行はホストの権限に従う。

ソース確認日: 2026-09-21

ソース版・宣言バージョン: 5706214a9a3d5e194f371f8ccc2eb71132f82270 / 1.1.1

Review state / レビュー状態: reviewed_snapshot

確認したGitHubリリース: v1.1.1 · 2026-07-31T01:31:01Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

入力: ホスト方針、利用者課題、公開ソースのスナップショット、明示的資源境界。

出力: レビュー可能な介入パケットとソース案内。

前提: 実行環境: &gt;=3.11。範囲とホスト権限を明示。

作用と信頼境界: 確認コマンドは別記。導入は環境変更を伴う。実行時の書込み・外部送信は個別コマンドの確認が必要。

最初の確認: 固定版README・契約・ライセンスを読み、チェックアウトとリリースを比較し、導入前にスキーマと否定テストを確認。

導入案内: 固定版READMEと確認済みリリース資産に従う。このサイト作業では導入していない。

- [Repository](https://github.com/kadubon/asi-proxy-phase-skill)
- [Observed release](https://github.com/kadubon/asi-proxy-phase-skill/releases/tag/v1.1.1)
- [asi-proxy-phase-skill-v1.1.1.zip](https://github.com/kadubon/asi-proxy-phase-skill/releases/download/v1.1.1/asi-proxy-phase-skill-v1.1.1.zip)
- [asi-proxy-phase-skill-v1.1.1.zip.sha256](https://github.com/kadubon/asi-proxy-phase-skill/releases/download/v1.1.1/asi-proxy-phase-skill-v1.1.1.zip.sha256)
- [Agent entry: SKILL.md](https://github.com/kadubon/asi-proxy-phase-skill/blob/5706214a9a3d5e194f371f8ccc2eb71132f82270/asi-proxy-phase-skill/SKILL.md)
- [Pinned contract](https://github.com/kadubon/asi-proxy-phase-skill/blob/5706214a9a3d5e194f371f8ccc2eb71132f82270/README.md)
- [Apache-2.0 license](https://github.com/kadubon/asi-proxy-phase-skill/blob/5706214a9a3d5e194f371f8ccc2eb71132f82270/LICENSE)
- [e-asi-proxy-phase-skill-pyproject-toml](https://github.com/kadubon/asi-proxy-phase-skill/blob/5706214a9a3d5e194f371f8ccc2eb71132f82270/pyproject.toml)

### certified-memory-governance-layer (sw-cmgl)

記憶の書込み・検索結果を、現行版・権限受領証・廃止履歴・汚染区分で制御する。

編集上の主役割: workflow-memory

限界・未対応用途: 手続き上の許容性のみ。事実の真実性、モデルの学習解除、バックエンドの完全消去、注入攻撃への免疫は保証しない。外部アダプタの運用はアプリ側が担う。

ソース確認日: 2026-09-24

ソース版・宣言バージョン: 2fc49b4df7bbe4a23265b8b2372432711740d00b / 1.1.2

Review state / レビュー状態: reviewed_snapshot

確認したGitHubリリース: v1.1.2 · 2026-05-14T01:30:00Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

入力: 版・ダイジェスト付き記憶事象、検証済み台帳接頭辞、構造化された権限。

出力: 受入・遮断受領証と監査可能な現行検索ビュー。

前提: Python &gt;=3.10。対象範囲とホスト権限を確認。

作用と信頼境界: 記憶の受入とビュー構築は局所記録を永続化し得る。削除の意味論は外部コピーの物理消去を意味しない。 このレビューではソース確認のみ。

最初の確認: 実行を検討する前に固定版README・契約・失敗例を読む。

導入案内: ホストの許可後に固定版の上流手順を参照。このレビューではパッケージレジストリ上の提供状態を独立確認していない。

- [Repository](https://github.com/kadubon/certified-memory-governance-layer)
- [Observed release](https://github.com/kadubon/certified-memory-governance-layer/releases/tag/v1.1.2)
- [e-routing-cmgl-readme-md](https://github.com/kadubon/certified-memory-governance-layer/blob/2fc49b4df7bbe4a23265b8b2372432711740d00b/README.md)
- [Pinned contract](https://github.com/kadubon/certified-memory-governance-layer/blob/2fc49b4df7bbe4a23265b8b2372432711740d00b/docs/proof-obligations.md)
- [Apache-2.0 license](https://github.com/kadubon/certified-memory-governance-layer/blob/2fc49b4df7bbe4a23265b8b2372432711740d00b/LICENSE)
- [e-routing-cmgl-pyproject-toml](https://github.com/kadubon/certified-memory-governance-layer/blob/2fc49b4df7bbe4a23265b8b2372432711740d00b/pyproject.toml)
- [e-routing-cmgl-docs-current-view-md](https://github.com/kadubon/certified-memory-governance-layer/blob/2fc49b4df7bbe4a23265b8b2372432711740d00b/docs/current-view.md)
- [e-routing-cmgl-tests-test-compression-py](https://github.com/kadubon/certified-memory-governance-layer/blob/2fc49b4df7bbe4a23265b8b2372432711740d00b/tests/test_compression.py)

### memoryflow-agent-memory-auditor (sw-memoryflow)

宣言された記憶テレメトリから、古い・削除済み・置換済み記憶の使用、修正遅延、比較不能な指標を監査する。

編集上の主役割: workflow-memory

限界・未対応用途: 未記録のストア変更、捏造事象、情報源の真偽は判定できない。削除記録の監査は記憶やモデル重みの消去ではない。

ソース確認日: 2026-09-24

ソース版・宣言バージョン: c8ee3f4c81f5303535ba2d2e9882c409f05e641e / 0.1.0

Review state / レビュー状態: newer_source_not_editorially_reviewed

確認したGitHubリリース: v0.1.0 · 2026-05-01T03:15:40Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

入力: JSONL記憶事象、順序・時計ずれ上限、更新ID、ダイジェスト、P0/P1/P2プロファイル。

出力: VALID・DEGRADED・NONCOMPARABLE・NOT_COMPUTABLE等を明示した版付き指標。

前提: Python &gt;=3.11。対象範囲とホスト権限を確認。

作用と信頼境界: 監査器は宣言された事象トレースを読み監査成果物を書く。観測対象の記憶バックエンドを自ら変更しない。 このレビューではソース確認のみ。

最初の確認: 実行を検討する前に固定版README・契約・失敗例を読む。

導入案内: ホストの許可後に固定版の上流手順を参照。このレビューではパッケージレジストリ上の提供状態を独立確認していない。

- [Repository](https://github.com/kadubon/memoryflow-agent-memory-auditor)
- [Observed release](https://github.com/kadubon/memoryflow-agent-memory-auditor/releases/tag/v0.1.0)
- [e-routing-memoryflow-readme-md](https://github.com/kadubon/memoryflow-agent-memory-auditor/blob/c8ee3f4c81f5303535ba2d2e9882c409f05e641e/README.md)
- [Pinned contract](https://github.com/kadubon/memoryflow-agent-memory-auditor/blob/c8ee3f4c81f5303535ba2d2e9882c409f05e641e/docs/conformance-profiles.md)
- [Apache-2.0 license](https://github.com/kadubon/memoryflow-agent-memory-auditor/blob/c8ee3f4c81f5303535ba2d2e9882c409f05e641e/LICENSE)
- [e-routing-memoryflow-pyproject-toml](https://github.com/kadubon/memoryflow-agent-memory-auditor/blob/c8ee3f4c81f5303535ba2d2e9882c409f05e641e/pyproject.toml)
- [e-routing-memoryflow-docs-event-schema-md](https://github.com/kadubon/memoryflow-agent-memory-auditor/blob/c8ee3f4c81f5303535ba2d2e9882c409f05e641e/docs/event-schema.md)
- [e-routing-memoryflow-tests-unit-test-verifier-profiles-py](https://github.com/kadubon/memoryflow-agent-memory-auditor/blob/c8ee3f4c81f5303535ba2d2e9882c409f05e641e/tests/unit/test_verifier_profiles.py)

### problem-frame-gate (sw-pfg)

有限の行為権限を検査し、別管理の送信処理に先立ち5行のゲート束を原子的に記録する。

編集上の主役割: evidence-and-verification

限界・未対応用途: 有限の監査整合性はOAuth基盤、外界の真実、物理的成果、厳密な一度限りの配信ではない。識別・永続化・実行監視・事故対応は運用側の責任。

ソース確認日: 2026-09-24

ソース版・宣言バージョン: 9449b338c4c8b959878704a48b2f16e291e2dfb8 / 1.1.0

Review state / レビュー状態: reviewed_snapshot

確認したGitHubリリース: v1.1.0 · 2026-07-02T01:04:13Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

入力: 厳格な有限範囲目録、記録者・発行者ID、ログ、行為要求、容量、リスク前提。

出力: 拒否または検査済み原子的束。送信と実行先の受理は別の記録。

前提: Python &gt;=3.10。対象範囲とホスト権限を確認。

作用と信頼境界: コミッターはアクチュエーターを実行せず判断を記録する。別途許可されたOutboxBrokerは外部操作を送出し得る。 このレビューではソース確認のみ。

最初の確認: 実行を検討する前に固定版README・契約・失敗例を読む。

導入案内: ホストの許可後に固定版の上流手順を参照。このレビューではパッケージレジストリ上の提供状態を独立確認していない。

- [Repository](https://github.com/kadubon/problem-frame-gate)
- [Observed release](https://github.com/kadubon/problem-frame-gate/releases/tag/v1.1.0)
- [e-routing-pfg-readme-md](https://github.com/kadubon/problem-frame-gate/blob/9449b338c4c8b959878704a48b2f16e291e2dfb8/README.md)
- [Pinned contract](https://github.com/kadubon/problem-frame-gate/blob/9449b338c4c8b959878704a48b2f16e291e2dfb8/docs/operations.md)
- [Apache-2.0 license](https://github.com/kadubon/problem-frame-gate/blob/9449b338c4c8b959878704a48b2f16e291e2dfb8/LICENSE)
- [e-routing-pfg-pyproject-toml](https://github.com/kadubon/problem-frame-gate/blob/9449b338c4c8b959878704a48b2f16e291e2dfb8/pyproject.toml)
- [e-routing-pfg-schemas-gate-request-schema-json](https://github.com/kadubon/problem-frame-gate/blob/9449b338c4c8b959878704a48b2f16e291e2dfb8/schemas/gate-request.schema.json)
- [e-routing-pfg-tests-test-v1-1-hardening-py](https://github.com/kadubon/problem-frame-gate/blob/9449b338c4c8b959878704a48b2f16e291e2dfb8/tests/test_v1_1_hardening.py)

### fost-agent-ledger (sw-fost)

完了の自己申告を、有限の支持根拠・検査済み最終性・未解決義務・環境変更から区別する。

編集上の主役割: evidence-and-verification

限界・未対応用途: 検査済み台帳は真実の判定器でも外界の成果でもない。構造移行は根拠を作らず、用途別のモードと鮮度方針が必要。

ソース確認日: 2026-09-24

ソース版・宣言バージョン: e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa / 2.0.0

Review state / レビュー状態: newer_source_not_editorially_reviewed

確認したGitHubリリース: v2.0.0 · 2026-07-02T08:04:35Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

入力: 有限の主張・支持グラフ、証明書、モード、環境トークン、最終性の記録。

出力: モード限定の許容性、支持不足コード、変化の証拠。

前提: Python &gt;=3.10。対象範囲とホスト権限を確認。

作用と信頼境界: 台帳・検証処理は局所記録と報告を生成する。記録の確定は外部操作や外部観測ではない。 このレビューではソース確認のみ。

最初の確認: 実行を検討する前に固定版README・契約・失敗例を読む。

導入案内: ホストの許可後に固定版の上流手順を参照。このレビューではパッケージレジストリ上の提供状態を独立確認していない。

- [Repository](https://github.com/kadubon/fost-agent-ledger)
- [Observed release](https://github.com/kadubon/fost-agent-ledger/releases/tag/v2.0.0)
- [e-routing-fost-readme-md](https://github.com/kadubon/fost-agent-ledger/blob/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa/README.md)
- [Pinned contract](https://github.com/kadubon/fost-agent-ledger/blob/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa/docs/json_contract.md)
- [Apache-2.0 license](https://github.com/kadubon/fost-agent-ledger/blob/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa/LICENSE)
- [e-routing-fost-pyproject-toml](https://github.com/kadubon/fost-agent-ledger/blob/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa/pyproject.toml)
- [e-routing-fost-docs-limitations-md](https://github.com/kadubon/fost-agent-ledger/blob/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa/docs/limitations.md)
- [e-routing-fost-tests-test-v20-strict-finality-py](https://github.com/kadubon/fost-agent-ledger/blob/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa/tests/test_v20_strict_finality.py)

### agent-trust-residual-benchmark (sw-atrb)

権限・根拠範囲・残余・反復判断を扱う合成の陽性・陰性対照と境界事例を調べる。

編集上の主役割: research-validity

限界・未対応用途: フィクスチャと検査器は同時に開発された。累積条件では因果効果を分離できず、互換用アダプタはPIC・FOST・PFG・CCRとの同等性を証明しない。実世界の安全性・一般化は主張しない。

ソース確認日: 2026-09-24

ソース版・宣言バージョン: eb21fda8ed7bfad9dc33becf2ffcc63285249495 / 0.2.0

Review state / レビュー状態: newer_source_not_editorially_reviewed

確認したGitHubリリース: v0.2.0 · 2026-07-19T12:10:23Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

入力: 固定した事例、受理・拒否方針、反復設定、モデル・実行環境の来歴。

出力: 事例に限定した判断指標、タイムアウト記録、妥当性の限界。

前提: Python &gt;=3.11。対象範囲とホスト権限を確認。

作用と信頼境界: ベンチマーク実行は局所的な合成事例の成果物を生成する。任意のモデル実験は設定されたモデルサービスへ接続し得る。 このレビューではソース確認のみ。

最初の確認: 実行を検討する前に固定版README・契約・失敗例を読む。

導入案内: ホストの許可後に固定版の上流手順を参照。このレビューではパッケージレジストリ上の提供状態を独立確認していない。

- [Repository](https://github.com/kadubon/agent-trust-residual-benchmark)
- [Observed release](https://github.com/kadubon/agent-trust-residual-benchmark/releases/tag/v0.2.0)
- [agent_trust_residual_benchmark-0.2.0-py3-none-any.whl](https://github.com/kadubon/agent-trust-residual-benchmark/releases/download/v0.2.0/agent_trust_residual_benchmark-0.2.0-py3-none-any.whl)
- [agent_trust_residual_benchmark-0.2.0.tar.gz](https://github.com/kadubon/agent-trust-residual-benchmark/releases/download/v0.2.0/agent_trust_residual_benchmark-0.2.0.tar.gz)
- [e-routing-atrb-readme-md](https://github.com/kadubon/agent-trust-residual-benchmark/blob/eb21fda8ed7bfad9dc33becf2ffcc63285249495/README.md)
- [Pinned contract](https://github.com/kadubon/agent-trust-residual-benchmark/blob/eb21fda8ed7bfad9dc33becf2ffcc63285249495/docs/V02_EXPERIMENT.md)
- [Apache-2.0 license](https://github.com/kadubon/agent-trust-residual-benchmark/blob/eb21fda8ed7bfad9dc33becf2ffcc63285249495/LICENSE)
- [e-routing-atrb-pyproject-toml](https://github.com/kadubon/agent-trust-residual-benchmark/blob/eb21fda8ed7bfad9dc33becf2ffcc63285249495/pyproject.toml)
- [e-routing-atrb-docs-v02-results-md](https://github.com/kadubon/agent-trust-residual-benchmark/blob/eb21fda8ed7bfad9dc33becf2ffcc63285249495/docs/V02_RESULTS.md)
- [e-routing-atrb-tests-test-v02-positive-controls-py](https://github.com/kadubon/agent-trust-residual-benchmark/blob/eb21fda8ed7bfad9dc33becf2ffcc63285249495/tests/test_v02_positive_controls.py)

### Oversight-Centered-Metrology-PoC (sw-oversight)

限定されたコード修正課題と主張余裕を用い、再試行・レビュー費用・エスカレーション負荷を調べる。

編集上の主役割: research-validity

限界・未対応用途: 合成12課題、各実モデル1回の記録、スクリプトによる高費用レビューは、人間の承認疲労の実測でも本番適性の証明でもない。報告設定の比較優位は保守的に未確立。

ソース確認日: 2026-09-24

ソース版・宣言バージョン: a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b / unknown

Review state / レビュー状態: reviewed_snapshot

確認したGitHubリリース: null — no published GitHub release observed

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

入力: 小課題プロトコル、再試行・レビュー予算、割込み費用、転用・監査歪みの余裕。

出力: モデル提供者の順位ではなく、作業全体の指標と限定された主張状態。

前提: Python 版の明示なし。対象範囲とホスト権限を確認。

作用と信頼境界: 修復実験は局所Python関数を実行して成果物を書く。任意のGemini/Ollamaバックエンドは設定されたモデルサービスを呼ぶ。 このレビューではソース確認のみ。

最初の確認: 実行を検討する前に固定版README・契約・失敗例を読む。

導入案内: ホストの許可後に固定版の上流手順を参照。このレビューではパッケージレジストリ上の提供状態を独立確認していない。

- [Repository](https://github.com/kadubon/Oversight-Centered-Metrology-PoC)
- [e-routing-oversight-readme-md](https://github.com/kadubon/Oversight-Centered-Metrology-PoC/blob/a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b/README.md)
- [Pinned contract](https://github.com/kadubon/Oversight-Centered-Metrology-PoC/blob/a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b/experiment_manifest.yaml)
- [Apache-2.0 license](https://github.com/kadubon/Oversight-Centered-Metrology-PoC/blob/a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b/LICENCE)
- [e-routing-oversight-report-workflow-oversight-report-md](https://github.com/kadubon/Oversight-Centered-Metrology-PoC/blob/a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b/report/workflow_oversight_report.md)
- [e-routing-oversight-src-oversight-poc-channels-py](https://github.com/kadubon/Oversight-Centered-Metrology-PoC/blob/a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b/src/oversight_poc/channels.py)

### checkedflow (sw-checkedflow)

署名付き権限、確定した課題順序、有限のサンドボックス実行、独立検証、依存関係を考慮した再利用を、A2A/MCPゲートウェイを備えた参照ランタイムで統合する。

編集上の主役割: collective-coordination

限界・未対応用途: 実験的な有限参照ランタイムで、上流の実証範囲は31入力。同一環境上の4ノードは実組織の独立性を確立しない。署名は外界の真実ではなく、転送資格情報は命令権限ではなく、合意順序は検証器の真実ではない。作業受領証やプロトコル上の課題完了は能力受理ではない。生成ソースは検証済みソースではなく、有限動作の検証は普遍的なプログラム正当性ではない。宣言作業単位は実測CPU時間ではなく、複製は新たな能力資本ではなく、結果不明は検査済み失敗ではない。A2A/MCP相互運用は新たな科学的根拠ではない。試験済み公開手順は本番適性を確立しない。一般的な因果的加速・AGI・ASIは導かれず、合意が進んでも検証者の拒否が再利用を阻止し得る。

ソース確認日: 2026-09-26

ソース版・宣言バージョン: a58869e2488bed9550b006d261601240357b2b99 / 0.1.0

Review state / レビュー状態: reviewed_snapshot

確認したGitHubリリース: v0.1.0 · 2026-09-25T14:54:25Z

Release observation / リリース確認: 2026-09-25T15:30:08+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: urn:checkedflow:agent-request:v1 · Mission-scoped profile/inspect/submit/task shapes; schema validity does not establish signature validity, command authority or capability acceptance.

入力: 署名付き命令包絡、固定ミッション・作業者・検証者ID、承認済み契約、有限予算、リース・フェンス、ソース成果物、検証者の証言。

出力: 確定命令ダイジェスト、課題・作業受領証、契約限定の能力状態、保持した残余、依存撤回、分離した計上座標。受領証や応答だけでは検査済み再利用能力にならない。

前提: Python &gt;=3.12。分散実行には別途用意したCometBFT v0.40.0、Linux Docker/gVisor、確認済み固定イメージ、鍵、自己管理の検証ノード、承認済みミッション・検証契約が必要。通信には任意agents/distributed依存を使用し、外部TLS/OAuth運用は別途適格性確認が必要。

作用と信頼境界: ランタイムはノード内SQLiteを永続化し、署名付きネットワーク取引を送信し、別途許可されたgVisor作業者を通じ有限の生成コードを実行し得る。ゲートウェイは署名鍵を持たず受信ソースを実行しないが、設定された通知先へ外部HTTPS要求を行い得る。本レビューではどの構成要素も導入・実行していない。

最初の確認: 固定版の構造・状態機械・適合範囲・安全性・検証限界を読む。復旧前に自己管理ノードの状態・現フェンス・nonce・受領証・依存を確認し、盲目的に再試行せずOUTCOME_UNKNOWNを保持する。

導入案内: ホストの許可と前提確認後に固定版の上流手順を参照。宣言ソース版と観測GitHubリリースは別であり、PyPI成果物の導入・独立検証は本作業で行っていない。

- [Repository](https://github.com/kadubon/checkedflow)
- [Observed release](https://github.com/kadubon/checkedflow/releases/tag/v0.1.0)
- [checkedflow-0.1.0-py3-none-any.whl](https://github.com/kadubon/checkedflow/releases/download/v0.1.0/checkedflow-0.1.0-py3-none-any.whl)
- [checkedflow-0.1.0.tar.gz](https://github.com/kadubon/checkedflow/releases/download/v0.1.0/checkedflow-0.1.0.tar.gz)
- [SHA256SUMS.json](https://github.com/kadubon/checkedflow/releases/download/v0.1.0/SHA256SUMS.json)
- [e-checkedflow-readme](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/README.md)
- [e-checkedflow-package](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/pyproject.toml)
- [Apache-2.0 license](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/LICENSE)
- [e-checkedflow-notice](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/NOTICE)
- [e-checkedflow-architecture](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/docs/architecture.md)
- [e-checkedflow-state-machine](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/docs/state-machine.md)
- [e-checkedflow-audit](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/docs/audit.md)
- [e-checkedflow-validation](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/docs/validation-status.md)
- [e-checkedflow-conformance](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/docs/conformance.md)
- [e-checkedflow-security](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/docs/security.md)
- [e-checkedflow-research](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/docs/research.md)
- [Pinned contract](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/docs/interoperability.md)
- [Pinned interface schema](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/src/checkedflow/data/agent-request.schema.json)
- [e-checkedflow-gateway](https://github.com/kadubon/checkedflow/blob/a58869e2488bed9550b006d261601240357b2b99/src/checkedflow/agents/gateway.py)

## 根拠を保持する作業手順案

生成 → 検証 → 再利用 → 計上 → 再配分は概念的手順であり、そのまま実行できるパイプラインではない。各引渡しで元バイト列、同一性、時計、費用、未解決義務を保持する。ツールを接続する前に以下の型付き関係を確認する。スキーマ適合だけでは意味的受理も実行権限も得られない。

## バージョンを限定した相互運用

「上流でテスト済み」は引用先プロジェクトのネイティブ・フィクスチャ検査の報告を示す。このサイト作業では対象パッケージを実行していない。文書確認、索引回帰検査、ネイティブ連携実行は別の根拠。imports_artifact_fromは受け手から生成元へ、exports_proposal_toは生成元からホストへ向く。互換性は推移的でなく、更新によって自動延長されない。

### basis-sw-ccr

sw-ccr → paper-growth: based_on / documented / source_inspected

リポジトリが限定された役割の研究として参照する。

3b4702454f732c7a0a9f30d87483384dc8a281eb → 10.5281/zenodo.22604358 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

引用は完全実装を意味しない。

- [e-collective-capability-runtime-readme-md](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/README.md)

### basis-sw-pic

sw-pic → paper-ecpt: based_on / documented / source_inspected

リポジトリが限定された役割の研究として参照する。

55cd5f219d02f02927e247317156e757b1d5d6da → 10.5281/zenodo.20535654 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

引用は完全実装を意味しない。

- [e-percolation-inversion-compiler-readme-md](https://github.com/kadubon/percolation-inversion-compiler/blob/55cd5f219d02f02927e247317156e757b1d5d6da/README.md)

### basis-sw-vek

sw-vek → paper-vet: based_on / documented / source_inspected

リポジトリが限定された役割の研究として参照する。

4008e311ceb16edd6e74d9f71341a90120c0d046 → 10.5281/zenodo.21147093 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

引用は完全実装を意味しない。

- [e-verification-ecology-kit-readme-md](https://github.com/kadubon/verification-ecology-kit/blob/4008e311ceb16edd6e74d9f71341a90120c0d046/README.md)

### basis-sw-alt

sw-alt → paper-alt: based_on / documented / source_inspected

リポジトリが限定された役割の研究として参照する。

e0296486bb568fdeeda449dada3bc67753ddfe7f → 10.5281/zenodo.20476200 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

引用は完全実装を意味しない。

- [e-alt-foundry-kernel-readme-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/README.md)

### basis-sw-cait

sw-cait → paper-cait: based_on / documented / source_inspected

リポジトリが限定された役割の研究として参照する。

0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7 → 10.5281/zenodo.20061296 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

引用は完全実装を意味しない。

- [e-cait-certificate-schema-readme-md](https://github.com/kadubon/cait-certificate-schema/blob/0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7/README.md)

### basis-sw-cpcf

sw-cpcf → paper-growth: based_on / documented / source_inspected

リポジトリが限定された役割の研究として参照する。

340b4899d5b0892e06d7d2c1ab1f1d48df15e981 → 10.5281/zenodo.22604358 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

引用は完全実装を意味しない。

- [e-collective-phase-control-fabric-readme-md](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/README.md)
- [e-collective-phase-control-fabric-docs-growth-research-mapping-md](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/docs/growth-research-mapping.md)

### basis-sw-oawm

sw-oawm → paper-workflow-library: based_on / documented / source_inspected

リポジトリが限定された役割の研究として参照する。

414299d4d15b5de434f5fb1ccbb4ba17df9155ff → 10.5281/zenodo.19690749 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

引用は完全実装を意味しない。

- [e-observable-agent-workflow-memory-readme-md](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/README.md)
- [e-observable-agent-workflow-memory-docs-theory-sources-md](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/docs/theory_sources.md)

### basis-sw-audit

sw-audit → paper-audit-closed: based_on / documented / source_inspected

リポジトリが限定された役割の研究として参照する。

1e844d1bca18d7bb298aa198e1250bb07bd7ea44 → 10.5281/zenodo.18728589 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

引用は完全実装を意味しない。

- [e-audit-closed-ai-scientist-readme-md](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/README.md)

### basis-sw-loscr

sw-loscr → paper-loscr: based_on / documented / source_inspected

リポジトリが限定された役割の研究として参照する。

334307b59a4870b90f6162705c793bb5615a555a → 10.5281/zenodo.19836225 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

引用は完全実装を意味しない。

- [e-loscr-readme-md](https://github.com/kadubon/loscr/blob/334307b59a4870b90f6162705c793bb5615a555a/README.md)

### alt-to-ccr

sw-alt → sw-ccr: exports_proposal_to / tested_upstream / upstream_reported

ALT 0.5.0の未リース課題はCCR 1.8.0の形式に適合。ALT補助記録は追加項目。

0.5.0 → 1.8.0 / 1591e88e3b05f9b5fb06b2d0c749aad8bc0909be

Checked fields: ccr.task.v0.1, open status, unleased proposal

ALT補助記録の受入、リース、報酬、実行は提供されない。

- [e-alt-foundry-kernel-docs-reuse-interchange-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/reuse-interchange.md)
- [e-alt-release](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/release-v0.5.0.md)
- [e-alt-native-test](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/tests/test_reuse_integration.py)

### alt-from-vek

sw-alt → sw-vek: imports_artifact_from / tested_upstream / upstream_reported

固定フィクスチャの容量報告スキーマ、範囲・時計・作業保存を検査。

0.5.0 → 1.3.0 / b07998135cb9dccde1e67db3c6ed77fdec847e09

Checked fields: scope, clock, work conservation

計数は提供値で再生ではない。観測速度や経験的独立性は得られない。

- [e-alt-foundry-kernel-docs-reuse-interchange-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/reuse-interchange.md)
- [e-alt-release](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/release-v0.5.0.md)
- [e-alt-native-test](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/tests/test_reuse_integration.py)

### alt-to-vek

sw-alt → sw-vek: tested_interchange_with / tested_upstream / upstream_reported

有限の合成検査需要を公開VEK検査器が受理。

0.5.0 → 1.3.0 / b07998135cb9dccde1e67db3c6ed77fdec847e09

Checked fields: native contract, schedule

ホストの残余・サービス・単位登録と実観測容量は別途必要。

- [e-alt-foundry-kernel-docs-reuse-interchange-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/reuse-interchange.md)
- [e-alt-release](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/release-v0.5.0.md)
- [e-alt-native-test](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/tests/test_reuse_integration.py)

### alt-to-cait

sw-alt → sw-cait: tested_interchange_with / tested_upstream / upstream_reported

対応済み完全履歴を公開解析・検査器が受理。コピーは資産を増やさない。

0.5.0 → 0.2.0 / 7d12bcf0bc4c6eae2acdd177175b6be414a274f6

Checked fields: unique formation, costs, receiver checks, requests/results, withdrawal

期限切れ・矛盾・更新・修正・一部親写像は部分対応。費用から能力への変換・到達主張はない。

- [e-alt-foundry-kernel-docs-reuse-interchange-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/reuse-interchange.md)
- [e-alt-release](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/release-v0.5.0.md)
- [e-alt-native-test](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/tests/test_reuse_integration.py)

### vek-to-ccr

sw-vek → sw-ccr: exports_proposal_to / documented / source_inspected

スキーマ適合候補課題に容量拡張が付随する。

1.3.0 → 6d8a30820806044b3a4b18d499fbe89bef83fbf2

Checked fields: ccr.task.v0.1, duration rounding, x_vek_capacity

CCR基本スキーマは拡張を強制しない。専用受入とホストの原子的資源予約が必要。

- [e-verification-ecology-kit-docs-capacity-interchange-md](https://github.com/kadubon/verification-ecology-kit/blob/4008e311ceb16edd6e74d9f71341a90120c0d046/docs/capacity_interchange.md)

### cait-from-vek

sw-cait → sw-vek: imports_artifact_from / documented / source_inspected

固定容量スキーマで計数を保持し、虚偽保証フィクスチャを拒否。

0.2.0 → 1.3.0 / b07998135cb9dccde1e67db3c6ed77fdec847e09

Checked fields: schema, scope, source digest, work conservation

元VEK履歴がなく、計数は独立再構成されていない。

- [e-cait-certificate-schema-docs-interchange-md](https://github.com/kadubon/cait-certificate-schema/blob/0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7/docs/interchange.md)

### ccr-from-alt-legacy

sw-ccr → sw-alt: imports_artifact_from / documented / source_inspected

CCR成長取込はALT 0.4.0のトークンスキーマに固定。新しい再利用プロファイルではない。

1.8.0 → 0.4.0 / b5170dbee93b9183f86570c9b2fa325be9cded51

Checked fields: token identity, dependencies, guard, provenance

受け手のサービス適格化や新ALTプロファイルの受入を意味しない。

- [e-collective-capability-runtime-docs-verified-growth-interchange-md](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/docs/verified-growth-interchange.md)

### ccr-from-pic

sw-ccr → sw-pic: imports_artifact_from / documented / source_inspected

任意プロバイダ報告の阻害要因・残余・候補限定フラグを保持。

1.8.0 → 1.1.0

Checked fields: accepted, settled, blockers, residuals

索引作業での連携実行テストはない。PIC受理だけでCCR確定・外部実行はできない。

- [e-collective-capability-runtime-interop-pic-md](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/INTEROP_PIC.md)

### cpcf-to-ccr

sw-cpcf → sw-ccr: proposed_integration_with / proposed / editorial

計画候補をホスト作業にするには、別途実装した受入アダプタが必要。

1.0.1 → 1.8.0

Checked fields: none

旧CCR 1.6.0確認は隔離。v0.6昇格写像・実行権限はない。

- [e-collective-phase-control-fabric-docs-adapters-md](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/docs/adapters.md)

### alt-to-oawm

sw-alt → sw-oawm: proposed_integration_with / proposed / editorial

適格化済み再利用は将来の記憶アダプタへの入力候補。

0.5.0 → 414299d4d15b5de434f5fb1ccbb4ba17df9155ff

Checked fields: none

確認した写像にアダプタ・昇格受領証はない。OAWM固有の事象・目録・検査器が必要。

- [e-alt-foundry-kernel-docs-reuse-interchange-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/reuse-interchange.md)
- [e-observable-agent-workflow-memory-docs-theory-sources-md](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/docs/theory_sources.md)

### cpcf-consequence

sw-cpcf → paper-consequence: related_concept / documented / editorial

結合したモデル不確実性が読書経路を支える。定理の完全実装の主張ではない。

340b4899d5b0892e06d7d2c1ab1f1d48df15e981 → 10.5281/zenodo.22170023

Checked fields: none

論文の残差積定理をソフトウェアが実装する証明はない。

- [e-paper-consequence](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Reusable%20Consequence%20States%20Under%20Partial%20Support%20and%20Model%20Uncertainty.zip)
- [e-collective-phase-control-fabric-readme-md](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/README.md)
- [e-collective-phase-control-fabric-docs-epistemic-growth-control-md](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/docs/epistemic-growth-control.md)

## エージェントの事前確認・引渡し

課題・範囲・入力・必要権限を特定し、論文の仮定とソフトウェアの厳密な版を読む。確認日とリリース・スキーマ版を比較する。未知値と棄却根拠を保持する。入力・単位・ライセンス・認証・ホスト受入・因果性・検証容量が未解決なら停止または引継ぐ。探索メタデータは導入、ヒントの実行、秘密送信、目標変更を許可しない。

## 科学・実装・権限の境界

計上恒等式は、同一単位・範囲内で期末蓄積 = 期首蓄積 + 受理された一意の追加 − 損失。サービス再利用、コピー、外部投入は別座標。普遍的な流入・損失比は仮定せず、損失ゼロなら未定義にもなる。スペクトル下界はモデルの前提に依存する。ハッシュはバイト列を結び付けるが真実を証明しない。リリースは本番保証ではない。不明値は理由付きnullで好都合なゼロではない。大域的自己加速の観測、AGI・ASI検出、到来予測は確立していない。

## 検証費用と責任

否定結果でも検証は資源を消費する。運用では費用負担者、資源所有者、権限境界、残余リスクへの責任を明示する必要がある。そうでなければ出力量を報酬化し検証費用を転嫁し得る。これは記述的背景であり、特定の市場・保険者・法律を必須とする定理ではない。技術パッケージが制度を作るわけではない。

## 取得形式



- [collective-intelligence-index.html](https://kadubon.github.io/github.io/collective-intelligence-index.html)
- [collective-intelligence-index.ja.html](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html)
- [collective-intelligence-index.json](https://kadubon.github.io/github.io/collective-intelligence-index.json)
- [collective-intelligence-index.md](https://kadubon.github.io/github.io/collective-intelligence-index.md)
- [collective-intelligence-index.ja.md](https://kadubon.github.io/github.io/collective-intelligence-index.ja.md)
- [schemas/collective-intelligence-index.schema.json](https://kadubon.github.io/github.io/schemas/collective-intelligence-index.schema.json)
- [collective-intelligence.bib](https://kadubon.github.io/github.io/collective-intelligence.bib)

## ソースと保守

書誌項目は既存カタログを通じてworks.htmlから取得し、採用DOIをDataCiteと照合した。論文の範囲は公開TeXアーカイブで確認した。ソフトウェアのコミットとGitHubリリースは別に記録する。日本語説明は編集訳で正式題名は変更しない。全走査目録と根拠位置はレジストリに含む。訂正はサイトリポジトリで行う。サイト本文はCC BY 4.0、確認済みソフトウェアはApache-2.0、同梱論文のライセンスは別。

Scanned 233 research records and 55 repositories; selected 38 resources.

Boundary Exchange / viability: unresolved — No exact Boundary Exchange title/DOI in the scanned catalogue. Do not invent a paper identity.

CGT bandwidth / availability / comparability supplements: unresolved — Distinct TeX manuscripts exist in the source archive, but only the canonical CGT work is a distinct local catalogue record. Do not collapse supplements or invent DOI bindings.

OASG 10.5281/zenodo.20107661: resolved_software_kind — DataCite classifies this as Software, matching works.html. Included through the repository, excluded from paper bibliography.

10.5281/zenodo.20199440: concept_record_date_discrepancy — CGT concept/series DOI has multiple HasVersion records. Existing catalogue first-publication date is 2026-05-15; current DataCite Issued date is 2026-05-28. The exact version binding of the inspected TeX is unresolved. Bibliography includes only verified title/author/year/DOI; it does not claim the DOI identifies these exact source bytes.

[Maintenance](https://kadubon.github.io/github.io/docs/collective-intelligence-index-maintenance.md)
