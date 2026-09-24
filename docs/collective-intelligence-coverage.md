# Collective Intelligence routing coverage / 経路カバレッジ

Offline, deterministic lexical acceptance diagnostic for the supplied A–O seed families.
語句の到達性を測る保守診断。検索順位・検索意図全般の精度・クローラー採用・科学的妥当性の証拠ではない。

An exact declared alias can lead to a bounded diagnostic route, not necessarily an implementation of the searched feature. Read each route’s unsupported and stop conditions.
一致は限定的な診断経路への入口であり、検索された機能の実装を保証しない。未対応条件・停止条件を参照。

Baseline registry: `c6abad1f1f23229d3744fb3a4448bce1e72c5826`; baseline matching was casefold/trim over legacy queries and IDs only.
Baseline values are frozen measured observations, not a second operational routing table.

| Family | Seeds per language | Baseline EN / JA | Current EN / JA | Unresolved EN / JA |
|---|---:|---:|---:|---:|
| A | 15 | 0 / 0 | 15 / 15 | 0 / 0 |
| B | 15 | 0 / 0 | 15 / 15 | 0 / 0 |
| C | 9 | 0 / 0 | 9 / 9 | 0 / 0 |
| D | 10 | 0 / 0 | 10 / 10 | 0 / 0 |
| E | 12 | 0 / 0 | 10 / 10 | 2 / 2 |
| F | 11 | 0 / 0 | 8 / 8 | 3 / 3 |
| G | 14 | 0 / 0 | 14 / 14 | 0 / 0 |
| H | 8 | 0 / 0 | 8 / 8 | 0 / 0 |
| I | 11 | 0 / 0 | 11 / 11 | 0 / 0 |
| J | 13 | 0 / 0 | 13 / 13 | 0 / 0 |
| K | 9 | 0 / 0 | 9 / 9 | 0 / 0 |
| L | 10 | 0 / 0 | 10 / 10 | 0 / 0 |
| M | 8 | 0 / 0 | 8 / 8 | 0 / 0 |
| N | 14 | 0 / 0 | 14 / 14 | 0 / 0 |
| O | 9 | 0 / 0 | 9 / 9 | 0 / 0 |

## All seed queries / 全シード

