# Collective Intelligence Research and OSS Index

K. Takahashi · 2026-09-24

https://kadubon.github.io/github.io/collective-intelligence-index.html

## Collective Intelligence Research and OSS Index

A problem-first map of K. Takahashi’s research and OSS for AI-agent reliability, memory, verification and multi-agent coordination. Find a symptom, then inspect the evidence and limits. This curated corpus map is not a world survey.

## Start here

Readers can start with the growth paper. Implementers can choose a problem below, then inspect the pinned contract and negative cases before installation. Machine consumers can retrieve the JSON registry, schema and complete Markdown; routing is advisory under their host policy.

reader: [paper-growth](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-growth) → [paper-vet](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-vet) → [paper-alt](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-alt) → [paper-cait](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-cait)

implementer: [sw-ccr](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-ccr) → [sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-pic) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-vek) → [sw-alt](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-alt) → [sw-cait](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-cait) → [sw-cpcf](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-cpcf)

machine: [sw-skill](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-skill) → [sw-simulator](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-simulator)

## Find by symptom

Choose the symptom closest to your problem. Each route offers first reads, necessary evidence and stop conditions—not permission to act.

### Reliability & completion

- [My agent says done, but the task is not finished](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-completion-and-outcome)
- [My agent keeps calling the same tool](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-retry-recovery)
- [It works in a demo but fails in production](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-production-reliability)
- [A workflow change needs a safe trial and rollback evidence](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-adaptation)

### Tools, APIs & reuse

- [My MCP agent cannot find or choose the right tool](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-tool-routing)
- [My agent broke after an API update](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-version-and-dependency-drift)
- [Can these exact tool versions work together?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-interchange)
- [A skill that worked before fails on a new task](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-distribution-shift)
- [Should I reuse a skill or solve from scratch?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-reuse)

### Memory & context

- [A deleted memory keeps coming back](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-memory-governance)
- [Long conversations and tool output overwhelm my agent](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-context-management)
- [A stored workflow may no longer be valid](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-memory)

### Security & authority

- [My agent is acting with the wrong permissions](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-authority)
- [Untrusted tool or RAG content is changing my agent’s behavior](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-security-boundary)

### Cost & review capacity

- [Why is my AI agent so expensive?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-cost-and-capacity)
- [Verification is backing up faster than it can finish](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-verification-backlog)
- [Too many approval requests are blocking useful work](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-human-oversight)
- [Which check is worth doing before investing more?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-information)
- [Who pays for verification and unresolved risk?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-verification-funding)

### Evaluation & evidence

- [Benchmark scores improved but production got worse](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-evaluation-integrity)
- [The citation does not support the agent’s claim](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-evidence-support)
- [Generated output still has unchecked obligations](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-obligations)
- [Repeated hypothesis tests may overstate the evidence](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-adaptive-research)
- [Can these results predict when ASI will arrive?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-forecast)

### Multi-agent coordination

- [More agents create duplicate work or overwrite each other](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-coordinate)
- [Did copied artifacts actually add capability?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-accounting)

### Incident response

- [I need to stop, contain and recover an agent incident](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-incident-response)

### Specific intents not yet supported

- OAuth for agents — No source-reviewed implementation of this specific identity protocol or package-name security mechanism. Consult the relevant host/provider documentation.
- MCP token passthrough — No source-reviewed implementation of this specific identity protocol or package-name security mechanism. Consult the relevant host/provider documentation.
- package hallucination — No source-reviewed implementation of this specific identity protocol or package-name security mechanism. Consult the relevant host/provider documentation.
- slopsquatting — No source-reviewed implementation of this specific identity protocol or package-name security mechanism. Consult the relevant host/provider documentation.
- AI coding agent installed wrong package — No source-reviewed implementation of this specific identity protocol or package-name security mechanism. Consult the relevant host/provider documentation.

## Definitions and non-claims

Collective intelligence concerns what interaction contributes under a declared task and comparison protocol. Collective capability growth concerns net changes in checked, reusable task and research capacity. Operational self-acceleration is the stronger claim that existing capability contributes to faster future formation under matched resources, quality, time and external inputs. These are separate propositions. Phase normally denotes a proposed protocol-relative regime here; the Gibbs-model paper states its own narrower mathematical premises.

## Find a route by problem



### My agent says done, but the task is not finished (completion-and-outcome)

[sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-pic) → [sw-fost](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-fost) → [paper-operational-claims](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-operational-claims)

Required inputs: Declared postconditions, claimed completion, receipts and independent observations.

Expected outputs: Separate reported, checked and externally observed completion; keep open obligations.

Conditions: A receipt or checked ledger cannot establish an unobserved external outcome.

Stop / handoff: If the postcondition cannot be observed, retain unknown and hand off before reporting done.

Other common phrasings:

- AI agent says "done" but task is not finished
- false completion
- tool receipt vs actual outcome
- postcondition verification
- why does my AI agent say done when it isn't finished?

Related problems: [My agent keeps calling the same tool](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-retry-recovery) · [Generated output still has unchecked obligations](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-obligations) · [The citation does not support the agent’s claim](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-evidence-support)

### My agent keeps calling the same tool (retry-recovery)

[sw-pfg](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-pfg) → [sw-ccr](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-ccr) → [sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-pic)

Required inputs: Attempt IDs, lease/dispatch records, retry budget, idempotency contract and external receipts.

Expected outputs: Distinguish replay of evidence from rerunning an action; expose unfinished or uncertain effects.

Conditions: No universal termination proof, retry scheduler or exactly-once side-effect guarantee. Provider backoff and deduplication remain host obligations.

Stop / handoff: Stop blind retries after an uncertain effect or exhausted budget; reconcile with the actuator owner.

Other common phrasings:

- agent keeps retrying
- agent stuck in a loop
- repeated tool calls
- agent never terminates
- partial failure
- crash recovery
- duplicate side effects
- idempotency
- replay vs rerun
- uncertain external outcome
- reconciliation
- rate limits / 429
- retry storms
- retry amplification
- agent keeps retrying the same MCP tool

Related problems: [My agent says done, but the task is not finished](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-completion-and-outcome) · [Why is my AI agent so expensive?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-cost-and-capacity) · [I need to stop, contain and recover an agent incident](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-incident-response)

### It works in a demo but fails in production (production-reliability)

[sw-loscr](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-loscr) → [paper-loscr](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-loscr) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-vek)

Required inputs: Repeated-run workload, versioned environment, failures, service windows and matched resource limits.

Expected outputs: Scope service claims to supported observations, degradation and unresolved capacity.

Conditions: Release presence, one success or synthetic capacity is not an SLO/SLA guarantee. This route supplies no pass^k estimator or provider 429 handler.

Stop / handoff: With missing denominators, independence, drift checks or error budgets, withhold readiness and escalate to service owners.

Other common phrasings:

- AI agent works in demo but fails in production
- AI agent reliability
- AI agent success rate
- agent SLO / SLA
- error budget
- repeated-run consistency
- pass^k
- flaky AI agent
- fault tolerance
- graceful degradation
- production readiness

Related problems: [Benchmark scores improved but production got worse](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-evaluation-integrity) · [My agent broke after an API update](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-version-and-dependency-drift) · [Verification is backing up faster than it can finish](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-verification-backlog)

### How can local workflow policy change under protected limits? (adaptation)

[sw-oasg](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-oasg) → [paper-conversion](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-conversion)

Recognize this problem: A workflow change needs a safe trial and rollback evidence

Required inputs: Ledger prefixes, candidate policy, trial workload and rollback evidence.

Expected outputs: Shadow/lease trial result and gated promotion or rejection.

Conditions: Advisory route under host policy. Protected regression, incomplete receipts or host execution authority missing.

Stop / handoff: Protected regression, incomplete receipts or host execution authority missing.

Related problems: [It works in a demo but fails in production](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-production-reliability) · [My agent broke after an API update](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-version-and-dependency-drift) · [I need to stop, contain and recover an agent incident](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-incident-response)

### My MCP agent cannot find or choose the right tool (tool-routing)

[sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-pic) → [sw-pfg](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-pfg)

Required inputs: Task, candidate tool descriptions, input schemas, effects, evidence and required authority.

Expected outputs: A bounded inspection of input obligations and authorization before a host selects a tool.

Conditions: Diagnostic entry only: no MCP search engine, tool-ranking algorithm or large-tool-set performance evidence. Discoverability does not imply permission.

Stop / handoff: Ambiguous descriptions or arguments require clarification and host-side schema checks; never infer permission from a match.

Other common phrasings:

- AI agent chooses wrong tool
- AI agent cannot find a tool
- too many MCP tools
- MCP tool overload
- tool search / tool routing
- function calling with many tools
- tool selected correctly but wrong arguments
- tool metadata ambiguity

Related problems: [My agent is acting with the wrong permissions](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-authority) · [My agent broke after an API update](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-version-and-dependency-drift) · [Can these exact tool versions work together?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-interchange)

### My agent broke after an API update (version-and-dependency-drift)

[sw-oawm](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-oawm) → [sw-fost](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-fost) → [sw-loscr](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-loscr)

Required inputs: Old/new versions, schemas, dependency digests, stored workflow contracts and replay evidence.

Expected outputs: Invalidate affected assumptions and require renewed checks for the changed environment.

Conditions: A JSON shape match or structural migration does not prove semantic/backward compatibility. No universal dependency vulnerability scanner.

Stop / handoff: Quarantine stale workflows when version bindings or required revalidation are missing.

Other common phrasings:

- tool schema changed
- function-calling schema changed
- MCP tool stopped working after update
- API update broke agent
- stale tool definition
- JSON Schema compatibility
- backward compatibility
- semantic drift
- stored workflow still uses old API
- revalidation after dependency/tool version change
- dependency update broke agent
- transitive dependency drift
- agent broke after model update

Further relevant resources: [paper-cgt](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-cgt)

Related problems: [A stored workflow may no longer be valid](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-memory) · [My MCP agent cannot find or choose the right tool](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-tool-routing) · [It works in a demo but fails in production](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-production-reliability)

### Which integration has actually been checked at these versions? (interchange)

[sw-alt](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-alt) → [sw-ccr](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-ccr) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-vek)

Recognize this problem: Can these exact tool versions work together?

Required inputs: Exact producer/consumer versions, fixture schema hashes, scope and host admission rules.

Expected outputs: Version-scoped mappings plus explicit missing custom sidecar admission.

Conditions: Advisory route under host policy. No custom host admission; newer versions; unsupported lifecycle or transitive compatibility inference.

Stop / handoff: No custom host admission; newer versions; unsupported lifecycle or transitive compatibility inference.

Further relevant resources: [sw-cait](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-cait)

Related problems: [My agent broke after an API update](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-version-and-dependency-drift) · [My MCP agent cannot find or choose the right tool](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-tool-routing) · [My agent is acting with the wrong permissions](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-authority)

### A skill that worked before fails on a new task (distribution-shift)

[sw-alt](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-alt) → [paper-alt](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-alt) → [sw-oawm](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-oawm)

Required inputs: Named receiver/task/context, dependency versions, transfer checks and matched scratch baseline.

Expected outputs: Receiver-qualified reuse with rejected/unknown transfers and maintenance costs retained.

Conditions: No general distribution-shift detector or external-validity guarantee; previous verification is not transport evidence.

Stop / handoff: On receiver mismatch, requalify or solve from scratch; do not treat copied artifacts as new capability.

