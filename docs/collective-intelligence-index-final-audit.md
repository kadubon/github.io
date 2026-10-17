# Collective Intelligence Index 最終スナップショット監査 — 2026-10-17

この文書は今回の監査記録であり、資源・書誌・関係の新たな正規データ源ではない。

基準コミット: `a209fdc7ce84da99756e53966e38d5ada30fac70`。開始: `2026-10-17T19:00:15.320697+09:00`。実施日: 2026-10-17 JST。Windows / Python 3.13.5 / jsonschema 4.26.0。既存の未追跡 `output/` は変更・収録していない。

## 確認の深さと修正

選定済み論文20件のTeXの要旨・範囲・限界・結論と、DataCite書誌を照合した。OSS21件の固定README、ライセンス、宣言版、既存の相互運用根拠・公開検証報告を確認した。定理の独立した証明検証、OSSのインストール・実行、ベンチマーク、LLM呼出し、配布wheel/sdistのバイト検証は行っていない。既存の否定的結果と未確認事項を維持した。

- コミットの不一致から新旧順序を推定する表示を修正。固定レビュー対象の状態と現行観測の不一致・取得不能を区別し、既存schemaのenumは維持した。
- GitHub観測と別に、2026-10-17の宣言版・PyPI観測を記録。GitHubの定期更新はパッケージ観測日を更新しない。今回は選定21件だけをrefreshした。
- Works既存ソフトウェア記録のCCRを1.9.0、OASGを1.2.0へ更新し、OSS catalogと英日索引にも反映した。DOI・旧版のレビュー・関係の版境界は保持した。
- 日本語の根拠範囲、走査説明、観測説明を整備。evidence-supportの「不在の根拠」を「取得・確認できない根拠」へ修正し、unavailableをabsenceと誤訳しないようにした。検索語・別名は変えていない。
- 配信検証に形式別MIME判定を追加。HEADが405/501の場合のみ限定GETを使用。BibTeXのapplication/octet-streamはGitHub Pagesのダウンロード配信として、バイト一致・UTF-8検証を伴って許容する。
- 固定版の引用・復元手順を英日と保守文書に追加。サイト自身の新リリースは所有者の直接指示に従い、掲載OSSをリリースしない。

## 元資料・来歴

既存155 evidenceを取得し、100件は既存ハッシュと一致した。55件の旧OSSハッシュはCRLF正規化したテキストに一致し、生のHTTP応答とは異なった。元レコードは改変せず、同じ固定URL・commitの生バイトSHA-256を `-raw-20261017` の55レコードで追記した。zip資料は元のlocatorが指すTeX部材を比較した。20 DOIのDataCite応答も取得・書誌照合した。取得不能の既存evidenceは0件。

現在版のpyproject 20件、動的版を持つEGRのversionファイル1件、PyPI応答14件を metadata-only evidenceとして追記した。合計245 evidence（155 + 55 + 35）。資源の旧evidence_refsとsource review日は変更していない。PyPI JSONのハッシュは応答の識別であり、配布アーカイブを検証したハッシュではない。

## 維持した集合・契約

変更前後とも41資源（論文20、OSS21）、28問題、13役割、20関係、8症状群、5未解決意図。資源・問題・関係・群・未解決意図のID集合、役割列、全関係、読書経路、agent_routingは基準版と一致する。提案のtestedへの昇格なし。ソフトウェアの旧レビュー日は保持。coverage fixtureとschemaは変更なし。168 seed/言語は163 routed・5 unresolvedのまま。

全件表の「確認」は英日概要・限界・出典の照合を示し、有効性・完全実装の認証ではない。OSSでは入力・出力・前提・導入・権限境界も照合した。

