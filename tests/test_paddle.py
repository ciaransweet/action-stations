from assertpy import assert_that

from src.paddle import ping


def test_that_paddle_pongs_when_pinged():
    assert_that(ping()).is_equal_to("pong")
