import unittest
import csv
from get_user_infs import get_user_infs


class GetUserInfsTest(unittest.TestCase):
    def setUp(self):
        self.user_infs = get_user_infs()
        self.user_infs.execute()

    # 1 - Crie um teste onde self._user é um array e é maior do que zero (objetivo é verificar) se os dados estão
    # sendo retornados no banco de dados.
    def test_user_array_not_empty(self):
        assert len(self.user_infs._users) > 0

    # 2 - Crie um teste em self._user que acesse uma determinada linha (pode ser a primeira posição)
    # e verifique se o dicionário contem os seguintes atributos:
    # name, age, document e data_record
    def test_user_dictionary_contains_attributes(self):
        user_dict = self.user_infs._users[0]
        expected_attributes = ["name", "age", "document", "data_record"]
        for attribute in expected_attributes:
            assert attribute in user_dict

    # 3 - Crie um teste em self._before_data_structure que avalie se existem os seguintes atributos:
    # "name", "age", "document", "data_record"
    def test_before_data_structure_contains_attributes(self):
        expected_attributes = ["name", "age", "document", "data_record"]
        for attribute in expected_attributes:
            assert attribute in self.user_infs._before_data_structure

    # 4 - Ainda na mesma variável de três, crie um teste para verificar apenas esses atributos existem,
    # se não há mais nenhum para além desses sendo criado.
        assert set(self.user_infs._before_data_structure.keys()) == set(expected_attributes)

    # 5 - Crie um teste que verifique se o arquivo file.csv realmente foi criado ao término da execução do software.
    def test_csv_file_created(self):
        try:
            with open("file.csv", "r") as file:
                pass
        except FileNotFoundError:
            assert False

    # 6 - Crie um teste que verifique se o conteúdo do arquivo corresponde ao que se faz presente
    # dentro do array self._user
    def test_csv_file_content(self):
        with open("file.csv", "r") as file:
            reader = csv.DictReader(file)
            csv_data = list(reader)

        assert csv_data == self.user_infs._users


if __name__ == '__main__':
    unittest.main()