| ID | EN | JA | EN route | JA route | Expected result |
|---|---|---|---|---|---|
| a-01 | AI agent says "done" but task is not finished | AIエージェントが完了と言うのに実際には終わっていない | completion-and-outcome | completion-and-outcome | PASS |
| a-02 | false completion | 完了の誤報告 | completion-and-outcome | completion-and-outcome | PASS |
| a-03 | tool receipt vs actual outcome | ツールの受領証と実際の成果の違い | completion-and-outcome | completion-and-outcome | PASS |
| a-04 | postcondition verification | 実行後の完了条件を確認したい | completion-and-outcome | completion-and-outcome | PASS |
| a-05 | agent keeps retrying | エージェントが再試行を続ける | retry-recovery | retry-recovery | PASS |
| a-06 | agent stuck in a loop | エージェントがループから抜けない | retry-recovery | retry-recovery | PASS |
| a-07 | repeated tool calls | 同じツール呼び出しを繰り返す | retry-recovery | retry-recovery | PASS |
| a-08 | agent never terminates | エージェントがいつまでも終了しない | retry-recovery | retry-recovery | PASS |
| a-09 | partial failure | 処理が途中だけ失敗した | retry-recovery | retry-recovery | PASS |
| a-10 | crash recovery | クラッシュ後に処理を復旧したい | retry-recovery | retry-recovery | PASS |
| a-11 | duplicate side effects | 外部への操作が二重に実行された | retry-recovery | retry-recovery | PASS |
| a-12 | idempotency | 再試行の冪等性を確認したい | retry-recovery | retry-recovery | PASS |
| a-13 | replay vs rerun | 履歴の再生と処理の再実行は違うのか | retry-recovery | retry-recovery | PASS |
| a-14 | uncertain external outcome | 外部で操作が成功したかわからない | retry-recovery | retry-recovery | PASS |
| a-15 | reconciliation | 外部の実行結果と台帳を照合したい | retry-recovery | retry-recovery | PASS |
| b-01 | AI agent works in demo but fails in production | デモでは動くのに本番で失敗する | production-reliability | production-reliability | PASS |
| b-02 | AI agent reliability | AIエージェントの信頼性を評価したい | production-reliability | production-reliability | PASS |
| b-03 | AI agent success rate | エージェントの成功率をどう測るか | production-reliability | production-reliability | PASS |
| b-04 | agent SLO / SLA | エージェントのSLOやSLAを設定したい | production-reliability | production-reliability | PASS |
| b-05 | error budget | 失敗を許容する予算を決めたい | production-reliability | production-reliability | PASS |
| b-06 | repeated-run consistency | 繰り返し実行すると結果が安定しない | production-reliability | production-reliability | PASS |
| b-07 | pass^k | 連続試行の成功指標pass^kを評価したい | production-reliability | production-reliability | PASS |
| b-08 | flaky AI agent | エージェントが時々失敗する | production-reliability | production-reliability | PASS |
| b-09 | fault tolerance | エージェントの障害耐性を確認したい | production-reliability | production-reliability | PASS |
| b-10 | rate limits / 429 | 429制限でエージェントが再試行する | retry-recovery | retry-recovery | PASS |
| b-11 | retry storms | 再試行が集中して負荷が増える | retry-recovery | retry-recovery | PASS |
| b-12 | queue backlog | 検証キューがたまっている | verification-backlog | verification-backlog | PASS |
| b-13 | verification bottleneck | 検証がボトルネックになっている | verification-backlog | verification-backlog | PASS |
| b-14 | graceful degradation | 障害時に機能を段階的に制限したい | production-reliability | production-reliability | PASS |
| b-15 | production readiness | エージェントを本番投入してよいか | production-reliability | production-reliability | PASS |
| c-01 | AI agent chooses wrong tool | エージェントが間違ったツールを選ぶ | tool-routing | tool-routing | PASS |
| c-02 | AI agent cannot find a tool | エージェントが必要なツールを見つけられない | tool-routing | tool-routing | PASS |
| c-03 | too many MCP tools | MCPツールが多すぎる | tool-routing | tool-routing | PASS |
| c-04 | MCP tool overload | MCPツールの説明で文脈が埋まる | tool-routing | tool-routing | PASS |
| c-05 | tool search / tool routing | ツールの検索と振り分けを見直したい | tool-routing | tool-routing | PASS |
| c-06 | function calling with many tools | 多数のツールでfunction callingを使いたい | tool-routing | tool-routing | PASS |
| c-07 | tool selected correctly but wrong arguments | ツールは合っているが引数が間違う | tool-routing | tool-routing | PASS |
| c-08 | tool metadata ambiguity | ツールの説明が曖昧で選べない | tool-routing | tool-routing | PASS |
| c-09 | tool discoverability vs permission | ツールの発見と使用許可を区別したい | authority | authority | PASS |
| d-01 | tool schema changed | ツールのスキーマが変更された | version-and-dependency-drift | version-and-dependency-drift | PASS |
| d-02 | function-calling schema changed | 関数呼出しのスキーマ変更で壊れた | version-and-dependency-drift | version-and-dependency-drift | PASS |
| d-03 | MCP tool stopped working after update | 更新後にMCPツールが動かなくなった | version-and-dependency-drift | version-and-dependency-drift | PASS |
| d-04 | API update broke agent | API更新後にエージェントが壊れた | version-and-dependency-drift | version-and-dependency-drift | PASS |
| d-05 | stale tool definition | 古いツール定義を使っている | version-and-dependency-drift | version-and-dependency-drift | PASS |
| d-06 | JSON Schema compatibility | JSON Schemaの互換性を再確認したい | version-and-dependency-drift | version-and-dependency-drift | PASS |
| d-07 | backward compatibility | 後方互換性の根拠を確認したい | version-and-dependency-drift | version-and-dependency-drift | PASS |
| d-08 | semantic drift | 同じ形式でも意味が変わった | version-and-dependency-drift | version-and-dependency-drift | PASS |
| d-09 | stored workflow still uses old API | 保存した手続きが古いAPIを使う | version-and-dependency-drift | version-and-dependency-drift | PASS |
| d-10 | revalidation after dependency/tool version change | 依存やツールの更新後に再検証したい | version-and-dependency-drift | version-and-dependency-drift | PASS |
| e-01 | AI agent acting with wrong permissions | エージェントが誤った権限で動く | authority | authority | PASS |
| e-02 | agent acting as admin | エージェントが管理者として動いている | authority | authority | PASS |
| e-03 | service account too privileged | サービスアカウントの権限が強すぎる | authority | authority | PASS |
| e-04 | agent acting on behalf of user | エージェントが利用者を代理して操作する | authority | authority | PASS |
| e-05 | delegated authorization | 委任された権限の範囲を確認したい | authority | authority | PASS |
| e-06 | OAuth for agents | エージェント向けOAuthの実装方法 | UNRESOLVED | UNRESOLVED | PASS |
| e-07 | confused deputy | 代理実行で権限が混同される | authority | authority | PASS |
| e-08 | MCP token passthrough | MCPのトークンパススルー対策 | UNRESOLVED | UNRESOLVED | PASS |
| e-09 | subagent credential inheritance | 子エージェントに資格情報を継承してよいか | authority | authority | PASS |
| e-10 | capable vs authorized | 実行できることと許可されることは違う | authority | authority | PASS |
| e-11 | approval vs authority | 承認と権限の違いを確認したい | authority | authority | PASS |
| e-12 | tool discovered vs tool permitted | 見つけたツールを使ってよいとは限らない | authority | authority | PASS |
| f-01 | prompt injection through tools / RAG / MCP | ツールやRAGやMCP経由のプロンプト注入 | security-boundary | security-boundary | PASS |
| f-02 | malicious MCP server | 悪意あるMCPサーバからの入力を隔離したい | security-boundary | security-boundary | PASS |
| f-03 | MCP supply-chain attack | MCPの供給網攻撃の信頼境界を確認したい | security-boundary | security-boundary | PASS |
| f-04 | tool poisoning | ツールの説明に不正な指示が混入した | security-boundary | security-boundary | PASS |
| f-05 | dependency update broke agent | 依存関係の更新でエージェントが壊れた | version-and-dependency-drift | version-and-dependency-drift | PASS |
| f-06 | transitive dependency drift | 間接依存の変更で挙動が変わった | version-and-dependency-drift | version-and-dependency-drift | PASS |
| f-07 | package hallucination | 存在しないパッケージ名をAIが提案した | UNRESOLVED | UNRESOLVED | PASS |
| f-08 | slopsquatting | 生成されたパッケージ名の先取り攻撃を検出したい | UNRESOLVED | UNRESOLVED | PASS |
| f-09 | AI coding agent installed wrong package | AIが間違ったパッケージをインストールした | UNRESOLVED | UNRESOLVED | PASS |
| f-10 | dependency provenance | 依存パッケージの来歴と信頼範囲を確認したい | security-boundary | security-boundary | PASS |
| f-11 | compromised evaluator / trusted base | 評価器や信頼基盤が侵害された | evaluation-integrity | evaluation-integrity | PASS |
| g-01 | stale agent memory | エージェントが古い記憶を使い続ける | memory-governance | memory-governance | PASS |
| g-02 | deleted memory still used | 削除した記憶をまた使ってしまう | memory-governance | memory-governance | PASS |
| g-03 | agent remembers deleted data | エージェントが消したデータを思い出す | memory-governance | memory-governance | PASS |
| g-04 | how to make an AI agent forget | AIエージェントに情報を忘れさせたい | memory-governance | memory-governance | PASS |
| g-05 | memory deletion | エージェントの記憶を削除したい | memory-governance | memory-governance | PASS |
| g-06 | tombstone | 記憶の廃止印を検索に反映したい | memory-governance | memory-governance | PASS |
| g-07 | memory correction | 記憶の誤りを修正したい | memory-governance | memory-governance | PASS |
| g-08 | superseded memory | 置き換え済みの記憶が使われる | memory-governance | memory-governance | PASS |
| g-09 | memory expiry | 記憶の有効期限を管理したい | memory-governance | memory-governance | PASS |
| g-10 | derived summary still contains deleted information | 派生した要約に削除済み情報が残っている | memory-governance | memory-governance | PASS |
| g-11 | cache resurrects deleted information | キャッシュから消した情報が復活する | memory-governance | memory-governance | PASS |
| g-12 | dependency withdrawal invalidates workflow memory | 依存の撤回で保存手続きが無効になった | memory | memory | PASS |
| g-13 | procedural memory revalidation | 手続き記憶を再検証したい | memory | memory | PASS |
| g-14 | RAG deletion vs model unlearning | RAGからの削除とモデルの学習解除の違い | memory-governance | memory-governance | PASS |
| h-01 | long conversation makes agent worse | 会話が長くなるとエージェントの判断が悪化する | context-management | context-management | PASS |
| h-02 | context window overload | コンテキスト窓がいっぱいになる | context-management | context-management | PASS |
| h-03 | tool output overload | ツール出力が多すぎる | context-management | context-management | PASS |
| h-04 | context compression | 根拠を残して文脈を圧縮したい | context-management | context-management | PASS |
| h-05 | summarization loses evidence | 要約すると根拠が失われる | context-management | context-management | PASS |
| h-06 | agent forgets earlier instruction | 前に伝えた指示をエージェントが忘れる | context-management | context-management | PASS |
| h-07 | context grows too large | 文脈が大きくなりすぎる | context-management | context-management | PASS |
| h-08 | evidence-preserving compression | 証拠を保持したまま圧縮したい | context-management | context-management | PASS |
| i-01 | AI agent too expensive | AIエージェントの費用が高すぎる | cost-and-capacity | cost-and-capacity | PASS |
| i-02 | token usage too high | トークン使用量が多すぎる | cost-and-capacity | cost-and-capacity | PASS |
| i-03 | agent burns tokens | エージェントがトークンを浪費する | cost-and-capacity | cost-and-capacity | PASS |
| i-04 | multi-agent cost explosion | 複数エージェントで費用が急増する | cost-and-capacity | cost-and-capacity | PASS |
| i-05 | subagent duplication | 子エージェントが同じ作業をしている | coordinate | coordinate | PASS |
| i-06 | retry amplification | 再試行が連鎖して費用が膨らむ | retry-recovery | retry-recovery | PASS |
| i-07 | verification cost | 検証にかかる費用を測りたい | cost-and-capacity | cost-and-capacity | PASS |
| i-08 | LLM agent budget | LLMエージェントの予算を管理したい | cost-and-capacity | cost-and-capacity | PASS |
| i-09 | cost attribution by task/agent/tool | 課題やエージェントやツール別に費用を把握したい | cost-and-capacity | cost-and-capacity | PASS |
| i-10 | cheaper model but higher total workflow cost | 安いモデルにしたのに作業全体の費用が増えた | cost-and-capacity | cost-and-capacity | PASS |
| i-11 | tokens vs money vs human review time | トークンと金額と人間のレビュー時間を分けたい | cost-and-capacity | cost-and-capacity | PASS |
| j-01 | benchmark improved but production got worse | ベンチマークは改善したのに本番性能が悪化した | evaluation-integrity | evaluation-integrity | PASS |
| j-02 | Goodhart's law | 指標を最適化したら目的から外れた | evaluation-integrity | evaluation-integrity | PASS |
| j-03 | reward hacking | 報酬ハッキングを疑っている | evaluation-integrity | evaluation-integrity | PASS |
| j-04 | agent cheating tests | エージェントがテストをすり抜ける | evaluation-integrity | evaluation-integrity | PASS |
| j-05 | evaluator tampering | 評価器を改変してスコアを上げている | evaluation-integrity | evaluation-integrity | PASS |
| j-06 | LLM judge bias | LLM評価器の偏りを確認したい | evaluation-integrity | evaluation-integrity | PASS |
| j-07 | benchmark contamination | ベンチマークの汚染を疑っている | evaluation-integrity | evaluation-integrity | PASS |
| j-08 | search-time contamination | 探索中に評価用情報が混入した | evaluation-integrity | evaluation-integrity | PASS |
| j-09 | evaluation overfitting | 評価に過適合している | evaluation-integrity | evaluation-integrity | PASS |
| j-10 | optional stopping | 有利な時点で検定を打ち切ってよいか | adaptive-research | adaptive-research | PASS |
| j-11 | hypothesis shopping | 都合のよい仮説を選び続けている | adaptive-research | adaptive-research | PASS |
| j-12 | test oracle problem | テストの正解判定自体が信用できない | evaluation-integrity | evaluation-integrity | PASS |
| j-13 | synthetic evaluation vs real-world evidence | 合成評価と実世界の根拠を区別したい | evaluation-integrity | evaluation-integrity | PASS |
| k-01 | skill worked before but fails on new task | 以前使えたスキルが新しい課題では失敗する | distribution-shift | distribution-shift | PASS |
| k-02 | negative transfer | 再利用した知識が逆効果になる | distribution-shift | distribution-shift | PASS |
| k-03 | distribution shift | 課題の分布が変わった | distribution-shift | distribution-shift | PASS |
| k-04 | reuse vs solve from scratch | 再利用と一から解く方法を比較したい | distribution-shift | distribution-shift | PASS |
| k-05 | receiver mismatch | スキルと受け手の条件が合わない | distribution-shift | distribution-shift | PASS |
| k-06 | workflow valid for one context but not another | ある文脈で有効な手続きが別の文脈では使えない | distribution-shift | distribution-shift | PASS |
| k-07 | external validity | 検証結果を別の環境へ適用してよいか | distribution-shift | distribution-shift | PASS |
| k-08 | copied artifact vs new capability | 成果物のコピーと新しい能力を区別したい | accounting | accounting | PASS |
| k-09 | qualified reuse | 条件を満たした再利用か確認したい | reuse | reuse | PASS |
| l-01 | more agents make system slower | エージェントを増やすと遅くなる | coordinate | coordinate | PASS |
| l-02 | agents overwrite each other's changes | エージェント同士が変更を上書きする | coordinate | coordinate | PASS |
| l-03 | Git / merge conflict between coding agents | コーディングエージェント間でGitのマージが競合する | coordinate | coordinate | PASS |
| l-04 | duplicate work | 複数エージェントの作業が重複する | coordinate | coordinate | PASS |
| l-05 | correlated errors | エージェント同士が同じ間違いをする | coordinate | coordinate | PASS |
| l-06 | multi-agent agreement without evidence | 根拠なしにエージェントが同意している | coordinate | coordinate | PASS |
| l-07 | credit assignment | エージェントの貢献を割り当てたい | accounting | accounting | PASS |
| l-08 | which agent contributed | どのエージェントが貢献したのか | accounting | accounting | PASS |
| l-09 | work leasing | エージェントの作業をリースで管理したい | coordinate | coordinate | PASS |
| l-10 | disagreement preservation | エージェントの意見の相違を消さずに保持したい | coordinate | coordinate | PASS |
| m-01 | too many approval requests | 承認依頼が多すぎる | human-oversight | human-oversight | PASS |
| m-02 | human-in-the-loop bottleneck | 人間の確認待ちがボトルネックになる | human-oversight | human-oversight | PASS |
| m-03 | approval fatigue | 承認疲れで確認が雑になる | human-oversight | human-oversight | PASS |
| m-04 | automation bias | 自動化された判断を信じすぎてしまう | human-oversight | human-oversight | PASS |
| m-05 | when should agent escalate | どの時点で人間へ引き継ぐべきか | human-oversight | human-oversight | PASS |
| m-06 | selective human review | 必要な案件だけ人間がレビューしたい | human-oversight | human-oversight | PASS |
| m-07 | human review capacity | 人間のレビュー容量を見積もりたい | human-oversight | human-oversight | PASS |
| m-08 | approval is not verification | 承認したことと検証したことを区別したい | human-oversight | human-oversight | PASS |
| n-01 | how to stop an AI agent | AIエージェントを停止したい | incident-response | incident-response | PASS |
| n-02 | AI agent kill switch | エージェントの緊急停止を設計したい | incident-response | incident-response | PASS |
| n-03 | rogue agent | 暴走したエージェントを封じ込めたい | incident-response | incident-response | PASS |
| n-04 | agent keeps acting after stop | 停止後もエージェントが操作を続ける | incident-response | incident-response | PASS |
| n-05 | rollback agent action | エージェントの操作を巻き戻したい | incident-response | incident-response | PASS |
| n-06 | circuit breaker | 危険な呼出しを遮断したい | incident-response | incident-response | PASS |
| n-07 | disable dangerous tool | 危険なツールを無効にしたい | incident-response | incident-response | PASS |
| n-08 | revoke agent credentials | エージェントの資格情報を失効させたい | incident-response | incident-response | PASS |
| n-09 | child agent still running | 子エージェントがまだ動いている | incident-response | incident-response | PASS |
| n-10 | compensation vs rollback | 補償処理と巻戻しの違いを確認したい | incident-response | incident-response | PASS |
| n-11 | uncertain side effect | 副作用が起きたかわからない | incident-response | incident-response | PASS |
| n-12 | post-incident reconciliation | 事故後に実行状態を照合したい | incident-response | incident-response | PASS |
| n-13 | quarantine compromised memory/workflow | 汚染された記憶や手続きを隔離したい | incident-response | incident-response | PASS |
| n-14 | restart criteria after incident | 事故後の再開条件を決めたい | incident-response | incident-response | PASS |
| o-01 | AI citation does not support claim | AIの引用が主張の根拠になっていない | evidence-support | evidence-support | PASS |
| o-02 | fake / weak citation support | 引用が捏造または根拠として弱い | evidence-support | evidence-support | PASS |
| o-03 | claim-to-evidence mapping | 主張と根拠の対応を確認したい | evidence-support | evidence-support | PASS |
| o-04 | evidence provenance | 根拠の来歴をたどりたい | evidence-support | evidence-support | PASS |
| o-05 | signed record does not prove truth | 署名済み記録でも真実とは限らない | evidence-support | evidence-support | PASS |
| o-06 | generated != verified | 生成されたことは検証済みを意味しない | obligations | obligations | PASS |
| o-07 | verified != reusable | 検証済みでも再利用できるとは限らない | reuse | reuse | PASS |
| o-08 | unknown must remain unknown | 不明なものを不明のまま残したい | obligations | obligations | PASS |
| o-09 | adaptive AI research validity | 適応的AI研究の妥当性を確認したい | adaptive-research | adaptive-research | PASS |

