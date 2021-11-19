{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
        :alt: GitHub
{% if cookiecutter.use_pypi_deployment_with_travis == 'y' or cookiecutter.deploy_to_pypy == 'y' %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
{%- endif %}
{% if cookiecutter.use_pypi_deployment_with_travis == 'y' %}
.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
{%- endif %}
{% if cookiecutter.use_circleci == 'y' %}
.. image:: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tree/master.svg?style=shield
        :target: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tree/master 
{%- endif %}
.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status
{%- endif %}
{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates
{%- endif %}
{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and `rstms/cookiecutter-python-cli`, a fork of the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`rstms/cookiecutter-python-cli`: https://github.com/rstms/cookiecutter-python-cli
