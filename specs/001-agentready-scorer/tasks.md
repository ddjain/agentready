# Tasks: AgentReady Repository Scorer

**Input**: Design documents from `/specs/001-agentready-scorer/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: NOT REQUESTED - Implementation follows library-first + CLI wrapper pattern per constitution Principle IV

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/agentready/`, `tests/` at repository root per plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directory structure matching plan.md (src/agentready/{cli,assessors,models,services,reporters,templates,data})
- [X] T002 Initialize Python project with pyproject.toml including Click, Jinja2, PyYAML, gitpython, radon, lizard, pytest dependencies
- [X] T003 [P] Configure black, isort, flake8, and pytest-cov in pyproject.toml per constitution
- [X] T004 [P] Create README.md with project overview and installation instructions
- [X] T005 [P] Copy agent-ready-codebase-attributes.md to src/agentready/data/
- [X] T006 [P] Create .agentready-config.example.yaml with documented weight customization examples
- [X] T007 [P] Create src/agentready/data/default-weights.yaml with tier-based weight distribution per research.md

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T008 [P] Create Repository model in src/agentready/models/repository.py (path, name, url, branch, commit_hash, languages, total_files, total_lines)
- [X] T009 [P] Create Attribute model in src/agentready/models/attribute.py (id, name, category, tier, description, criteria, default_weight)
- [X] T010 [P] Create Finding model in src/agentready/models/finding.py (attribute, status, score, measured_value, threshold, evidence, remediation, error_message)
- [X] T011 [P] Create Citation model in src/agentready/models/citation.py (source, title, url, relevance)
- [X] T012 [P] Create Remediation model (inline in finding.py) (summary, steps, tools, commands, examples, citations)
- [X] T013 [P] Create Config model in src/agentready/models/config.py (weights, excluded_attributes, language_overrides, output_dir)
- [X] T014 Create Assessment model in src/agentready/models/assessment.py (repository, timestamp, overall_score, certification_level, attributes_assessed, attributes_skipped, attributes_total, findings, config, duration_seconds)
- [X] T015 [P] Create BaseAssessor abstract interface in src/agentready/assessors/base.py with attribute_id, tier, assess(), is_applicable() methods
- [X] T016 [P] Implement LanguageDetector service in src/agentready/services/language_detector.py (file extension mapping, gitignore awareness)
- [X] T017 [P] Implement ResearchLoader service in src/agentready/services/research_loader.py (load bundled report, validate structure, support updates)
- [X] T018 Create Scorer service in src/agentready/services/scorer.py (tier-based weight calculation, certification level determination, score normalization)
- [X] T019 Create Scanner service in src/agentready/services/scanner.py (orchestrate assessment workflow, try-assess-skip error handling, progress tracking)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Score Repository Against Agent-Ready Criteria (Priority: P1) 🎯 MVP

**Goal**: Assess repository against all 25 attributes and generate overall agent-readiness score with findings

**Independent Test**: Run agentready on any git repository and verify it produces valid JSON assessment data with score, certification level, and findings for all 25 attributes

### Implementation for User Story 1

#### Assessor Implementations (12 category assessors for 25 attributes)

