import unittest
import Airport


class TestException(unittest.TestCase):

    def test_both_icao_iata_none_exc_parent(self):
        # Test that AirportLogicError is parent for BothIcaoIataNoneError
        self.assertTrue(Airport.BothIcaoIataNoneError.__bases__[0] == Airport.AirportLogicError)


class TestAirportConstructorPos(unittest.TestCase):

    def setUp(self):
        self.airport_ex = Airport.Airport('Los Angeles International Airport', iata='LAX', icao='KLAX')

    def test_name(self):
        # Test airport_ex NAME is correct
        self.assertEqual(self.airport_ex.name, 'Los Angeles International Airport')

    def test_iata(self):
        # Test airport_ex IATA is correct
        self.assertEqual(self.airport_ex.iata, 'LAX')

    def test_icao(self):
        # Test airport_ex ICAO is correct
        self.assertEqual(self.airport_ex.icao, 'KLAX')

    def test_name_type_str(self):
        # Make sure airport NAME type is STR
        self.assertIsInstance(self.airport_ex.name, str)
        # other ways to check types:
        # self.assertTrue(type(self.airport_ex.name) is str)
        # self.assertIs(type(self.airport_ex.name), str)
        # self.assertIs(self.airport_ex.name, str)
        # self.assertTrue(isInstance

    def test_iata_type_str(self):
        # Make sure airport IATA type is STR
        self.assertIsInstance(self.airport_ex.iata, str)

    def test_icao_type_str(self):
        # Make sure airport ICAO type is STR
        self.assertIsInstance(self.airport_ex.icao, str)


class TestAirportConstructorNeg(unittest.TestCase):

    def test_iata_and_icao_missing(self):
        # Test exception is raised if BOTH IATA and ICAO MISSING
        self.assertRaises(Airport.AirportLogicError, Airport.Airport, 'name')

    def test_name_type_none(self):
        # Make sure TypeError is raised if airport NAME is a NONE type
        self.assertRaises(TypeError, Airport.Airport, None, iata='LAX', icao='KLAX')

    def test_name_type_non_str(self):
        # Make sure TypeError is raised if airport NAME is a NON STR (bool) type
        self.assertRaises(TypeError, Airport.Airport, True, iata='LAX', icao='KLAX')

    def test_iata_type_non_str(self):
        # Make sure TypeError is raised if airport IATA is a NON STR (bool) type
        self.assertRaises(TypeError, Airport.Airport, 'Los Angeles International Airport', iata=True, icao='KLAX')

    def test_icao_type_non_str(self):
        # Make sure TypeError is raised if airport ICAO is a NON STR (bool) type
        self.assertRaises(TypeError, Airport.Airport, 'Los Angeles International Airport', iata='LAX', icao=True)

    def test_iata_too_short(self):
        # Make sure IATA is not too SHORT (2 symbols)
        self.assertRaises(ValueError, Airport.Airport, 'name', iata='LA')

    def test_iata_too_long(self):
        # Make sure IATA is not too LONG (4 symbols)
        self.assertRaises(ValueError, Airport.Airport, 'name', iata='LAXX')

    def test_icao_too_short(self):
        # Make sure ICAO is not too SHORT (3 symbols)
        self.assertRaises(ValueError, Airport.Airport, 'name', icao='KLA')

    def test_icao_too_long(self):
        # Make sure ICAO is not too LONG (5 symbols)
        self.assertRaises(ValueError, Airport.Airport, 'name', iata='KLAXX')


class TestAirportEq(unittest.TestCase):

    def setUp(self):
        self.airport_ex = Airport.Airport('Los Angeles International Airport', iata='LAX', icao='KLAX')

    def test_eq_same(self):
        # Make sure __eq__ method states 2 SAME airports are EQUAL
        self.assertEqual(self.airport_ex, Airport.Airport('Los Angeles International Airport', iata='LAX', icao='KLAX'))

    def test_eq_diff(self):
        # Make sure __eq__ method states 2 DIFF airports are NOT equal
        self.assertNotEqual(self.airport_ex, Airport.Airport('New York Airport', iata='JFK', icao='KJFK'))

    def test_eq_diff_name(self):
        # Make sure __eq__ method states 2 airports with DIFF NAMES are NOT equal
        self.assertNotEqual(self.airport_ex, Airport.Airport('LA Airport', iata='LAX', icao='KLAX'))

    def test_eq_diff_iata(self):
        # Make sure __eq__ method states 2 airports with DIFF IATA are NOT equal
        self.assertNotEqual(self.airport_ex, Airport.Airport('Los Angeles International Airport',
                                                             iata='JFK', icao='KLAX'))

    def test_eq_diff_icao(self):
        # Make sure __eq__ method states 2 airports with DIFF ICAO are NOT equal
        self.assertNotEqual(self.airport_ex, Airport.Airport('Los Angeles International Airport',
                                                             iata='LAX', icao='KJFK'))


class TestAirportFindAirportInList(unittest.TestCase):

    def setUp(self):
        self.airports_list = Airport.Airport.get_airports_from_csv('.\\test_data\\airports.csv', csv_header=True)

    def test_find_airport_in_list_by_name(self):
        # Make sure airport is found by its NAME
        self.assertEqual(Airport.Airport.find_airport_in_list('Los Angeles International Airport', self.airports_list),
                         Airport.Airport('Los Angeles International Airport', iata='LAX', icao='KLAX'))

    def test_find_airport_in_list_by_iata(self):
        # Make sure airport is found by IATA
        self.assertEqual(Airport.Airport.find_airport_in_list('LAX', self.airports_list),
                         Airport.Airport('Los Angeles International Airport', iata='LAX', icao='KLAX'))

    def test_find_airport_in_list_by_icao(self):
        # Make sure airport is found by ICAO
        self.assertEqual(Airport.Airport.find_airport_in_list('KLAX', self.airports_list),
                         Airport.Airport('Los Angeles International Airport', iata='LAX', icao='KLAX'))

    def test_find_airport_in_list_by_wrong_field(self):
        # Make sure empty list is returned if NO airport matches given field
        self.assertEqual(Airport.Airport.find_airport_in_list('OOOPSIE', self.airports_list), None)

    def test_find_airport_in_list_by_empty_field(self):
        # Make sure ValueError is raised if given field is EMPTY
        self.assertRaises(ValueError, Airport.Airport.find_airport_in_list, '', self.airports_list)


