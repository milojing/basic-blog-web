# -*- coding: utf-8 -*-

from basicblogweb.cli import main

from click.testing import CliRunner


def test_cli_should_echo_hello():
    """The basic test, which tests if cli works.
    GIVEN: command.
    WHEN: No option is given.
    THEN: cli should echo message with default value of option.
    """
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.exit_code == 0
    assert 'Hello welcome to use basic-blog-web' in result.output