- [ ] T020 [P] [US1] Implement DocumentationAssessor in src/agentready/assessors/documentation.py (attributes 1.1-2.3: CLAUDE.md, README size, docstrings, ADRs)
- [ ] T021 [P] [US1] Implement CodeQualityAssessor in src/agentready/assessors/code_quality.py (attributes 3.1-3.4: cyclomatic complexity, file length, type annotations, code smells)
- [ ] T022 [P] [US1] Implement StructureAssessor in src/agentready/assessors/structure.py (attributes 4.1-4.2: layout patterns, separation of concerns)
- [ ] T023 [P] [US1] Implement TestingAssessor in src/agentready/assessors/testing.py (attributes 5.1-5.3: coverage, naming, pre-commit hooks)
- [ ] T024 [P] [US1] Implement DependenciesAssessor in src/agentready/assessors/dependencies.py (attributes 6.1-6.2: lock files, freshness/security)
- [ ] T025 [P] [US1] Implement VCSAssessor in src/agentready/assessors/vcs.py (attributes 7.1-7.3: conventional commits, gitignore, PR/issue templates)
- [ ] T026 [P] [US1] Implement BuildAssessor in src/agentready/assessors/build.py (attributes 8.1-8.3: one-command setup, build docs, containerization)
- [ ] T027 [P] [US1] Implement ErrorsAssessor in src/agentready/assessors/errors.py (attributes 9.1-9.2: error clarity, structured logging)
- [ ] T028 [P] [US1] Implement APIDocsAssessor in src/agentready/assessors/api_docs.py (attributes 10.1-10.2: OpenAPI/Swagger, GraphQL schemas)
- [ ] T029 [P] [US1] Implement ModularityAssessor in src/agentready/assessors/modularity.py (attributes 11.1-11.3: DRY violations, naming consistency, semantic files)
- [ ] T030 [P] [US1] Implement CICDAssessor in src/agentready/assessors/cicd.py (attributes 12.1-12.2: pipeline visibility, branch protection)
- [ ] T031 [P] [US1] Implement SecurityAssessor in src/agentready/assessors/security.py (attributes 13.1-13.2: security scanning, secrets management)
- [ ] T032 [P] [US1] Implement PerformanceAssessor in src/agentready/assessors/performance.py (attribute 15.1: performance benchmarks)

#### Core Workflow

- [ ] T033 [US1] Integrate all 13 assessors into Scanner service with parallel/sequential execution strategy
- [ ] T034 [US1] Implement Repository validation in Scanner (check for .git directory per FR-017)
- [ ] T035 [US1] Implement graceful degradation with MissingToolError, PermissionError handling per research.md
- [ ] T036 [US1] Implement progress tracking with assessed/skipped/error counts (FR-018, FR-028)
- [ ] T037 [US1] Implement weighted score calculation with tier-based defaults (FR-004, FR-031)
- [ ] T038 [US1] Implement certification level mapping (Platinum/Gold/Silver/Bronze/Needs Improvement per FR-016)
- [ ] T039 [US1] Add JSON serialization for Assessment model using dataclasses.asdict() per data-model.md
- [ ] T040 [US1] Implement Config loading from .agentready-config.yaml with weight validation (FR-032, FR-033)

#### CLI Interface

- [ ] T041 [US1] Create Click CLI entry point in src/agentready/cli/main.py with repository path argument
- [ ] T042 [US1] Add --verbose flag for detailed logging (FR-029)
- [ ] T043 [US1] Add --output-dir flag for custom report location (FR-021)
- [ ] T044 [US1] Add --config flag for custom configuration file path
- [ ] T045 [US1] Implement stdout progress summary and stderr error output (FR-028, FR-030)
- [ ] T046 [US1] Add --version flag showing agentready and research report versions

**Checkpoint**: At this point, User Story 1 should produce complete JSON assessment with score and findings

---

## Phase 4: User Story 2 - View Interactive HTML Report (Priority: P2)

**Goal**: Generate self-contained HTML report with interactive filtering, sorting, and collapsible sections

**Independent Test**: Generate HTML report and verify it opens in browser with working filters, sort controls, and expandable attribute details (no internet required)

### Implementation for User Story 2