| ID | 種別 / 選定 | 英日照合 | 固定根拠 | 保持した限界 |
|---|---|---|---|---|
| paper-growth | paper / core | 確認 | e-paper-growth | 有限期間、情報・資源を揃えた比較、校正とモデルの前提が必要。合成例は実運用の加速を実証しない。 |
| paper-vet | paper / core | 確認 | e-paper-vet | 構造的主張は宣言した遷移モデル内。パケット受理は外界の真実の証明ではない。 |
| paper-ecpt | paper / core | 確認 | e-paper-ecpt | 商・応答則・基準・証明には個別の証拠が必要。到達可能性だけでは不十分。 |
| paper-alt | paper / core | 確認 | e-paper-alt | 正の認証済み剰余には測定・移転・権限・確定の前提が必要。圧縮だけでは足りない。 |
| paper-cait | paper / core | 確認 | e-paper-cait | 合成には領域証拠が必要。スペクトル診断や到達形式の記録は実際のASIを検出しない。 |
| paper-loscr | paper / core | 確認 | e-paper-loscr | 推定・評価・基準・保守の根拠は前提であり、検査器が生成して補えるものではない。 |
| paper-collective-phase | paper / core | 確認 | e-paper-collective-phase | 統計力学モデル、混合性、スカラー代理量の仮定に依存する。AIの実際の相転移は導かれない。 |
| paper-audit-closed | paper / core | 確認 | e-paper-audit-closed | 統計的保証には宣言した観測・標本化の仮定が必要。合成ベンチマークの範囲は有限。 |
| paper-consequence | paper / supporting | 確認 | e-paper-consequence | 有限の動力学・プログラムが基礎。局所的包絡は保守的になり得る。CPCFとの関係は概念的支援。 |
| paper-operational-claims | paper / supporting | 確認 | e-paper-operational-claims | 来歴と有限記録の検査は根拠の真実性、因果識別、物理的安全性を確立しない。 |
| paper-bit | paper / supporting | 確認 | e-paper-bit | 裏付けのない座標は報告しない。整合した台帳と資源を揃えた比較が必要。 |
| paper-sqot | paper / supporting | 確認 | e-paper-sqot | プロトコル相対の診断は棄権・隔離を許す。注意の優先順位は普遍的目的ではない。 |
| paper-cgt | paper / supporting | 確認 | e-paper-cgt | このカタログ記録はこの論文のみを指す。シリーズ情報を共有する関連原稿を同一視しない。 概念・シリーズDOIのカタログ日付2026-05-15とDataCite発行日2026-05-28は異なり、TeXと版の厳密な対応は未解決。 |
| paper-conversion | paper / supporting | 確認 | e-paper-conversion | 一様保証または検証用分割、不確実性契約、厳格なゲートが必要。 |
| paper-continuity | paper / supporting | 確認 | e-paper-continuity | 信頼基盤と違反履歴を消さない条件付き保証であり、AGIの確認ではない。 |
| paper-workflow-library | paper / supporting | 確認 | e-paper-workflow-library | 構成的結果は型付き有限課題群、信頼する検査器、保守包絡に制限される。 |
| paper-split-inference | paper / supporting | 確認 | e-paper-split-inference | 通信・検証費用と強い単体エージェントの比較対象を保持する必要がある。 |
| paper-pcs | paper / supporting | 確認 | e-paper-pcs | 信頼は最小検査器と宣言した観測基点に限定。受領証は無制限の意味的真実ではない。 |
| paper-verification-limited | paper / supporting | 確認 | e-paper-verification-limited | 条件付き加速包絡には観測可能な前提と能力への意味的対応が必要。 |
| sw-ccr | software / core | 確認 | e-collective-capability-runtime-readme-md, e-collective-capability-runtime-docs-verified-growth-md, e-collective-capability-runtime-license, e-collective-capability-runtime-pyproject-toml | 成長例は合成。根拠の受理は確定ではない。外部実行には別の承認が必要。 |
| sw-pic | software / core | 確認 | e-percolation-inversion-compiler-readme-md, e-percolation-inversion-compiler-docs-resource-matched-measurement-md, e-percolation-inversion-compiler-license, e-percolation-inversion-compiler-pyproject-toml | ヒントは非実行。有限証明の受理は実行・真実・物理的成功を意味しない。 |
| sw-vek | software / core | 確認 | e-verification-ecology-kit-readme-md, e-verification-ecology-kit-docs-capacity-md, e-verification-ecology-kit-license, e-verification-ecology-kit-pyproject-toml | 実験的な局所容量プロファイルは最大12作業・行動、16スロット。合成・モデル計上のみ。観測・保証サービスはnull。 |
| sw-alt | software / core | 確認 | e-alt-foundry-kernel-readme-md, e-alt-foundry-kernel-docs-collective-reuse-md, e-alt-foundry-kernel-license, e-alt-foundry-kernel-pyproject-toml | 集団再利用プロファイルはAlpha。適格化は確定・実行権限を与えない。配布はGitHub Release資産でPyPIを仮定しない。 |
| sw-cait | software / core | 確認 | e-cait-certificate-schema-readme-md, e-cait-certificate-schema-docs-accounting-md, e-cait-certificate-schema-license, e-cait-certificate-schema-pyproject-toml | 実験的計上。コピーは新しい資産ではない。VEKの数値は提供値であり、欠けた元履歴から再構成していない。 |
| sw-cpcf | software / core | 確認 | e-collective-phase-control-fabric-readme-md, e-collective-phase-control-fabric-docs-epistemic-growth-control-md, e-collective-phase-control-fabric-license, e-collective-phase-control-fabric-pyproject-toml | Beta研究実装。有限モデルの例のみ。署名付き観測は因果モデルを認証しない。経験的加速実験はない。 |
| sw-oawm | software / supporting | 確認 | e-observable-agent-workflow-memory-readme-md, e-observable-agent-workflow-memory-docs-theory-mapping-md, e-observable-agent-workflow-memory-license, e-observable-agent-workflow-memory-pyproject-toml | 手続きの許容性は事実の真実性ではない。GitHubリリースは未確認。レビュー対象ソースの宣言は0.1.0 beta。別日時のパッケージ観測とは区別する。 |
| sw-oasg | software / supporting | 確認 | e-oasg-readme-md, e-oasg-docs-architecture-md, e-oasg-license, e-oasg-pyproject-toml | 参照実装・本番利用はAlpha。変更対象はモデル重みではなく方策。試行はホスト方針の下で局所コマンドを実行し得る。 |
| sw-audit | software / supporting | 確認 | e-audit-closed-ai-scientist-readme-md, e-audit-closed-ai-scientist-license, e-audit-closed-ai-scientist-pyproject-toml | ベンチマークは任意の実験室・エージェントを認証しない。実行は成果物を書き込む。ソフトはApache-2.0、同梱論文はCC BY 4.0。 |
| sw-loscr | software / supporting | 確認 | e-loscr-readme-md, e-loscr-docs-theory-map-md, e-loscr-license, e-loscr-pyproject-toml | 構造検査には外部の統計的前提が必要。doctorも局所状態を初期化し得る。 |
| sw-simulator | software / supporting | 確認 | e-asi-proxy-phase-growth-simulator-readme-md, e-asi-proxy-phase-growth-simulator-docs-model-reference-md, e-asi-proxy-phase-growth-simulator-license, e-asi-proxy-phase-growth-simulator-pyproject-toml | 世界予測・ASI到来日・確率は提供しない。合成パラメータは測定値ではない。 |
| sw-skill | software / supporting | 確認 | e-asi-proxy-phase-skill-readme-md, e-asi-proxy-phase-skill-license, e-asi-proxy-phase-skill-pyproject-toml | 助言用スキルであり稼働サービスではない。同梱コーパスは古いスナップショット。導入・実行はホストの権限に従う。 |
| sw-cmgl | software / supporting | 確認 | e-routing-cmgl-readme-md, e-routing-cmgl-docs-proof-obligations-md, e-routing-cmgl-license, e-routing-cmgl-pyproject-toml, e-routing-cmgl-docs-current-view-md, e-routing-cmgl-tests-test-compression-py | 手続き上の許容性のみ。事実の真実性、モデルの学習解除、バックエンドの完全消去、注入攻撃への免疫は保証しない。外部アダプタの運用はアプリ側が担う。 |
| sw-memoryflow | software / supporting | 確認 | e-routing-memoryflow-readme-md, e-routing-memoryflow-docs-conformance-profiles-md, e-routing-memoryflow-license, e-routing-memoryflow-pyproject-toml, e-routing-memoryflow-docs-event-schema-md, e-routing-memoryflow-tests-unit-test-verifier-profiles-py | 未記録のストア変更、捏造事象、情報源の真偽は判定できない。削除記録の監査は記憶やモデル重みの消去ではない。 |
| sw-pfg | software / supporting | 確認 | e-routing-pfg-readme-md, e-routing-pfg-docs-operations-md, e-routing-pfg-license, e-routing-pfg-pyproject-toml, e-routing-pfg-schemas-gate-request-schema-json, e-routing-pfg-tests-test-v1-1-hardening-py | 有限の監査整合性はOAuth基盤、外界の真実、物理的成果、厳密な一度限りの配信ではない。識別・永続化・実行監視・事故対応は運用側の責任。 |
| sw-fost | software / supporting | 確認 | e-routing-fost-readme-md, e-routing-fost-docs-json-contract-md, e-routing-fost-license, e-routing-fost-pyproject-toml, e-routing-fost-docs-limitations-md, e-routing-fost-tests-test-v20-strict-finality-py | 検査済み台帳は真実の判定器でも外界の成果でもない。構造移行は根拠を作らず、用途別のモードと鮮度方針が必要。 |
| sw-atrb | software / supporting | 確認 | e-routing-atrb-readme-md, e-routing-atrb-docs-v02-experiment-md, e-routing-atrb-license, e-routing-atrb-pyproject-toml, e-routing-atrb-docs-v02-results-md, e-routing-atrb-tests-test-v02-positive-controls-py | フィクスチャと検査器は同時に開発された。累積条件では因果効果を分離できず、互換用アダプタはPIC・FOST・PFG・CCRとの同等性を証明しない。実世界の安全性・一般化は主張しない。 |
| sw-oversight | software / supporting | 確認 | e-routing-oversight-readme-md, e-routing-oversight-experiment-manifest-yaml, e-routing-oversight-licence, e-routing-oversight-report-workflow-oversight-report-md, e-routing-oversight-src-oversight-poc-channels-py | 合成12課題、各実モデル1回の記録、スクリプトによる高費用レビューは、人間の承認疲労の実測でも本番適性の証明でもない。報告設定の比較優位は保守的に未確立。 |
| sw-checkedflow | software / supporting | 確認 | e-checkedflow-readme, e-checkedflow-package, e-checkedflow-license, e-checkedflow-notice, e-checkedflow-architecture, e-checkedflow-state-machine, e-checkedflow-audit, e-checkedflow-validation, e-checkedflow-conformance, e-checkedflow-security, e-checkedflow-research, e-checkedflow-interoperability, e-checkedflow-agent-request, e-checkedflow-gateway | 実験的な有限参照ランタイムで、上流の実証範囲は31入力。同一環境上の4ノードは実組織の独立性を確立しない。署名は外界の真実ではなく、転送資格情報は命令権限ではなく、合意順序は検証器の真実ではない。作業受領証やプロトコル上の課題完了は能力受理ではない。生成ソースは検証済みソースではなく、有限動作の検証は普遍的なプログラム正当性ではない。宣言作業単位は実測CPU時間ではなく、複製は新たな能力資本ではなく、結果不明は検査済み失敗ではない。A2A/MCP相互運用は新たな科学的根拠ではない。試験済み公開手順は本番適性を確立しない。一般的な因果的加速・AGI・ASIは導かれず、合意が進んでも検証者の拒否が再利用を阻止し得る。 |
| sw-cio | software / supporting | 確認 | e-cio-readme, e-cio-package, e-cio-license, e-cio-concepts, e-cio-reference, e-cio-architecture, e-cio-security, e-cio-tutorial, e-cio-handoff, e-cio-tests, e-cio-validation, e-cio-051-readme, e-cio-051-package, e-cio-051-reference, e-cio-051-release | 公開済みの安定化版0.5.1。上流検証は本索引による独立再現ではなく、旧0.5.0候補の記録は履歴として保持。上流報告は初回ネイティブ失敗の原因未確定を記録し、本番・高負荷動作は未測定。過去のPASS・ACCEPT・署名・完了受領証は現在の採用・実行権限・業務品質を確立しない。ストック差分には受信側・範囲・方針・対象集合が比較可能な観測が必要。複製や新しいハッシュは機能的新規性・因果的貢献・知能成長を確立しない。欠落した時計・費用は不明のままとし、予約は消費ではなく包含時間は合算しない。上流の試行はassay_not_readyでCIOの蓄積優位性は未確立。独立した実行再現・本番保証・他の掲載ソフトとの検証済み統合を主張しない。 |
| sw-egr | software / supporting | 確認 | e-egr-readme, e-egr-package, e-egr-version, e-egr-license, e-egr-completion, e-egr-api, e-egr-security, e-egr-migration, e-egr-models, e-egr-runner, e-egr-tests, e-egr-validation | Alpha段階の契約・制御実装であり、エージェント／モデルサービス・ネットワークゲートウェイ・スケジューラではない。有限カタログの完了後も外部の完全性は不明で、意味的真実や統計的独立性を保証しない。コールバックビューは隔離ではなく、スナップショットは認証済み履歴ではなく、有限ステップは実時間・CPU制限を強制しない。信頼・影響・資源測定・単一書込はホストの責任。未完呼出・不明な影響や費用は未完として保持し、自動再試行・返金・障害復旧・exactly-onceを保証しない。上流v0.2.4実験は否定的結果を報告し、v0.3.0は新規効果実験を行わず実証的有用性は未測定。独立実行・一般的加速・他の掲載プロジェクトとの検証済み統合を主張しない。 |
| paper-phase-engineering | paper / core | 確認 | e-paper-phase-engineering | 理論プレプリントであり、加速の実証や物理的相転移ではない。保証には宣言した有限契約、条件を揃えた完全軌跡、妥当な検証偏り・裾・ドリフト境界、固定保持目標、裏付けある資金が必要。監査ラベルは潜在的真実ではなく、条件付き平均成長は全軌跡の正成長ではない。選択対象は生成済み利用可能アーカイブで、未生成成果物の最適生成ではない。統計的被覆は事後確率や恒久的安全性ではない。ソフト統合の実装や普遍的AGI・ASIの主張は導かれない。 |

