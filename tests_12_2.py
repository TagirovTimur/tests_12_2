from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_Ysein = Runner("Усэйн",10)
        self.runner_Andrey = Runner("Андрей", 9)
        self.runner_Nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_running_1(self):
        running = Tournament(90, self.runner_Ysein,self.runner_Nik)
        result = running.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'ошибка')
        self.all_results['running_1'] = result



    def test_running_2(self):
        running = Tournament(90, self.runner_Andrey,self.runner_Nik)
        result = running.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник','ошибка')
        self.all_results['running_2'] = result

    def test_running_3(self):
        running = Tournament(90, self.runner_Ysein,self.runner_Andrey,self.runner_Nik)
        result = running.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник','ошибка')
        self.all_results['running_3'] = result

    if __name__ == '__main__':
        unittest.main()