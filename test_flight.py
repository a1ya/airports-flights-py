import unittest
import Airport
import Flight
from xml.etree.ElementTree import ParseError
from lxml import etree


class TestFlightConstructorPos(unittest.TestCase):

    def setUp(self):
        self.airport_1 = Airport.Airport('John F. Kennedy International Airport', iata='JFK', icao='KJFK')
        self.airport_2 = Airport.Airport('Los Angeles International Airport', iata='LAX', icao='KLAX')
        self.flight_ex = Flight.Flight('AD832', 'Virgin America',
                                       airport_from=self.airport_1, airport_to=self.airport_2)

    def test_flight_number(self):
        # Make sure flight_ex FLIGHT_NUMBER is correct
        self.assertEqual(self.flight_ex.flight_number, 'AD832')

    def test_airline(self):
        # Make sure flight_ex AIRLINE is correct
        self.assertEqual(self.flight_ex.airline, 'Virgin America')

    def test_airport_from(self):
        # Make sure flight_ex AIRPORT_FROM is correct
        self.assertEqual(self.flight_ex.airport_from, self.airport_1)

    def test_airport_to(self):
        # Make sure flight_ex AIRPORT_TO is correct
        self.assertEqual(self.flight_ex.airport_to, self.airport_2)

    def test_flight_number_type_str(self):
        # Make sure FLIGHT_NUMBER type is STR
        self.assertIsInstance(self.flight_ex.flight_number, str)  # str

    def test_airline_type_str(self):
        # Make sure AIRLINE type is STR
        self.assertIsInstance(self.flight_ex.airline, str)  # str

    def test_airport_from_type_airport(self):
        # Make sure AIRPORT_FROM is an instance of AIRPORT CLASS
        self.assertIsInstance(self.flight_ex.airport_from, Airport.Airport)  # Airport

    def test_airport_to_type_airport(self):
        # Make sure AIRPORT_TO is an instance of AIRPORT CLASS
        self.assertIsInstance(self.flight_ex.airport_to, Airport.Airport)  # Airport


class TestFlightConstructorNeg(unittest.TestCase):

    def setUp(self):
        self.airport_1 = Airport.Airport('John F. Kennedy International Airport', iata='JFK', icao='KJFK')
        self.airport_2 = Airport.Airport('Los Angeles International Airport', iata='LAX', icao='KLAX')

    def test_flight_number_type_none(self):
        # Make sure TypeError is raised if FLIGHT_NUMBER is a NONE type
        self.assertRaises(TypeError, Flight.Flight, None, 'Virgin America',
                          airport_from=self.airport_1, airport_to=self.airport_2)  # None

    def test_flight_number_type_non_str(self):
        # Make sure TypeError is raised if FLIGHT_NUMBER is a NON STR (bool) type
        self.assertRaises(TypeError, Flight.Flight, True, 'Virgin America',
                          airport_from=self.airport_1, airport_to=self.airport_2)  # bool

    def test_airline_type_none(self):
        # Make sure TypeError is raised if AIRLINE is a NONE
        self.assertRaises(TypeError, Flight.Flight, 'AD832', None,
                          airport_from=self.airport_1, airport_to=self.airport_2)  # None

    def test_airline_type_non_str(self):
        # Make sure TypeError is raised if AIRLINE is a NON STR (bool) type
        self.assertRaises(TypeError, Flight.Flight, 'AD832', True,
                          airport_from=self.airport_1, airport_to=self.airport_2)  # bool

    def test_airport_from_type_none(self):
        # Make sure TypeError is raised if AIRPORT_FROM is a NONE
        self.assertRaises(TypeError, Flight.Flight, 'AD832', 'Virgin America',
                          airport_from=None, airport_to=self.airport_2)  # None

    def test_airport_from_type_str(self):
        # Make sure TypeError is raised if AIRPORT_FROM is STR (instead of Airport)
        self.assertRaises(TypeError, Flight.Flight, 'AD832', 'Virgin America',
                          airport_from='Los Angeles International Airport, LAX, KLAX',
                          airport_to=self.airport_2)  # str

    def test_airport_to_type_none(self):
        # Make sure TypeError is raised if AIRPORT_TO is a NONE
        self.assertRaises(TypeError, Flight.Flight, 'AD832', 'Virgin America',
                          airport_from=self.airport_1, airport_to=None)  # None

    def test_airport_to_type_str(self):
        # Make sure TypeError is raised if AIRPORT_TO is STR (instead of Airport)
        self.assertRaises(TypeError, Flight.Flight, 'AD832', 'Virgin America',
                          airport_from=self.airport_1,
                          airport_to='John F. Kennedy International Airport, JFK, KJFK')  # str