## 最新版・パッケージ観測（2026-10-17）

版の一致は配布物の同一性・互換性・性能を認定しない。404はその宣言名のPyPI endpointでの観測であり、他の配布方法の不存在を意味しない。

| ID | 宣言版 | GitHub release | PyPI | 観測commit |
|---|---|---|---|---|
| sw-ccr | 1.9.0 | v1.9.0 | 1.9.0 | `d6806b158ffb9ff76937c6c3eb3f9391a1fcf21a` |
| sw-pic | 1.1.0 | v1.1.0 | 1.1.0 | `b971bc6374325b9486c038546733d9b53745787c` |
| sw-vek | 1.3.0 | v1.3.0 | 1.3.0 | `c5a2f9ec85c8dbeaf058dd15eba6136634fbc8a3` |
| sw-alt | 0.5.0 | v0.5.0 | not_found | `2d8f2cf404cdd9f023e4f55beb6c5bd2e9ce674b` |
| sw-cait | 0.2.0 | v0.2.0 | 0.2.0 | `6b3fcc410c3fb43756e89b9127c5ed0191b3949d` |
| sw-cpcf | 1.0.1 | v1.0.1 | 1.0.1 | `340b4899d5b0892e06d7d2c1ab1f1d48df15e981` |
| sw-oawm | 0.2.0b0 | none observed | not_found | `dddaea42073fc9629122cdb798f547c5d6a116e9` |
| sw-oasg | 1.2.0 | v1.2.0 | 1.2.0 | `f3bee90f2ed8b2dba9b9a96ce485375295760036` |
| sw-audit | 0.2.0 | v0.2.0 | 0.2.0 | `1e844d1bca18d7bb298aa198e1250bb07bd7ea44` |
| sw-loscr | 0.1.0 | v0.1.0 | not_found | `a4c45677e9d9ba1c97b7cfd108efca88275cc6a5` |
| sw-simulator | 0.1.0 | v0.1.0 | 0.1.0 | `24690a225c86fde2a24de4d9f93e2a282789b67d` |
| sw-skill | 1.1.1 | v1.1.1 | not_found | `5706214a9a3d5e194f371f8ccc2eb71132f82270` |
| sw-cmgl | 1.1.2 | v1.1.2 | 1.1.2 | `8fcf99d512c4262c4cea0787e72993ff6eb3b059` |
| sw-memoryflow | 0.1.0 | v0.1.0 | not_found | `018a857bd3a1e87c3f33ac3d1a3047c8c4808ca6` |
| sw-pfg | 1.1.0 | v1.1.0 | 1.1.0 | `ed51d588afab6312287a31baa1d911c0fa3a943d` |
| sw-fost | 2.0.0 | v2.0.0 | 2.0.0 | `5fbdc2a9851b27c5529ed332dfcb9cbf07e027de` |
| sw-atrb | 0.2.0 | v0.2.0 | not_found | `a14475a0a57ac7e1dbcc5f3a5c7fd2078ea86da2` |
| sw-oversight | unknown | none observed | unknown | `a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b` |
| sw-checkedflow | 0.2.0 | v0.2.0 | 0.2.0 | `850f2d7b7799dbe000ea85a6e8f32b289b971bfd` |
| sw-cio | 0.5.1 | v0.5.1 | 0.5.1 | `46276b4080dadd70ffa2608533139e8df6dcf75d` |
| sw-egr | 0.3.0 | v0.3.0 | 0.3.0 | `0e5def78422de55db6c80723f28b753ef91e017b` |