Other common phrasings:

- skill worked before but fails on new task
- negative transfer
- distribution shift
- reuse vs solve from scratch
- receiver mismatch
- workflow valid for one context but not another
- external validity

Related problems: [Should I reuse a skill or solve from scratch?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-reuse) · [A stored workflow may no longer be valid](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-memory) · [My agent broke after an API update](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-version-and-dependency-drift)

### When does reuse beat solving a task again? (reuse)

[paper-alt](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-alt) → [sw-alt](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-alt) → [paper-pcs](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-pcs)

Recognize this problem: Should I reuse a skill or solve from scratch?

Required inputs: Named receiver/task, matched scratch baseline and all formation/transfer/check/maintenance costs.

Expected outputs: Qualified receiver options, exact typed costs and bounded comparison.

Conditions: Advisory route under host policy. Receiver mismatch, missing cost, expiry or unsupported lifecycle mapping.

Stop / handoff: Receiver mismatch, missing cost, expiry or unsupported lifecycle mapping.

Other common phrasings:

- qualified reuse
- verified != reusable

Related problems: [A skill that worked before fails on a new task](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-distribution-shift) · [Did copied artifacts actually add capability?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-accounting) · [A stored workflow may no longer be valid](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-memory)

### A deleted memory keeps coming back (memory-governance)

[sw-cmgl](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-cmgl) → [sw-memoryflow](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-memoryflow) → [sw-oawm](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-oawm)

Required inputs: Memory/update IDs, source lineage, tombstones, expiry, authority and read/use telemetry.

Expected outputs: Admit current supported memory; block invalidated versions and audit stale/deleted use.

Conditions: A retrieval tombstone is not physical erasure or model unlearning. Derived summaries/caches need lineage and their own invalidation; silent store changes are invisible.

Stop / handoff: Missing version bindings or deletion lineage requires blocking reuse and backend reconciliation.

Other common phrasings:

- stale agent memory
- deleted memory still used
- agent remembers deleted data
- how to make an AI agent forget
- memory deletion
- tombstone
- memory correction
- superseded memory
- memory expiry
- derived summary still contains deleted information
- cache resurrects deleted information
- RAG deletion vs model unlearning

Related problems: [A stored workflow may no longer be valid](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-memory) · [Long conversations and tool output overwhelm my agent](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-context-management) · [My agent broke after an API update](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-version-and-dependency-drift)

### Long conversations and tool output overwhelm my agent (context-management)

[sw-cmgl](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-cmgl) → [paper-split-inference](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-split-inference) → [paper-sqot](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-sqot)

Required inputs: Source evidence, context limits, compression lineage, recoverability checks and attention budget.

Expected outputs: Keep source links and unresolved obligations when forming smaller context or summaries.

Conditions: No general context compressor or guarantee of instruction retention. A summary is not certified fact; a model context advantage is not observed performance.

Stop / handoff: If evidence or instruction provenance is lost, retrieve the original and recheck instead of promoting the summary.

Other common phrasings:

- long conversation makes agent worse
- context window overload
- tool output overload
- context compression
- summarization loses evidence
- agent forgets earlier instruction
- context grows too large
- evidence-preserving compression

Related problems: [A deleted memory keeps coming back](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-memory-governance) · [Why is my AI agent so expensive?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-cost-and-capacity) · [More agents create duplicate work or overwrite each other](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-coordinate)

### How can a procedure remain reusable after failure or withdrawal? (memory)

[sw-oawm](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-oawm) → [paper-workflow-library](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-workflow-library) → [paper-continuity](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-continuity)

Recognize this problem: A stored workflow may no longer be valid

Required inputs: Observable events, checker receipts, workflow contract and explicit promotion.

Expected outputs: Version-bound admissibility with contradictions and tombstones retained.

Conditions: Advisory route under host policy. Missing promotion receipt; a factual truth or automatic ALT promotion request.

Stop / handoff: Missing promotion receipt; a factual truth or automatic ALT promotion request.

Other common phrasings:

- dependency withdrawal invalidates workflow memory
- procedural memory revalidation

Related problems: [A deleted memory keeps coming back](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-memory-governance) · [My agent broke after an API update](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-version-and-dependency-drift) · [A skill that worked before fails on a new task](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-distribution-shift)

### My agent is acting with the wrong permissions (authority)

[sw-pfg](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-pfg) → [sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-pic) → [sw-ccr](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-ccr)

Required inputs: Actor, delegated scope, issuer, expiry, action target and protected-operation manifest.

Expected outputs: Separate capability, approval, authority and action evidence under an explicit host policy.

Conditions: No OAuth provider, token exchange protocol or automatic credential inheritance. A local accepted gate cannot grant external or legal authority.

Stop / handoff: Deny or hand off if actor, scope, expiry or delegation cannot be established; discovery is not permission.

Other common phrasings:

- tool discoverability vs permission
- AI agent acting with wrong permissions
- agent acting as admin
- service account too privileged
- agent acting on behalf of user
- delegated authorization
- confused deputy
- subagent credential inheritance
- capable vs authorized
- approval vs authority
- tool discovered vs tool permitted

Related problems: [My MCP agent cannot find or choose the right tool](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-tool-routing) · [Untrusted tool or RAG content is changing my agent’s behavior](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-security-boundary) · [I need to stop, contain and recover an agent incident](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-incident-response)

### Untrusted tool or RAG content is changing my agent’s behavior (security-boundary)

[sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-pic) → [sw-atrb](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-atrb) → [sw-cmgl](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-cmgl)

Required inputs: Untrusted inputs, origin and dependency records, authority boundary and evaluator trust assumptions.

Expected outputs: Keep candidate content separate from authority and record residual contamination/evaluator risks.

Conditions: No prompt-injection immunity, malware scanner, MCP server attestation or supply-chain certification. Synthetic fixtures are not adversarial deployment validation.

Stop / handoff: Quarantine affected evidence or memory and hand off to host security owners if the trusted base is compromised.

Other common phrasings:

- prompt injection through tools / RAG / MCP
- malicious MCP server
- MCP supply-chain attack
- tool poisoning
- dependency provenance

Related problems: [My agent is acting with the wrong permissions](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-authority) · [I need to stop, contain and recover an agent incident](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-incident-response) · [Benchmark scores improved but production got worse](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-evaluation-integrity)

### Why is my AI agent so expensive? (cost-and-capacity)

[sw-cait](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-cait) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-vek) → [paper-bit](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-bit)

Required inputs: Per-task/agent/tool event costs, retries, tokens, money, review time and shared capacity in declared units.

Expected outputs: Separate typed costs and resource bottlenecks before comparing a cheaper model or more agents.

Conditions: No automatic billing integration, token-to-money conversion or guaranteed savings. Missing telemetry remains unknown; model capacity is not measured service.

Stop / handoff: Stop or reallocate when budgets or verification capacity are exhausted; do not collapse incompatible units.

Other common phrasings:

- AI agent too expensive
- token usage too high
- agent burns tokens
- multi-agent cost explosion
- verification cost
- LLM agent budget
- cost attribution by task/agent/tool
- cheaper model but higher total workflow cost
- tokens vs money vs human review time
- why is my agent using so many tokens?

Related problems: [My agent keeps calling the same tool](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-retry-recovery) · [Verification is backing up faster than it can finish](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-verification-backlog) · [Long conversations and tool output overwhelm my agent](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-context-management)

### What should change when verification becomes the bottleneck? (verification-backlog)

[paper-vet](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-vet) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-vek) → [paper-sqot](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-sqot)

Recognize this problem: Verification is backing up faster than it can finish

Required inputs: Checks, integer slots, registered service eligibility and typed budgets.

Expected outputs: Finite schedule, backlog, repair and unfinished-work report.

Conditions: Advisory route under host policy. Observed service requested from synthetic local profile, unsupported preemption, or finite bounds exceeded.

Stop / handoff: Observed service requested from synthetic local profile, unsupported preemption, or finite bounds exceeded.

Other common phrasings:

- queue backlog
- verification bottleneck

Further relevant resources: [paper-verification-limited](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-verification-limited)

Related problems: [Why is my AI agent so expensive?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-cost-and-capacity) · [Too many approval requests are blocking useful work](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-human-oversight) · [It works in a demo but fails in production](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-production-reliability)

### Too many approval requests are blocking useful work (human-oversight)

[sw-oversight](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-oversight) → [paper-sqot](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-sqot) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-vek)

Required inputs: Review capacity, interrupt costs, risk scope, escalation rules and detection evidence.

Expected outputs: Compare workflow-level review load with explicit claim margins and remaining obligations.

Conditions: Scripted costly review is not a human-subject study of fatigue or automation bias. Approval does not verify truth; no universal escalation threshold.

Stop / handoff: Escalate unresolved high-impact obligations; if reviewers are unavailable, retain uncertainty rather than invent approval.

Other common phrasings:

- too many approval requests
- human-in-the-loop bottleneck
- approval fatigue
- automation bias
- when should agent escalate
- selective human review
- human review capacity
- approval is not verification

Related problems: [My agent is acting with the wrong permissions](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-authority) · [Verification is backing up faster than it can finish](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-verification-backlog) · [Why is my AI agent so expensive?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-cost-and-capacity)

### Which observations could change the next investment decision? (information)

[paper-growth](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-growth) → [sw-cpcf](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-cpcf) → [paper-consequence](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-consequence)

Recognize this problem: Which check is worth doing before investing more?

Required inputs: Finite coupled models, observation kernels, costs and funded continuation.

Expected outputs: Observation-based policy and conditional information-use comparison.

Conditions: Advisory route under host policy. Impossible observation, exhausted search budget or real-world acceleration claim.

Stop / handoff: Impossible observation, exhausted search budget or real-world acceleration claim.

Related problems: [Why is my AI agent so expensive?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-cost-and-capacity) · [Verification is backing up faster than it can finish](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-verification-backlog) · [Who pays for verification and unresolved risk?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-verification-funding)

### Who funds verification and carries residual risk? (verification-funding)

[paper-conversion](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-conversion) → [paper-bit](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-bit) → [sw-vek](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-vek)

Recognize this problem: Who pays for verification and unresolved risk?

Required inputs: Declared payer, authority, resource ownership and accountability arrangement.

Expected outputs: Contextual funding questions and typed costs, not a generated market.

Conditions: Advisory route under host policy. Missing institutional agreement; a package cannot assign legal authority or liability.

Stop / handoff: Missing institutional agreement; a package cannot assign legal authority or liability.

Related problems: [Too many approval requests are blocking useful work](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-human-oversight) · [Why is my AI agent so expensive?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-cost-and-capacity) · [My agent is acting with the wrong permissions](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-authority)

### Benchmark scores improved but production got worse (evaluation-integrity)

[sw-loscr](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-loscr) → [sw-atrb](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-atrb) → [sw-audit](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-audit)

Required inputs: Held-out cases, evaluator/version provenance, adaptation history, failures and deployment comparison protocol.

Expected outputs: Distinguish fixture conformance, observed benchmark results and externally valid claims.

Conditions: No universal contamination detector, unbiased LLM judge or solution to the test-oracle problem. Shared fixture development and repeated peeking limit inference.

Stop / handoff: With evaluator tampering, leaked tests or undeclared selection, quarantine the strong claim and obtain independent evidence.

Other common phrasings:

