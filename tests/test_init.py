import ready


def test_init() -> None:
    assert ready

    assert isinstance(ready.__version_info__, tuple)
    assert ready.__version_info__
    assert isinstance(ready.__version__, str)
    assert len(ready.__version__)
