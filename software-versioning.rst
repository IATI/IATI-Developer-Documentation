IATI Software Versioning Protocol
=================================

Beginning with the release of the first version of the IATI Validator (September 2020) to be adopted across our products, we version software in the common three element format - Major.Minor.Patch.
We adopt this form, following as closely as possible the rules defined at `Semantic Versioning 2.0.0 <https://semver.org/>`__  

In addition, we add a layer of meaning in regard to communication, illustrated in the table below:

.. list-table::
    :header-rows: 1

    * - 
      - Major
      - Minor
      - Patch

    * - **Communicate Externally**
      - Yes
      - Yes
      - No
    
    * - **Consult Externally**
      - Yes
      - No
      - No

In other words:

- **If a change is a Major Version bump, it requires us to consult with the external community**, for example 1.0.0 to 2.0.0. This might include a major change to a UI or breaking changes to a public facing API.
- **If a change is a Minor Version bump, it requires us to publish a notification of changes externally**, for example 1.0.0 to 1.1.0. This might include minor changes to a UI or non-breaking functional changes to a public facing API, for example the addition of a parameter.
- **If a change is a Patch, it does not require external communication**, for example 1.0.1 to 1.0.2. This would include bug fixes and other changes that make no functional difference.

Details of all code changes are available in GitHub Releases for each repository: 

  https://github.com/IATI/<repository-name>/releases