- [X] T047 [P] [US2] Create Jinja2 template in src/agentready/templates/report.html.j2 with structure from contracts/report-html-schema.md
- [X] T048 [P] [US2] Add embedded CSS in template (header, controls, summary cards, findings, certification ladder, footer)
- [X] T049 [P] [US2] Add embedded JavaScript in template (filtering by status, sorting by score/tier/category, search, smooth scroll)
- [X] T050 [P] [US2] Implement BaseReporter interface in src/agentready/reporters/base.py with generate() method
- [X] T051 [US2] Implement HTMLReporter in src/agentready/reporters/html.py extending BaseReporter
- [X] T052 [US2] Add Jinja2 template rendering with Assessment data embedded as JSON constant
- [X] T053 [US2] Implement collapsible sections using HTML5 details/summary elements per contracts/report-html-schema.md
- [X] T054 [US2] Add color-coded score indicators (red <40, yellow 40-74, green 75+) per contracts/report-html-schema.md
- [X] T055 [US2] Add tier badges with color coding (Tier 1 red, Tier 2 orange, Tier 3 yellow, Tier 4 green)
- [X] T056 [US2] Implement category summary cards with progress bars and click-to-scroll behavior
- [X] T057 [US2] Add filter controls (All, Pass, Fail, Skipped) with dynamic count badges
- [X] T058 [US2] Add sort dropdown (Category, Score Asc/Desc, Tier) with JavaScript implementation
- [X] T059 [US2] Add search box with real-time attribute filtering
- [X] T060 [US2] Implement certification ladder with active level highlighting
- [X] T061 [US2] Add responsive breakpoints for mobile/tablet/desktop per contracts/report-html-schema.md
- [X] T062 [US2] Integrate HTMLReporter into Scanner workflow (dual-format generation per FR-005, FR-019)
- [X] T063 [US2] Add timestamp-based filename with latest symlink per research.md (report-2025-11-20T14-30-00.html)
- [X] T064 [US2] Verify HTML report works offline with no CDN dependencies (FR-003, SC-003)

**Checkpoint**: At this point, User Stories 1 AND 2 should produce both JSON and interactive HTML

---

## Phase 5: User Story 3 - Receive Remediation Guidance (Priority: P3)

**Goal**: For each failing attribute, provide actionable remediation with tools, commands, examples, and research citations

**Independent Test**: Review remediation sections in reports for failing attributes and verify they include specific tools, executable commands, and links to documentation

### Implementation for User Story 3

- [ ] T065 [P] [US3] Create remediation templates in src/agentready/assessors/base.py (summary, steps, tools, commands, examples, citations)
- [ ] T066 [P] [US3] Extract remediation guidance from agent-ready-codebase-attributes.md per attribute
- [ ] T067 [P] [US3] Add language-specific remediation commands (Python: black/pytest-cov, JS: eslint/jest, etc.)
- [ ] T068 [P] [US3] Add tool installation instructions in remediation.tools field (pip install, npm install, etc.)
- [ ] T069 [US3] Implement remediation generation in each assessor's assess() method for failing attributes
- [ ] T070 [US3] Add priority ranking in "Next Steps" section based on tier and point potential
- [ ] T071 [US3] Include research report citations in remediation.citations with source, title, url, relevance
- [ ] T072 [US3] Add code examples in remediation.examples showing before/after transformations
- [ ] T073 [US3] Update HTML template to display remediation in collapsible details blocks per contracts/report-html-schema.md
- [ ] T074 [US3] Add syntax highlighting for code blocks in remediation commands/examples using CSS
- [ ] T075 [US3] Verify all citations from research report preserved in outputs (SC-009)

**Checkpoint**: All user stories should now provide complete scoring, interactive viewing, and actionable remediation

---

## Phase 6: User Story 4 - Read Markdown Report for Version Control (Priority: P4)

**Goal**: Generate GitHub-Flavored Markdown report that renders properly in version control platforms and enables diff-based progress tracking

**Independent Test**: Generate Markdown report, commit to git, and verify it renders with tables, formatting, and links intact on GitHub

### Implementation for User Story 4