class TestFlightEq(unittest.TestCase):

    def setUp(self):
        self.airport_1 = Airport.Airport('John F. Kennedy International Airport', iata='JFK', icao='KJFK')
        self.airport_2 = Airport.Airport('Los Angeles International Airport', iata='LAX', icao='KLAX')
        self.flight_ex = Flight.Flight('AD832', 'Virgin America',
                                       airport_from=self.airport_1, airport_to=self.airport_2)

    def test_eq_same(self):
        # Make sure __eq__ method states 2 SAME flights are EQUAL
        self.assertEqual(self.flight_ex,
                         Flight.Flight('AD832', 'Virgin America',
                                       airport_from=Airport.Airport('John F. Kennedy International Airport',
                                                                    iata='JFK', icao='KJFK'),
                                       airport_to=Airport.Airport('Los Angeles International Airport',
                                                                  iata='LAX', icao='KLAX')))

    def test_eq_diff(self):
        # Make sure __eq__ method states 2 DIFF flights are NOT equal
        self.assertNotEqual(self.flight_ex,
                            Flight.Flight('AM13', 'S7',
                                          airport_from=Airport.Airport('Pulkovo', iata='LED', icao='ULLI'),
                                          airport_to=Airport.Airport('Domodedovo', iata='DME', icao='UUDD')))

    def test_eq_diff_flight_number(self):
        # Make sure __eq__ method states 2 flights with DIFF FLIGHT_NUMBERS are NOT equal
        self.assertNotEqual(self.flight_ex,
                            Flight.Flight('XXXXX', 'Virgin America',
                                          airport_from=Airport.Airport('John F. Kennedy International Airport',
                                                                       iata='JFK', icao='KJFK'),
                                          airport_to=Airport.Airport('Los Angeles International Airport',
                                                                     iata='LAX', icao='KLAX')))

    def test_eq_diff_airline(self):
        # Make sure __eq__ method states 2 flights with DIFF AIRLINES are NOT equal
        self.assertNotEqual(self.flight_ex,
                            Flight.Flight('AD832', 'XXXXX Airlines',
                                          airport_from=Airport.Airport('John F. Kennedy International Airport',
                                                                       iata='JFK', icao='KJFK'),
                                          airport_to=Airport.Airport('Los Angeles International Airport',
                                                                     iata='LAX', icao='KLAX')))

    def test_eq_diff_airport_from(self):
        # Make sure __eq__ method states 2 flights with DIFF AIRPORTS_FROM are NOT equal
        self.assertNotEqual(self.flight_ex,
                            Flight.Flight('AD832', 'Virgin America',
                                          airport_from=Airport.Airport('Pulkovo', iata='LED', icao='ULLI'),
                                          airport_to=Airport.Airport('Los Angeles International Airport',
                                                                     iata='LAX', icao='KLAX')))

    def test_eq_diff_airport_to(self):
        # Make sure __eq__ method states 2 flights with DIFF AIRPORTS_TO are NOT equal
        self.assertNotEqual(self.flight_ex,
                            Flight.Flight('AD832', 'Virgin America',
                                          airport_from=Airport.Airport('John F. Kennedy International Airport',
                                                                       iata='JFK', icao='KJFK'),
                                          airport_to=Airport.Airport('Domodedovo', iata='DME', icao='UUDD')))