## Explicit gaps / 未解決

- e-06: OAuth for agents / エージェント向けOAuthの実装方法
  No source-reviewed implementation of this specific identity protocol or package-name security mechanism. Consult the relevant host/provider documentation. この識別プロトコルまたはパッケージ名の防御機構について、ソース確認済みの実装はない。該当ホスト・提供者の資料を参照。
- e-08: MCP token passthrough / MCPのトークンパススルー対策
  No source-reviewed implementation of this specific identity protocol or package-name security mechanism. Consult the relevant host/provider documentation. この識別プロトコルまたはパッケージ名の防御機構について、ソース確認済みの実装はない。該当ホスト・提供者の資料を参照。
- f-07: package hallucination / 存在しないパッケージ名をAIが提案した
  No source-reviewed implementation of this specific identity protocol or package-name security mechanism. Consult the relevant host/provider documentation. この識別プロトコルまたはパッケージ名の防御機構について、ソース確認済みの実装はない。該当ホスト・提供者の資料を参照。
- f-08: slopsquatting / 生成されたパッケージ名の先取り攻撃を検出したい
  No source-reviewed implementation of this specific identity protocol or package-name security mechanism. Consult the relevant host/provider documentation. この識別プロトコルまたはパッケージ名の防御機構について、ソース確認済みの実装はない。該当ホスト・提供者の資料を参照。