- compromised evaluator / trusted base
- benchmark improved but production got worse
- Goodhart's law
- reward hacking
- agent cheating tests
- evaluator tampering
- LLM judge bias
- benchmark contamination
- search-time contamination
- evaluation overfitting
- test oracle problem
- synthetic evaluation vs real-world evidence

Related problems: [Repeated hypothesis tests may overstate the evidence](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-adaptive-research) · [It works in a demo but fails in production](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-production-reliability) · [The citation does not support the agent’s claim](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-evidence-support)

### The citation does not support the agent’s claim (evidence-support)

[sw-fost](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-fost) → [sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-pic) → [paper-operational-claims](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-operational-claims)

Required inputs: Specific claim, original source, scope, time, provenance and missing-support records.

Expected outputs: Claim-to-support obligations with explicit unavailable evidence and bounded finality.

Conditions: No automatic factual truth or entailment oracle. A signature/hash binds a record, not its truth; generated is not verified and verified is not reusable.

Stop / handoff: If source support cannot be established, narrow or withhold the claim and retain unknowns; timeout is not checked negative.

Other common phrasings:

- AI citation does not support claim
- fake / weak citation support
- claim-to-evidence mapping
- evidence provenance
- signed record does not prove truth

Related problems: [Generated output still has unchecked obligations](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-obligations) · [My agent says done, but the task is not finished](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-completion-and-outcome) · [Benchmark scores improved but production got worse](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-evaluation-integrity)

### What remains to be checked before an output is reusable? (obligations)

[sw-pic](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-pic) → [paper-ecpt](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-ecpt) → [paper-operational-claims](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-operational-claims)

Recognize this problem: Generated output still has unchecked obligations

Required inputs: Output, declared schema, evidence and known/unknown measurements.

Expected outputs: Residual-preserving packet and bounded next checks.

Conditions: Advisory route under host policy. Missing source evidence or requested execution outside authority.

Stop / handoff: Missing source evidence or requested execution outside authority.

Other common phrasings:

- generated != verified
- unknown must remain unknown

Related problems: [My agent says done, but the task is not finished](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-completion-and-outcome) · [The citation does not support the agent’s claim](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-evidence-support) · [Should I reuse a skill or solve from scratch?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-reuse)

### How should adaptive research preserve valid evidence? (adaptive-research)

[paper-audit-closed](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-audit-closed) → [sw-audit](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-audit) → [sw-loscr](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-loscr)

Recognize this problem: Repeated hypothesis tests may overstate the evidence

Required inputs: Preregistered protocol, sampling/observation assumptions, seed and alpha budget.

Expected outputs: Declared benchmark evidence and supported claim level.

Conditions: Advisory route under host policy. Undeclared adaptation, unmodeled laboratory or request for universal certification.

Stop / handoff: Undeclared adaptation, unmodeled laboratory or request for universal certification.

Other common phrasings:

- optional stopping
- hypothesis shopping
- adaptive AI research validity

Related problems: [Benchmark scores improved but production got worse](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-evaluation-integrity) · [The citation does not support the agent’s claim](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-evidence-support) · [Which check is worth doing before investing more?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-information)

### Can this index forecast an ASI arrival date? (forecast)

[sw-simulator](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-simulator) → [sw-skill](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-skill)

Recognize this problem: Can these results predict when ASI will arrive?

Required inputs: A clearly labeled conditional scenario, if scenario analysis is desired.

Expected outputs: Unsupported forecast; only conditional sensitivity analysis is offered.

Conditions: Advisory route under host policy. Stop date/probability prediction: no empirical ASI arrival model is established.

Stop / handoff: Stop date/probability prediction: no empirical ASI arrival model is established.

Related problems: [Did copied artifacts actually add capability?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-accounting) · [It works in a demo but fails in production](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-production-reliability) · [Benchmark scores improved but production got worse](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-evaluation-integrity)

### How should multiple agents divide work and preserve disagreements? (coordinate)

[sw-ccr](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-ccr) → [paper-split-inference](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-split-inference) → [paper-collective-phase](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-collective-phase)

Recognize this problem: More agents create duplicate work or overwrite each other

Required inputs: Mission scope, independent proposals, leases, common budget.

Expected outputs: Leased work and unresolved disagreements with traceable evidence.

Conditions: Advisory route under host policy. No authority to dispatch; missing independent verification or expired lease.

Stop / handoff: No authority to dispatch; missing independent verification or expired lease.

Other common phrasings:

- subagent duplication
- more agents make system slower
- agents overwrite each other's changes
- Git / merge conflict between coding agents
- duplicate work
- correlated errors
- multi-agent agreement without evidence
- work leasing
- disagreement preservation

Related problems: [Why is my AI agent so expensive?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-cost-and-capacity) · [My agent is acting with the wrong permissions](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-authority) · [Benchmark scores improved but production got worse](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-evaluation-integrity)

### Did the system accumulate capability, or just copy artifacts? (accounting)

[paper-cait](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-cait) → [sw-cait](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-cait) → [paper-growth](https://kadubon.github.io/github.io/collective-intelligence-index.html#paper-growth)

Recognize this problem: Did copied artifacts actually add capability?

Required inputs: Unique source history, origins, lifecycle events, typed costs and stock/service units.

Expected outputs: Separate unique stock, service, external input and unresolved attribution.

Conditions: Advisory route under host policy. Missing original journal, valuation witness, compatible units or causal design.

Stop / handoff: Missing original journal, valuation witness, compatible units or causal design.

Other common phrasings:

- copied artifact vs new capability
- credit assignment
- which agent contributed

Related problems: [Should I reuse a skill or solve from scratch?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-reuse) · [Why is my AI agent so expensive?](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-cost-and-capacity) · [More agents create duplicate work or overwrite each other](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-coordinate)

### I need to stop, contain and recover an agent incident (incident-response)

[sw-pfg](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-pfg) → [sw-ccr](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-ccr) → [sw-cmgl](https://kadubon.github.io/github.io/collective-intelligence-index.html#sw-cmgl)

Required inputs: Action/child-task inventory, dispatch history, credentials, affected memory and independent recovery evidence.

Expected outputs: A host-owned containment checklist: stop new dispatch, retain unknown effects, quarantine and reconcile before restart.

Conditions: No global kill switch, automatic credential revocation or rollback of arbitrary external actions. Compensation is another action, not erasure of history.

Stop / handoff: Escalate to the host/actuator owner; do not restart until child work, authority and unresolved effects are reconciled.

Other common phrasings:

- how to stop an AI agent
- AI agent kill switch
- rogue agent
- agent keeps acting after stop
- rollback agent action
- circuit breaker
- disable dangerous tool
- revoke agent credentials
- child agent still running
- compensation vs rollback
- uncertain side effect
- post-incident reconciliation
- quarantine compromised memory/workflow
- restart criteria after incident

Related problems: [My agent is acting with the wrong permissions](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-authority) · [My agent keeps calling the same tool](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-retry-recovery) · [A deleted memory keeps coming back](https://kadubon.github.io/github.io/collective-intelligence-index.html#problem-memory-governance)

## Core software



### collective-capability-runtime (sw-ccr)

Coordinate leased tasks, independent workcells, disagreements and verification-aware growth accounting.

Primary editorial role: collective-coordination

Limits / unsupported uses: Synthetic growth examples; accepted evidence is not settlement. Dispatch requires separate approval.

Source reviewed: 2026-09-21

Source revision / declared version: 3b4702454f732c7a0a9f30d87483384dc8a281eb / 1.8.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v1.8.0 · 2026-09-12T23:16:29Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: https://kadubon.github.io/collective-capability-runtime/schemas/task.schema.json · Inspected schema identity only; runtime and semantic admission remain separate.

Inputs: Tasks, evidence, mission scope, resource envelope and approval bindings.

Outputs: Task/lease state, packets, residuals and candidate growth reports.

Prerequisites: &gt;=3.10; explicit scope and host authority.

Effects and trust boundary: Inspection commands are documented separately. Installation changes the environment; runtime writes and remote dispatch require command-specific review.

First inspection: Read pinned README, contract and license; compare checkout and release; inspect schema and negative tests before installation.

Installation guidance: Follow the pinned README and observed release assets; no installation was performed for this website.

Source-inspected interface (not executed): ccr agent explain --json — Inspect public interface; not executed by this index review. Ref: 3b4702454f732c7a0a9f30d87483384dc8a281eb; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/collective-capability-runtime)
- [Pinned interface schema](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/schemas/task.schema.json)
- [Observed release](https://github.com/kadubon/collective-capability-runtime/releases/tag/v1.8.0)
- [collective_capability_runtime-1.8.0-py3-none-any.whl](https://github.com/kadubon/collective-capability-runtime/releases/download/v1.8.0/collective_capability_runtime-1.8.0-py3-none-any.whl)
- [collective_capability_runtime-1.8.0.tar.gz](https://github.com/kadubon/collective-capability-runtime/releases/download/v1.8.0/collective_capability_runtime-1.8.0.tar.gz)
- [SHA256SUMS](https://github.com/kadubon/collective-capability-runtime/releases/download/v1.8.0/SHA256SUMS)
- [Agent entry: agent-manifest.json](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/agent-manifest.json)
- [Agent entry: SKILL.md](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/.agents/skills/collective-capability-runtime/SKILL.md)
- [e-collective-capability-runtime-readme-md](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/README.md)
- [Pinned contract](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/docs/verified-growth.md)
- [Apache-2.0 license](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/LICENSE)
- [e-collective-capability-runtime-pyproject-toml](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/pyproject.toml)

### percolation-inversion-compiler (sw-pic)

Compile finite agent outputs into checked packets and preserve unknown output obligations.

Primary editorial role: evidence-and-verification

Limits / unsupported uses: Hints are inert; finite certificate acceptance is not execution, truth or physical success.

Source reviewed: 2026-09-21

Source revision / declared version: 55cd5f219d02f02927e247317156e757b1d5d6da / 1.1.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v1.1.0 · 2026-07-11T07:05:56Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: null — upstream schema has no $id · Inspected schema identity only; runtime and semantic admission remain separate.

Inputs: Finite JSON inputs, declared frame, evidence and verifier witnesses.

Outputs: Typed reports, residual ledger, verifier tasks and candidate routes.

Prerequisites: &gt;=3.11; explicit scope and host authority.

Effects and trust boundary: Inspection commands are documented separately. Installation changes the environment; runtime writes and remote dispatch require command-specific review.

First inspection: Read pinned README, contract and license; compare checkout and release; inspect schema and negative tests before installation.

Installation guidance: Follow the pinned README and observed release assets; no installation was performed for this website.

Source-inspected interface (not executed): pic agent check --compact — Inspect public interface; not executed by this index review. Ref: 55cd5f219d02f02927e247317156e757b1d5d6da; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

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

Record verifier packets and allocate finite verification work with explicit shared resources.

Primary editorial role: verification-capacity

Limits / unsupported uses: Experimental local capacity profile: at most 12 work/actions and 16 slots; synthetic/model accounting only. Observed and guaranteed service remain null.

Source reviewed: 2026-09-21

Source revision / declared version: 4008e311ceb16edd6e74d9f71341a90120c0d046 / 1.3.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v1.3.0 · 2026-09-12T23:26:21Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: https://verification-ecology-kit.org/schemas/capacity-report.schema.json · Inspected schema identity only; runtime and semantic admission remain separate.

Inputs: Registered checks, service eligibility, integer slots, typed budgets and residuals.

Outputs: Schedules, independent checks, capacity reports and unfinished-work accounting.

Prerequisites: &gt;=3.11; explicit scope and host authority.

Effects and trust boundary: Inspection commands are documented separately. Installation changes the environment; runtime writes and remote dispatch require command-specific review.

First inspection: Read pinned README, contract and license; compare checkout and release; inspect schema and negative tests before installation.

Installation guidance: Follow the pinned README and observed release assets; no installation was performed for this website.

Source-inspected interface (not executed): vek schema list — Inspect public interface; not executed by this index review. Ref: 4008e311ceb16edd6e74d9f71341a90120c0d046; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

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

Qualify bounded reusable candidates for named receivers and compare full costs with solving from scratch.

Primary editorial role: reusable-abstraction

Limits / unsupported uses: Alpha collective-reuse profile; receiver qualification grants no settlement or execution. GitHub Release assets, not an assumed PyPI distribution.

Source reviewed: 2026-09-21

Source revision / declared version: e0296486bb568fdeeda449dada3bc67753ddfe7f / 0.5.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v0.5.0 · 2026-09-20T04:42:20Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: urn:alt-foundry-kernel:schema:token:0.4.0 · Inspected schema identity only; runtime and semantic admission remain separate.

Inputs: Immutable traces, receiver contracts, formation/transfer/check costs and lifecycle events.

Outputs: Reuse portfolios, qualification records, cost accounts and partial interchange sidecars.

Prerequisites: &gt;=3.11; explicit scope and host authority.

Effects and trust boundary: Inspection commands are documented separately. Installation changes the environment; runtime writes and remote dispatch require command-specific review.

First inspection: Read pinned README, contract and license; compare checkout and release; inspect schema and negative tests before installation.

Installation guidance: Follow the pinned README and observed release assets; no installation was performed for this website.

Source-inspected interface (not executed): altk --help — Inspect public interface; not executed by this index review. Ref: e0296486bb568fdeeda449dada3bc67753ddfe7f; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

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

Replay finite accounting histories to separate unique stock, service reuse, copies and unresolved origin.

Primary editorial role: capability-accounting

Limits / unsupported uses: Experimental accounting; copies are not new assets. VEK counters are supplied, not reconstructed from the absent original journal.

Source reviewed: 2026-09-21

Source revision / declared version: 0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7 / 0.2.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v0.2.0 · 2026-09-13T00:23:18Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: https://cait-schema.local/schemas/accounting/v1/report.schema.json · Inspected schema identity only; runtime and semantic admission remain separate.

Inputs: Source events, typed resource costs, scope, provenance and conditional model witnesses.

Outputs: Exact window balances, residuals, independently checked accounting reports.

Prerequisites: &gt;=3.11; explicit scope and host authority.

Effects and trust boundary: Inspection commands are documented separately. Installation changes the environment; runtime writes and remote dispatch require command-specific review.

First inspection: Read pinned README, contract and license; compare checkout and release; inspect schema and negative tests before installation.

Installation guidance: Follow the pinned README and observed release assets; no installation was performed for this website.

Source-inspected interface (not executed): cait-analyze --help — Inspect public interface; not executed by this index review. Ref: 0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

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

Choose finite information gathering and paid capability investment while preserving coupled model uncertainty.

Primary editorial role: finite-control-and-information

Limits / unsupported uses: Beta research; finite model demonstrations only. Signed observations do not certify causal models. No empirical acceleration experiment.

Source reviewed: 2026-09-21

Source revision / declared version: 340b4899d5b0892e06d7d2c1ab1f1d48df15e981 / 1.0.1

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v1.0.1 · 2026-09-13T15:02:46Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Interface schema identity / スキーマ識別子: https://schemas.cpcf.dev/v0.6.0/phase-contract.schema.json · Inspected schema identity only; runtime and semantic admission remain separate.

Inputs: Finite model catalogue, observation kernel, typed resources, obligations and continuation horizon.

Outputs: Checked finite plans, model supports, incomplete-search statuses and proposed interventions.

Prerequisites: &gt;=3.12,&lt;3.15,!=3.14.0,!=3.14.1; explicit scope and host authority.

Effects and trust boundary: Inspection commands are documented separately. Installation changes the environment; runtime writes and remote dispatch require command-specific review.

First inspection: Read pinned README, contract and license; compare checkout and release; inspect schema and negative tests before installation.

Installation guidance: Follow the pinned README and observed release assets; no installation was performed for this website.

Source-inspected interface (not executed): cpcf agent explain --json — Inspect public interface; not executed by this index review. Ref: 340b4899d5b0892e06d7d2c1ab1f1d48df15e981; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

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

## Core papers



### Observing and Accelerating Collective Capability Growth (paper-growth)

Joint task/research service, interaction ablation, evidence costs and funded continuation.

Primary editorial role: finite-control-and-information

Limits / unsupported uses: Finite horizon; matched information/resources; calibration and model premises. Synthetic examples do not establish deployed acceleration.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.22604358

Publication / 著者・発表: K. Takahashi · 2026-09-07 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.22604358)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-09-07-observing-and-accelerating-collective-capability-growth-22604358/)
- [e-paper-growth](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Observing%20and%20Accelerating%20Collective%20Capability%20Growth.zip)

### Verifier Ecology Theory: Packetized Self-Verification Under Residual Accountability (paper-vet)

Scoped verifier packets preserve residuals and revisable boundaries when verification is the bottleneck.

Primary editorial role: verification-capacity

Limits / unsupported uses: Structural claims concern the declared transition model; packet acceptance is not external truth.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.21147093

Publication / 著者・発表: K. Takahashi · 2026-07-03 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.21147093)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-07-03-verifier-ecology-theory-packetized-self-verification-under-residual-accountability-21147093/)
- [e-paper-vet](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Verifier%20Ecology%20Theory.zip)

### Executable Capability Percolation Theory (paper-ecpt)

Executable packet hypergraphs connect finite capability formation, queues and typed phase diagnostics.

Primary editorial role: capability-formation

Limits / unsupported uses: Quotients, response laws, baselines and certificates require their own witnesses; reachability alone is insufficient.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.20535654

Publication / 著者・発表: K. Takahashi · 2026-06-04 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.20535654)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-06-04-executable-capability-percolation-theory-20535654/)
- [e-paper-ecpt](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Executable%20Capability%20Percolation%20Theory.zip)