class TestFlightGetFlightsFromCsvPos(unittest.TestCase):

    def setUp(self):
        self.airports_list = Airport.Airport.get_airports_from_csv('.\\test_data\\airports.csv', csv_header=True)
        self.csv_flights_list = Flight.Flight.get_flights_from_csv('.\\test_data\\flights.csv',
                                                                   self.airports_list, csv_header=True)

    def test_get_flights_from_csv_correct_data(self):
        # Test List of FLIGHTS from CSV file and CREATED with constructor are EQUAL
        flights_list_to_compare = [Flight.Flight('AD832', 'Virgin America',
                                                 Airport.Airport('John F. Kennedy International Airport', iata='JFK',
                                                                 icao='KJFK'),
                                                 Airport.Airport('Los Angeles International Airport', iata='LAX',
                                                                 icao='KLAX')),
                                   Flight.Flight('AM13', 'S7',
                                                 Airport.Airport('Pulkovo', iata='LED', icao='ULLI'),
                                                 Airport.Airport('Domodedovo', iata='DME', icao='UUDD'))]
        self.assertEqual(flights_list_to_compare, self.csv_flights_list)

    def test_get_flights_from_csv_empty_file(self):
        # Test EMPTY LIST is returned if FILE is EMPTY
        self.assertEqual(Flight.Flight.get_flights_from_csv('.\\test_data\\flights_empty.csv', self.airports_list), [])

    def test_get_flights_from_csv_header_only(self):
        #  Test EMPTY LIST is returned if file has HEADER ONLY
        self.assertEqual(Flight.Flight.get_flights_from_csv('.\\test_data\\flights_header_only.csv',
                                                            self.airports_list, csv_header=True), [])

    def test_get_flights_from_csv_empty_flight_number(self):
        #  Test LIST with EMPTY FLIGHT_NUMBER is returned if FILE has EMPTY FLIGHT_NUMBER fields
        flights_list_to_compare = [Flight.Flight('', 'Virgin America',
                                                 Airport.Airport('John F. Kennedy International Airport', iata='JFK',
                                                                 icao='KJFK'),
                                                 Airport.Airport('Los Angeles International Airport', iata='LAX',
                                                                 icao='KLAX')),
                                   Flight.Flight('', 'S7',
                                                 Airport.Airport('Pulkovo', iata='LED', icao='ULLI'),
                                                 Airport.Airport('Domodedovo', iata='DME', icao='UUDD'))]
        self.assertEqual(flights_list_to_compare,
                         Flight.Flight.get_flights_from_csv('.\\test_data\\flights_empty_flight_number.csv',
                                                            self.airports_list, csv_header=True))

    def test_get_flights_from_csv_empty_airline(self):
        # Test LIST with EMPTY AIRLINE is returned if FILE has EMPTY AIRLINE fields
        flights_list_to_compare = [Flight.Flight('AD832', '',
                                                 Airport.Airport('John F. Kennedy International Airport',
                                                                 iata='JFK', icao='KJFK'),
                                                 Airport.Airport('Los Angeles International Airport',
                                                                 iata='LAX', icao='KLAX')),
                                   Flight.Flight('AM13', '',
                                                 Airport.Airport('Pulkovo', iata='LED', icao='ULLI'),
                                                 Airport.Airport('Domodedovo', iata='DME', icao='UUDD'))]
        self.assertEqual(flights_list_to_compare,
                         Flight.Flight.get_flights_from_csv('.\\test_data\\flights_empty_airline.csv',
                                                            self.airports_list, csv_header=True))

    def test_get_flights_from_csv_empty_flight_number_and_airline(self):
        # Test LIST with EMPTY AIRLINE AND FLIGHT_NUMBER is returned if FILE has EMPTY AIRLINE AND FLIGHT_NUMBER fields
        flights_list_to_compare = [Flight.Flight('', '',
                                                 Airport.Airport('John F. Kennedy International Airport',
                                                                 iata='JFK', icao='KJFK'),
                                                 Airport.Airport('Los Angeles International Airport',
                                                                 iata='LAX', icao='KLAX')),
                                   Flight.Flight('', '',
                                                 Airport.Airport('Pulkovo', iata='LED', icao='ULLI'),
                                                 Airport.Airport('Domodedovo', iata='DME', icao='UUDD'))]
        self.assertEqual(flights_list_to_compare,
                         Flight.Flight.get_flights_from_csv('.\\test_data\\flights_empty_flight_number_and_airline.csv',
                                                            self.airports_list, csv_header=True))