PyPI14件観測、宣言名6件404、1件（Oversight）はpyproject取得404・識別名未確定。GitHub公開releaseは19件観測、OAWMとOversightは未観測。OAWMの旧0.1 betaの限界と現在の0.2.0b0を分離した。

## 問題・関係の英日対応

全28問題の質問、症状、入力、出力、前提、停止条件を照合。役割・群・未解決意図は既存境界を維持した。

| 問題ID | 英日確認 |
|---|---|
| completion-and-outcome | 確認（evidence-supportのみ上記訳語修正） |
| retry-recovery | 確認（evidence-supportのみ上記訳語修正） |
| production-reliability | 確認（evidence-supportのみ上記訳語修正） |
| adaptation | 確認（evidence-supportのみ上記訳語修正） |
| tool-routing | 確認（evidence-supportのみ上記訳語修正） |
| version-and-dependency-drift | 確認（evidence-supportのみ上記訳語修正） |
| interchange | 確認（evidence-supportのみ上記訳語修正） |
| distribution-shift | 確認（evidence-supportのみ上記訳語修正） |
| reuse | 確認（evidence-supportのみ上記訳語修正） |
| memory-governance | 確認（evidence-supportのみ上記訳語修正） |
| context-management | 確認（evidence-supportのみ上記訳語修正） |
| memory | 確認（evidence-supportのみ上記訳語修正） |
| authority | 確認（evidence-supportのみ上記訳語修正） |
| security-boundary | 確認（evidence-supportのみ上記訳語修正） |
| cost-and-capacity | 確認（evidence-supportのみ上記訳語修正） |
| verification-backlog | 確認（evidence-supportのみ上記訳語修正） |
| human-oversight | 確認（evidence-supportのみ上記訳語修正） |
| information | 確認（evidence-supportのみ上記訳語修正） |
| verification-funding | 確認（evidence-supportのみ上記訳語修正） |
| evaluation-integrity | 確認（evidence-supportのみ上記訳語修正） |
| evidence-support | 確認（evidence-supportのみ上記訳語修正） |
| obligations | 確認（evidence-supportのみ上記訳語修正） |
| adaptive-research | 確認（evidence-supportのみ上記訳語修正） |
| forecast | 確認（evidence-supportのみ上記訳語修正） |
| coordinate | 確認（evidence-supportのみ上記訳語修正） |
| accounting | 確認（evidence-supportのみ上記訳語修正） |
| incident-response | 確認（evidence-supportのみ上記訳語修正） |
| rsi-evidence | 確認（evidence-supportのみ上記訳語修正） |

