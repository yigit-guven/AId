# Changelog

All notable changes to **AId** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.3] - 2026-09-24

### Security
- Pinned `softprops/action-gh-release` in the release workflow to a full commit SHA (`3bb1273` / v2.6.2) to remediate CodeQL unpinned-tag security alert.

## [0.1.2] - 2026-09-23

### Changed
- Restricted CodeQL workflow triggers to Python source files, workflows, and dependency manifests, ignoring documentation and markdown edits.

## [0.1.1] - 2026-09-23

### Added
- Automated CodeQL static analysis and security scanning workflow.
- Automated version synchronization for `CITATION.md` and `SECURITY.md` in the release pipeline.
- Discord Developer Portal compliance policies: `TERMS_OF_SERVICE.md` and `PRIVACY_POLICY.md`.
- Contributor guidelines in `CONTRIBUTING.md` and Contributor Covenant in `CODE_OF_CONDUCT.md`.
- Structured pull request template `.github/pull_request_template.md`.
- Environment template `.env.example` and standard `.gitignore`.
- Repository `CODEOWNERS` and academic citation reference in `CITATION.md`.
- Expanded GitHub issue templates for prompt schemas, performance reports, and community support links.

## [0.1.0] - 2026-09-23

### Added
- Project foundation, architecture guidelines, and repository setup.
- Core project documentation, installation steps, and environment configuration in `README.md`.
- GitHub issue templates and vulnerability disclosure guidelines in `SECURITY.md`.
- Automated release workflow and GitHub wiki synchronization.