class TestFlightGetFlightsFromCsvNeg(unittest.TestCase):

    def setUp(self):
        self.airports_list = Airport.Airport.get_airports_from_csv('.\\test_data\\airports.csv', csv_header=True)
        self.csv_flights_list = Flight.Flight.get_flights_from_csv('.\\test_data\\flights.csv',
                                                                   self.airports_list, csv_header=True)

    def test_get_flights_from_csv_wrong_file(self):
        # Test IOError is raised if WRONG file NAME is given
        self.assertRaises(IOError, Flight.Flight.get_flights_from_csv, '.\\test_data\\flights_none.csv',
                          self.airports_list, csv_header=True)

    def test_get_flights_from_csv_wrong_extension(self):
        # Test IOError is raised if WRONG file EXTENSION is given
        self.assertRaises(IOError, Flight.Flight.get_flights_from_csv, '.\\test_data\\flights.txt',
                          self.airports_list, csv_header=True)

    # TO DO
    # def test_get_flights_from_csv_locked(self):
    #     # Test IOError is raised if file is LOCKED
    #     self.assertRaises(IOError, Flight.Flight.get_flights_from_csv, '.\\test_data\\flights_locked.csv',
    #                       self.airports_list, csv_header=True)

    def test_get_flights_from_csv_data_long(self):
        # Test ValueError is raised if FLIGHT DATA is too LONG (more than 4 fields)
        # ??? Probably this check should be removed (test and code) as it is OK to have more data ???
        self.assertRaises(ValueError, Flight.Flight.get_flights_from_csv,
                          '.\\test_data\\flights_data_long.csv', self.airports_list, csv_header=True)

    def test_get_flights_from_csv_data_short(self):
        # Test ValueError is raised if FLIGHT DATA is too SHORT (less than 4 fields)
        self.assertRaises(ValueError, Flight.Flight.get_flights_from_csv,
                          '.\\test_data\\flights_data_short.csv', self.airports_list, csv_header=True)

    def test_get_flights_from_csv_empty_data(self):
        #  Test ValueError is raised if file has EMPTY DATA separated WITH COMMAS
        #  (Airport field can not be empty! check in Airport.Airport.find_airport_in_list method)
        self.assertRaises(ValueError, Flight.Flight.get_flights_from_csv,
                          '.\\test_data\\flights_empty_data.csv', self.airports_list)

    def test_get_flights_from_csv_empty_from(self):
        #  Test ValueError is raised if file has EMPTY AIRPORT_FROM field
        #  (Airport field can not be empty! check in Airport.Airport.find_airport_in_list method)
        self.assertRaises(ValueError, Flight.Flight.get_flights_from_csv,
                          '.\\test_data\\flights_empty_from.csv', self.airports_list, csv_header=True)

    def test_get_flights_from_csv_empty_to(self):
        #  Test ValueError is raised if file has EMPTY AIRPORT_TO field
        #  (Airport field can not be empty! check in Airport.Airport.find_airport_in_list method)
        self.assertRaises(ValueError, Flight.Flight.get_flights_from_csv,
                          '.\\test_data\\flights_empty_to.csv', self.airports_list, csv_header=True)