| 関係ID | 保持した状態 | 根拠 |
|---|---|---|
| basis-sw-ccr | documented / source_inspected | e-collective-capability-runtime-readme-md |
| basis-sw-pic | documented / source_inspected | e-percolation-inversion-compiler-readme-md |
| basis-sw-vek | documented / source_inspected | e-verification-ecology-kit-readme-md |
| basis-sw-alt | documented / source_inspected | e-alt-foundry-kernel-readme-md |
| basis-sw-cait | documented / source_inspected | e-cait-certificate-schema-readme-md |
| basis-sw-cpcf | documented / source_inspected | e-collective-phase-control-fabric-readme-md, e-collective-phase-control-fabric-docs-growth-research-mapping-md |
| basis-sw-oawm | documented / source_inspected | e-observable-agent-workflow-memory-readme-md, e-observable-agent-workflow-memory-docs-theory-sources-md |
| basis-sw-audit | documented / source_inspected | e-audit-closed-ai-scientist-readme-md |
| basis-sw-loscr | documented / source_inspected | e-loscr-readme-md |
| alt-to-ccr | tested_upstream / upstream_reported | e-alt-foundry-kernel-docs-reuse-interchange-md, e-alt-release, e-alt-native-test |
| alt-from-vek | tested_upstream / upstream_reported | e-alt-foundry-kernel-docs-reuse-interchange-md, e-alt-release, e-alt-native-test |
| alt-to-vek | tested_upstream / upstream_reported | e-alt-foundry-kernel-docs-reuse-interchange-md, e-alt-release, e-alt-native-test |
| alt-to-cait | tested_upstream / upstream_reported | e-alt-foundry-kernel-docs-reuse-interchange-md, e-alt-release, e-alt-native-test |
| vek-to-ccr | documented / source_inspected | e-verification-ecology-kit-docs-capacity-interchange-md |
| cait-from-vek | documented / source_inspected | e-cait-certificate-schema-docs-interchange-md |
| ccr-from-alt-legacy | documented / source_inspected | e-collective-capability-runtime-docs-verified-growth-interchange-md |
| ccr-from-pic | documented / source_inspected | e-collective-capability-runtime-interop-pic-md |
| cpcf-to-ccr | proposed / editorial | e-collective-phase-control-fabric-docs-adapters-md |
| alt-to-oawm | proposed / editorial | e-observable-agent-workflow-memory-docs-theory-sources-md, e-alt-foundry-kernel-docs-reuse-interchange-md |
| cpcf-consequence | documented / editorial | e-paper-consequence, e-collective-phase-control-fabric-readme-md, e-collective-phase-control-fabric-docs-epistemic-growth-control-md |