- f-09: AI coding agent installed wrong package / AIが間違ったパッケージをインストールした
  No source-reviewed implementation of this specific identity protocol or package-name security mechanism. Consult the relevant host/provider documentation. この識別プロトコルまたはパッケージ名の防御機構について、ソース確認済みの実装はない。該当ホスト・提供者の資料を参照。

## Interpretation / 解釈

The original 12 routes covered research concepts such as verification, reuse and accounting, but these practical seed phrases were not exact aliases. The expanded 27 routes retain those IDs and add practical questions in eight groups. This is an explicit curated vocabulary, not open-ended natural-language understanding.
旧12経路は検証・再利用・計上などを扱っていたが、この実務シード群の表現は一致語として登録されていなかった。既存IDを保持し、8群・27経路へ拡張した。自由文全般の理解ではなく、明示的に選定した語彙である。

Tool search, incident containment and security routes expose evidence/host obligations, not a new MCP search service, universal kill switch, OAuth implementation, attack immunity or production guarantee.
ツール探索・事故封じ込め・安全性の経路は根拠とホストの義務を示す。MCP検索サービス、万能停止装置、OAuth実装、攻撃耐性保証、本番保証を新設したものではない。

## Additional source review / 追加ソースレビュー

Source inspection only; no indexed software was installed or executed. These six supporting resources add bounded evidence, not tested interoperability. No papers or bibliography identities were added.
ソース確認のみ。対象OSSの導入・実行は行っていない。6件は補助資料として追加し、検証済み相互運用を主張しない。論文・書誌IDの追加はない。