- [ ] T076 [P] [US4] Implement MarkdownReporter in src/agentready/reporters/markdown.py extending BaseReporter
- [ ] T077 [US4] Generate header section with repository metadata, timestamp, overall score per contracts/report-markdown-schema.md
- [ ] T078 [US4] Generate summary table with categories, scores, status emoji (✅⚠️❌)
- [ ] T079 [US4] Generate detailed findings with attribute subsections using proper heading hierarchy
- [ ] T080 [US4] Add collapsible remediation using details/summary HTML tags (valid in GFM)
- [ ] T081 [US4] Format evidence as bulleted lists with emoji indicators
- [ ] T082 [US4] Format remediation steps as ordered lists with code blocks (bash, python, yaml syntax highlighting)
- [ ] T083 [US4] Add certification level section with score ladder and "YOUR LEVEL" marker
- [ ] T084 [US4] Add "Next Steps" section with top 3-5 improvements ranked by tier and point potential
- [ ] T085 [US4] Generate footer with assessment metadata (duration, research version, repository snapshot)
- [ ] T086 [US4] Preserve all external citation links with absolute URLs per contracts/report-markdown-schema.md
- [ ] T087 [US4] Integrate MarkdownReporter into Scanner workflow (dual-format atomic generation per FR-019)
- [ ] T088 [US4] Add timestamp-based filename with latest symlink (report-2025-11-20T14-30-00.md)
- [ ] T089 [US4] Verify Markdown renders correctly on GitHub/GitLab/Bitbucket (SC-004)

