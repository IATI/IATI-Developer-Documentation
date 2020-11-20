Code of practice
================

The IATI technical team follows a code of practice when developing and maintaining software:

- We should know which code is ‘ours’: when possible, IATI code should be a part of the IATI GitHub.
- Projects and code should be appropriately branded. Please email the IATI technical team for branding guidelines: support@iatistandard.org
- Projects and code should be in version control and present links to issue trackers and source code.
- Code should have a document, roadmap, estimate of resources and a licence.
- Updates to IATI code must not break existing functionality.
- Deployed code should be on servers available to the IATI technical team.
- Status of software should be indicated in deployments: development, staging and live versions should be properly identified.
- When possible, code should log details about its usage.
- Developers should be able to find help and useful resources easily.
- We should protect our users’ privacy and ensure our code is secure.
- Projects should have continuous integration and testing with Travis or other appropriate tools
- Projects should make use of Requires.io or other appropriate tools to ensure that dependencies are updated when possible.

Our Gitflow
-----------

1. Repositories should contain protected master and dev/develop branches.
2. Bug fixes and feature work should be branched off from the dev branch.
3. Pull requests from these branches are then made to the dev branch.
4. Code reviews for pull requests are made in local environments.
5. The dev branch is deployed and tested in a development environment or server.
6. Once the feature branches have been merged, deployed and tested in the development environment, a pull request can be made from the dev branch to the master branch.
7. The main/master branch is then deployed to the live environment.

  - Only the main/master branch should be deployed to live environments.
  - Urgent hotfixes can have pull requests done to the main/master branch and this should be undertaken only by the IATI Technical Team.
  - Content and general use reviews should be done in a staging environment, built using the development branch.
