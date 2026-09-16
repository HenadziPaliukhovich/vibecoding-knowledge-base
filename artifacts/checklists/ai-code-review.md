# AI-generated code review checklist

- [ ] The requirement maps to the acceptance criteria
- [ ] The diff is scoped to one logical task
- [ ] No unexpected changes outside the agreed scope
- [ ] New dependencies are justified
- [ ] No secrets or personal data leaked into code or logs
- [ ] Input is validated
- [ ] Authorization is checked at the resource level
- [ ] Errors are not swallowed and return the expected contract
- [ ] API preserves backward compatibility, or the change is documented
- [ ] Happy path and negative scenarios are covered by tests
- [ ] Linter, tests, dependency audit, and security checks pass
- [ ] The change was manually verified in a user scenario
