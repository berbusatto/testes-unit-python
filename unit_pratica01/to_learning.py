import pandas as pd
import unittest


class get_user_infs:
    def __init__(self):
        self._clients = []
        self._before_data_structure = {}
        self._pd_structure = None

    def execute(self):
        self._get_clients()
        self._select_infs_of_user()
        self._build_pandas_structure()
        self._write_csv_file()

    def _get_clients(self):
        self._clients.append(
            self._structure_of_db(
                "Jose",
                23,
                "Engenheiro Civil"
            )
        )

        self._clients.append(
            self._structure_of_db(
                "Alexandre",
                30,
                "Juíz"
            )
        )

        self._clients.append(
            self._structure_of_db(
                "Aline",
                29,
                "Médica"
            )
        )

        self._clients.append(
            self._structure_of_db(
                "Fernando",
                21,
                "Desenvolvedora de Software"
            )
        )

        self._clients.append(
            self._structure_of_db(
                "Cassia",
                31,
                "Dentista"
            )
        )

    def _select_infs_of_user(self):
        self._before_data_structure['name'] = list(map(lambda element: element["name"], self._clients))
        self._before_data_structure['age'] = list(map(lambda element: element["age"], self._clients))
        self._before_data_structure['job'] = list(map(lambda element: element["job"], self._clients))

    def _build_pandas_structure(self):
        self._pd_structure = pd.DataFrame(
            data=self._before_data_structure
        )

    def _write_csv_file(self):
        self._pd_structure.to_csv("file.csv")

    def _structure_of_db(self, name, age, job):
        return {
            "name": name,
            "age": age,
            "job": job
        }


class Test_get_user_infs(unittest.TestCase):

    def test_get_clients(self):
        get_user_infs_test_one = get_user_infs()
        get_user_infs_test_one._get_clients()

        self.assertNotEqual(len(get_user_infs_test_one._clients), 0)

    def test_select_infs_of_user(self):
        select_infs_test = get_user_infs()
        select_infs_test._select_infs_of_user()

        self.assertIn('job', select_infs_test._before_data_structure)


if __name__ == '__main__':
    unittest.main()