### certified-memory-governance-layer

- Revision: [2fc49b4df7bbe4a23265b8b2372432711740d00b](https://github.com/kadubon/certified-memory-governance-layer/tree/2fc49b4df7bbe4a23265b8b2372432711740d00b)
- Declared source version: 1.1.2; license: Apache-2.0; inspected: 2026-09-24
- Selected because: Gate memory writes and retrieval using current versions, authority receipts, tombstones and contamination lanes. 記憶の書込み・検索結果を、現行版・権限受領証・廃止履歴・汚染区分で制御する。
- Limits: Procedural admissibility only; no factual truth, model unlearning, backend deletion guarantee or prompt-injection immunity. Optional adapters remain application-owned. 手続き上の許容性のみ。事実の真実性、モデルの学習解除、バックエンドの完全消去、注入攻撃への免疫は保証しない。外部アダプタの運用はアプリ側が担う。

### memoryflow-agent-memory-auditor

- Revision: [c8ee3f4c81f5303535ba2d2e9882c409f05e641e](https://github.com/kadubon/memoryflow-agent-memory-auditor/tree/c8ee3f4c81f5303535ba2d2e9882c409f05e641e)
- Declared source version: 0.1.0; license: Apache-2.0; inspected: 2026-09-24
- Selected because: Audit declared memory telemetry for stale, deleted or superseded use, correction latency and non-comparable metrics. 宣言された記憶テレメトリから、古い・削除済み・置換済み記憶の使用、修正遅延、比較不能な指標を監査する。
- Limits: Cannot observe silent backend changes, fabricated events or source truth. Auditing deletion telemetry does not erase memory or model weights. 未記録のストア変更、捏造事象、情報源の真偽は判定できない。削除記録の監査は記憶やモデル重みの消去ではない。

### problem-frame-gate

- Revision: [9449b338c4c8b959878704a48b2f16e291e2dfb8](https://github.com/kadubon/problem-frame-gate/tree/9449b338c4c8b959878704a48b2f16e291e2dfb8)
- Declared source version: 1.1.0; license: Apache-2.0; inspected: 2026-09-24
- Selected because: Check finite action authority and atomically commit a five-row gate bundle before a separately controlled outbox dispatcher. 有限の行為権限を検査し、別管理の送信処理に先立ち5行のゲート束を原子的に記録する。
- Limits: Finite audit consistency is not OAuth infrastructure, external truth, physical outcome or exactly-once delivery. Deployment owns identities, durable storage, actuator monitoring and incident response. 有限の監査整合性はOAuth基盤、外界の真実、物理的成果、厳密な一度限りの配信ではない。識別・永続化・実行監視・事故対応は運用側の責任。

### fost-agent-ledger

- Revision: [e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa](https://github.com/kadubon/fost-agent-ledger/tree/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa)
- Declared source version: 2.0.0; license: Apache-2.0; inspected: 2026-09-24
- Selected because: Separate claimed completion from finite support, checked finality, unresolved obligations and environment changes. 完了の自己申告を、有限の支持根拠・検査済み最終性・未解決義務・環境変更から区別する。
- Limits: A checked ledger is not a truth oracle or external outcome. Structural migration cannot invent evidence; project-specific modes and freshness policies remain necessary. 検査済み台帳は真実の判定器でも外界の成果でもない。構造移行は根拠を作らず、用途別のモードと鮮度方針が必要。

### agent-trust-residual-benchmark

- Revision: [eb21fda8ed7bfad9dc33becf2ffcc63285249495](https://github.com/kadubon/agent-trust-residual-benchmark/tree/eb21fda8ed7bfad9dc33becf2ffcc63285249495)
- Declared source version: 0.2.0; license: Apache-2.0; inspected: 2026-09-24
- Selected because: Inspect positive/negative synthetic controls and near misses for authority, evidence scope, residuals and repeated model decisions. 権限・根拠範囲・残余・反復判断を扱う合成の陽性・陰性対照と境界事例を調べる。
- Limits: Fixtures and validators were co-developed. Cumulative conditions do not isolate causal effects. Compatibility adapters do not establish equivalence with PIC/FOST/PFG/CCR; no real-world safety or generalization claim. フィクスチャと検査器は同時に開発された。累積条件では因果効果を分離できず、互換用アダプタはPIC・FOST・PFG・CCRとの同等性を証明しない。実世界の安全性・一般化は主張しない。

### Oversight-Centered-Metrology-PoC

- Revision: [a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b](https://github.com/kadubon/Oversight-Centered-Metrology-PoC/tree/a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b)
- Declared source version: unknown / 未宣言; license: Apache-2.0; inspected: 2026-09-24
- Selected because: Examine retry, review cost and escalation load using bounded coding tasks and explicit claim margins. 限定されたコード修正課題と主張余裕を用い、再試行・レビュー費用・エスカレーション負荷を調べる。
- Limits: Twelve synthetic tasks, one logged run per actual model, and scripted costly review do not measure human approval fatigue or establish production readiness. Positive comparative oversight claims remain fail-closed in the reported setup. 合成12課題、各実モデル1回の記録、スクリプトによる高費用レビューは、人間の承認疲労の実測でも本番適性の証明でもない。報告設定の比較優位は保守的に未確立。