ALTのnative CCR/VEK/CAIT確認は上流公開検証記録の範囲に限定し、この監査による実行とはしていない。CIOのIntel Python 3.13未説明失敗・高負荷未計測、EGRの0 new LLM callsと既存負の結果を保持した。Phase Engineeringのモデル・条件付き結果は経験的加速としない。CGTのconcept DOIと版日付の相違は既存identity issueのまま明示する。

## 検証と独立した観点の最終レビュー

基準39テスト成功。修正後43テスト成功・失敗0・skip0。追加4件は不一致/欠落revision、MIME、HEAD fallback、選定refreshと別日付保持の回帰検証。日本語出力の修正は凍結された旧27経路テストで明示的な例外として検証し、テスト内コピーのみ旧訳に戻して従来ハッシュを照合する。

実行: `generate_agent_catalogs.py --offline`、`generate_paper_pages.py`、`validate_paper_pages.py`（230論文ページ・4 software records）、`generate_collective_intelligence_index.py`、同 `--check`、`validate_collective_intelligence_index.py`、`audit_collective_intelligence_coverage.py --check`、`python -m unittest discover -s tests -v`、`git diff --check`。スキーマ・digest・英日HTML/Markdown/JSON-LD対応・582ローカルリンクを検証。同入力で2回生成しバイト一致を確認する。必要依存は既存環境にあり、掲載OSSは導入していない。

