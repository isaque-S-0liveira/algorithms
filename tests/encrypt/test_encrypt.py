import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError) as exc_info:
        encrypt_message("message", "key")
    assert str(exc_info.value) == "tipo inválido para key"

    with pytest.raises(TypeError) as exc_info:
        encrypt_message(3, 2)
    assert str(exc_info.value) == "tipo inválido para message"

    message = "xablau"
    key = 7
    encrypted_message = encrypt_message(message, key)
    assert encrypted_message == "ualbax"

    message = "xablau"
    key = 2
    encrypted_message = encrypt_message(message, key)
    assert encrypted_message == "ualb_ax"

    message = "xablau"
    key = 3
    encrypted_message = encrypt_message(message, key)
    assert encrypted_message == "bax_ual"
