import unittest
import dex
import pandas as pd
import numpy as np


class TestingDEX(unittest.TestCase):
    def setUp(self):
        self.dexmodel = dex.DEXModel("./SKP Evaluation version 3.xml")
        self.indata = pd.read_csv("optionsDexHeacat3.dat", delimiter="\t").set_index(
            "Unnamed: 0"
        )

    def test_loaded(self):
        default = self.dexmodel.get_intput_attributes()

    def __prepare_data(self, key):
        data = dict()
        for k in self.dexmodel.get_intput_attributes():
            data[k] = self.indata[key][k]

        return data

    def __compare(self, key, eres):
        # print(np.sort(self.indata[key]['SKP Evaluation'].split(';')))
        # print(np.sort(eres['SKP Evaluation']))
        return np.all(
            np.sort(self.indata[key]["SKP Evaluation"].split(";"))
            == np.sort(eres["SKP Evaluation"])
        )

    def test_barmen_Mons(self):
        data = self.__prepare_data("barmen Mons")
        eres, qq_res = self.dexmodel.evaluate_model(data)

        self.assertTrue(self.__compare("barmen Mons", eres))

    def test_barmen_Coffee_shop(self):
        data = self.__prepare_data("barmen Coffee shop")
        eres, qq_res = self.dexmodel.evaluate_model(data)

        self.assertTrue(self.__compare("barmen Coffee shop", eres))

    def test_barmen_Union(self):
        data = self.__prepare_data("barmen Union")
        eres, qq_res = self.dexmodel.evaluate_model(data)

        self.assertTrue(self.__compare("barmen Union", eres))

    def test_barmen_Test(self):
        data = self.__prepare_data("barmen Test")
        eres, qq_res = self.dexmodel.evaluate_model(data)

        self.assertTrue(self.__compare("barmen Test", eres))


if __name__ == "__main__":
    unittest.main()