class TestFlightGetFlightsFromXmlPos(unittest.TestCase):

    def setUp(self):
        self.airports_list = Airport.Airport.get_airports_from_csv('.\\test_data\\airports.csv', csv_header=True)
        self.xml_flights_list = Flight.Flight.get_flights_from_xml('.\\test_data\\flights.xml', self.airports_list)

    def test_get_flights_from_xml_correct_data(self):
        # Test LIST of FLIGHTS from XML file and CREATED with constructor are EQUAL
        flights_list_to_compare = [Flight.Flight('AD832', 'Virgin America',
                                                 Airport.Airport('John F. Kennedy International Airport', iata='JFK',
                                                                 icao='KJFK'),
                                                 Airport.Airport('Los Angeles International Airport', iata='LAX',
                                                                 icao='KLAX')),
                                   Flight.Flight('AM13', 'S7',
                                                 Airport.Airport('Pulkovo', iata='LED', icao='ULLI'),
                                                 Airport.Airport('Domodedovo', iata='DME', icao='UUDD'))]
        self.assertEqual(flights_list_to_compare, self.xml_flights_list)

    def test_get_flights_from_xml_empty_flight_number(self):
        #  Test CORRECT LIST of flights with EMPTY FLIGHT_NUMBER is created if FLIGHT_NUMBER attribute in xml is EMPTY
        flights_list_to_compare = [Flight.Flight('', 'Virgin America',
                                                 Airport.Airport('John F. Kennedy International Airport', iata='JFK',
                                                                 icao='KJFK'),
                                                 Airport.Airport('Los Angeles International Airport', iata='LAX',
                                                                 icao='KLAX')),
                                   Flight.Flight('', 'S7',
                                                 Airport.Airport('Pulkovo', iata='LED', icao='ULLI'),
                                                 Airport.Airport('Domodedovo', iata='DME', icao='UUDD'))]
        self.assertEqual(flights_list_to_compare,
                         Flight.Flight.get_flights_from_xml('.\\test_data\\flights_empty_flight_number.xml',
                                                            self.airports_list))

    def test_get_flights_from_xml_extra_data(self):
        #  Test CORRECT LIST of flights is created if flights in xml have EXTRA ELEMENTS
        flights_list_to_compare = [Flight.Flight('AD832', 'Virgin America',
                                                 Airport.Airport('John F. Kennedy International Airport', iata='JFK',
                                                                 icao='KJFK'),
                                                 Airport.Airport('Los Angeles International Airport', iata='LAX',
                                                                 icao='KLAX')),
                                   Flight.Flight('AM13', 'S7',
                                                 Airport.Airport('Pulkovo', iata='LED', icao='ULLI'),
                                                 Airport.Airport('Domodedovo', iata='DME', icao='UUDD'))]
        self.assertEqual(flights_list_to_compare,
                         Flight.Flight.get_flights_from_xml('.\\test_data\\flights_extra_data.xml', self.airports_list))


