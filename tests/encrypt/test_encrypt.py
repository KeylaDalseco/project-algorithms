import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    'Testa se a função, quando passados dados válidos, retorna o encrypt'
    assert encrypt_message('testee', 3) == 'set_eet'
    with pytest.raises(TypeError):
        encrypt_message("testee", "key_inválida")
    with pytest.raises(TypeError):
        encrypt_message(123, 3)
    'Testa se a função, quando passado key fora da range, retorna o erro'
    assert encrypt_message("testee", 20) == 'eetset'
