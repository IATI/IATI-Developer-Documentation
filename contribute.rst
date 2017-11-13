Contribution Guide
==================

IATI is a living project with a number of tools that are owned by the IATI Secretariat. We are an open-source project and we encourage code contributions.

Please follow this guide if you wish your Pull Requests to be reviewed by us. This guide was created with to ensure your contributions have a meaningful long-term impact on the IATI code base by ensuring your code can be maintained over the long-term. It is also beneficial to open a Github Issue about any significant features you may wish to add as we reserve the right to reject pull requests that clash with, or otherwise hinder, existing or ongoing work.

This style guide is inspired by the `React contribution guides <https://facebook.github.io/react-native/docs/contributing.html#how-to-contribute>`_.

Code Conventions
-------------------------

It is important to remember that IATI is still a relatively young project and so our current code base has varying standards of code quality and style. We are continuously working towards improving this situation. With this in mind, we ask that you use our `pyIATI <https://github.com/IATI/pyIATI>`_ work as the expected standard to work towards.

`pyIATI is part of our current work to improve the stability and maintainability of our
infrastructure <https://discuss.iatistandard.org/t/introducing-the-iati-python-library/720>`_ and we believe it exemplifies our move towards stronger architecture and adoption of industry-standard best practices wherever possible and be consistent with the coding style used with this project whenever possible.

For guiding principles we use: `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ and the `Google Python Style
Guide <https://google.github.io/styleguide/pyguide.html>`_.

Generally speaking we expect all contributions to adhere to the following conventions:

-  Human readable code:

   - Write your code clearly with descriptive variable names.
   - Write your code with the intention that any developer could read it.
   - You are contributing to a community - write your code for them, not just for you.

-  Robustly tested code:

   -  All core functionality unit tested with `py.test <https://docs.pytest.org/en/latest/>`_ and edge cases considered. We strongly suggest you use Test Driven Development. We also require details and evidence of any manual testing to show no existing functionality is unexpectedly broken.

-  Documented code:

   -  We expect a clear docstring per module, class, and function, explaining what it does at a minimum. This is to reduce developer onboarding time and reduce barriers to entry for new developers who want to get involved. They should be formatted as per `Google-style Sphinx Docstrings <http://www.sphinx-doc.org/en/stable/ext/example_google.html>`_.

-  No code smells:

   -  Don’t Repeat Yourself, keep your code DRY.

   -  Avoid excessive use of conditional statements, your functions should be doing the minimum possible for maximum effect. Think about `polymorphism <https://www.digitalocean.com/community/tutorials/how-to-apply-polymorphism-to-classes-in-python-3>`_ and the `Single Responsibility Princible (SRP) <https://robots.thoughtbot.com/back-to-basics-solid#single-responsibility-principle>`_.

   -  Consider `other kinds of code smell <https://sourcemaking.com/refactoring/smells>`_.

-  Use `pyIATI <https://github.com/IATI/pyIATI>`_ wherever possible:

   -  We have built this library with the intention of reducing the need to reinvent the wheel. We want to improve the time it takes for external developers to contribute to our code base. As time goes on pyIATI will have increased functionality for many common tasks needed to interface with IATI data. Keep an eye on the `changelog <https://github.com/IATI/pyIATI/blob/master/CHANGELOG.md>`_ for updates on what pyIATI can do and planned improvements.

Linting
---------

We run:

-  pylint

-  flake8

-  pydocstyle

We run these locally in editors and as git-hooks to prevent commits from being made when the linters do not pass. These linters also run as part of our automated tests to aid contributors with their linting. We expect all code to pass the linters before we review it.

You may add in-line linting exceptions in these scenarios:

-  Where linting rules obscure function or variable names clarity should be prioritised over linting.

-  Docstrings are not expected to adhere to low line length limits. Please soft-wrap docstrings in your code editor if you don’t like long lines. Hard-wrapping must never be undertaken mid-sentence.

Relevant sources:
------------------------

-  What is good code?
       `*https://robots.thoughtbot.com/what-is-good-code* <https://robots.thoughtbot.com/what-is-good-code>`__

-  Writing good unit tests:
       `*http://defragdev.com/blog/?p=783* <http://defragdev.com/blog/?p=783>`__

-  Test Driven Development:
       `*https://www.madetech.com/blog/9-benefits-of-test-driven-development* <https://www.madetech.com/blog/9-benefits-of-test-driven-development>`__

-  Refactoring unruly code:
       `*https://sourcemaking.com/refactoring/refactorings* <https://sourcemaking.com/refactoring/refactorings>`__



The following section is to be reviewed for relevant content:



Contributing
============

We appreciate all contributions to our open source projects.

* We're interested in user experience and feedback from using the application.
* We'd like people to fix bugs and contribute to features.
* We're interested in people using the code for their own purposes.
* We're interested in suggestions, modifications and improvements.

All our code can be found at https://github.com/IATI

Each project should have a specific ``CONTRIBUTING.rst`` file that gives more specific information about how to contribute to that particular project.

Everything we are working on, or considering, is kept in GitHub issues. Feel free to contribute to any of these.

Bitesize issues
^^^^^^^^^^^^^^^
Getting started on someone else's software project can be daunting. So when we have an issue that we think would be a good task for someone new to the project, we mark them as  Bitesize.

Look for issues marked with the `Bitesize <https://github.com/issues?q=is%3Aopen+is%3Aissue+user%3AIATI+label%3ABitesize>`__ label if you want somewhere to start.