**Checkpoint**: All four user stories complete - MVP delivers scoring, HTML viewing, remediation, and version control

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T090 [P] Create comprehensive unit tests in tests/unit/ for models, services, assessors (>80% coverage per constitution)
- [ ] T091 [P] Create integration tests in tests/integration/test_scan_workflow.py using fixture repositories per research.md
- [ ] T092 [P] Create contract tests in tests/contract/ validating report schemas against contracts/
- [ ] T093 [P] Create test fixtures in tests/fixtures/repositories/ (minimal-python, gold-standard-python, polyglot, edge-cases)
- [ ] T094 Add --update-research CLI command to download latest research report (FR-023, FR-024)
- [ ] T095 Add --generate-config CLI command to create example .agentready-config.yaml
- [ ] T096 Add --validate-config CLI command to check configuration file validity (FR-033)
- [ ] T097 Implement report cleanup logic (keep last N runs) per research.md
- [ ] T098 Add JSON sidecar files for automation integration (assessment-{timestamp}.json)
- [ ] T099 Optimize file system scanning with caching per research.md (don't traverse multiple times)
- [ ] T100 Add performance benchmarks ensuring <5 minutes for <10k files (SC-001)
- [ ] T101 Verify deterministic scoring (same input → same output) (SC-010)
- [ ] T102 Add language-specific analyzer lazy loading per research.md
- [ ] T103 [P] Update README.md with full usage documentation and examples
- [ ] T104 [P] Validate quickstart.md instructions work end-to-end (<5 minutes install to report)
- [ ] T105 Run black, isort, flake8 on entire codebase per constitution
- [ ] T106 Run pytest with coverage report ensuring >80% test coverage
- [ ] T107 Create package distribution configuration for PyPI (setup.py or pyproject.toml build config)
- [ ] T108 Add entry point configuration for `agentready` command in pyproject.toml

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User Story 1 (P1): Scoring engine - Can start after Phase 2
  - User Story 2 (P2): HTML reports - Depends on US1 JSON output
  - User Story 3 (P3): Remediation - Depends on US1 findings, enhances US2 HTML
  - User Story 4 (P4): Markdown reports - Depends on US1 JSON output
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: FOUNDATIONAL - Scoring engine required by all other stories
- **User Story 2 (P2)**: Consumes US1 JSON output, independently adds HTML generation
- **User Story 3 (P3)**: Enhances US1 findings and US2/US4 reports with remediation
- **User Story 4 (P4)**: Consumes US1 JSON output, independently adds Markdown generation

### Within Each User Story

- **US1**: Models → Services → Assessors → Scanner → CLI (sequential dependencies)
- **US2**: Template → Reporter → Integration (sequential)
- **US3**: Remediation templates → Assessor integration → Report integration (sequential)
- **US4**: Markdown reporter → Integration (sequential)

### Parallel Opportunities

- **Phase 1 (Setup)**: All tasks [P] can run in parallel (T003-T007)
- **Phase 2 (Foundational)**: All model creation tasks (T008-T014) can run in parallel, all service tasks (T016-T019) can run in parallel
- **Phase 3 (US1)**: All 13 assessor implementations (T020-T032) can run fully in parallel (different files)
- **Phase 4 (US2)**: Template design (T047-T049) can run in parallel, reporter features (T051-T064) sequential
- **Phase 5 (US3)**: Remediation extraction (T065-T068) can run in parallel
- **Phase 6 (US4)**: Markdown sections (T076-T086) largely parallelizable
- **Phase 7 (Polish)**: Test creation (T090-T093) can run in parallel, documentation (T103-T104) can run in parallel

**Note**: User Story 2 and User Story 4 could potentially be worked on in parallel after US1 completes, as both independently transform US1's JSON output to different formats.

---

## Parallel Example: User Story 1 Assessors

```bash
# Launch all 13 assessor implementations together:
T020: "Implement DocumentationAssessor in src/agentready/assessors/documentation.py"
T021: "Implement CodeQualityAssessor in src/agentready/assessors/code_quality.py"
T022: "Implement StructureAssessor in src/agentready/assessors/structure.py"
T023: "Implement TestingAssessor in src/agentready/assessors/testing.py"
T024: "Implement DependenciesAssessor in src/agentready/assessors/dependencies.py"
T025: "Implement VCSAssessor in src/agentready/assessors/vcs.py"
T026: "Implement BuildAssessor in src/agentready/assessors/build.py"
T027: "Implement ErrorsAssessor in src/agentready/assessors/errors.py"
T028: "Implement APIDocsAssessor in src/agentready/assessors/api_docs.py"
T029: "Implement ModularityAssessor in src/agentready/assessors/modularity.py"
T030: "Implement CICDAssessor in src/agentready/assessors/cicd.py"
T031: "Implement SecurityAssessor in src/agentready/assessors/security.py"
T032: "Implement PerformanceAssessor in src/agentready/assessors/performance.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T007)
2. Complete Phase 2: Foundational (T008-T019) - CRITICAL
3. Complete Phase 3: User Story 1 (T020-T046)
4. **STOP and VALIDATE**: Run agentready on test repository, verify JSON output
5. Optionally proceed to US2 (HTML) or US4 (Markdown) for human-readable reports

**Rationale**: US1 alone provides immediate value - repository owners get a comprehensive score with findings. HTML/Markdown reports enhance UX but core assessment functionality works without them.

### Incremental Delivery

1. **Sprint 1**: Setup + Foundational → Can run assessments programmatically
2. **Sprint 2**: User Story 1 → MVP with JSON output + CLI
3. **Sprint 3**: User Story 2 → Add interactive HTML reports
4. **Sprint 4**: User Story 3 → Add actionable remediation guidance
5. **Sprint 5**: User Story 4 → Add version-control-friendly Markdown reports
6. **Sprint 6**: Polish → Testing, optimization, documentation

### Parallel Team Strategy

With 3-4 developers after Foundational phase:

1. **Developer A**: User Story 1 (scoring engine)
2. **Developer B**: User Story 2 (HTML reporter) - starts after US1 JSON structure defined
3. **Developer C**: User Story 4 (Markdown reporter) - starts after US1 JSON structure defined
4. **Developer D**: User Story 3 (remediation) - coordinates with A/B/C to enhance outputs

**Critical Path**: US1 is on critical path (blocks US2/US3/US4). Parallelizing assessor implementations (T020-T032) is key to reducing US1 duration.

---

## Notes

- [P] tasks = different files, no dependencies, safe to parallelize
- [Story] label maps task to specific user story (US1, US2, US3, US4)
- Tests NOT included per constitution (TDD requested but not in spec)
- Each assessor is independently implementable (strategy pattern per research.md)
- Constitution compliance: library-first (assessors/services/models standalone), tool-second (CLI wrapper)
- File paths follow plan.md structure exactly
- Checkpoint after each user story enables incremental validation
- US1 assessors (T020-T032) are largest parallelization opportunity (13 independent files)
