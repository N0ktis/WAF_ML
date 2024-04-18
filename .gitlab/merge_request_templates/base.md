## New MR checklist
When adding a new MR, make sure:
- [ ] merge request is associated with a Youtrack issue (MR name must start with ML-{issue_id}.{short_description}). This can be cover with [push-rules](https://docs.gitlab.com/ee/user/project/repository/push_rules.html#validate-branch-names)
- [ ] Add issue_id at the end of MR description. If you want this MR to be linked to youtrack history
- [ ] Main ideas are highlighted:
    - [ ] What is the purpose of MR?
    - [ ] Do not forget to add tests
    - [ ] Link to mlflow experiment (if available)
    - [ ] Link to wiki documentation (if available)