英日ページを通常desktop幅・390pxで描画確認し、長いcommitを含む折返しと横方向にはみ出さない状態を確認。日本語detailsはEnterで開閉可能。言語切替先とダウンロードは静的リンクとして検証。JavaScript無効化および実ブラウザ200%拡大は利用中の操作APIで設定できず未実施。静的HTMLに全内容が存在する検査は、これらの描画実測の代用とはしない。

別観点の最終レビュー: 変更差分を「誤同定・主張昇格・未来の公開を先取り・実行権限の混入・旧根拠の破壊」の観点で再読。科学的レビューを自動更新せず、入力集合と旧証拠の一致を別途assertした。監査時点の重大な未解決不整合は検出していない。これは別人による独立レビューではない。

## 固定版と公開状態

この編集スナップショットのregistry content_digest: `0e1684e67d87df9e15482612977087e7376e57f83517738fc0da271d9d96c061`。自動catalog更新は観測時刻を更新するため、公開後のdigestはリリース記録を参照。自己参照を避け、以下のハッシュに監査文書自身を含めない。

| ファイル | SHA-256（UTF-8 / LF） |
|---|---|
| collective-intelligence-index.json | `d790f7b4c0c617e17a4072f8f3355505ec2cb564c26422f57a6efb87121ada81` |
| collective-intelligence-index.html | `62364344d90691369c5dcfe49cc36488349871c556487e7b43899c65d3e07f4a` |
| collective-intelligence-index.ja.html | `83e739476341f906fbb6d4ce1f22dbe5ed97315520e5954f8302a4a11defa206` |
| collective-intelligence-index.md | `d1b1c9aa2f91f8c8dbf89208fcf302d059742420072d58f88aacfbf263c8c658` |
| collective-intelligence-index.ja.md | `9238676f5e38fb9f288aefad1524ff6d4408991856ed79c9696b946a3a7cf5e8` |
| schemas/collective-intelligence-index.schema.json | `5c1a1d1a91a76bc4b9ad2becde5215c3d30cee5923b7bfb3aab2ce301b716168` |
| data/collective-intelligence-coverage-seeds.json | `b0507cd2b3ba8434b250a1d5ac2412bad8b2021e0e817852375f48424c26fdac` |

本記録作成時: ローカル検証済み、commit/PR・merge・Pages公開・公開後照合は未完了。後続の実際の最終SHA、Pages deployment SHA、HTTP/UTF-8/MIME/バイト一致、PR作成可否をリリース説明および最終応答に記録する。未公開のHEADと公開mainを比較して配信障害とは判定しない。

固定取得・再生成は[保守文書](collective-intelligence-index-maintenance.md)の実SHA checkout手順に従う。索引はURL・編集日・resource ID・digest/commitを、原著はDOI・個別版・箇所を引用する。ソフトウェアは固定commitと確認範囲を伴う。既存の著者・DOI・ライセンス（OSS Apache-2.0とサイトCC BY 4.0の対象範囲）を混同しない。外部資料の永続保存、互換性、研究の真実性、実運用の効果、将来の採用・検索掲載は保証しない。