### Abstraction Liquidity Theory (paper-alt)

Receiver-relative search-cost reduction is charged for formation, transfer, verification and lifecycle costs.

Primary editorial role: reusable-abstraction

Limits / unsupported uses: Positive certified surplus needs compatible measurement, transport, authority and finality premises; compression is insufficient.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.20476200

Publication / 著者・発表: K. Takahashi · 2026-05-31 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.20476200)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-05-31-abstraction-liquidity-theory-20476200/)
- [e-paper-alt](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Abstraction%20Liquidity%20Theory.zip)

### Certified Autocatalytic Intelligence Theory: Net-Growth Certificate Algebra for Verified Capability Capital (paper-cait)

Typed partial certificates separate endogenous verified capital reproduction from copied outputs and external inputs.

Primary editorial role: capability-accounting

Limits / unsupported uses: Composition needs domain witnesses; spectral diagnostics and accepted arrival-shaped records do not detect real ASI.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.20061296

Publication / 著者・発表: K. Takahashi · 2026-05-07 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.20061296)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-05-07-certified-autocatalytic-intelligence-theory-net-growth-20061296/)
- [e-paper-cait](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Certified%20Autocatalytic%20Intelligence%20Theory.zip)

### Layered Online Service and Replay Control for Verified AI R and D Acceleration (paper-loscr)

Online ledgers, service obligations and replay libraries determine the strongest supported R&amp;D claim.

Primary editorial role: evidence-and-verification

Limits / unsupported uses: Estimator, evaluator, baseline and maintenance evidence remain premises; a claim checker cannot manufacture them.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.19836225

Publication / 著者・発表: K. Takahashi · 2026-04-28 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.19836225)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-04-28-layered-online-service-and-replay-control-for-veri-19836225/)
- [e-paper-loscr](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Layered%20Online%20Service%20and%20Replay%20Control%20for%20Verified%20AI%20R%20and%20D%20Acceleration.zip)

### Collective Phase Transitions beyond Individual Saturation (paper-collective-phase)

A Gibbs-model construction separates individual saturation from collective advantage and local evaluability.

Primary editorial role: collective-coordination

Limits / unsupported uses: Statistical-mechanical model assumptions, mixing and a scalar proxy are explicit; no empirical AI phase transition follows.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.17853555

Publication / 著者・発表: K. Takahashi · 2025-12-08 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.17853555)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2025-12-08-collective-phase-transitions-beyond-individual-s-17853555/)
- [e-paper-collective-phase](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Collective_Phase_Transitions_beyond_Individual_Saturation.zip)

### Audit-Closed AI Scientist Protocol (paper-audit-closed)

Transparency logs, sequential e-processes and alpha accounting constrain adaptive research decisions.

Primary editorial role: research-validity

Limits / unsupported uses: Statistical guarantees require the declared observation and sampling assumptions; synthetic benchmarks are bounded.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.18728589

Publication / 著者・発表: K. Takahashi · 2026-02-22 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.18728589)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-02-22-audit-closed-ai-scientist-protocol-18728589/)
- [e-paper-audit-closed](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Audit-Closed%20AI%20Scientist%20Protocol.zip)

## Supporting research and tools



### Reusable Consequence States Under Partial Support and Model Uncertainty (paper-consequence)

Reusable update states retain globally coupled model uncertainty across later actions and observations.

Primary editorial role: finite-control-and-information

Limits / unsupported uses: Finite dynamics/programs; local rectangular envelopes can be conservative. This is conceptual support, not a CPCF implementation identity.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.22170023

Publication / 著者・発表: K. Takahashi · 2026-08-30 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.22170023)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-08-30-reusable-consequence-states-under-partial-support-and-model-uncertainty-22170023/)
- [e-paper-consequence](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Reusable%20Consequence%20States%20Under%20Partial%20Support%20and%20Model%20Uncertainty.zip)

### Evidence-Carrying Operational Claims in Open Systems: Physical Ledgers, Typed Interfaces, and One-Sided Deployment Guarantees (paper-operational-claims)

Typed evidence connects physical/resource ledgers, uncertainty and one-sided finite-horizon deployment claims.

Primary editorial role: evidence-and-verification

Limits / unsupported uses: Provenance and finite record checking do not establish evidence truth, causal identification or physical safety.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.21531413

Publication / 著者・発表: K. Takahashi · 2026-07-24 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.21531413)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-07-24-evidence-carrying-operational-claims-in-open-systems-physical-ledgers-typed-interfaces-and-one-sided-deployment-guarantees-21531413/)
- [e-paper-operational-claims](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Evidence-Carrying%20Operational%20Claims%20in%20Open%20Systems.zip)

### Bottleneck Inversion Theory: Machine-Readable Witness Calculus for Unlockable Potential (paper-bit)

Unit-typed intervention witnesses bound unlockable target value and resource displacement.

Primary editorial role: resource-viability

Limits / unsupported uses: Unsupported coordinates remain unreported; compatible ledgers and resource-matched comparisons are required.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.20545356

Publication / 著者・発表: K. Takahashi · 2026-06-04 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.20545356)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-06-04-bottleneck-inversion-theory-machine-readable-witness-calculus-20545356/)
- [e-paper-bit](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Bottleneck%20Inversion%20Theory.zip)

