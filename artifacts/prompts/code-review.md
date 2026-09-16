# Code review prompt

Do an independent review of the current diff. Do not assume the implementation is correct.

Check for:
- alignment with the acceptance criteria;
- logic errors and edge cases;
- authorization and access to other users' data;
- input validation;
- error handling;
- leaked secrets or personal data;
- API backward compatibility;
- missing tests.

For each issue, report severity, file and line, a reproduction scenario, and the minimal fix.
