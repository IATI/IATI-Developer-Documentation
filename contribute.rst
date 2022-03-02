Developer contributions
=======================

IATI is an open data standard and developers are encouraged to build tools that are open source, to allow for code contributions. `IATI's GitHub organisation account <https://github.com/IATI>`__ are the place to comment on IATI software, to raise a bug or to see what is happening at the code level with our various tools.

Raising issues
--------------

For bugs, feature requests, or other general enquiries about the IATI code base, we ask that appropriate issues are raised in the corresponding repository. Please follow templates provided to raise different types of issues, to help both the IATI Technical Team and other users to understand the context.

To make it clear what is currently a problem and being actively addressed, we only keep active issues open and will ask contributors to close issues that have been resolved or are not currently reproducible in the codebase.

Making pull requests
--------------------
Pull requests must be made from forked versions of our repositories and should be made towards development branches of the repository when available. Branches must be clearly identified and given the number of the issue linked to it (i.e. 43-adding-button).

Please follow this guide if you wish to have your pull requests reviewed by the IATI Technical Team. This guide was created to ensure that contributions have a meaningful long-term impact on the IATI code base. It is also beneficial to open a GitHub issue about any significant features you may wish to add, as the IATI Technical Team reserves the right to reject pull requests that fall outside their scheduled work.

Contributions must follow the following conventions.

- Human readable code
  - Write your code clearly with descriptive variable names.
  - Write your code so that any developer could read it.
  - You are contributing to a community – write your code for the members, as well as for yourself.
- Robustly tested code
  - All core functionality is to be unit tested and edge cases considered. We strongly suggest that you use Test Driven Development. We also require details and evidence of any manual testing to show that no existing functionality is unexpectedly broken.
- Documented code
  - We expect a clear docstring per module, class and function, explaining what it does at a minimum. This is to reduce both developer onboarding time and the barriers to entry for new developers who want to contribute.
- General coding principles
  - Don’t Repeat Yourself: keep your code DRY.
  - Avoid excessive use of conditional statements; your functions should be doing the minimum possible for maximum effect.
  - Consider polymorphism and the single responsibility principle when viable.
  - KISS: keep it short and simple.

For detailed information about contributing to IATI tools maintained by the IATI Technical Team, please review the CONTRIBUTING.rst files for the repository you wish to work with.

Contributing to IATI tools managed by external vendors
------------------------------------------------------

For contributions to IATI tools that are not directly managed by the IATI Technical Team, please refer to the vendor’s contribution guidelines. These tools include `d-portal <https://github.com/devinit/D-Portal>`__.