class TestAirportGetAirportsFromCsvPos(unittest.TestCase):

    def setUp(self):
        self.airports_list = Airport.Airport.get_airports_from_csv('.\\test_data\\airports.csv', csv_header=True)

    def test_get_airports_from_csv_correct_data(self):
        # List of airports from csv file and created with constructor should be EQUAL
        airports_list_to_compare = [Airport.Airport('Pulkovo', iata='LED', icao='ULLI'),
                                    Airport.Airport('Domodedovo', iata='DME', icao='UUDD'),
                                    Airport.Airport('Los Angeles International Airport', iata='LAX', icao='KLAX'),
                                    Airport.Airport('John F. Kennedy International Airport', iata='JFK', icao='KJFK')]
        self.assertEqual(Airport.Airport.get_airports_from_csv('.\\test_data\\airports.csv', csv_header=True),
                         airports_list_to_compare)

    def test_get_airports_from_csv_empty_file(self):
        # Test EMPTY LIST is returned if FILE is EMPTY
        self.assertEqual(Airport.Airport.get_airports_from_csv('.\\test_data\\airports_empty.csv'), [])

    def test_get_airports_from_csv_header_only(self):
        #  Test EMPTY LIST is returned if file has HEADER ONLY
        self.assertEqual(Airport.Airport.get_airports_from_csv('.\\test_data\\airports_header_only.csv',
                                                               csv_header=True), [])

    def test_get_airports_from_csv_empty_name(self):
        #  Test list with empty names is returned if csv file has empty names
        airports_list_to_compare = [Airport.Airport('', iata='LED', icao='ULLI'),
                                    Airport.Airport('', iata='DME', icao='UUDD'),
                                    Airport.Airport('', iata='LAX', icao='KLAX'),
                                    Airport.Airport('', iata='JFK', icao='KJFK')]
        self.assertEqual(Airport.Airport.get_airports_from_csv('.\\test_data\\airports_empty_name.csv',
                                                               csv_header=True), airports_list_to_compare)

    def test_get_airports_from_csv_empty_name_and_iata(self):
        #  Test list with empty names and iata is returned if csv file has empty names and iata
        airports_list_to_compare = [Airport.Airport('', iata='', icao='ULLI'),
                                    Airport.Airport('', iata='', icao='UUDD'),
                                    Airport.Airport('', iata='', icao='KLAX'),
                                    Airport.Airport('', iata='', icao='KJFK')]
        self.assertEqual(Airport.Airport.get_airports_from_csv('.\\test_data\\airports_empty_name_and_iata.csv',
                                                               csv_header=True), airports_list_to_compare)

    def test_get_airports_from_csv_empty_name_and_icao(self):
        #  Test list with empty names and icao is returned if file has empty names and icao
        airports_list_to_compare = [Airport.Airport('', iata='LED', icao=''),
                                    Airport.Airport('', iata='DME', icao=''),
                                    Airport.Airport('', iata='LAX', icao=''),
                                    Airport.Airport('', iata='JFK', icao='')]
        self.assertEqual(Airport.Airport.get_airports_from_csv('.\\test_data\\airports_empty_name_and_icao.csv',
                                                               csv_header=True), airports_list_to_compare)


class TestAirportGetAirportsFromCsvNeg(unittest.TestCase):

    def test_get_airports_from_csv_wrong_file(self):
        # Test IOError is raised if NON EXISTING FILE NAME is given
        self.assertRaises(IOError, Airport.Airport.get_airports_from_csv, '.\\test_data\\airports_none.csv')

    def test_get_airports_from_csv_wrong_extension(self):
        # Test IOError is raised if WRONG file EXTENSION is given
        self.assertRaises(IOError, Airport.Airport.get_airports_from_csv, '.\\test_data\\airports.txt')

    # TO DO
    # def test_get_airports_from_csv_locked(self):
    #     # Test IOError is raised if file is LOCKED
    #     # To do - implement locking file with python
    #     self.assertRaises(IOError, Airport.Airport.get_airports_from_csv, '.\\test_data\\airports_locked.csv')

    def test_get_airports_from_csv_empty_data(self):
        #  Test Airport.AirportLogicError is raised if file has EMPTY DATA separated WITH COMMAS
        #  (both IATA and ICAO missing check)
        self.assertRaises(Airport.AirportLogicError, Airport.Airport.get_airports_from_csv,
                          '.\\test_data\\airports_empty_data.csv')

    def test_get_airports_from_csv_data_long(self):
        # Test ValueError is raised if airport DATA is TOO LONG (more than 3 fields)
        # ??? Probably this check should be removed (test and code) as it is OK to have more data ???
        self.assertRaises(ValueError, Airport.Airport.get_airports_from_csv,
                          '.\\test_data\\airports_data_long.csv', csv_header=True)

    def test_get_airports_from_csv_data_short(self):
        # Test ValueError is raised if airport DATA is too SHORT (less than 3 fields, ex. 2)
        self.assertRaises(ValueError, Airport.Airport.get_airports_from_csv,
                          '.\\test_data\\airports_data_short.csv', csv_header=True)

if __name__ == '__main__':
    unittest.main()