### Salience-Queue Occupation Theory (paper-sqot)

Finite attention, diagnostic reserves and verification queues expose opportunity and audit costs.

Primary editorial role: verification-capacity

Limits / unsupported uses: Protocol-relative diagnostics allow abstention and quarantine; attention priorities are not a universal objective.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.20526451

Publication / 著者・発表: K. Takahashi · 2026-06-03 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.20526451)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-06-03-salience-queue-occupation-theory-20526451/)
- [e-paper-sqot](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Salience-Queue%20Occupation%20Theory.zip)

### Constraint Generative Theory: Typed Constraint Effects and Scientific Availability (paper-cgt)

Typed constraint effects distinguish identical final reports from different generation and verification conditions.

Primary editorial role: interoperability-and-discovery

Limits / unsupported uses: The catalogue record identifies this work only; related CGT source manuscripts sharing series metadata are not collapsed into it. Concept/series DOI: catalogue date 2026-05-15 differs from DataCite issued 2026-05-28; exact TeX/version binding unresolved.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.20199440

Publication / 著者・発表: K. Takahashi · 2026-05-15 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.20199440)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-05-15-constraint-generative-theory-typed-constraint-effects-and-scien-20199440/)
- [e-paper-cgt](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Constraint%20Generative%20Theory.zip)

### Certified Conversion Networks for AI Workflows (paper-conversion)

Certified value throughput includes validation, authorization, queue capacity and maintenance bottlenecks.

Primary editorial role: resource-viability

Limits / unsupported uses: Uniform or held-out certification, uncertainty contracts and hard gates are required.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.19994795

Publication / 著者・発表: K. Takahashi · 2026-05-03 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.19994795)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-05-03-certified-conversion-networks-for-ai-workflows-19994795/)
- [e-paper-conversion](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Certified%20Conversion%20Networks%20for%20AI%20Workflows.zip)

### Certified Service Is Not Enough for Long-Running AGI (paper-continuity)

Recovery, authority, identity and memory integrity remain obligations beyond certified task service.

Primary editorial role: workflow-memory

Limits / unsupported uses: Conditional assurance depends on trusted bases and non-erasing violation histories, not an AGI finding.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.19719004

Publication / 著者・発表: K. Takahashi · 2026-04-24 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.19719004)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-04-24-certified-service-is-not-enough-for-long-running-agi-19719004/)
- [e-paper-continuity](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Certified%20Service%20Is%20Not%20Enough%20for%20Long-Running%20AGI.zip)

### Controller Scale Is Not Enough for Long-Running AGI: A Workflow Theory with Reusable Certified Libraries (paper-workflow-library)

Reusable audited workflow libraries are compared with resource-matched flat control under replay ceilings.

Primary editorial role: workflow-memory

Limits / unsupported uses: Bounded typed families, trusted checkers and maintenance envelopes limit the constructive result.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.19690749

Publication / 著者・発表: K. Takahashi · 2026-04-22 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.19690749)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-04-22-controller-scale-is-not-enough-for-long-running-agi-19690749/)
- [e-paper-workflow-library](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Controller%20Scale%20Is%20Not%20Enough%20for%20Long-Running%20AGI.zip)

### When Should Inference Be Split? A Fixed-Budget Theory of Predictable Multi-Agent Advantage under Local Context Ceilings (paper-split-inference)

Fixed-budget inference splitting asks when local context limits permit a multi-agent advantage.

Primary editorial role: collective-coordination

Limits / unsupported uses: Communication and verification costs and a strong single-agent comparator must be retained.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.18932509

Publication / 著者・発表: K. Takahashi · 2026-03-10 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.18932509)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-03-10-when-should-inference-be-split-a-fixed-budget-th-18932509/)
- [e-paper-split-inference](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/When%20Should%20Inference%20Be%20Split.zip)

### Stop Recomputing for AI/LLMs: Proof-Carrying Skills for Compute-Saving Inference Reuse (paper-pcs)

Bounded observable predicates and invocation-bound receipts support reuse without full recomputation.

Primary editorial role: reusable-abstraction

Limits / unsupported uses: Trust is limited to the minimal checker and declared anchors; receipts are not unrestricted semantic truth.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.18490939

Publication / 著者・発表: K. Takahashi · 2026-02-05 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.18490939)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-02-05-stop-recomputing-for-ai-llms-proof-carrying-skil-18490939/)
- [e-paper-pcs](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Stop%20Recomputing%20for%20AILLMs%20Proof-Carrying%20Skills%20for%20Compute-Saving%20Inference%20Reuse.zip)

### Verification-Limited Intelligence Acceleration: Observable-Only Laws, Bounded Derivation, and Diagnostics under No-Meta Constraints (paper-verification-limited)

Strict observable progress credit prevents missing evidence from inflating reported progress.

Primary editorial role: verification-capacity

Limits / unsupported uses: Conditional acceleration envelopes require observable premises and a semantic adequacy link to capability.

Source reviewed: 2026-09-21

DOI: 10.5281/zenodo.18436828

Publication / 著者・発表: K. Takahashi · 2026-01-31 · Preprint

Source scope / 根拠範囲: Public TeX scope inspection and DataCite bibliographic identity; no independent theorem proof.