class TestFlightGetFlightsFromXmlNeg(unittest.TestCase):

    def setUp(self):
        self.airports_list = Airport.Airport.get_airports_from_csv('.\\test_data\\airports.csv', csv_header=True)

    def test_get_flights_from_xml_empty_file(self):
        # Test ParseError is raised if FILE is EMPTY
        self.assertRaises(ParseError, Flight.Flight.get_flights_from_xml,
                          '.\\test_data\\flights_empty.xml', self.airports_list)

    def test_get_flights_from_xml_empty_airline(self):
        # Test TypeError is raised if AIRLINE company value is EMPTY
        self.assertRaises(TypeError, Flight.Flight.get_flights_from_xml,
                          '.\\test_data\\flights_empty_airline.xml', self.airports_list)

    def test_get_flights_from_xml_empty_from(self):
        # Test ValueError is raised if AIRPORT_FROM value is EMPTY
        self.assertRaises(ValueError, Flight.Flight.get_flights_from_xml,
                          '.\\test_data\\flights_empty_from.xml', self.airports_list)

    def test_get_flights_from_xml_empty_to(self):
        # Test ValueError is raised if AIRPORT_TO value is EMPTY
        self.assertRaises(ValueError, Flight.Flight.get_flights_from_xml,
                          '.\\test_data\\flights_empty_to.xml', self.airports_list)

    def test_get_flights_from_xml_missing_airline(self):
        # Test AttributeError is raised if AIRLINE company element is MISSING
        self.assertRaises(AttributeError, Flight.Flight.get_flights_from_xml,
                          '.\\test_data\\flights_missing_airline.xml', self.airports_list)

    def test_get_flights_from_xml_missing_from(self):
        # Test AttributeError is raised if AIRPORT_FROM element is MISSING
        self.assertRaises(AttributeError, Flight.Flight.get_flights_from_xml,
                          '.\\test_data\\flights_missing_from.xml', self.airports_list)

    def test_get_flights_from_xml_missing_to(self):
        # Test AttributeError is raised if AIRPORT_TO element is MISSING
        self.assertRaises(AttributeError, Flight.Flight.get_flights_from_xml,
                          '.\\test_data\\flights_missing_to.xml', self.airports_list)

    def test_get_flights_from_xml_missing_flight_number(self):
        # Test KeyError is raised if FLIGHT_NUMBER attribute is MISSING
        self.assertRaises(KeyError, Flight.Flight.get_flights_from_xml,
                          '.\\test_data\\flights_missing_flight_number.xml', self.airports_list)

    def test_get_flights_from_xml_wrong_file(self):
        # Test IOError is raised if WRONG FILE NAME is given
        self.assertRaises(IOError, Flight.Flight.get_flights_from_xml, '.\\test_data\\flights_none.xml',
                          self.airports_list)

    def test_get_flights_from_xml_wrong_extension(self):
        # IOError should be raised if WRONG FILE EXTENSION is given
        self.assertRaises(IOError, Flight.Flight.get_flights_from_xml, '.\\test_data\\flights.txt',
                          self.airports_list)

    # TO DO
    # def test_get_flights_from_xml_locked(self):
    #     # Test IOError is raised if file is LOCKED
    #     self.assertRaises(IOError, Flight.Flight.get_flights_from_xml, '.\\test_data\\flights_locked.xml',
    #                       self.airports_list)


class TestFlightCsvXmlEq(unittest.TestCase):
    def setUp(self):
        self.airports_list = Airport.Airport.get_airports_from_csv('.\\test_data\\airports.csv', csv_header=True)
        self.csv_flights_list = Flight.Flight.get_flights_from_csv('.\\test_data\\flights.csv',
                                                                   self.airports_list, csv_header=True)
        self.xml_flights_list = Flight.Flight.get_flights_from_xml('.\\test_data\\flights.xml',
                                                                   self.airports_list)
        self.flights_list_to_compare = [Flight.Flight('AD832', 'Virgin America',
                                                      Airport.Airport('John F. Kennedy International Airport',
                                                                      iata='JFK', icao='KJFK'),
                                                      Airport.Airport('Los Angeles International Airport',
                                                                      iata='LAX', icao='KLAX')),
                                        Flight.Flight('AM13', 'S7',
                                                      Airport.Airport('Pulkovo', iata='LED', icao='ULLI'),
                                                      Airport.Airport('Domodedovo', iata='DME', icao='UUDD'))]

    def test_csv_xml_flight_eq(self):
        # Test MAIN SCENARIO: FLIGHT LISTS from CSV and from XML are EQUAL:
        self.assertEqual(self.csv_flights_list, self.xml_flights_list)


class TestXmlValidation(unittest.TestCase):

    def setUp(self):

        from Validator import Validator

        self.validator = Validator('./test_data/flights.xsd')

    def test_validate_xml_against_xsd(self):
        # Validates flights xml file with xsd schema
        self.xml_file_path = './test_data/flights.xml'
        self.assertTrue(self.validator.validate(self.xml_file_path))

    def test_validate_xml_against_xsd_neg(self):
        # Test validation fails if element is missing (ex. airline company element)
        self.xml_file_path = './test_data/flights_missing_airline.xml'
        self.assertFalse(self.validator.validate(self.xml_file_path))

if __name__ == '__main__':
    unittest.main()