- [DOI](https://doi.org/10.5281/zenodo.18436828)
- [Scholarly landing page](https://kadubon.github.io/github.io/papers/2026-01-31-verification-limited-intelligence-acceleration-o-18436828/)
- [e-paper-verification-limited](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/verification_limited_intelligence_acceleration.zip)

### observable-agent-workflow-memory (sw-oawm)

Promote verified procedures through evidence manifests and explicit promotion receipts.

Primary editorial role: workflow-memory

Limits / unsupported uses: Procedural admissibility is not factual truth; no GitHub release was found. Source declares 0.1.0 beta.

Source reviewed: 2026-09-21

Source revision / declared version: 414299d4d15b5de434f5fb1ccbb4ba17df9155ff / 0.1.0b0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: null — no published GitHub release observed

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Inputs: Observable events, candidate workflow, evidence manifest and checker results.

Outputs: Receipt-bound workflow contracts and audit-visible retired/contradicted memory.

Prerequisites: &gt;=3.11; explicit scope and host authority.

Effects and trust boundary: Inspection commands are documented separately. Installation changes the environment; runtime writes and remote dispatch require command-specific review.

First inspection: Read pinned README, contract and license; compare checkout and release; inspect schema and negative tests before installation.

Installation guidance: Follow the pinned README and observed release assets; no installation was performed for this website.

Source-inspected interface (not executed): oawm --help — Inspect public interface; not executed by this index review. Ref: 414299d4d15b5de434f5fb1ccbb4ba17df9155ff; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/observable-agent-workflow-memory)
- [e-observable-agent-workflow-memory-readme-md](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/README.md)
- [Pinned contract](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/docs/theory_mapping.md)
- [Apache-2.0 license](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/LICENSE)
- [e-observable-agent-workflow-memory-pyproject-toml](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/pyproject.toml)

### oasg (sw-oasg)

Trial bounded local workflow-policy changes and promote only receipt-backed non-regression.

Primary editorial role: workflow-adaptation

Limits / unsupported uses: Reference/alpha production status; changes workflow policy, not model weights. Runtime trials can execute local commands under host policy.

Source reviewed: 2026-09-21

Source revision / declared version: 7593f74b5d6a4701865dc97b079c3e725c4fd7ee / 1.1.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v1.1.0 · 2026-05-10T08:47:02Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Inputs: Observable JSONL ledgers, policy mutations, shadow/lease trials and rollback receipts.

Outputs: Viability/debt reports, trial decisions, promoted or quarantined policy state.

Prerequisites: &gt;=3.12; explicit scope and host authority.

Effects and trust boundary: Inspection commands are documented separately. Installation changes the environment; runtime writes and remote dispatch require command-specific review.

First inspection: Read pinned README, contract and license; compare checkout and release; inspect schema and negative tests before installation.

Installation guidance: Follow the pinned README and observed release assets; no installation was performed for this website.

Source-inspected interface (not executed): oasg --help — Inspect public interface; not executed by this index review. Ref: 7593f74b5d6a4701865dc97b079c3e725c4fd7ee; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/oasg)
- [Observed release](https://github.com/kadubon/oasg/releases/tag/v1.1.0)
- [e-oasg-readme-md](https://github.com/kadubon/oasg/blob/7593f74b5d6a4701865dc97b079c3e725c4fd7ee/README.md)
- [Pinned contract](https://github.com/kadubon/oasg/blob/7593f74b5d6a4701865dc97b079c3e725c4fd7ee/docs/architecture.md)
- [Apache-2.0 license](https://github.com/kadubon/oasg/blob/7593f74b5d6a4701865dc97b079c3e725c4fd7ee/LICENSE)
- [e-oasg-pyproject-toml](https://github.com/kadubon/oasg/blob/7593f74b5d6a4701865dc97b079c3e725c4fd7ee/pyproject.toml)

### audit-closed-ai-scientist (sw-audit)

Benchmark adaptive scientific discovery with committed logs and sequential testing.

Primary editorial role: research-validity

Limits / unsupported uses: Benchmarks do not certify arbitrary laboratories or agents; every benchmark writes output artifacts. Software Apache-2.0; bundled paper CC BY 4.0.

Source reviewed: 2026-09-21

Source revision / declared version: 1e844d1bca18d7bb298aa198e1250bb07bd7ea44 / 0.2.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v0.2.0 · 2026-08-26T02:05:53Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Inputs: Declared synthetic benchmark configuration, seed, trial adapter and alpha budget.

Outputs: False-discovery, replication, sequential-evidence and adversarial benchmark reports.

Prerequisites: &gt;=3.10; explicit scope and host authority.

Effects and trust boundary: Inspection commands are documented separately. Installation changes the environment; runtime writes and remote dispatch require command-specific review.

First inspection: Read pinned README, contract and license; compare checkout and release; inspect schema and negative tests before installation.

Installation guidance: Follow the pinned README and observed release assets; no installation was performed for this website.

Source-inspected interface (not executed): audit-closed-ai-scientist --help — Inspect public interface; not executed by this index review. Ref: 1e844d1bca18d7bb298aa198e1250bb07bd7ea44; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/audit-closed-ai-scientist)
- [Observed release](https://github.com/kadubon/audit-closed-ai-scientist/releases/tag/v0.2.0)
- [Agent entry: SKILL.md](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/.agents/skills/audit-closed-ai-scientist/SKILL.md)
- [Pinned contract](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/README.md)
- [Apache-2.0 license](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/LICENSE)
- [e-audit-closed-ai-scientist-pyproject-toml](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/pyproject.toml)

### loscr (sw-loscr)

Downgrade or quarantine strong R&amp;D claims when replay, service, evaluator or dependency evidence fails.

Primary editorial role: evidence-and-verification

Limits / unsupported uses: Structural claim checking requires external statistical premises. Even doctor may initialize local state.

Source reviewed: 2026-09-21

Source revision / declared version: 334307b59a4870b90f6162705c793bb5615a555a / 0.1.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v0.1.0 · 2026-04-29T05:30:28Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Inputs: Append-only JSONL evidence and explicit claim contracts.

Outputs: Supported claim level, failure codes, replay and library records.

Prerequisites: &gt;=3.12; explicit scope and host authority.

Effects and trust boundary: Inspection commands are documented separately. Installation changes the environment; runtime writes and remote dispatch require command-specific review.

First inspection: Read pinned README, contract and license; compare checkout and release; inspect schema and negative tests before installation.

Installation guidance: Follow the pinned README and observed release assets; no installation was performed for this website.

Source-inspected interface (not executed): loscr --help — Inspect public interface; not executed by this index review. Ref: 334307b59a4870b90f6162705c793bb5615a555a; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/loscr)
- [Observed release](https://github.com/kadubon/loscr/releases/tag/v0.1.0)
- [e-loscr-readme-md](https://github.com/kadubon/loscr/blob/334307b59a4870b90f6162705c793bb5615a555a/README.md)
- [Pinned contract](https://github.com/kadubon/loscr/blob/334307b59a4870b90f6162705c793bb5615a555a/docs/theory-map.md)
- [Apache-2.0 license](https://github.com/kadubon/loscr/blob/334307b59a4870b90f6162705c793bb5615a555a/LICENSE)
- [e-loscr-pyproject-toml](https://github.com/kadubon/loscr/blob/334307b59a4870b90f6162705c793bb5615a555a/pyproject.toml)

### asi-proxy-phase-growth-simulator (sw-simulator)

Explore verification, resource, coordination and memory shocks in conditional scenarios.

Primary editorial role: scenario-analysis

Limits / unsupported uses: No world forecast, ASI date or probability; synthetic parameter choices are not measurements.

Source reviewed: 2026-09-21

Source revision / declared version: 24690a225c86fde2a24de4d9f93e2a282789b67d / 0.1.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v0.1.0 · 2026-07-21T04:16:46Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Inputs: Declared scenario parameters, finite resource stocks, seed and solver choices.

Outputs: Conditional trajectories, sensitivity and Monte Carlo reports.

Prerequisites: &gt;=3.12,&lt;3.14; explicit scope and host authority.

Effects and trust boundary: Inspection commands are documented separately. Installation changes the environment; runtime writes and remote dispatch require command-specific review.

First inspection: Read pinned README, contract and license; compare checkout and release; inspect schema and negative tests before installation.

Installation guidance: Follow the pinned README and observed release assets; no installation was performed for this website.

Source-inspected interface (not executed): apxsim --help — Inspect public interface; not executed by this index review. Ref: 24690a225c86fde2a24de4d9f93e2a282789b67d; effects: no_external_network; cwd: Reviewed checkout or installed environment; see linked README.

- [Repository](https://github.com/kadubon/asi-proxy-phase-growth-simulator)
- [Observed release](https://github.com/kadubon/asi-proxy-phase-growth-simulator/releases/tag/v0.1.0)
- [asi_proxy_phase_growth_simulator-0.1.0-py3-none-any.whl](https://github.com/kadubon/asi-proxy-phase-growth-simulator/releases/download/v0.1.0/asi_proxy_phase_growth_simulator-0.1.0-py3-none-any.whl)
- [asi_proxy_phase_growth_simulator-0.1.0.tar.gz](https://github.com/kadubon/asi-proxy-phase-growth-simulator/releases/download/v0.1.0/asi_proxy_phase_growth_simulator-0.1.0.tar.gz)
- [e-asi-proxy-phase-growth-simulator-readme-md](https://github.com/kadubon/asi-proxy-phase-growth-simulator/blob/24690a225c86fde2a24de4d9f93e2a282789b67d/README.md)
- [Pinned contract](https://github.com/kadubon/asi-proxy-phase-growth-simulator/blob/24690a225c86fde2a24de4d9f93e2a282789b67d/docs/model-reference.md)
- [Apache-2.0 license](https://github.com/kadubon/asi-proxy-phase-growth-simulator/blob/24690a225c86fde2a24de4d9f93e2a282789b67d/LICENSE)
- [e-asi-proxy-phase-growth-simulator-pyproject-toml](https://github.com/kadubon/asi-proxy-phase-growth-simulator/blob/24690a225c86fde2a24de4d9f93e2a282789b67d/pyproject.toml)

### asi-proxy-phase-skill (sw-skill)

An installable skill supplies evidence-gated discovery and bounded intervention guidance.

Primary editorial role: interoperability-and-discovery

Limits / unsupported uses: An advisory skill is not a running service; its bundled corpus is an older snapshot. Installation/execution needs host authorization.

Source reviewed: 2026-09-21

Source revision / declared version: 5706214a9a3d5e194f371f8ccc2eb71132f82270 / 1.1.1

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v1.1.1 · 2026-07-31T01:31:01Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Inputs: Host policy, user task, public source snapshot and explicit resource boundaries.

Outputs: Reviewable intervention packets and source routing.

Prerequisites: &gt;=3.11; explicit scope and host authority.

Effects and trust boundary: Inspection commands are documented separately. Installation changes the environment; runtime writes and remote dispatch require command-specific review.

First inspection: Read pinned README, contract and license; compare checkout and release; inspect schema and negative tests before installation.

Installation guidance: Follow the pinned README and observed release assets; no installation was performed for this website.

- [Repository](https://github.com/kadubon/asi-proxy-phase-skill)
- [Observed release](https://github.com/kadubon/asi-proxy-phase-skill/releases/tag/v1.1.1)
- [asi-proxy-phase-skill-v1.1.1.zip](https://github.com/kadubon/asi-proxy-phase-skill/releases/download/v1.1.1/asi-proxy-phase-skill-v1.1.1.zip)
- [asi-proxy-phase-skill-v1.1.1.zip.sha256](https://github.com/kadubon/asi-proxy-phase-skill/releases/download/v1.1.1/asi-proxy-phase-skill-v1.1.1.zip.sha256)
- [Agent entry: SKILL.md](https://github.com/kadubon/asi-proxy-phase-skill/blob/5706214a9a3d5e194f371f8ccc2eb71132f82270/asi-proxy-phase-skill/SKILL.md)
- [Pinned contract](https://github.com/kadubon/asi-proxy-phase-skill/blob/5706214a9a3d5e194f371f8ccc2eb71132f82270/README.md)
- [Apache-2.0 license](https://github.com/kadubon/asi-proxy-phase-skill/blob/5706214a9a3d5e194f371f8ccc2eb71132f82270/LICENSE)
- [e-asi-proxy-phase-skill-pyproject-toml](https://github.com/kadubon/asi-proxy-phase-skill/blob/5706214a9a3d5e194f371f8ccc2eb71132f82270/pyproject.toml)

### certified-memory-governance-layer (sw-cmgl)

Gate memory writes and retrieval using current versions, authority receipts, tombstones and contamination lanes.

Primary editorial role: workflow-memory

Limits / unsupported uses: Procedural admissibility only; no factual truth, model unlearning, backend deletion guarantee or prompt-injection immunity. Optional adapters remain application-owned.

Source reviewed: 2026-09-24

Source revision / declared version: 2fc49b4df7bbe4a23265b8b2372432711740d00b / 1.1.2

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v1.1.2 · 2026-05-14T01:30:00Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Inputs: Memory events with version/digest bindings, verified ledger prefix and structured authority.

Outputs: Admit/block receipts and an audit-visible current retrieval view.

Prerequisites: Python &gt;=3.10; declared scope and host authority.

Effects and trust boundary: Memory admission and view construction can persist local records; deletion semantics do not imply physical erasure of external copies. This review inspected source only.

First inspection: Read the pinned README, contract and failure cases before considering execution.

Installation guidance: Follow the pinned upstream source instructions only after host authorization; package registry availability was not independently checked in this review.

- [Repository](https://github.com/kadubon/certified-memory-governance-layer)
- [Observed release](https://github.com/kadubon/certified-memory-governance-layer/releases/tag/v1.1.2)
- [e-routing-cmgl-readme-md](https://github.com/kadubon/certified-memory-governance-layer/blob/2fc49b4df7bbe4a23265b8b2372432711740d00b/README.md)
- [Pinned contract](https://github.com/kadubon/certified-memory-governance-layer/blob/2fc49b4df7bbe4a23265b8b2372432711740d00b/docs/proof-obligations.md)
- [Apache-2.0 license](https://github.com/kadubon/certified-memory-governance-layer/blob/2fc49b4df7bbe4a23265b8b2372432711740d00b/LICENSE)
- [e-routing-cmgl-pyproject-toml](https://github.com/kadubon/certified-memory-governance-layer/blob/2fc49b4df7bbe4a23265b8b2372432711740d00b/pyproject.toml)
- [e-routing-cmgl-docs-current-view-md](https://github.com/kadubon/certified-memory-governance-layer/blob/2fc49b4df7bbe4a23265b8b2372432711740d00b/docs/current-view.md)
- [e-routing-cmgl-tests-test-compression-py](https://github.com/kadubon/certified-memory-governance-layer/blob/2fc49b4df7bbe4a23265b8b2372432711740d00b/tests/test_compression.py)

### memoryflow-agent-memory-auditor (sw-memoryflow)

Audit declared memory telemetry for stale, deleted or superseded use, correction latency and non-comparable metrics.

Primary editorial role: workflow-memory

Limits / unsupported uses: Cannot observe silent backend changes, fabricated events or source truth. Auditing deletion telemetry does not erase memory or model weights.

Source reviewed: 2026-09-24

Source revision / declared version: c8ee3f4c81f5303535ba2d2e9882c409f05e641e / 0.1.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v0.1.0 · 2026-05-01T03:15:40Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Inputs: JSONL memory events, ordering/skew bounds, update IDs, digests and chosen P0/P1/P2 profile.

Outputs: Version-bound metrics with VALID, DEGRADED, NONCOMPARABLE or NOT_COMPUTABLE status.

Prerequisites: Python &gt;=3.11; declared scope and host authority.

Effects and trust boundary: The auditor reads declared event traces and writes audit artifacts; it does not itself alter the observed memory backend. This review inspected source only.

First inspection: Read the pinned README, contract and failure cases before considering execution.

Installation guidance: Follow the pinned upstream source instructions only after host authorization; package registry availability was not independently checked in this review.

- [Repository](https://github.com/kadubon/memoryflow-agent-memory-auditor)
- [Observed release](https://github.com/kadubon/memoryflow-agent-memory-auditor/releases/tag/v0.1.0)
- [e-routing-memoryflow-readme-md](https://github.com/kadubon/memoryflow-agent-memory-auditor/blob/c8ee3f4c81f5303535ba2d2e9882c409f05e641e/README.md)
- [Pinned contract](https://github.com/kadubon/memoryflow-agent-memory-auditor/blob/c8ee3f4c81f5303535ba2d2e9882c409f05e641e/docs/conformance-profiles.md)
- [Apache-2.0 license](https://github.com/kadubon/memoryflow-agent-memory-auditor/blob/c8ee3f4c81f5303535ba2d2e9882c409f05e641e/LICENSE)
- [e-routing-memoryflow-pyproject-toml](https://github.com/kadubon/memoryflow-agent-memory-auditor/blob/c8ee3f4c81f5303535ba2d2e9882c409f05e641e/pyproject.toml)
- [e-routing-memoryflow-docs-event-schema-md](https://github.com/kadubon/memoryflow-agent-memory-auditor/blob/c8ee3f4c81f5303535ba2d2e9882c409f05e641e/docs/event-schema.md)
- [e-routing-memoryflow-tests-unit-test-verifier-profiles-py](https://github.com/kadubon/memoryflow-agent-memory-auditor/blob/c8ee3f4c81f5303535ba2d2e9882c409f05e641e/tests/unit/test_verifier_profiles.py)

### problem-frame-gate (sw-pfg)

Check finite action authority and atomically commit a five-row gate bundle before a separately controlled outbox dispatcher.

Primary editorial role: evidence-and-verification

Limits / unsupported uses: Finite audit consistency is not OAuth infrastructure, external truth, physical outcome or exactly-once delivery. Deployment owns identities, durable storage, actuator monitoring and incident response.

Source reviewed: 2026-09-24

Source revision / declared version: 9449b338c4c8b959878704a48b2f16e291e2dfb8 / 1.1.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v1.1.0 · 2026-07-02T01:04:13Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Inputs: Strict horizon manifest, writer/issuer identities, log, action request, capacities and risk premises.

Outputs: Rejected request or checked atomic bundle; dispatch and actuator acceptance remain separate records.

Prerequisites: Python &gt;=3.10; declared scope and host authority.

Effects and trust boundary: The committer records decisions without executing an actuator. A separately authorized OutboxBroker can dispatch external actions. This review inspected source only.

First inspection: Read the pinned README, contract and failure cases before considering execution.

Installation guidance: Follow the pinned upstream source instructions only after host authorization; package registry availability was not independently checked in this review.

- [Repository](https://github.com/kadubon/problem-frame-gate)
- [Observed release](https://github.com/kadubon/problem-frame-gate/releases/tag/v1.1.0)
- [e-routing-pfg-readme-md](https://github.com/kadubon/problem-frame-gate/blob/9449b338c4c8b959878704a48b2f16e291e2dfb8/README.md)
- [Pinned contract](https://github.com/kadubon/problem-frame-gate/blob/9449b338c4c8b959878704a48b2f16e291e2dfb8/docs/operations.md)
- [Apache-2.0 license](https://github.com/kadubon/problem-frame-gate/blob/9449b338c4c8b959878704a48b2f16e291e2dfb8/LICENSE)
- [e-routing-pfg-pyproject-toml](https://github.com/kadubon/problem-frame-gate/blob/9449b338c4c8b959878704a48b2f16e291e2dfb8/pyproject.toml)
- [e-routing-pfg-schemas-gate-request-schema-json](https://github.com/kadubon/problem-frame-gate/blob/9449b338c4c8b959878704a48b2f16e291e2dfb8/schemas/gate-request.schema.json)
- [e-routing-pfg-tests-test-v1-1-hardening-py](https://github.com/kadubon/problem-frame-gate/blob/9449b338c4c8b959878704a48b2f16e291e2dfb8/tests/test_v1_1_hardening.py)

### fost-agent-ledger (sw-fost)

Separate claimed completion from finite support, checked finality, unresolved obligations and environment changes.

Primary editorial role: evidence-and-verification

Limits / unsupported uses: A checked ledger is not a truth oracle or external outcome. Structural migration cannot invent evidence; project-specific modes and freshness policies remain necessary.

Source reviewed: 2026-09-24

Source revision / declared version: e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa / 2.0.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v2.0.0 · 2026-07-02T08:04:35Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Inputs: Finite claim/support graph, certificates, mode, environment tokens and finality records.

Outputs: Mode-scoped admissibility, missing-support codes and transition witnesses.

Prerequisites: Python &gt;=3.10; declared scope and host authority.

Effects and trust boundary: Ledger and verification operations produce local records and reports; finality of those records is not an external action or observation. This review inspected source only.

First inspection: Read the pinned README, contract and failure cases before considering execution.

Installation guidance: Follow the pinned upstream source instructions only after host authorization; package registry availability was not independently checked in this review.

- [Repository](https://github.com/kadubon/fost-agent-ledger)
- [Observed release](https://github.com/kadubon/fost-agent-ledger/releases/tag/v2.0.0)
- [e-routing-fost-readme-md](https://github.com/kadubon/fost-agent-ledger/blob/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa/README.md)
- [Pinned contract](https://github.com/kadubon/fost-agent-ledger/blob/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa/docs/json_contract.md)
- [Apache-2.0 license](https://github.com/kadubon/fost-agent-ledger/blob/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa/LICENSE)
- [e-routing-fost-pyproject-toml](https://github.com/kadubon/fost-agent-ledger/blob/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa/pyproject.toml)
- [e-routing-fost-docs-limitations-md](https://github.com/kadubon/fost-agent-ledger/blob/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa/docs/limitations.md)
- [e-routing-fost-tests-test-v20-strict-finality-py](https://github.com/kadubon/fost-agent-ledger/blob/e3a937a4a3f28c4077b5f658d6bfb1fc67ddd8fa/tests/test_v20_strict_finality.py)

### agent-trust-residual-benchmark (sw-atrb)

Inspect positive/negative synthetic controls and near misses for authority, evidence scope, residuals and repeated model decisions.

Primary editorial role: research-validity

Limits / unsupported uses: Fixtures and validators were co-developed. Cumulative conditions do not isolate causal effects. Compatibility adapters do not establish equivalence with PIC/FOST/PFG/CCR; no real-world safety or generalization claim.

Source reviewed: 2026-09-24

Source revision / declared version: eb21fda8ed7bfad9dc33becf2ffcc63285249495 / 0.2.0

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: v0.2.0 · 2026-07-19T12:10:23Z

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Inputs: Pinned cases, expected accept/reject policy, replication settings and declared model/runtime provenance.

Outputs: Fixture-scoped decision metrics, timeout records and explicit validity limits.

Prerequisites: Python &gt;=3.11; declared scope and host authority.

Effects and trust boundary: Benchmark runs produce local synthetic-case artifacts; optional model experiments can contact configured model services. This review inspected source only.

First inspection: Read the pinned README, contract and failure cases before considering execution.

Installation guidance: Follow the pinned upstream source instructions only after host authorization; package registry availability was not independently checked in this review.

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

Examine retry, review cost and escalation load using bounded coding tasks and explicit claim margins.

Primary editorial role: research-validity

Limits / unsupported uses: Twelve synthetic tasks, one logged run per actual model, and scripted costly review do not measure human approval fatigue or establish production readiness. Positive comparative oversight claims remain fail-closed in the reported setup.

Source reviewed: 2026-09-24

Source revision / declared version: a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b / unknown

Review state / レビュー状態: reviewed_snapshot

Observed GitHub release: null — no published GitHub release observed

Release observation / リリース確認: 2026-09-21T08:58:00+00:00 · current

License: Apache-2.0

Inputs: Declared small-task protocol, retry/review budgets, channel costs and transport/audit-distortion margins.

Outputs: Workflow metrics and bounded claim status, not a provider leaderboard.

Prerequisites: Python version not declared here; declared scope and host authority.

Effects and trust boundary: Repair experiments execute local Python functions and write artifacts; optional Gemini/Ollama backends invoke configured model services. This review inspected source only.

First inspection: Read the pinned README, contract and failure cases before considering execution.

Installation guidance: Follow the pinned upstream source instructions only after host authorization; package registry availability was not independently checked in this review.

- [Repository](https://github.com/kadubon/Oversight-Centered-Metrology-PoC)
- [e-routing-oversight-readme-md](https://github.com/kadubon/Oversight-Centered-Metrology-PoC/blob/a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b/README.md)
- [Pinned contract](https://github.com/kadubon/Oversight-Centered-Metrology-PoC/blob/a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b/experiment_manifest.yaml)
- [Apache-2.0 license](https://github.com/kadubon/Oversight-Centered-Metrology-PoC/blob/a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b/LICENCE)
- [e-routing-oversight-report-workflow-oversight-report-md](https://github.com/kadubon/Oversight-Centered-Metrology-PoC/blob/a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b/report/workflow_oversight_report.md)
- [e-routing-oversight-src-oversight-poc-channels-py](https://github.com/kadubon/Oversight-Centered-Metrology-PoC/blob/a814d7e02e52d3c7e2a3ce268e2c1bcc0b5ba43b/src/oversight_poc/channels.py)

## Proposed evidence-preserving workflow

Generate → Verify → Reuse → Account → Reallocate is a conceptual workflow, not an executable pipeline. Preserve original bytes, identities, clocks, costs and unresolved obligations at each handoff. Use the typed relationships below before connecting any two tools. A schema match alone grants neither semantic acceptance nor execution authority.

## Version-bound interoperability

“Tested upstream” attributes native fixture checks to the cited project; none of those packages was executed in this website task. Document inspection, index regression tests and native integration execution are different evidence origins. Direction matters: imports_artifact_from points from consumer to producer; exports_proposal_to points from producer to host. Compatibility is neither transitive nor automatically renewed by a release.

### basis-sw-ccr

sw-ccr → paper-growth: based_on / documented / source_inspected

Repository cites this research for a bounded role.

3b4702454f732c7a0a9f30d87483384dc8a281eb → 10.5281/zenodo.22604358 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

A citation does not establish complete implementation.

- [e-collective-capability-runtime-readme-md](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/README.md)

### basis-sw-pic

sw-pic → paper-ecpt: based_on / documented / source_inspected

Repository cites this research for a bounded role.

55cd5f219d02f02927e247317156e757b1d5d6da → 10.5281/zenodo.20535654 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

A citation does not establish complete implementation.

- [e-percolation-inversion-compiler-readme-md](https://github.com/kadubon/percolation-inversion-compiler/blob/55cd5f219d02f02927e247317156e757b1d5d6da/README.md)

### basis-sw-vek

sw-vek → paper-vet: based_on / documented / source_inspected

Repository cites this research for a bounded role.

4008e311ceb16edd6e74d9f71341a90120c0d046 → 10.5281/zenodo.21147093 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

A citation does not establish complete implementation.

- [e-verification-ecology-kit-readme-md](https://github.com/kadubon/verification-ecology-kit/blob/4008e311ceb16edd6e74d9f71341a90120c0d046/README.md)

### basis-sw-alt

sw-alt → paper-alt: based_on / documented / source_inspected

Repository cites this research for a bounded role.

e0296486bb568fdeeda449dada3bc67753ddfe7f → 10.5281/zenodo.20476200 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

A citation does not establish complete implementation.

- [e-alt-foundry-kernel-readme-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/README.md)

### basis-sw-cait

sw-cait → paper-cait: based_on / documented / source_inspected

Repository cites this research for a bounded role.

0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7 → 10.5281/zenodo.20061296 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

A citation does not establish complete implementation.

- [e-cait-certificate-schema-readme-md](https://github.com/kadubon/cait-certificate-schema/blob/0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7/README.md)

### basis-sw-cpcf

sw-cpcf → paper-growth: based_on / documented / source_inspected

Repository cites this research for a bounded role.

340b4899d5b0892e06d7d2c1ab1f1d48df15e981 → 10.5281/zenodo.22604358 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

A citation does not establish complete implementation.

- [e-collective-phase-control-fabric-readme-md](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/README.md)
- [e-collective-phase-control-fabric-docs-growth-research-mapping-md](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/docs/growth-research-mapping.md)

### basis-sw-oawm

sw-oawm → paper-workflow-library: based_on / documented / source_inspected

Repository cites this research for a bounded role.

414299d4d15b5de434f5fb1ccbb4ba17df9155ff → 10.5281/zenodo.19690749 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

A citation does not establish complete implementation.

- [e-observable-agent-workflow-memory-readme-md](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/README.md)
- [e-observable-agent-workflow-memory-docs-theory-sources-md](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/docs/theory_sources.md)

### basis-sw-audit

sw-audit → paper-audit-closed: based_on / documented / source_inspected

Repository cites this research for a bounded role.

1e844d1bca18d7bb298aa198e1250bb07bd7ea44 → 10.5281/zenodo.18728589 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

A citation does not establish complete implementation.

- [e-audit-closed-ai-scientist-readme-md](https://github.com/kadubon/audit-closed-ai-scientist/blob/1e844d1bca18d7bb298aa198e1250bb07bd7ea44/README.md)

### basis-sw-loscr

sw-loscr → paper-loscr: based_on / documented / source_inspected

Repository cites this research for a bounded role.

334307b59a4870b90f6162705c793bb5615a555a → 10.5281/zenodo.19836225 / archive 7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd

Checked fields: citation

A citation does not establish complete implementation.

- [e-loscr-readme-md](https://github.com/kadubon/loscr/blob/334307b59a4870b90f6162705c793bb5615a555a/README.md)

### alt-to-ccr

sw-alt → sw-ccr: exports_proposal_to / tested_upstream / upstream_reported

ALT 0.5.0 native open/unleased task parses against CCR 1.8.0; ALT sidecar is additional.

0.5.0 → 1.8.0 / 1591e88e3b05f9b5fb06b2d0c749aad8bc0909be

Checked fields: ccr.task.v0.1, open status, unleased proposal

Custom ALT sidecar admission, leases, rewards and execution are not supplied.

- [e-alt-foundry-kernel-docs-reuse-interchange-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/reuse-interchange.md)
- [e-alt-release](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/release-v0.5.0.md)
- [e-alt-native-test](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/tests/test_reuse_integration.py)

### alt-from-vek

sw-alt → sw-vek: imports_artifact_from / tested_upstream / upstream_reported

Capacity report schema and scope/clock/work-conservation checks on pinned fixtures.

0.5.0 → 1.3.0 / b07998135cb9dccde1e67db3c6ed77fdec847e09

Checked fields: scope, clock, work conservation

Counters are supplied, not replayed; no observed rate or empirical independence.

- [e-alt-foundry-kernel-docs-reuse-interchange-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/reuse-interchange.md)
- [e-alt-release](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/release-v0.5.0.md)
- [e-alt-native-test](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/tests/test_reuse_integration.py)

### alt-to-vek

sw-alt → sw-vek: tested_interchange_with / tested_upstream / upstream_reported

Finite synthetic check demand accepted by the released VEK checker.

0.5.0 → 1.3.0 / b07998135cb9dccde1e67db3c6ed77fdec847e09

Checked fields: native contract, schedule

Host residual/service/unit registration and real observed capacity are absent.

- [e-alt-foundry-kernel-docs-reuse-interchange-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/reuse-interchange.md)
- [e-alt-release](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/release-v0.5.0.md)
- [e-alt-native-test](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/tests/test_reuse_integration.py)

### alt-to-cait

sw-alt → sw-cait: tested_interchange_with / tested_upstream / upstream_reported

Supported complete history passes released analyzer/checker; copies do not create assets.

0.5.0 → 0.2.0 / 7d12bcf0bc4c6eae2acdd177175b6be414a274f6

Checked fields: unique formation, costs, receiver checks, requests/results, withdrawal

Expiry, contradiction, refresh, correction and some parent mappings remain partial; no cost-to-capital or arrival claim.

- [e-alt-foundry-kernel-docs-reuse-interchange-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/reuse-interchange.md)
- [e-alt-release](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/release-v0.5.0.md)
- [e-alt-native-test](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/tests/test_reuse_integration.py)

### vek-to-ccr

sw-vek → sw-ccr: exports_proposal_to / documented / source_inspected

Capacity extension accompanies schema-valid candidate task.

1.3.0 → 6d8a30820806044b3a4b18d499fbe89bef83fbf2

Checked fields: ccr.task.v0.1, duration rounding, x_vek_capacity

CCR base schema does not enforce extensions; custom admission and atomic host reservation required.

- [e-verification-ecology-kit-docs-capacity-interchange-md](https://github.com/kadubon/verification-ecology-kit/blob/4008e311ceb16edd6e74d9f71341a90120c0d046/docs/capacity_interchange.md)

### cait-from-vek

sw-cait → sw-vek: imports_artifact_from / documented / source_inspected

Pinned capacity schema preserves counters and rejects a false guarantee fixture.

0.2.0 → 1.3.0 / b07998135cb9dccde1e67db3c6ed77fdec847e09

Checked fields: schema, scope, source digest, work conservation

Original VEK reducer journal is absent; counters are not independently reconstructed.

- [e-cait-certificate-schema-docs-interchange-md](https://github.com/kadubon/cait-certificate-schema/blob/0ecb3afd2ea1d99cedcabd7a9e01e405ae1808a7/docs/interchange.md)

### ccr-from-alt-legacy

sw-ccr → sw-alt: imports_artifact_from / documented / source_inspected

CCR growth importer pins ALT 0.4.0 token schema, not the new reuse profile.

1.8.0 → 0.4.0 / b5170dbee93b9183f86570c9b2fa325be9cded51

Checked fields: token identity, dependencies, guard, provenance

Receiver service qualification and newer ALT profile acceptance are not implied.

- [e-collective-capability-runtime-docs-verified-growth-interchange-md](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/docs/verified-growth-interchange.md)

### ccr-from-pic

sw-ccr → sw-pic: imports_artifact_from / documented / source_inspected

Optional provider reports preserve blockers, residuals and candidate-only flags.

1.8.0 → 1.1.0

Checked fields: accepted, settled, blockers, residuals

No index-run interoperability test; PIC acceptance alone cannot settle CCR or authorize dispatch.

- [e-collective-capability-runtime-interop-pic-md](https://github.com/kadubon/collective-capability-runtime/blob/3b4702454f732c7a0a9f30d87483384dc8a281eb/INTEROP_PIC.md)

### cpcf-to-ccr

sw-cpcf → sw-ccr: proposed_integration_with / proposed / editorial

A planner candidate could become host work only through a separately implemented admitted adapter.

1.0.1 → 1.8.0

Checked fields: none

Legacy CCR 1.6.0 inspection is quarantined; no v0.6 promotion mapping or execution authority.

- [e-collective-phase-control-fabric-docs-adapters-md](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/docs/adapters.md)

### alt-to-oawm

sw-alt → sw-oawm: proposed_integration_with / proposed / editorial

Qualified reuse may be relevant input to a future memory adapter.

0.5.0 → 414299d4d15b5de434f5fb1ccbb4ba17df9155ff

Checked fields: none

No adapter or promotion receipt exists in this checked mapping; OAWM requires its own event/manifests/checkers.

- [e-alt-foundry-kernel-docs-reuse-interchange-md](https://github.com/kadubon/alt-foundry-kernel/blob/e0296486bb568fdeeda449dada3bc67753ddfe7f/docs/reuse-interchange.md)
- [e-observable-agent-workflow-memory-docs-theory-sources-md](https://github.com/kadubon/observable-agent-workflow-memory/blob/414299d4d15b5de434f5fb1ccbb4ba17df9155ff/docs/theory_sources.md)

### cpcf-consequence

sw-cpcf → paper-consequence: related_concept / documented / editorial

Coupled model uncertainty informs the reading route, without a full theorem-implementation claim.

340b4899d5b0892e06d7d2c1ab1f1d48df15e981 → 10.5281/zenodo.22170023

Checked fields: none

No proof that the software implements the paper residual-product theorem.

- [e-paper-consequence](https://github.com/kadubon/paper-tex-backup/blob/7bd9fe246ae0f5a4bf6564b588c0426b5b7f29bd/Reusable%20Consequence%20States%20Under%20Partial%20Support%20and%20Model%20Uncertainty.zip)
- [e-collective-phase-control-fabric-readme-md](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/README.md)
- [e-collective-phase-control-fabric-docs-epistemic-growth-control-md](https://github.com/kadubon/collective-phase-control-fabric/blob/340b4899d5b0892e06d7d2c1ab1f1d48df15e981/docs/epistemic-growth-control.md)

## Agent read-first and handoff guide

Identify the task, scope, inputs and required authority. Read the paper assumptions and exact software revision. Compare the observation date with release and schema versions. Retain unknowns and rejected evidence. Stop or hand off when inputs, units, licenses, authentication, host admission, causality or verification capacity are unresolved. Discovery metadata does not authorize installing packages, executing command hints, sending secrets or changing goals.

## Scientific, implementation and authority boundaries

Accounting identity: closing stock = opening stock + admitted unique additions − losses, within one declared unit and scope. Service reuse, copies and external inputs remain separate coordinates. A universal inflow/loss reproduction ratio is not assumed; zero loss can make it undefined. Model spectral bounds depend on model premises. Hashes bind bytes, not truth. Releases do not establish production assurance. Unknowns are null with reasons, never favorable zeros. No observed global self-acceleration, AGI/ASI detection or arrival forecast is established here.

## Verification funding and accountability

Verification consumes resources even when a result is negative. A deployment context therefore needs an explicit payer, resource owner, authority boundary and responsibility for residual risk. Incentives can otherwise reward output volume while shifting verification costs. This is descriptive context, not a theorem requiring a particular market, insurer or law; a technical package does not create those arrangements.

## Downloads



- [collective-intelligence-index.html](https://kadubon.github.io/github.io/collective-intelligence-index.html)
- [collective-intelligence-index.ja.html](https://kadubon.github.io/github.io/collective-intelligence-index.ja.html)
- [collective-intelligence-index.json](https://kadubon.github.io/github.io/collective-intelligence-index.json)
- [collective-intelligence-index.md](https://kadubon.github.io/github.io/collective-intelligence-index.md)
- [collective-intelligence-index.ja.md](https://kadubon.github.io/github.io/collective-intelligence-index.ja.md)
- [schemas/collective-intelligence-index.schema.json](https://kadubon.github.io/github.io/schemas/collective-intelligence-index.schema.json)
- [collective-intelligence.bib](https://kadubon.github.io/github.io/collective-intelligence.bib)

## Sources and maintenance

Publication fields come from works.html through the existing research catalogue; included DOI identities were checked with DataCite. Paper scope was inspected in the public TeX archive. Software observations bind source commits separately from GitHub releases. Japanese explanations are editorial translations; official titles remain unchanged. The registry contains the complete screened inventory and evidence locators. Corrections belong in the website repository. Website prose remains CC BY 4.0; inspected software is Apache-2.0, and bundled paper licenses remain separate.

Scanned 233 research records and 54 repositories; selected 37 resources.

Boundary Exchange / viability: unresolved — No exact Boundary Exchange title/DOI in the scanned catalogue. Do not invent a paper identity.

CGT bandwidth / availability / comparability supplements: unresolved — Distinct TeX manuscripts exist in the source archive, but only the canonical CGT work is a distinct local catalogue record. Do not collapse supplements or invent DOI bindings.

OASG 10.5281/zenodo.20107661: resolved_software_kind — DataCite classifies this as Software, matching works.html. Included through the repository, excluded from paper bibliography.

10.5281/zenodo.20199440: concept_record_date_discrepancy — CGT concept/series DOI has multiple HasVersion records. Existing catalogue first-publication date is 2026-05-15; current DataCite Issued date is 2026-05-28. The exact version binding of the inspected TeX is unresolved. Bibliography includes only verified title/author/year/DOI; it does not claim the DOI identifies these exact source bytes.

[Maintenance](https://kadubon.github.io/github.io/docs/collective-intelligence-index-maintenance.md)
